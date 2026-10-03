"""
parse_pdf.py
Tahap PARSING: PDF -> Markdown dengan LlamaParse.

Setiap halaman PDF diawali penanda halaman agar tahap berikutnya tahu
asal halaman setiap teks (dasar sitasi). Header dan footer halaman yang
dipisahkan LlamaParse ikut disertakan utuh (judul slide, keterangan sumber
data, penanda "LAMPIRAN" kadang ada di sana); penyaringan isi yang berulang
dilakukan di tahap processing, bukan di sini:

    <!-- page: 37 -->
    <!-- header -->
    **BAB IV**
    # 4.9. HILIRISASI RISET
    <!-- /header -->
    ...isi halaman...
    <!-- footer -->
    Indikator Kinerja Utama (IKU) Diktisaintek Berdampak 37 |
    <!-- /footer -->

Output per dokumen di data/parsed/:
- <nama>.md          Markdown lengkap dengan penanda halaman
- <nama>.pages.json  hasil mentah per halaman dari LlamaParse (isi, header,
                     footer, nomor halaman tercetak) sebagai cadangan agar
                     tidak perlu parsing ulang

Job LlamaParse dicatat di data/parsed/_jobs.json begitu dibuat. Jika script
terhenti saat menunggu, menjalankannya lagi akan melanjutkan job yang sama
tanpa membayar parsing ulang. Job yang FAILED/CANCELLED diganti job baru.

Jalankan dari mana saja:
    python src/parsing/parse_pdf.py             # parsing dokumen yang belum ada hasilnya
    python src/parsing/parse_pdf.py --force     # parsing ulang semua dokumen (job baru, pakai kredit)
    python src/parsing/parse_pdf.py --rebuild   # susun ulang .md dari .pages.json (tanpa API, tanpa kredit)
"""

from pathlib import Path
import argparse
import json
import os
import sys

from dotenv import load_dotenv
from pypdf import PdfReader

PROJECT_ROOT = Path(__file__).resolve().parents[2]
INPUT_DIR = PROJECT_ROOT / "data" / "raw"
OUTPUT_DIR = PROJECT_ROOT / "data" / "parsed"
JOBS_FILE = OUTPUT_DIR / "_jobs.json"

# (nama file PDF di data/raw, nama dasar file output)
DOCUMENTS = [
    ("Buku IKU Diktisaintek Berdampak_V1.pdf", "Buku_IKU_Diktisaintek_Berdampak_V1"),
    ("PPT IKU Diktisaintek Berdampak_PTS V2.pdf", "PPT_IKU_Diktisaintek_Berdampak_PTS_V2"),
]

TIER = "agentic_plus"
VERSION = "latest"
WAIT_TIMEOUT_SECONDS = 3600

PAGE_MARKER = "<!-- page: {page} -->"
FAILED_PAGE_MARKER = "<!-- page: {page} | GAGAL DIPARSING: {error} -->"


def load_jobs() -> dict:
    if JOBS_FILE.exists():
        return json.loads(JOBS_FILE.read_text(encoding="utf-8"))
    return {}


def save_jobs(jobs: dict):
    JOBS_FILE.write_text(json.dumps(jobs, indent=2), encoding="utf-8")


def wrap(tag: str, text: str | None) -> str:
    text = (text or "").strip()
    return f"<!-- {tag} -->\n{text}\n<!-- /{tag} -->" if text else ""


def build_markdown(pages: list[dict]) -> tuple[str, list[int], list[int]]:
    """Gabungkan halaman berurutan (dict hasil model_dump / .pages.json), masing-masing
    diawali penanda halaman, dengan header/footer halaman disertakan utuh.
    Halaman gagal dan halaman kosong tetap diberi penanda agar tidak ada yang hilang diam-diam."""
    parts, failed, empty = [], [], []

    for page in sorted(pages, key=lambda p: p["page_number"]):
        number = page["page_number"]
        if not page.get("success"):
            error = " ".join(str(page.get("error")).split())[:200]
            parts.append(FAILED_PAGE_MARKER.format(page=number, error=error))
            failed.append(number)
            continue

        content = (page.get("markdown") or "").strip()
        if not content:
            empty.append(number)

        sections = [PAGE_MARKER.format(page=number), wrap("header", page.get("header")),
                    content, wrap("footer", page.get("footer"))]
        parts.append("\n\n".join(s for s in sections if s))

    return "\n\n".join(parts) + "\n", failed, empty


def write_outputs(stem: str, pages: list[dict], pdf_page_count: int, report_errors: bool = True):
    md_path = OUTPUT_DIR / f"{stem}.md"
    markdown, failed, empty = build_markdown(pages)
    md_path.write_text(markdown, encoding="utf-8")

    parsed_numbers = {p["page_number"] for p in pages}
    missing = sorted(set(range(1, pdf_page_count + 1)) - parsed_numbers)
    n_header = sum(1 for p in pages if (p.get("header") or "").strip())
    n_footer = sum(1 for p in pages if (p.get("footer") or "").strip())

    print(f"[OK] Markdown : {md_path}")
    print(f"[CEK] Halaman PDF {pdf_page_count} | diparsing {len(parsed_numbers)} | "
          f"tidak dikembalikan {missing or '-'} | gagal {failed or '-'} | kosong {empty or '-'} | "
          f"header disertakan {n_header} hlm | footer disertakan {n_footer} hlm")
    if missing or failed:
        print("[PERINGATAN] Ada halaman yang tidak lengkap. Periksa daftar di atas sebelum lanjut.")
        if report_errors:
            for page in pages:
                if not page.get("success"):
                    print(f"    hlm {page['page_number']}: {' '.join(str(page.get('error')).split())[:200]}")


