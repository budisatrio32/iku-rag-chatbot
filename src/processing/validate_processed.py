"""
validate_processed.py
Validasi otomatis untuk output tahap PROCESSING (data/processed/*.json)
terhadap markdown hasil parsing (data/parsed/*.md).

Cek yang dilakukan:
1. Kelengkapan konten kasar (word count) — deteksi potensi data hilang
2. Kelengkapan ANGKA — setiap angka yang seharusnya dipertahankan harus muncul
   di hasil processing (angka paling penting untuk soal perhitungan)
3. Integritas tabel — bandingkan jumlah baris <table> asli vs baris markdown table hasil
   + struktur rumus: baris "Formula" berbentuk pecahan wajib punya tanda bagi (/, \\frac, ÷)
4. Cakupan halaman — halaman yang tidak menghasilkan blok sama sekali
5. Block kosong / anomali (mis. heading yang isinya kepanjangan / bukan heading asli)
6. Duplikasi block (content persis sama, berpotensi bug regex overlap)

"Yang seharusnya dipertahankan" = isi markdown setelah aturan buang yang disengaja
di process_markdown.py (header/footer berulang, nomor halaman, gambar dekoratif tanpa data).

Output: ringkasan ke stdout + detail issue ke JSON report per dokumen
"""

import json
import re
import sys
from pathlib import Path
from collections import Counter
from bs4 import BeautifulSoup

sys.path.insert(0, str(Path(__file__).parent))
from process_markdown import (  # noqa: E402
    NOISE_LINE_PATTERNS, IMAGE_LINE_RE, INLINE_IMAGE_RE, MD_TABLE_ROW_RE, MD_TABLE_SEP_RE,
    PAGE_MARKER_RE, REGION_OPEN_RE, REGION_CLOSE_RE,
    image_alt_text, replace_inline_images, is_running_header_line,
)

PROJECT_ROOT = Path(__file__).resolve().parents[2]
PARSED_DIR = PROJECT_ROOT / "data" / "parsed"
PROCESSED_DIR = PROJECT_ROOT / "data" / "processed"
REPORT_DIR = PROJECT_ROOT / "reports" / "validation"

NUMBER_RE = re.compile(r"\d+(?:[.,]\d+)*")


def word_count(text: str) -> int:
    return len(re.findall(r"\w+", text))


def numbers(text: str) -> Counter:
    """Angka dinormalisasi (tanpa titik/koma) agar '1.540' dan '1,540' dianggap sama."""
    return Counter(re.sub(r"[.,]", "", x) for x in NUMBER_RE.findall(text))


def count_original_tables(md_text: str):
    """Ambil jumlah baris <tr> tiap <table> di markdown asli, berurutan."""
    tables = re.findall(r"<table.*?</table>", md_text, flags=re.DOTALL)
    return [len(BeautifulSoup(t, "html.parser").find_all("tr")) for t in tables]


def count_md_table_rows(md_table_content: str) -> int:
    """Hitung baris (termasuk header) pada markdown table hasil processing."""
    return len([l for l in md_table_content.strip().split("\n") if l.strip().startswith("|")])


