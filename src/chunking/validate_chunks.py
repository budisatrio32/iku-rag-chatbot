"""
validate_chunks.py
Validasi otomatis output tahap CHUNKING (data/chunks/chunks.jsonl) terhadap
hasil processing (data/processed/*_processed.json).

Cek yang dilakukan:
1. Setiap blok processing tercatat di minimal satu chunk (block_ids)
2. Cakupan kata per blok: kata-kata blok harus ada di chunk yang mencatat blok tsb
3. Cakupan ANGKA per dokumen: tidak ada angka yang hilang dari processing ke chunk
4. Tidak ada chunk yang isinya hanya judul (heading-only)
5. Sebaran ukuran token (bge-m3) dan chunk yang melewati batas
6. Catatan cacat sumber (source_notes) ikut terbawa ke chunk

Jalankan dari root project:
    python src/chunking/validate_chunks.py
    python src/chunking/validate_chunks.py --max-tokens 512
"""

import argparse
import json
import re
import statistics
import sys
from collections import Counter
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
PROCESSED_DIR = PROJECT_ROOT / "data" / "processed"
CHUNKS_FILE = PROJECT_ROOT / "data" / "chunks" / "chunks.jsonl"
REPORT_FILE = PROJECT_ROOT / "reports" / "validation" / "chunks_v2_validation.json"

BLOCK_COVERAGE_MIN = 0.99


def words(text: str) -> Counter:
    return Counter(re.findall(r"\w+", text.lower()))


def numbers(text: str) -> Counter:
    return Counter(re.sub(r"[.,]", "", x) for x in re.findall(r"\d+(?:[.,]\d+)*", text))


