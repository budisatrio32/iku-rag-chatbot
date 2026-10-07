"""
run_calc_tests.py
Jalankan soal hitungan (H01-H30) dari test set:
1. HITUNG  : kalkulator IKU (src/calculator/iku_formulas.py) dengan input terstruktur
             dari data/evaluation/test_inputs_hitung.json -> bandingkan dengan kunci jawaban
2. SITASI  : cari chunk sumber lewat retriever (koleksi Chroma v2) memakai teks soal,
             lalu pilih chunk IKU yang sama dengan prioritas Bab V Buku > Lampiran > PPT
             -> bandingkan halamannya dengan halaman kunci

Belum ada LLM di sini: angka dari kalimat soal ditulis manual di JSON (nanti tugas LLM).

Jalankan dari root project:
    python src/evaluation/run_calc_tests.py
    python src/evaluation/run_calc_tests.py --id H07          # satu soal saja
"""

import argparse
import json
import sys
from datetime import datetime
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(PROJECT_ROOT / "src" / "calculator"))
sys.path.insert(0, str(PROJECT_ROOT / "src" / "evaluation"))
sys.path.insert(0, str(PROJECT_ROOT / "src" / "retrieval"))

from iku_formulas import hitung  # noqa: E402
from eval_retrieval import load_test_set, TEST_SET_FILE  # noqa: E402
from retriever import Retriever  # noqa: E402

INPUTS_FILE = PROJECT_ROOT / "data" / "evaluation" / "test_inputs_hitung.json"
RESULTS_DIR = PROJECT_ROOT / "reports" / "evaluation"
TOLERANCE = 0.01


def same(actual, expected) -> bool:
    if isinstance(expected, dict):
        return isinstance(actual, dict) and all(same(actual.get(k), v) for k, v in expected.items())
    if isinstance(expected, (int, float)) and isinstance(actual, (int, float)):
        return abs(actual - expected) <= TOLERANCE
    return actual == expected


def fmt(value) -> str:
    if isinstance(value, dict):
        return ", ".join(f"{k} = {fmt(v)}" for k, v in value.items())
    if isinstance(value, float):
        return f"{value:,.2f}".replace(",", "#").replace(".", ",").replace("#", ".")
    if isinstance(value, int):
        return f"{value:,}".replace(",", ".")
    return str(value)


def pick_citation(results: list[dict], target: dict) -> tuple[dict | None, str]:
    """Pilih chunk sitasi: IKU & jenis sama, dengan prioritas Bab V Buku > Lampiran Buku > PPT."""
    same_iku = [r for r in results if r.get("iku_id") == target["iku_id"] and r.get("jenis") == target["jenis"]]
    tiers = [
        ("Bab utama Buku", lambda r: r["source_file"].startswith("Buku") and r.get("doc_part") == "utama"),
        ("Lampiran Buku", lambda r: r["source_file"].startswith("Buku") and r.get("doc_part") == "lampiran"),
        ("PPT", lambda r: r["source_file"].startswith("PPT")),
    ]
    for label, cond in tiers:
        found = [r for r in same_iku if cond(r)]
        if found:
            return found[0], label
    return None, "tidak ditemukan"


def main():
    parser = argparse.ArgumentParser(description="Uji soal hitungan: kalkulator + sitasi")
    parser.add_argument("--collection", default="pmpt_qa_v2")
    parser.add_argument("--candidates", type=int, default=10, help="jumlah kandidat chunk dari retriever")
    parser.add_argument("--id", help="jalankan satu soal saja, mis. H07")
    args = parser.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    questions = {q["id"]: q for q in load_test_set(TEST_SET_FILE)}
    cases = json.loads(INPUTS_FILE.read_text(encoding="utf-8"))["cases"]
    if args.id:
        cases = [c for c in cases if c["id"] == args.id.upper()]

    print("Load retriever...")
    retriever = Retriever.v2(top_k=args.candidates, collection_name=args.collection)

    rows, report = [], []
    for case in cases:
        q = questions[case["id"]]
        out = hitung(case["fungsi"], **case["argumen"])
        correct = same(out["hasil"], case["harapan"])

        results = retriever.search(q["question"])
        chosen, tier = pick_citation(results, case["sitasi"])
        expected_pages = case["sitasi"]["halaman"]
        if chosen:
            rank = results.index(chosen) + 1
            pages = (chosen["page_start"], chosen["page_end"])
            page_label = str(pages[0]) if pages[0] == pages[1] else f"{pages[0]}–{pages[1]}"
            page_ok = any(pages[0] <= p <= pages[1] for p in expected_pages)
            cite = (f"{'Buku' if chosen['source_file'].startswith('Buku') else 'PPT'} hlm. {page_label} "
                    f"({tier}, peringkat #{rank} dari {len(results)}, bagian {chosen.get('bagian') or '-'})")
        else:
            page_label, page_ok, cite = "-", False, "tidak ada chunk IKU ini di kandidat"

        rows.append({"id": case["id"], "correct": correct, "page_ok": page_ok, "tier": tier})

        block = [
            f"\n{'=' * 100}",
            f"{case['id']} | {q['question']}",
            "-" * 100,
            f"Fungsi     : {case['fungsi']}",
            "Langkah    :",
            *[f"   {s}" for s in out["langkah"]],
            f"HASIL      : {fmt(out['hasil'])} {out['satuan'] if out['satuan'] not in ('%',) else '%'}",
            f"Kunci      : {fmt(case['harapan'])}  -> {'✅ BENAR' if correct else '❌ BEDA'}",
            f"Sumber rumus (kalkulator): {out['sumber']}",
            f"Sitasi (retrieval)       : {cite}  -> {'✅' if page_ok else '❌'} (kunci hlm. {', '.join(map(str, expected_pages))})",
        ]
        if out.get("catatan"):
            block.append(f"Catatan    : {out['catatan']}")
        if chosen and chosen.get("source_notes"):
            block += [f"Catatan sumber: [{n['id']}] {n['note']}" for n in chosen["source_notes"]]
        print("\n".join(block))
        report.append(block)

    n = len(rows)
    n_correct = sum(r["correct"] for r in rows)
    n_page = sum(r["page_ok"] for r in rows)
    tiers = {}
    for r in rows:
        tiers[r["tier"]] = tiers.get(r["tier"], 0) + 1
    summary = [
        f"\n{'=' * 100}",
        "RINGKASAN",
        f"Hasil hitung benar        : {n_correct}/{n}",
        f"Halaman sitasi benar      : {n_page}/{n}",
        f"Asal sitasi               : {tiers}",
        "Gagal hitung              : " + (", ".join(r["id"] for r in rows if not r["correct"]) or "-"),
        "Gagal sitasi              : " + (", ".join(r["id"] for r in rows if not r["page_ok"]) or "-"),
    ]
    print("\n".join(summary))

    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    path = RESULTS_DIR / f"calc_test_{args.collection}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
    lines = ["# Uji Soal Hitungan (kalkulator + sitasi)", "",
             f"Koleksi: `{args.collection}` | kandidat retriever: {args.candidates}", "", "```"]
    for block in report:
        lines += block
    lines += summary + ["```"]
    path.write_text("\n".join(lines), encoding="utf-8")
    print(f"\nLaporan: {path}")


if __name__ == "__main__":
    main()
