"""
Coba retriever secara interaktif.

    python src/retrieval/test_retrieval.py              # retriever v2 (koleksi pmpt_qa_v2)
    python src/retrieval/test_retrieval.py --lama       # retriever lama (koleksi pmpt_qa)
"""

import argparse
import sys

from retriever import Retriever


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--lama", action="store_true", help="pakai retriever & koleksi lama")
    parser.add_argument("--rerank", action="store_true", help="aktifkan reranker (unduh ±2 GB sekali)")
    args = parser.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    retriever = Retriever(top_k=5) if args.lama else Retriever.v2(top_k=5, rerank=args.rerank)

    question = input("Pertanyaan: ")

    results = retriever.search(question)

    print()
    print("=" * 70)
    print("HASIL RETRIEVAL")
    print("=" * 70)

    for i, result in enumerate(results, start=1):
        pages = (f"{result['page_start']}" if result["page_start"] == result["page_end"]
                 else f"{result['page_start']}–{result['page_end']}")
        print(f"\n--- RESULT {i} ---")
        print(f"Distance : {result['distance']:.4f}")
        print(f"Source   : {result['source_file']} ({result.get('doc_part') or '-'})")
        print(f"Page     : {pages}")
        print(f"IKU      : {result.get('iku_id') or '-'} ({result.get('jenis') or '-'}) | bagian: {result.get('bagian') or '-'}")
        print(f"Section  : {result['section_path']}")
        if result.get("also_in"):
            print(f"Juga di  : {'; '.join(result['also_in'])}")
        for note in result.get("source_notes", []):
            print(f"CATATAN SUMBER [{note['id']}]: {note['note']}")
        print(f"\n{result['content'][:1500]}")


if __name__ == "__main__":
    main()
