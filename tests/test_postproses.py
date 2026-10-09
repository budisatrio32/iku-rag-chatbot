"""
Unit test perapian jawaban LLM (src/generation/postproses.py).

Kasus diambil dari jawaban asli openai/gpt-oss-120b di laporan evaluasi 2026-10-09:
rujukan gaya bawaan model (【3】, 【2†L1-L3】) dan spasi khusus (U+202F) membuat
sitasi dan fakta kunci tidak terbaca walaupun isi jawabannya benar.
"""

import pytest

from postproses import rapikan_jawaban, tampak_menghitung_sendiri


@pytest.mark.parametrize("asli, harapan", [
    ("lulus tepat waktu【3】.", "lulus tepat waktu[3]."),
    ("semakin rendah semakin baik【2†L1-L3】.", "semakin rendah semakin baik[2]."),
    ("predikat A【1†L1-L4】【2†L1-L4】.", "predikat A[1][2]."),
    ("AEE ideal: 33 %", "AEE ideal: 33 %"),
    ("SDG 1, SDG 4", "SDG 1, SDG 4"),
    ("start‑up", "start-up"),
    ("sudah benar [1][2].", "sudah benar [1][2]."),
])
def test_rapikan_jawaban(asli, harapan):
    assert rapikan_jawaban(asli) == harapan


def test_teks_lain_dalam_kurung_khusus_tidak_diubah():
    assert rapikan_jawaban("catatan【lihat lampiran】") == "catatan【lihat lampiran】"


# potongan jawaban asli laporan 2026-10-09 yang dibuat TANPA kalkulator
@pytest.mark.parametrize("pertanyaan, jawaban", [
    ("Berapa capaian IKU 3?", r"\[ \text{IKU 3} = \frac{\sum n_i k_i}{t} \times 100\% \]"),        # H07
    ("Berapa capaian IKU 3?", "| Juara 2 tingkat provinsi | 4 | 0,2 | 4 × 0,2 = 0,8 |"),          # H08
    ("Nilai akhir evaluasi SAKIP sebuah PT adalah 82. Apa predikatnya?",
     "nilai akhir 82 berada pada rentang 80-89, sehingga predikatnya adalah A (Sangat Baik)[2]."),  # H16
    ("Dari 120 kerja sama, 30 luaran. Berapa IKU 5?", "Capaiannya 30 ÷ 120 × 100% = 25%."),
])
def test_hitung_sendiri_terdeteksi(pertanyaan, jawaban):
    assert tampak_menghitung_sendiri(pertanyaan, jawaban)


@pytest.mark.parametrize("pertanyaan, jawaban", [
    # D11: menjelaskan rumus dengan kata dan meminta data, tanpa menghitung
    ("Lulusan 400, yang bekerja 280, berapa capaian IKU 1?",
     "AEE = (Jumlah mahasiswa yang lulus tepat waktu ÷ Total mahasiswa) × 100 % [1]. "
     "Silakan sediakan data (misalnya: D3 – lulus 40 / total 120)."),
    ("Berapa besaran UKT di Universitas Gadjah Mada tahun 2026?",
     "Informasinya tidak ditemukan di dokumen IKU."),                                               # D12
    ("Apa saja predikat SAKIP?", "Predikat SAKIP terdiri atas AA, A, BB, B, CC, C, dan D [1]."),
    ("Berapa masa tempuh kurikulum S1?", "Masa tempuh S1 adalah 8 semester dengan AEE ideal 25% [1]."),
])
def test_jawaban_tanpa_hitungan_tidak_terdeteksi(pertanyaan, jawaban):
    assert not tampak_menghitung_sendiri(pertanyaan, jawaban)
