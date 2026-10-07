"""
chat_cli.py
Tanya-jawab dengan chatbot IKU di terminal.

    python src/generation/chat_cli.py
    python src/generation/chat_cli.py --detail     # tampilkan juga argumen kalkulator & chunk
"""

import argparse
import sys
import time

import openai

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
        mulai = time.perf_counter()
        try:
            hasil = bot.ask(question)
        except openai.RateLimitError:
            print("\n[!] Kuota Gemini habis (429). Tunggu beberapa saat, atau ganti LLM_MODEL di .env.\n")
            continue
        except openai.APITimeoutError:
            print("\n[!] Gemini tidak menjawab dalam batas waktu. Coba lagi.\n")
            continue
        except (openai.APIConnectionError, openai.APIStatusError) as e:
            print(f"\n[!] Gagal menghubungi LLM: {e}\n")
            continue
        print("\n" + tampilkan(hasil))
        print(f"\n(waktu jawab: {time.perf_counter() - mulai:.1f} detik)")
        if args.detail:
            for k in hasil["kalkulator"]:
                print(f"\n[kalkulator] argumen: {k['argumen']}\n[kalkulator] hasil  : {k['hasil'].get('hasil', k['hasil'])}")
            for i, c in enumerate(hasil["chunks"], start=1):
                print(f"[chunk {i}] {c['chunk_id']} | hlm {c['page_start']}-{c['page_end']} | IKU {c.get('iku_id')} {c.get('bagian') or ''}")
        print("\n" + "-" * 80 + "\n")



if __name__ == "__main__":
    main()
