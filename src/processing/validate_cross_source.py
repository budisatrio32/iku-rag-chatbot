"""
validate_cross_source.py
Validasi silang ANGKA antara dua dokumen sumber (Buku IKU vs PPT IKU) pada
hasil processing (data/processed/*.json).

Kedua dokumen memuat banyak tabel yang sama. Parser berbasis AI kadang salah
membaca atau mengarang angka (contoh nyata: sel 'G1.G' di PDF ditulis 91.9 oleh
parser). Angka yang salah seperti ini tidak terdeteksi oleh validasi "ada yang
hilang", tetapi terdeteksi bila tabel yang sama di dokumen lain berbeda.

Langkah:
1. Pasangkan setiap tabel PPT dengan tabel Buku yang isinya paling mirip.
2. Sejajarkan baris berdasarkan label teksnya (mis. nama universitas).
3. Bandingkan angka pada baris yang sejajar -> laporkan selisihnya.
4. Deteksi token angka yang cacat font (huruf G menggantikan angka 9, mis. 'G1.G', '83G').
Selisih yang sudah tercatat di data/metadata/known_source_issues.json ditandai.

Output: reports/validation/cross_source_numbers.md dan .json
"""

import json
import re
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
PROCESSED_DIR = PROJECT_ROOT / "data" / "processed"
REPORT_DIR = PROJECT_ROOT / "reports" / "validation"

PRIMARY = "Buku_IKU_Diktisaintek_Berdampak_V1"
SECONDARY = "PPT_IKU_Diktisaintek_Berdampak_PTS_V2"

TABLE_MATCH_MIN = 0.5    # kemiripan kata minimal agar dua tabel dianggap tabel yang sama
ROW_MATCH_MIN = 0.7      # kemiripan label minimal agar dua baris dianggap baris yang sama
MIN_NUMBERS_IN_ROW = 2   # baris dengan angka lebih sedikit tidak dibandingkan

NUMBER_RE = re.compile(r"\d+(?:[.,]\d+)*")
# token angka yang memuat huruf G di posisi digit ('G1.G', '83G', '202G'): cacat font di
# PDF sumber, huruf G tampil menggantikan angka 9 (terbukti di Buku hlm. 43 / PPT hlm. 39)
# (nama node diagram mermaid seperti G1["..."] dikecualikan)
GLITCH_TOKEN_RE = re.compile(
    r"(?<![A-Za-z\d])(?=[\dG.,]*\d)(?=[\dG.,]*G)[\dG]+(?:[.,][\dG]+)*(?![A-Za-z\d\[(])")


def load_tables(stem: str) -> list[dict]:
    blocks = json.loads((PROCESSED_DIR / f"{stem}_processed.json").read_text(encoding="utf-8"))
    tables = []
    for b in blocks:
        if b["block_type"] != "table":
            continue
        rows = []
        for line in b["content"].split("\n"):
            line = line.strip()
            if not line.startswith("|") or re.fullmatch(r"\|[\s:\-|]+\|", line):
                continue
            rows.append([c.strip() for c in line.strip("|").split("|")])
        tables.append({"block": b, "rows": rows, "words": set(words(b["content"]))})
    return tables


def words(text: str) -> list[str]:
    return re.findall(r"[a-z]{3,}|\d+(?:[.,]\d+)*", text.lower())


def label_words(cells: list[str]) -> set[str]:
    return set(re.findall(r"[a-z]{3,}", " ".join(cells).lower()))


def row_numbers(cells: list[str]) -> list[str]:
    return [re.sub(r"[.,]", "", n) for n in NUMBER_RE.findall(" ".join(cells))]


def jaccard(a: set, b: set) -> float:
    return len(a & b) / max(len(a | b), 1)


def compare(primary: list[dict], secondary: list[dict]) -> list[dict]:
    findings = []
    for st in secondary:
        best = max(primary, key=lambda pt: jaccard(st["words"], pt["words"]))
        table_sim = jaccard(st["words"], best["words"])
        if table_sim < TABLE_MATCH_MIN:
            continue

        for s_row in st["rows"]:
            s_nums = row_numbers(s_row)
            s_label = label_words(s_row)
            if len(s_nums) < MIN_NUMBERS_IN_ROW or not s_label:
                continue
            p_row = max(best["rows"], key=lambda r: jaccard(s_label, label_words(r)))
            row_sim = jaccard(s_label, label_words(p_row))
            if row_sim < ROW_MATCH_MIN:
                continue
            p_nums = row_numbers(p_row)
            only_secondary = sorted(set(s_nums) - set(p_nums))
            only_primary = sorted(set(p_nums) - set(s_nums))
            if not only_secondary and not only_primary:
                continue
            notes = {n["id"] for blk in (st["block"], best["block"]) for n in blk.get("source_notes", [])}
            findings.append({
                "secondary_page": st["block"]["page"],
                "primary_page": best["block"]["page"],
                "table_similarity": round(table_sim, 2),
                "row_similarity": round(row_sim, 2),
                "secondary_row": " | ".join(s_row),
                "primary_row": " | ".join(p_row),
                "numbers_only_in_secondary": only_secondary,
                "numbers_only_in_primary": only_primary,
                "known_issue": sorted(notes),
            })
    return findings


