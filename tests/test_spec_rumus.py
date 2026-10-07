"""
Uji konsistensi spec rumus (src/calculator/spec/buku_iku_v1.json) dengan kalkulator.

Tujuannya: spec boleh dibaca tim lain (BE/FE), jadi isinya harus lengkap dan
selalu cocok dengan fungsi Python. Bila ada yang menambah rumus di spec tanpa
fungsi, atau sebaliknya, tes ini gagal.
"""

import re

import pytest

from iku_formulas import REGISTRY, RUMUS, SPEC, daftar_rumus, hitung

FIELD_WAJIB = {"id", "fungsi", "pola", "ikuCode", "jenis", "nama", "formula_teks", "sumber", "catatan", "status"}
POLA = {"rasio", "berbobot", "khusus", "klasifikasi"}
STATUS = {"terverifikasi", "ada_tafsir", "perlu_konfirmasi_po"}
JUMLAH_HALAMAN_BUKU = 143


@pytest.mark.parametrize("rumus", SPEC["rumus"], ids=[r["id"] for r in SPEC["rumus"]])
def test_entri_spec_lengkap(rumus):
    assert FIELD_WAJIB <= set(rumus), f"field hilang: {FIELD_WAJIB - set(rumus)}"
    assert rumus["pola"] in POLA
    assert rumus["status"] in STATUS
    assert re.fullmatch(r"IKU \d{3}", rumus["ikuCode"]), "ikuCode harus format dasbor, mis. 'IKU 001'"
    assert rumus["formula_teks"], "formula_teks tidak boleh kosong"
    halaman = rumus["sumber"]["halaman"]
    assert halaman and all(isinstance(h, int) and 1 <= h <= JUMLAH_HALAMAN_BUKU for h in halaman)
    if rumus["status"] == "ada_tafsir":
        assert rumus["catatan"], "rumus dengan tafsir wajib punya catatan"


@pytest.mark.parametrize("rumus", SPEC["rumus"], ids=[r["id"] for r in SPEC["rumus"]])
def test_spec_menunjuk_fungsi_yang_ada(rumus):
    assert rumus["fungsi"] in REGISTRY
    if rumus["pola"] == "rasio":
        assert rumus["fungsi"] == "rasio"
        assert {"pembilang", "penyebut"} <= set(rumus["input"])
    else:
        assert rumus["id"] == rumus["fungsi"]


def test_setiap_fungsi_punya_entri_spec():
    tanpa_spec = {f for f in REGISTRY if f != "rasio"} - set(RUMUS)
    assert not tanpa_spec, f"fungsi tanpa entri spec: {tanpa_spec}"


def test_id_rumus_unik():
    ids = [r["id"] for r in SPEC["rumus"]]
    assert len(ids) == len(set(ids))


@pytest.mark.parametrize("kode", [r["id"] for r in SPEC["rumus"] if r["pola"] == "rasio"])
def test_semua_rasio_bisa_dihitung(kode):
    out = hitung("rasio", kode=kode, pembilang=1, penyebut=4)
    assert out["hasil"] == 25.0
    assert out["id"] == kode and out["ikuCode"] == RUMUS[kode]["ikuCode"]
    assert re.search(r"hlm\.\s*\d+", out["sumber"])


def test_keluaran_membawa_metadata_spec():
    out = hitung("iku1_aee_pt", realisasi_per_jenjang={"S1": 20})
    assert out["ikuCode"] == "IKU 001"
    assert out["rujukan"]["halaman"] == [49, 50]
    assert out["sumber"].endswith("hlm. 49–50")
    assert out["formula_teks"] == RUMUS["iku1_aee_pt"]["formula_teks"]


def test_daftar_rumus_per_iku():
    assert {r["id"] for r in daftar_rumus("IKU 001")} == {"iku1_aee_prodi", "iku1_aee_pt"}
    assert len(daftar_rumus()) == len(SPEC["rumus"])


@pytest.mark.parametrize("fungsi, argumen", [
    ("rasio", {"kode": "iku5", "pembilang": 10, "penyebut": 0}),
    ("rasio", {"kode": "iku5", "pembilang": -1, "penyebut": 10}),
    ("rasio", {"kode": "iku99", "pembilang": 1, "penyebut": 10}),
    ("iku1_aee_prodi", {"jenjang": "S9", "lulus_tepat_waktu": 1, "total_mahasiswa": 10}),
    ("iku1_aee_prodi", {"jenjang": "S1", "lulus_tepat_waktu": 50, "total_mahasiswa": 40}),
    ("iku1_aee_prodi", {"jenjang": "S1", "lulus_tepat_waktu": 0, "total_mahasiswa": 10, "drop_out": 10}),
    ("iku1_aee_pt", {"realisasi_per_jenjang": {}}),
    ("iku2", {"total_responden": 100, "kategori": {"bekerja_<6bln_>1.2ump": 120}}),
    ("iku2", {"total_responden": 100, "kategori": {"kategori_ngawur": 10}}),
    ("iku6", {"total_publikasi": 0, "publikasi": {"q1": 1}}),
    ("iku9", {"total_pendapatan": 100, "rincian": {"hibah_riset": 150}}),
    ("iku11b_predikat", {"nilai_akhir": 120}),
    ("iku12_penghasilan_minimum", {"ump": 3000000, "jabatan": ["rektor"]}),
])
def test_input_tidak_valid_ditolak(fungsi, argumen):
    with pytest.raises(ValueError):
        hitung(fungsi, **argumen)
