"""
run_answer_tests.py
Jalankan soal test set ke chatbot (tahap 7: retriever + LLM + kalkulator) dan bandingkan
jawabannya dengan jawaban yang diharapkan.

Sumber jawaban yang diharapkan:
- data/evaluation/test_set_buku_iku.md       -> "Jawaban benar" + halaman kunci (semua soal)
- data/evaluation/test_inputs_hitung.json     -> angka kunci soal hitungan (H01-H18)
- data/evaluation/test_fakta_definisi.json    -> fakta kunci soal definisi & jebakan (D01-D12)

Pemeriksaan otomatis per soal:
- Hitungan : kalkulator dipanggil, hasil kalkulator = kunci, angka kunci muncul di jawaban,
             halaman sitasi/rumus cocok dengan halaman kunci
- Definisi : semua fakta kunci muncul di jawaban, halaman sitasi cocok dengan halaman kunci
- Jebakan  : D11 meluruskan ke IKU 2; D12 menolak (tidak mengarang) dan tidak perlu sitasi
Pemeriksaan otomatis hanya bantuan: baca juga jawaban lengkap di laporan.

Setiap soal memanggil LLM (biasanya 1-3 kali). Pada Gemini free tier, beri jeda antar-soal
agar tidak terkena batas pemakaian.

Jalankan dari root project:
    python src/evaluation/run_answer_tests.py                     # semua 30 soal
    python src/evaluation/run_answer_tests.py --tipe hitung       # 18 soal hitungan saja
    python src/evaluation/run_answer_tests.py --tipe definisi     # 12 soal definisi & jebakan
    python src/evaluation/run_answer_tests.py --id H07,D11        # soal tertentu
    python src/evaluation/run_answer_tests.py --jeda 10           # jeda 10 detik antar-soal
"""

import argparse
import json
import re
import sys
import time
from datetime import datetime
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(PROJECT_ROOT / "src" / "evaluation"))
sys.path.insert(0, str(PROJECT_ROOT / "src" / "generation"))

from eval_retrieval import load_test_set, TEST_SET_FILE  # noqa: E402
from answer import Chatbot, varian_angka  # noqa: E402

INPUTS_HITUNG = PROJECT_ROOT / "data" / "evaluation" / "test_inputs_hitung.json"
FAKTA_DEFINISI = PROJECT_ROOT / "data" / "evaluation" / "test_fakta_definisi.json"
RESULTS_DIR = PROJECT_ROOT / "reports" / "evaluation"
TOLERANCE = 0.01


# ---------------------------------------------------------------------------
# Pemeriksaan
# ---------------------------------------------------------------------------

def sama(aktual, harapan) -> bool:
    if isinstance(harapan, dict):
        return isinstance(aktual, dict) and all(sama(aktual.get(k), v) for k, v in harapan.items())
    if isinstance(harapan, (int, float)) and isinstance(aktual, (int, float)):
        return abs(aktual - harapan) <= TOLERANCE
    return aktual == harapan


def nilai_kunci(harapan) -> list:
    return list(harapan.values()) if isinstance(harapan, dict) else [harapan]


def halaman_dikutip(hasil: dict) -> list[tuple[int, int]]:
    """Rentang halaman dari rujukan [n] yang valid di jawaban + dari sumber rumus kalkulator."""
    rentang = []
    chunks = hasil["chunks"]
    for n in {int(x) for x in re.findall(r"\[(\d+)\]", hasil["jawaban"])}:
        if 1 <= n <= len(chunks):
            rentang.append((chunks[n - 1]["page_start"], chunks[n - 1]["page_end"]))
    for sumber in hasil["sumber_rumus"]:
        for a, b in re.findall(r"hlm\.\s*(\d+)(?:\s*[–-]\s*(\d+))?", sumber):
            rentang.append((int(a), int(b or a)))
    return rentang


def cek_halaman(hasil: dict, halaman_kunci: list[int]) -> bool:
    return any(a <= p <= b for a, b in halaman_dikutip(hasil) for p in halaman_kunci)


def cek_hitungan(hasil: dict, kasus: dict, halaman_kunci: list[int]) -> dict:
    berhasil = [k for k in hasil["kalkulator"] if "error" not in k["hasil"]]
    harapan = kasus["harapan"]
    return {
        "kalkulator dipanggil": bool(berhasil),
        "hasil kalkulator = kunci": any(sama(k["hasil"]["hasil"], harapan) for k in berhasil),
        "angka kunci ada di jawaban": all(
            any(v in hasil["jawaban"] for v in varian_angka(x)) for x in nilai_kunci(harapan)),
        "halaman sitasi benar": cek_halaman(hasil, halaman_kunci),
    }