def parse_document(client, pdf_path: Path, stem: str, jobs: dict, force: bool):
    md_path = OUTPUT_DIR / f"{stem}.md"
    pages_path = OUTPUT_DIR / f"{stem}.pages.json"

    if md_path.exists() and not force:
        print(f"[SKIP] Output sudah ada: {md_path.name} (pakai --force untuk parsing ulang)")
        return

    pdf_page_count = len(PdfReader(str(pdf_path)).pages)
    print(f"\n[INFO] {pdf_path.name} ({pdf_page_count} halaman)")

    job_id = None if force else jobs.get(pdf_path.name)
    if job_id:
        status = client.parsing.get(job_id).job.status
        if status in ("FAILED", "CANCELLED"):
            print(f"[INFO] Job lama {job_id} berstatus {status}, membuat job baru.")
            job_id = None
        else:
            print(f"[INFO] Melanjutkan job yang sudah ada: {job_id} ({status})")
    if not job_id:
        print("[INFO] Upload file...")
        file = client.files.create(file=str(pdf_path), purpose="parse")
        job = client.parsing.create(
            file_id=file.id,
            tier=TIER,
            version=VERSION,
            # bawaan LlamaParse: job GAGAL TOTAL jika >5% halaman gagal. Kita izinkan
            # hasil sebagian; halaman gagal ditandai & dilaporkan oleh build_markdown().
            processing_control={"job_failure_conditions": {"allowed_page_failure_ratio": 1.0}},
        )
        job_id = job.id
        jobs[pdf_path.name] = job_id
        save_jobs(jobs)
        print(f"[INFO] Job dibuat: {job_id}")

    print(f"[INFO] Menunggu LlamaParse ({TIER}), maksimal {WAIT_TIMEOUT_SECONDS // 60} menit...")
    client.parsing.wait_for_completion(job_id, timeout=WAIT_TIMEOUT_SECONDS, verbose=True)

    result = client.parsing.get(job_id, expand=["markdown", "metadata"])
    if not result.markdown or not result.markdown.pages:
        raise RuntimeError(f"Job {job_id} selesai tetapi tidak mengembalikan markdown.")

    pages = [p.model_dump() for p in result.markdown.pages]
    pages_path.write_text(
        json.dumps(
            {
                "source_pdf": pdf_path.name,
                "job_id": job_id,
                "tier": TIER,
                "pdf_page_count": pdf_page_count,
                "markdown_pages": pages,
                "metadata_pages": (
                    [p.model_dump() for p in result.metadata.pages]
                    if result.metadata and getattr(result.metadata, "pages", None) else []
                ),
            },
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )
    print(f"[OK] Mentah   : {pages_path}")
    write_outputs(stem, pages, pdf_page_count)


def rebuild_document(stem: str):
    """Susun ulang .md dari .pages.json yang sudah ada, tanpa memanggil API."""
    pages_path = OUTPUT_DIR / f"{stem}.pages.json"
    if not pages_path.exists():
        print(f"[SKIP] {pages_path.name} belum ada; jalankan parsing biasa dulu.")
        return
    data = json.loads(pages_path.read_text(encoding="utf-8"))
    print(f"\n[INFO] Rebuild dari {pages_path.name} (job {data.get('job_id')})")
    write_outputs(stem, data["markdown_pages"], data["pdf_page_count"])


def main():
    parser = argparse.ArgumentParser(description="Parsing PDF ke Markdown dengan penanda halaman")
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--force", action="store_true",
                      help="parsing ulang walaupun output sudah ada (membuat job baru, memakai kredit)")
    mode.add_argument("--rebuild", action="store_true",
                      help="susun ulang .md dari .pages.json tanpa memanggil API")
    args = parser.parse_args()

    sys.stdout.reconfigure(encoding="utf-8")
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    if args.rebuild:
        for _, stem in DOCUMENTS:
            rebuild_document(stem)
        return

    load_dotenv(PROJECT_ROOT / ".env")
    api_key = os.getenv("LLAMA_CLOUD_API_KEY")
    if not api_key:
        raise RuntimeError(
            "LLAMA_CLOUD_API_KEY belum ditemukan. "
            "Buat file .env dari .env.example."
        )

    for pdf_name, _ in DOCUMENTS:
        if not (INPUT_DIR / pdf_name).exists():
            raise FileNotFoundError(f"PDF tidak ditemukan: {INPUT_DIR / pdf_name}")

    from llama_cloud import LlamaCloud  # hanya dibutuhkan saat memanggil API

    client = LlamaCloud(api_key=api_key)
    jobs = load_jobs()

    for pdf_name, stem in DOCUMENTS:
        parse_document(client, INPUT_DIR / pdf_name, stem, jobs, args.force)


if __name__ == "__main__":
    main()