def main():
    parser = argparse.ArgumentParser(description="Validasi chunk v2")
    parser.add_argument("--chunks", type=Path, default=CHUNKS_FILE)
    parser.add_argument("--max-tokens", type=int, default=512)
    args = parser.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    chunks = [json.loads(l) for l in args.chunks.read_text(encoding="utf-8").splitlines() if l.strip()]
    by_block: dict[str, list[dict]] = {}
    for c in chunks:
        for bid in c["block_ids"]:
            by_block.setdefault(bid, []).append(c)

    report = {"documents": {}, "chunks": {}}
    all_ok = True

    for path in sorted(PROCESSED_DIR.glob("*_processed.json")):
        blocks = json.loads(path.read_text(encoding="utf-8"))
        source = blocks[0]["source_file"]
        doc_chunks = [c for c in chunks if c["source_file"] == source]

        # 1) blok tercatat
        unassigned = [b["id"] for b in blocks if b["id"] not in by_block]

        # 2) cakupan kata per blok
        low = []
        for b in blocks:
            if b["id"] not in by_block:
                continue
            need = words(b["content"])
            if not need:            # blok tanpa kata (mis. garis pemisah '---')
                continue
            have = words("\n".join(c["text"] for c in by_block[b["id"]]))
            covered = sum(min(n, have[w]) for w, n in need.items()) / max(sum(need.values()), 1)
            if covered < BLOCK_COVERAGE_MIN:
                low.append({"block_id": b["id"], "page": b["page"], "coverage": round(covered, 3),
                            "missing": sorted((need - have).keys())[:15]})

        # 3) cakupan angka — judul bagian pindah ke header konteks chunk, jadi blok heading
        #    dicek terhadap teks lengkap (header + isi), blok lain terhadap isi saja
        missing_numbers = (
            numbers("\n".join(b["content"] for b in blocks if b["block_type"] != "heading"))
            - numbers("\n".join(c["content"] for c in doc_chunks))
        ) + (
            numbers("\n".join(b["content"] for b in blocks if b["block_type"] == "heading"))
            - numbers("\n".join(c["text"] for c in doc_chunks))
        )

        # 6) source_notes
        noted_blocks = {b["id"] for b in blocks if b.get("source_notes")}
        notes_lost = [bid for bid in noted_blocks
                      if not any(c["source_notes"] for c in by_block.get(bid, []))]

        ok = not unassigned and not low and not missing_numbers and not notes_lost
        all_ok &= ok
        report["documents"][source] = {
            "blocks": len(blocks),
            "chunks": len(doc_chunks),
            "blocks_not_in_any_chunk": unassigned,
            "blocks_low_word_coverage": low,
            "missing_numbers": dict(missing_numbers),
            "blocks_with_source_notes": len(noted_blocks),
            "source_notes_lost": notes_lost,
            "ok": ok,
        }
        print(f"\n=== {source} ===")
        print(f"  blok {len(blocks)} -> chunk {len(doc_chunks)}")
        print(f"  blok tidak masuk chunk mana pun : {len(unassigned)} {unassigned[:5]}")
        print(f"  blok cakupan kata < {BLOCK_COVERAGE_MIN:.0%}      : {len(low)} "
              f"{[(x['block_id'], x['coverage']) for x in low[:5]]}")
        print(f"  angka hilang                    : {sum(missing_numbers.values())} {dict(list(missing_numbers.items())[:10])}")
        print(f"  catatan sumber terbawa          : {len(noted_blocks) - len(notes_lost)}/{len(noted_blocks)}")
        print(f"  STATUS                          : {'OK' if ok else 'PERLU DICEK'}")

    # 4) & 5) kualitas chunk
    sizes = [c["n_tokens"] for c in chunks]
    heading_only = [c["chunk_id"] for c in chunks if len(re.findall(r"\w+", c["content"])) < 12]
    # chunk tabel definisi wajib tahu IKU-nya (bila tidak, pencarian "IKU 1" tidak akan menemukannya)
    no_iku = [(c["chunk_id"], c["page_start"], c["bagian"]) for c in chunks
              if c["bagian"] and c["bagian"] != "Isi" and not c["iku_id"]]
    # jalur bagian yang menyebut dua nomor IKU berbeda -> hierarki heading kemungkinan salah
    mixed_path = [(c["chunk_id"], c["page_start"]) for c in chunks
                  if len(set(re.findall(r"\bIKU\s*(\d+)\s*[:(]", c["section_path"]))) > 1]
    all_ok &= not no_iku and not mixed_path
    over = [(c["chunk_id"], c["n_tokens"]) for c in chunks if c["n_tokens"] > args.max_tokens]
    q = statistics.quantiles(sizes, n=20)
    report["chunks"] = {
        "total": len(chunks),
        "tokens_min": min(sizes), "tokens_median": statistics.median(sizes),
        "tokens_p95": q[18], "tokens_max": max(sizes),
        "chunks_over_max_tokens": over,
        "very_short_chunks(<12 kata)": heading_only,
        "definition_chunks_without_iku_id": no_iku,
        "section_path_with_mixed_iku": mixed_path,
        "per_jenis": dict(Counter(c.get("jenis") or "-" for c in chunks)),
        "per_bagian": dict(Counter(c["bagian"] or "-" for c in chunks)),
        "with_iku_id": sum(1 for c in chunks if c["iku_id"]),
    }
    print(f"\n=== Kualitas chunk ({len(chunks)} chunk) ===")
    print(f"  token bge-m3: min {min(sizes)} | median {statistics.median(sizes):.0f} | p95 {q[18]:.0f} | maks {max(sizes)}")
    print(f"  melewati {args.max_tokens} token : {len(over)} {over[:5]}")
    print(f"  chunk sangat pendek (<12 kata) : {len(heading_only)} {heading_only[:8]}")
    print(f"  per bagian: {report['chunks']['per_bagian']}")
    print(f"  chunk ber-iku_id: {report['chunks']['with_iku_id']} | per jenis: {report['chunks']['per_jenis']}")
    print(f"  chunk definisi tanpa iku_id     : {len(no_iku)} {no_iku[:6]}")
    print(f"  jalur bagian campur nomor IKU   : {len(mixed_path)} {mixed_path[:6]}")

    REPORT_FILE.parent.mkdir(parents=True, exist_ok=True)
    REPORT_FILE.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\nHASIL AKHIR: {'SEMUA OK - tidak ada informasi yang hilang' if all_ok else 'ADA YANG PERLU DICEK'}")
    print(f"Detail: {REPORT_FILE}")


if __name__ == "__main__":
    main()