def expected_content(md_text: str) -> tuple[list[str], list[str], list[str], set[int]]:
    """Pisahkan isi markdown yang SEHARUSNYA dipertahankan menjadi teks non-tabel,
    teks tabel HTML, dan teks tabel pipe — mengikuti aturan buang process_markdown.py."""
    nontable, html_tables, pipe_tables = [], [], []
    pages = set()

    for t in re.findall(r"<table.*?</table>", md_text, flags=re.DOTALL):
        soup = BeautifulSoup(t, "html.parser")
        html_tables.append(replace_inline_images(soup.get_text(" ")))
    text = re.sub(r"<table.*?</table>", "", md_text, flags=re.DOTALL)

    lines = text.split("\n")
    region = None
    k = 0
    while k < len(lines):
        raw = lines[k]
        line = raw.strip()
        m = PAGE_MARKER_RE.match(line)
        if m:
            pages.add(int(m.group(1)))
            region = None
            k += 1
            continue
        m = REGION_OPEN_RE.match(line)
        if m:
            region = m.group(1)
            k += 1
            continue
        if REGION_CLOSE_RE.match(line):
            region = None
            k += 1
            continue
        if region and is_running_header_line(line):
            k += 1
            continue
        if any(re.match(p, line) for p in NOISE_LINE_PATTERNS):
            k += 1
            continue
        img = IMAGE_LINE_RE.match(line)
        if img:
            kept = image_alt_text(img.group(1))
            if kept:
                nontable.append(kept)
            k += 1
            continue
        if (MD_TABLE_ROW_RE.match(line) and k + 1 < len(lines)
                and MD_TABLE_SEP_RE.match(lines[k + 1].strip())):
            rows = [line, lines[k + 1].strip()]
            k += 2
            while k < len(lines) and MD_TABLE_ROW_RE.match(lines[k].strip()):
                rows.append(lines[k].strip())
                k += 1
            pipe_tables.append(replace_inline_images("\n".join(rows)))
            continue
        nontable.append(replace_inline_images(raw) if INLINE_IMAGE_RE.search(raw) else raw)
        k += 1

    return nontable, html_tables, pipe_tables, pages


