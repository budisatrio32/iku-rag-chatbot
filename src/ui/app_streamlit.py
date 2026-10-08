"""
app_streamlit.py
Demo chatbot IKU berbasis Streamlit, untuk dicoba teman/PO lewat tunnel (ngrok/Cloudflare).
BUKAN produk akhir: produk sesungguhnya adalah chatbot di dasbor Next.js (lihat
docs/02-desain/integrasi_backend.md). Tujuan demo ini mengumpulkan pertanyaan nyata
dan penilaian 👍/👎 untuk memperkaya test set.

Jalankan dari root project:
    streamlit run src/ui/app_streamlit.py

Pengaturan opsional di .env:
    DEMO_PASSWORD=...              kata sandi demo (kosong = tanpa kata sandi; WAJIB diisi bila dibuka ke publik)
    DEMO_MAKS_PERTANYAAN=15        batas pertanyaan per pengguna (sesi browser)

Semua tanya-jawab dan penilaian dicatat ke data/feedback/demo_log.jsonl (tidak di-commit).
"""

import json
import os
import sys
import threading
import time
import uuid
from datetime import datetime
from pathlib import Path

# model embedding sudah ada di cache: jangan cek ke HuggingFace setiap kali aplikasi dimuat
os.environ.setdefault("HF_HUB_OFFLINE", "1")

import openai  # noqa: E402
import streamlit as st  # noqa: E402

PROJECT_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(PROJECT_ROOT / "src" / "generation"))

from answer import Chatbot  # noqa: E402  (juga memuat .env lewat llm_client)

LOG_FILE = Path(os.getenv("DEMO_LOG_FILE", PROJECT_ROOT / "data" / "feedback" / "demo_log.jsonl"))
DEMO_PASSWORD = os.getenv("DEMO_PASSWORD", "")
MAKS_PERTANYAAN = int(os.getenv("DEMO_MAKS_PERTANYAAN", "15"))
CONTOH_PERTANYAAN = [
    "Apa itu IKU 1?",
    "Prodi S1 punya 200 mahasiswa, 40 lulus tepat 8 semester. Berapa AEE dan tingkat pencapaiannya?",
    "Pendapatan apa saja yang tidak dihitung di IKU 9?",
    "Dari 120 kerja sama, ada 30 luaran. Berapa capaian IKU 5?",
]

st.set_page_config(page_title="Asisten IKU (demo)", page_icon="🎓")


# ---------------------------------------------------------------------------
# Sumber daya bersama (dimuat sekali untuk semua pengguna)
# ---------------------------------------------------------------------------

@st.cache_resource(show_spinner="Memuat model retrieval dan LLM (sekali saja)...")
def muat_chatbot() -> tuple[Chatbot, threading.Lock]:
    # kunci: pertanyaan dari banyak pengguna diproses bergantian, agar GPU tidak berebut
    # dan batas token per menit LLM tidak terlampaui
    return Chatbot(), threading.Lock()


def catat(baris: dict) -> None:
    LOG_FILE.parent.mkdir(parents=True, exist_ok=True)
    with LOG_FILE.open("a", encoding="utf-8") as f:
        f.write(json.dumps({"waktu": datetime.now().isoformat(timespec="seconds"), **baris},
                           ensure_ascii=False, default=str) + "\n")


def simpan_penilaian(id_jawaban: str, kunci_widget: str) -> None:
    nilai = st.session_state.get(kunci_widget)
    if nilai is not None:
        catat({"tipe": "penilaian", "id": id_jawaban, "nilai": "suka" if nilai == 1 else "tidak_suka"})


# ---------------------------------------------------------------------------
# Tampilan
# ---------------------------------------------------------------------------

def tampilkan_jawaban(item: dict) -> None:
    st.markdown(item["jawaban"])
    if item.get("sitasi") or item.get("sumber_rumus"):
        with st.expander("Sumber"):
            for s in item.get("sitasi", []):
                st.markdown(f"- {s}")
            for s in item.get("sumber_rumus", []):
                st.markdown(f"- Rumus: {s}")
    langkah = [k["hasil"] for k in item.get("kalkulator", []) if "langkah" in k["hasil"]]
    if langkah:
        with st.expander("Langkah perhitungan (kalkulator)"):
            for h in langkah:
                st.code("\n".join(h["langkah"]), language=None)
                if h.get("catatan"):
                    st.caption(f"Catatan tafsir: {h['catatan']}")
    if item.get("peringatan"):
        st.caption("⚠️ " + " ".join(item["peringatan"]))
    if item.get("id"):
        kunci = f"nilai_{item['id']}"
        st.feedback("thumbs", key=kunci, on_change=simpan_penilaian, args=(item["id"], kunci))


