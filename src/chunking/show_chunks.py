"""
show_chunks.py
Tampilkan isi chunk hasil chunk_structured.py untuk diperiksa secara manual.

Contoh (jalankan dari root project):
    python src/chunking/show_chunks.py --iku 3 --bagian Formula
    python src/chunking/show_chunks.py --iku 1 --jenis sub_indikator
    python src/chunking/show_chunks.py --iku LLDIKTI-2
    python src/chunking/show_chunks.py --cari "Dana Abadi" --sumber PPT
    python src/chunking/show_chunks.py --id BUKU_0152
    python src/chunking/show_chunks.py --catatan            # chunk yang membawa catatan cacat sumber
"""

import argparse
import json
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
CHUNKS_FILE = PROJECT_ROOT / "data" / "chunks" / "chunks.jsonl"


def main():
    parser = argparse.ArgumentParser(description="Tampilkan chunk v2")
    parser.add_argument("--chunks", type=Path, default=CHUNKS_FILE)
    parser.add_argument("--id", help="chunk_id, mis. BUKU_0152")
    parser.add_argument("--iku", help="iku_id, mis. 3, 11b, LLDIKTI-2")
    parser.add_argument("--bagian", help="Definisi / Kriteria / Ketentuan / Formula")
    parser.add_argument("--jenis", help="iku / sub_indikator / iku_lldikti")
    parser.add_argument("--sumber", choices=["Buku", "PPT"], help="filter dokumen sumber")
    parser.add_argument("--lampiran", action="store_true", help="hanya chunk Lampiran SK")
    parser.add_argument("--cari", help="kata/frasa yang harus ada di teks chunk (tidak peka huruf besar)")
    parser.add_argument("--catatan", action="store_true", help="hanya chunk yang membawa source_notes")
    parser.add_argument("--maks", type=int, default=5, help="jumlah chunk maksimal yang ditampilkan")
    args = parser.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    chunks = [json.loads(l) for l in args.chunks.read_text(encoding="utf-8").splitlines() if l.strip()]
    found = [
        c for c in chunks
        if (not args.id or c["chunk_id"] == args.id)
        and (not args.iku or (c.get("iku_id") or "").lower() == args.iku.lower())
        and (not args.bagian or (c.get("bagian") or "").lower() == args.bagian.lower())
        and (not args.jenis or c.get("jenis") == args.jenis)
        and (not args.sumber or c["source_file"].startswith(args.sumber))
        and (not args.lampiran or c["doc_part"] == "lampiran")
        and (not args.cari or args.cari.lower() in c["text"].lower())
        and (not args.catatan or c["source_notes"])
    ]

    print(f"Ditemukan {len(found)} chunk (ditampilkan maks {args.maks})")
    for c in found[:args.maks]:
        print("\n" + "=" * 100)
        print(f"{c['chunk_id']} | {c['n_tokens']} token | {c['source_file']} (prioritas {c['source_priority']}) | "
              f"{c['doc_part']} | jenis={c.get('jenis')} | iku_id={c.get('iku_id')} | bagian={c.get('bagian')} | "
              f"hlm {c['page_start']}-{c['page_end']}")
        for note in c["source_notes"]:
            print(f"CATATAN SUMBER [{note['id']}]: {note['note']}")
        print("-" * 100)
        print(c["text"])


if __name__ == "__main__":
    main()