def cek_definisi(hasil: dict, kasus: dict, halaman_kunci: list[int]) -> dict:
    teks = hasil["jawaban"].lower()
    cek = {}
    for kelompok in kasus["fakta"]:
        cek[f"fakta: {' / '.join(kelompok)}"] = any(alt.lower() in teks for alt in kelompok)
    if kasus.get("tanpa_sitasi"):
        cek["tidak mengarang sitasi"] = not hasil["sitasi"]
    elif halaman_kunci:
        cek["halaman sitasi benar"] = cek_halaman(hasil, halaman_kunci)
    return cek


# ---------------------------------------------------------------------------
# Laporan
# ---------------------------------------------------------------------------

def fmt(nilai) -> str:
    if isinstance(nilai, dict):
        return ", ".join(f"{k} = {fmt(v)}" for k, v in nilai.items())
    if isinstance(nilai, float):
        return f"{nilai:,.2f}".replace(",", "#").replace(".", ",").replace("#", ".")
    if isinstance(nilai, int) and not isinstance(nilai, bool):
        return f"{nilai:,}".replace(",", ".")
    return str(nilai)


def blok_soal(baris: dict) -> list[str]:
    status = "✅ LULUS" if baris["lulus"] else ("⚠️ ERROR" if baris.get("error") else "❌ PERLU DICEK")
    out = [
        f"### {baris['id']} — {status}",
        "",
        f"**Pertanyaan:** {baris['pertanyaan']}",
        "",
        "**Jawaban chatbot:**",
        "",
        "```text",
        baris.get("jawaban") or f"(tidak ada jawaban: {baris.get('error')})",
        "```",
        "",
    ]
    if baris.get("sitasi"):
        out += ["**Sitasi chatbot:**", ""] + [f"- {s}" for s in baris["sitasi"]] + [""]
    if baris.get("sumber_rumus"):
        out += ["**Sumber rumus (kalkulator):**", ""] + [f"- {s}" for s in baris["sumber_rumus"]] + [""]
    if baris.get("kalkulator"):
        out += ["**Panggilan kalkulator:**", ""]
        for k in baris["kalkulator"]:
            hasil = k["hasil"].get("hasil", k["hasil"].get("error"))
            out.append(f"- argumen `{k['argumen']}` → {fmt(hasil)}")
        out.append("")
    if baris.get("peringatan"):
        out += ["**Peringatan chatbot:**", ""] + [f"- {p}" for p in baris["peringatan"]] + [""]
    out += ["**Jawaban yang diharapkan:**", ""]
    if baris.get("harapan_angka") is not None:
        out.append(f"- Angka kunci: **{fmt(baris['harapan_angka'])}**")
    out += [f"- Halaman kunci: {', '.join(map(str, baris['halaman_kunci'])) or '-'}", "", baris["jawaban_benar"], ""]
    if baris.get("catatan"):
        out += [f"*Catatan soal:* {baris['catatan']}", ""]
    out += ["**Pemeriksaan otomatis:**", ""]
    out += [f"- {'✅' if ok else '❌'} {nama}" for nama, ok in baris.get("cek", {}).items()]
    out.append("")
    return out


