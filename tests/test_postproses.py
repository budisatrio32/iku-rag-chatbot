"""
Unit test perapian jawaban LLM (src/generation/postproses.py).

Kasus diambil dari jawaban asli openai/gpt-oss-120b di laporan evaluasi 2026-10-09:
rujukan gaya bawaan model (【3】, 【2†L1-L3】) dan spasi khusus (U+202F) membuat
sitasi dan fakta kunci tidak terbaca walaupun isi jawabannya benar.
"""

import pytest

from postproses import rapikan_jawaban


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