def gerbang_kata_sandi() -> bool:
    if not DEMO_PASSWORD or st.session_state.get("masuk"):
        return True
    st.title("🎓 Asisten IKU (demo)")
    sandi = st.text_input("Kata sandi demo", type="password")
    if sandi:
        if sandi == DEMO_PASSWORD:
            st.session_state["masuk"] = True
            st.rerun()
        st.error("Kata sandi salah.")
    return False


def jawab(pertanyaan: str) -> dict:
    bot, kunci = muat_chatbot()
    mulai = time.perf_counter()
    try:
        with kunci:
            hasil = bot.ask(pertanyaan)
    except openai.RateLimitError:
        item = {"jawaban": "Maaf, jatah pemakaian LLM sedang habis. Silakan coba lagi nanti.", "error": "429"}
    except (openai.APITimeoutError, openai.APIConnectionError):
        item = {"jawaban": "Maaf, layanan LLM tidak dapat dihubungi. Silakan coba lagi.", "error": "koneksi"}
    except openai.APIStatusError as e:
        item = {"jawaban": "Maaf, layanan LLM sedang bermasalah. Silakan coba lagi nanti.",
                "error": str(e.status_code)}
    else:
        item = None
    if item:  # error tetap dicatat agar terlihat seberapa sering demo gagal karena kuota/server
        catat({"tipe": "error", "pertanyaan": pertanyaan, "model": bot.model, "error": item["error"]})
        return item
    item = {k: hasil[k] for k in ("jawaban", "sitasi", "sumber_rumus", "kalkulator", "peringatan")}
    item["id"] = uuid.uuid4().hex[:12]
    catat({"tipe": "tanya_jawab", "id": item["id"], "pertanyaan": pertanyaan, "model": bot.model,
           "durasi_detik": round(time.perf_counter() - mulai, 1), **item})
    return item


def main() -> None:
    if not gerbang_kata_sandi():
        return

    riwayat = st.session_state.setdefault("riwayat", [])
    sisa = MAKS_PERTANYAAN - sum(1 for m in riwayat if m["peran"] == "user")

    with st.sidebar:
        st.header("Tentang demo ini")
        st.markdown(
            "Chatbot menjawab pertanyaan tentang **IKU Diktisaintek Berdampak** dari Buku IKU V1, "
            "lengkap dengan **sitasi halaman**. Perhitungan dikerjakan kalkulator rumus, bukan oleh AI.\n\n"
            "- Setiap pertanyaan dijawab terpisah (belum mengingat percakapan sebelumnya).\n"
            "- Jawaban dibuat AI: **periksa sebelum dipakai untuk pelaporan**.\n"
            "- Pertanyaan dan penilaian 👍/👎 **dicatat** untuk pengembangan. "
            "Jangan menulis data pribadi atau data internal kampus."
        )
        st.caption(f"Sisa pertanyaan di sesi ini: {max(sisa, 0)}")
        st.subheader("Contoh pertanyaan")
        for i, contoh in enumerate(CONTOH_PERTANYAAN):
            if st.button(contoh, key=f"contoh_{i}", width="stretch"):
                st.session_state["pertanyaan_contoh"] = contoh

    st.title("🎓 Asisten IKU (demo)")
    for pesan in riwayat:
        with st.chat_message(pesan["peran"]):
            if pesan["peran"] == "user":
                st.markdown(pesan["teks"])
            else:
                tampilkan_jawaban(pesan["isi"])

    pertanyaan = st.chat_input("Tanyakan definisi, kriteria, atau hitungan IKU...", max_chars=2000,
                               disabled=sisa <= 0)
    pertanyaan = pertanyaan or st.session_state.pop("pertanyaan_contoh", None)
    if sisa <= 0:
        st.info("Batas pertanyaan untuk sesi ini sudah tercapai. Terima kasih sudah mencoba!")
    if not pertanyaan or sisa <= 0:
        return

    pertanyaan = pertanyaan.strip()[:2000]
    riwayat.append({"peran": "user", "teks": pertanyaan})
    with st.chat_message("user"):
        st.markdown(pertanyaan)
    with st.chat_message("assistant"):
        with st.spinner("Mencari di Buku IKU dan menyusun jawaban..."):
            item = jawab(pertanyaan)
        tampilkan_jawaban(item)
    riwayat.append({"peran": "assistant", "isi": item})
    if sisa <= 1:
        st.rerun()  # batas tercapai: muat ulang agar kolom pertanyaan langsung terkunci


main()