def tulis_laporan(rows: list[dict], model: str, path: Path):
    n = len(rows)
    lulus = sum(r["lulus"] for r in rows)
    hitung = [r for r in rows if r["id"].startswith("H")]
    definisi = [r for r in rows if r["id"].startswith("D")]

    def rasio(daftar, kunci):
        relevan = [r for r in daftar if kunci in r.get("cek", {})]
        return f"{sum(r['cek'][kunci] for r in relevan)}/{len(relevan)}" if relevan else "-"

    lines = [
        "# Uji Jawaban Chatbot (retriever + LLM + kalkulator)",
        "",
        f"- Waktu: {datetime.now():%Y-%m-%d %H:%M:%S}",
        f"- Model LLM: `{model}`",
        f"- Soal: {n} (hitungan {len(hitung)}, definisi & jebakan {len(definisi)})",
        "",
        "## Ringkasan",
        "",
        "| Metrik | Hasil |",
        "|---|---|",
        f"| Lulus semua pemeriksaan otomatis | **{lulus}/{n}** |",
        f"| Hitungan: kalkulator dipanggil | {rasio(hitung, 'kalkulator dipanggil')} |",
        f"| Hitungan: hasil kalkulator = kunci | {rasio(hitung, 'hasil kalkulator = kunci')} |",
        f"| Hitungan: angka kunci ada di jawaban | {rasio(hitung, 'angka kunci ada di jawaban')} |",
        f"| Halaman sitasi benar (hitungan) | {rasio(hitung, 'halaman sitasi benar')} |",
        f"| Halaman sitasi benar (definisi) | {rasio(definisi, 'halaman sitasi benar')} |",
        f"| Soal error (API/kuota) | {sum(1 for r in rows if r.get('error'))} |",
        f"| Jawaban dengan peringatan chatbot | {sum(1 for r in rows if r.get('peringatan'))} |",
        "",
        "| ID | Status | Pemeriksaan yang gagal |",
        "|---|---|---|",
    ]
    for r in rows:
        gagal = [k for k, ok in r.get("cek", {}).items() if not ok]
        status = "✅" if r["lulus"] else ("⚠️ error" if r.get("error") else "❌")
        lines.append(f"| {r['id']} | {status} | {'; '.join(gagal) or (r.get('error') or '-')} |")
    lines += ["", "Pemeriksaan otomatis hanya bantuan. Baca jawaban lengkap di bawah dan bandingkan "
              "dengan jawaban yang diharapkan.", "", "## Detail per soal", ""]
    for r in rows:
        lines += blok_soal(r)
    path.write_text("\n".join(lines), encoding="utf-8")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Uji jawaban chatbot terhadap test set")
    parser.add_argument("--tipe", choices=["semua", "hitung", "definisi"], default="semua")
    parser.add_argument("--id", help="daftar ID dipisah koma, mis. H07,D11")
    parser.add_argument("--jeda", type=float, default=5.0,
                        help="jeda (detik) antar-soal agar tidak terkena batas free tier")
    args = parser.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    soal = load_test_set(TEST_SET_FILE)
    kasus_hitung = {c["id"]: c for c in json.loads(INPUTS_HITUNG.read_text(encoding="utf-8"))["cases"]}
    kasus_definisi = json.loads(FAKTA_DEFINISI.read_text(encoding="utf-8"))["cases"]

    if args.id:
        dipilih = {x.strip().upper() for x in args.id.split(",")}
        soal = [q for q in soal if q["id"] in dipilih]
    elif args.tipe == "hitung":
        soal = [q for q in soal if q["id"].startswith("H")]
    elif args.tipe == "definisi":
        soal = [q for q in soal if q["id"].startswith("D")]
    if not soal:
        print("Tidak ada soal yang cocok dengan filter.")
        return

    print("Memuat retriever dan LLM...")
    bot = Chatbot()
    print(f"Model: {bot.model} | {len(soal)} soal | jeda {args.jeda:g} detik\n")

    rows = []
    for i, q in enumerate(soal, start=1):
        kasus = kasus_hitung.get(q["id"]) or kasus_definisi.get(q["id"]) or {}
        baris = {
            "id": q["id"],
            "pertanyaan": q["question"],
            "jawaban_benar": q["expected_answer"],
            "halaman_kunci": q["expected_pages"],
            "harapan_angka": kasus.get("harapan") if q["id"].startswith("H") else None,
            "catatan": kasus.get("catatan"),
            "lulus": False,
        }
        print(f"[{i}/{len(soal)}] {q['id']} ... ", end="", flush=True)
        try:
            hasil = bot.ask(q["question"])
            if q["id"].startswith("H"):
                cek = cek_hitungan(hasil, kasus, q["expected_pages"])
            else:
                cek = cek_definisi(hasil, kasus, q["expected_pages"])
            baris.update({
                "jawaban": hasil["jawaban"], "sitasi": hasil["sitasi"], "sumber_rumus": hasil["sumber_rumus"],
                "kalkulator": hasil["kalkulator"], "peringatan": hasil["peringatan"], "cek": cek,
                "lulus": bool(cek) and all(cek.values()),
            })
            gagal = [k for k, ok in cek.items() if not ok]
            print("LULUS" if baris["lulus"] else f"PERLU DICEK ({'; '.join(gagal)})")
        except Exception as e:  # satu soal gagal (mis. kuota) tidak menghentikan soal lain
            baris["error"] = f"{type(e).__name__}: {e}"
            print(f"ERROR {baris['error'][:120]}")
        rows.append(baris)
        if i < len(soal):
            time.sleep(args.jeda)

    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    model_slug = re.sub(r"[^A-Za-z0-9.-]+", "-", bot.model)
    md_path = RESULTS_DIR / f"answer_test_{model_slug}_{stamp}.md"
    tulis_laporan(rows, bot.model, md_path)
    json_path = md_path.with_suffix(".json")
    json_path.write_text(json.dumps({"model": bot.model, "results": rows}, ensure_ascii=False, indent=2,
                                    default=str), encoding="utf-8")

    lulus = sum(r["lulus"] for r in rows)
    print(f"\nLulus semua pemeriksaan otomatis: {lulus}/{len(rows)}")
    print(f"Laporan : {md_path}")
    print(f"Detail  : {json_path}")


if __name__ == "__main__":
    main()
