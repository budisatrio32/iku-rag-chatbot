"""
Unit test pembacaan nominal uang di kalkulator (baca_nominal, iku9, iku12).

Kasus H27 (laporan 2026-10-10): LLM membaca "0,2 M" sebagai 0,2 juta (M = million) sehingga
capaian IKU 9 menjadi 15,01%, seharusnya 25%. Sejak itu LLM mengirim nominal persis seperti
di pertanyaan dan kalkulator yang mengubahnya ke rupiah. Format di sini diambil dari soal
ketahanan H25-H29.
"""

import pytest

from iku_formulas import baca_nominal, iku9, iku12_penghasilan_minimum


@pytest.mark.parametrize("teks, rupiah", [
    ("Rp1.250.000.000", 1_250_000_000),   # H26
    ("900jt", 900_000_000),
    ("150 juta", 150_000_000),
    ("Rp50.000.000", 50_000_000),
    ("0,2 M", 200_000_000),               # H27: M = miliar, bukan million
    ("1,5 M", 1_500_000_000),
    ("2 milyar", 2_000_000_000),
    ("2 miliar", 2_000_000_000),
    ("300M", 300_000_000_000),            # H25
    ("80 M", 80_000_000_000),
    ("3,5jt", 3_500_000),                 # H28
    ("Rp 4.250.000", 4_250_000),          # H29
    ("Rp. 2.500.000", 2_500_000),
    ("Rp1.000.000,-", 1_000_000),
    ("500 juta rupiah", 500_000_000),
    ("1.5 M", 1_500_000_000),             # titik + 1 angka = desimal
    ("4.250", 4_250),                     # titik + 3 angka = ribuan
    ("1.250.000,5", 1_250_000.5),
    ("10 rb", 10_000),
    ("1 T", 1_000_000_000_000),
    (1_250_000_000, 1_250_000_000),       # angka biasa tetap diterima
    (2.5, 2.5),
])
def test_baca_nominal(teks, rupiah):
    assert baca_nominal(teks, "x")[0] == pytest.approx(rupiah)


@pytest.mark.parametrize("teks", ["dua juta", "300 jeti", "1.2.3", "Rp", "", True])
def test_nominal_tak_terbaca_jadi_pesan_error(teks):
    with pytest.raises(ValueError):
        baca_nominal(teks, "x")


@pytest.mark.parametrize("total, rincian, harapan", [
    ("500 M", {"ukt": "300M", "boptn": "80 M", "hibah_riset": "50M", "konsultasi": "40 M",
               "unit_bisnis": "20 M", "hasil_dana_abadi": "10 M"}, 24.0),                       # H25
    ("Rp1.250.000.000", {"ukt": "900jt", "kontrak_riset": "150 juta", "royalti": "Rp50.000.000",
                         "boptn": "150jt"}, 16.0),                                                # H26
    ("2 milyar", {"hibah_riset": "300 jt", "konsultasi": "0,2 M", "ukt": "1,5 M"}, 25.0),         # H27
])
def test_iku9_dengan_nominal_teks(total, rincian, harapan):
    out = iku9(total, rincian)
    assert out["hasil"] == pytest.approx(harapan)
    assert not any("selisih" in langkah for langkah in out["langkah"])  # semua pos tercatat


def test_iku9_menampilkan_konversi_nominal():
    langkah = iku9("2 milyar", {"hibah_riset": "300 jt", "konsultasi": "0,2 M", "ukt": "1,5 M"})["langkah"]
    assert any('"0,2 M" = Rp200.000.000' in baris for baris in langkah)


def test_iku9_selisih_rincian_ditampilkan():
    # salah baca seperti H27 (konsultasi 0,2 alih-alih 200) jadi terlihat sebagai selisih
    langkah = iku9(2000, {"hibah_riset": 300, "konsultasi": 0.2, "ukt": 1500})["langkah"]
    assert any("selisih 199,8" in baris for baris in langkah)


def test_iku9_campuran_teks_dan_angka_ditolak():
    with pytest.raises(ValueError, match="tercampur"):
        iku9("2 milyar", {"hibah_riset": 300, "ukt": "1,5 M"})


@pytest.mark.parametrize("ump, jabatan, harapan", [
    ("3,5jt", ["lektor_kepala"], {"lektor_kepala": 14_000_000}),                                  # H28
    ("Rp 4.250.000", ["asisten_ahli", "profesor"], {"asisten_ahli": 6_375_000, "profesor": 25_500_000}),  # H29
])
def test_iku12_dengan_nominal_teks(ump, jabatan, harapan):
    assert iku12_penghasilan_minimum(ump, jabatan)["hasil"] == pytest.approx(harapan)