def glitch_cells(stem: str) -> list[dict]:
    """Cari token angka bercampur huruf G di SEMUA blok (tabel maupun paragraf)."""
    blocks = json.loads((PROCESSED_DIR / f"{stem}_processed.json").read_text(encoding="utf-8"))
    found = []
    for b in blocks:
        for line in b["content"].split("\n"):
            for m in GLITCH_TOKEN_RE.finditer(line):
                found.append({
                    "document": stem,
                    "page": b["page"],
                    "cell": m.group(0),
                    "row": " ".join(line.split())[:160],
                    "known_issue": sorted(n["id"] for n in b.get("source_notes", [])),
                })
    return found


def build_report(findings: list[dict], glitches: list[dict]) -> str:
    lines = ["# Validasi Silang Angka: Buku IKU vs PPT IKU", ""]
    lines.append(f"- Baris tabel dengan angka berbeda: **{len(findings)}** "
                 f"(sudah tercatat sebagai cacat sumber: {sum(1 for f in findings if f['known_issue'])})")
    lines.append(f"- Sel yang tampak cacat font/OCR: **{len(glitches)}**")
    lines.append("")
    lines.append("Selisih belum tentu salah parsing: bisa juga data yang memang berbeda antara Buku dan PPT. "
                 "Setiap baris di bawah perlu dicek ke PDF asli.")
    lines.append("")
    lines.append("## Baris dengan angka berbeda")
    lines.append("")
    lines.append("| PPT hlm. | Buku hlm. | Hanya di PPT | Hanya di Buku | Catatan sumber | Baris PPT | Baris Buku |")
    lines.append("|---|---|---|---|---|---|---|")
    for f in findings:
        lines.append(
            f"| {f['secondary_page']} | {f['primary_page']} | {', '.join(f['numbers_only_in_secondary']) or '-'} | "
            f"{', '.join(f['numbers_only_in_primary']) or '-'} | {', '.join(f['known_issue']) or '-'} | "
            f"{f['secondary_row'][:120].replace('|', '/')} | {f['primary_row'][:120].replace('|', '/')} |"
        )
    lines.append("")
    lines.append("## Sel yang tampak cacat font/OCR")
    lines.append("")
    lines.append("| Dokumen | Hlm. | Sel | Catatan sumber | Baris |")
    lines.append("|---|---|---|---|---|")
    for g in glitches:
        lines.append(f"| {g['document'][:4]} | {g['page']} | `{g['cell']}` | {', '.join(g['known_issue']) or '-'} | "
                     f"{g['row'].replace('|', '/')} |")
    lines.append("")
    lines.append("Angka dinormalisasi tanpa titik/koma ('1.540' = '1,540' = '1540').")
    return "\n".join(lines)


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    primary = load_tables(PRIMARY)
    secondary = load_tables(SECONDARY)

    findings = compare(primary, secondary)
    glitches = glitch_cells(PRIMARY) + glitch_cells(SECONDARY)

    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    (REPORT_DIR / "cross_source_numbers.json").write_text(
        json.dumps({"mismatched_rows": findings, "glitch_cells": glitches}, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    (REPORT_DIR / "cross_source_numbers.md").write_text(build_report(findings, glitches), encoding="utf-8")

    print(f"Tabel: Buku {len(primary)} | PPT {len(secondary)}")
    print(f"Baris dengan angka berbeda: {len(findings)} "
          f"(tercatat sebagai cacat sumber: {sum(1 for f in findings if f['known_issue'])})")
    for f in findings:
        print(f"  PPT hlm {f['secondary_page']} vs Buku hlm {f['primary_page']}: "
              f"PPT {f['numbers_only_in_secondary']} vs Buku {f['numbers_only_in_primary']} "
              f"{'[tercatat: ' + ','.join(f['known_issue']) + ']' if f['known_issue'] else ''}"
              f"\n      PPT : {f['secondary_row'][:110]}\n      Buku: {f['primary_row'][:110]}")
    print(f"Sel tampak cacat font/OCR: {len(glitches)}")
    for g in glitches:
        print(f"  {g['document'][:4]} hlm {g['page']}: '{g['cell']}' | {g['row'][:90]}")
    print(f"\nLaporan: {REPORT_DIR / 'cross_source_numbers.md'}")


if __name__ == "__main__":
    main()
