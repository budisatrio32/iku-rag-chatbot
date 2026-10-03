"""
chat_cli.py
Tanya-jawab dengan chatbot IKU di terminal.

    python src/generation/chat_cli.py
    python src/generation/chat_cli.py --detail     # tampilkan juga argumen kalkulator & chunk
"""

import argparse
import sys

from answer import Chatbot, tampilkan


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--detail", action="store_true", help="tampilkan argumen kalkulator dan chunk")
    args = parser.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    print("Memuat retriever dan LLM...")
    bot = Chatbot()
    print(f"Siap (model: {bot.model}). Ketik pertanyaan, atau Enter kosong untuk keluar.\n")

    while True:
        question = input("Pertanyaan: ").strip()
        if not question:
            break
        hasil = bot.ask(question)
        print("\n" + tampilkan(hasil))
        if args.detail:
            for k in hasil["kalkulator"]:
                print(f"\n[kalkulator] argumen: {k['argumen']}\n[kalkulator] hasil  : {k['hasil'].get('hasil', k['hasil'])}")
            for i, c in enumerate(hasil["chunks"], start=1):
                print(f"[chunk {i}] {c['chunk_id']} | hlm {c['page_start']}-{c['page_end']} | IKU {c.get('iku_id')} {c.get('bagian') or ''}")
        print("\n" + "-" * 80 + "\n")


if __name__ == "__main__":
    main()