def validate_file(md_path: Path, json_path: Path) -> dict:
    md_text = md_path.read_text(encoding="utf-8")
    blocks = json.loads(json_path.read_text(encoding="utf-8"))

    issues = {
        "missing_numbers": [],
        "formula_without_division": [],
        "pages_without_blocks": [],
        "empty_or_short_blocks": [],
        "suspicious_headings": [],
        "duplicate_blocks": [],
        "table_row_mismatch": [],
    }

    nontable, html_tables, pipe_tables, pages = expected_content(md_text)
    processed_all = "\n".join(b["content"] for b in blocks)

    # --- 1) Kelengkapan konten kasar ---
    original_nontable_wc = word_count("\n".join(nontable))
    original_table_wc = word_count("\n".join(html_tables)) + word_count("\n".join(pipe_tables))
    original_wc = original_nontable_wc + original_table_wc

    processed_nontable_wc = sum(word_count(b["content"]) for b in blocks if b["block_type"] != "table")
    processed_table_wc = sum(word_count(b["content"]) for b in blocks if b["block_type"] == "table")
    processed_wc = processed_nontable_wc + processed_table_wc

    # --- 2) Kelengkapan angka ---
    expected_numbers = numbers("\n".join(nontable + html_tables + pipe_tables))
    processed_numbers = numbers(processed_all)
    missing = expected_numbers - processed_numbers
    for num, cnt in sorted(missing.items()):
        issues["missing_numbers"].append({"number": num, "missing_count": cnt})
    number_coverage = 1 - sum(missing.values()) / max(sum(expected_numbers.values()), 1)

    # --- 3) Integritas tabel HTML ---
    original_table_rows = count_original_tables(md_text)
    processed_html_tables = [b for b in blocks if b.get("table_source") == "html"]
    processed_pipe_tables = [b for b in blocks if b.get("table_source") == "markdown_pipe"]
    mismatches = 0
    for i, b in enumerate(processed_html_tables):
        if i >= len(original_table_rows):
            break
        # baris pertama = header; pecahan dua-baris yang digabung mengurangi jumlah baris
        orig_body_rows = max(original_table_rows[i] - 1 - b.get("merged_formula_rows", 0), 0)
        new_body_rows = max(count_md_table_rows(b["content"]) - 2, 0)  # header + separator
        if new_body_rows != orig_body_rows:
            mismatches += 1
            issues["table_row_mismatch"].append({
                "table_index": i, "block_id": b["id"],
                "original_rows(approx_body)": orig_body_rows, "processed_rows(body)": new_body_rows,
            })
    if len(original_table_rows) != len(processed_html_tables):
        mismatches += 1
        issues["table_row_mismatch"].append({
            "table_index": "html_table_count",
            "original": len(original_table_rows), "processed": len(processed_html_tables),
        })
    if len(pipe_tables) != len(processed_pipe_tables):
        mismatches += 1
        issues["table_row_mismatch"].append({
            "table_index": "markdown_pipe_group_count",
            "original": len(pipe_tables), "processed": len(processed_pipe_tables),
        })

    # --- 3b) Struktur rumus: baris "Formula" yang berupa pecahan harus punya tanda bagi ---
    for b in blocks:
        if b["block_type"] != "table":
            continue
        for line in b["content"].split("\n"):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if not any(c.strip("* ").lower() == "formula" for c in cells):
                continue
            formula = " ".join(c for c in cells if c.strip("* ").lower() != "formula")
            if re.search(r"100\s*%|∑|Σ|\\sum", formula) and not re.search(r"/|\\frac|÷", formula):
                issues["formula_without_division"].append(
                    {"block_id": b["id"], "page": b["page"], "formula": formula[:160]})

    # --- 4) Cakupan halaman ---
    pages_with_blocks = {b["page"] for b in blocks}
    issues["pages_without_blocks"] = sorted(pages - pages_with_blocks)

    # --- 5) Block kosong / anomali ---
    for b in blocks:
        content = b["content"].strip()
        if not content:
            issues["empty_or_short_blocks"].append(b["id"])
        if b["block_type"] == "heading" and (len(content) > 120 or content.endswith((".", ",", ":"))):
            issues["suspicious_headings"].append({"id": b["id"], "content": content[:100]})

    # --- 6) Duplikasi ---
    content_counter = Counter(b["content"].strip() for b in blocks if b["content"].strip())
    for content, cnt in content_counter.items():
        if cnt > 1 and len(content) > 15:  # abaikan string pendek yang wajar berulang
            dup_ids = [b["id"] for b in blocks if b["content"].strip() == content]
            issues["duplicate_blocks"].append({"content": content[:80], "count": cnt, "ids": dup_ids})

    summary = {
        "source_file": md_path.name,
        "total_blocks": len(blocks),
        "block_type_counts": dict(Counter(b["block_type"] for b in blocks)),
        "original_word_count_cleaned": original_wc,
        "processed_word_count": processed_wc,
        "content_coverage_pct": round(processed_wc / max(original_wc, 1) * 100, 1),
        "content_coverage_nontable_pct": round(processed_nontable_wc / max(original_nontable_wc, 1) * 100, 1),
        "content_coverage_table_pct": round(processed_table_wc / max(original_table_wc, 1) * 100, 1),
        "number_coverage_pct": round(number_coverage * 100, 2),
        "missing_number_occurrences": sum(missing.values()),
        "pages_in_markdown": len(pages),
        "pages_without_blocks": issues["pages_without_blocks"],
        "original_table_count(html)": len(original_table_rows),
        "processed_table_count(html)": len(processed_html_tables),
        "original_table_count(markdown_pipe)": len(pipe_tables),
        "processed_table_count(markdown_pipe)": len(processed_pipe_tables),
        "table_row_mismatches": mismatches,
        "formula_without_division": [(x["page"], x["formula"][:70]) for x in issues["formula_without_division"]],
        "empty_blocks": len(issues["empty_or_short_blocks"]),
        "suspicious_headings": len(issues["suspicious_headings"]),
        "duplicate_block_groups": len(issues["duplicate_blocks"]),
        "blocks_with_source_notes": sum(1 for b in blocks if b.get("source_notes")),
    }

    report = {"summary": summary, "issues": issues}
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    out_path = REPORT_DIR / f"{md_path.stem}_validation.json"
    out_path.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")

    return summary


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    for md_file in sorted(PARSED_DIR.glob("*.md")):
        json_file = PROCESSED_DIR / f"{md_file.stem}_processed.json"
        if not json_file.exists():
            print(f"[SKIP] {json_file} tidak ditemukan")
            continue
        summary = validate_file(md_file, json_file)
        print(f"\n=== {summary['source_file']} ===")
        for k, v in summary.items():
            if k != "source_file":
                print(f"  {k}: {v}")
    print(f"\nDetail: {REPORT_DIR}")


if __name__ == "__main__":
    main()
