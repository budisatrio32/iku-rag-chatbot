"""
Unit test jembatan LLM -> kalkulator (src/generation/tools.py).

Model yang berbeda memanggil alat dengan format yang sedikit berbeda (nama alat terpotong,
argumen tidak dibungkus argumen_json, dsb.). Tes ini memastikan variasi yang wajar tetap
dihitung, dan yang benar-benar rusak dikembalikan sebagai pesan error yang jelas
(bukan crash), tanpa memanggil LLM sungguhan.
"""

import json

import pytest

from tools import NAMA_ALAT, jalankan_alat

RASIO_IKU5 = {"kode": "iku5", "pembilang": 30, "penyebut": 120}


def teks(obj) -> str:
    return json.dumps(obj)


@pytest.mark.parametrize("nama, argumen", [
    # format resmi: argumen_json berupa teks JSON
    (NAMA_ALAT, teks({"fungsi": "rasio", "argumen_json": teks(RASIO_IKU5)})),
    # argumen_json sudah berupa objek
    (NAMA_ALAT, teks({"fungsi": "rasio", "argumen_json": RASIO_IKU5})),
    # kunci 'argumen' alih-alih 'argumen_json'
    (NAMA_ALAT, teks({"fungsi": "rasio", "argumen": RASIO_IKU5})),
    # argumen langsung di tingkat atas
    (NAMA_ALAT, teks({"fungsi": "rasio", **RASIO_IKU5})),
    # nama alat terpotong / salah ketik (kasus H19 gpt-oss-120b), isi tetap jelas
    ("hit...", teks({"fungsi": "rasio", "argumen_json": teks(RASIO_IKU5)})),
    ("hitung-iku", teks({"fungsi": "rasio", "argumen_json": teks(RASIO_IKU5)})),
])
def test_variasi_format_tetap_dihitung(nama, argumen):
    out = jalankan_alat(nama, argumen)
    assert "error" not in out, out
    assert out["hasil"] == 25.0


@pytest.mark.parametrize("nama, argumen, potongan_pesan", [
    ("cari_web", teks({"q": "iku"}), "tidak dikenal"),
    (NAMA_ALAT, "{bukan json", "bukan JSON"),
    (NAMA_ALAT, teks({"fungsi": "rasio", "argumen_json": "{rusak"}), "bukan JSON"),
    (NAMA_ALAT, teks(["rasio"]), "objek JSON"),
    (NAMA_ALAT, teks({"fungsi": "iku99", "argumen_json": "{}"}), "tidak ada"),
    (NAMA_ALAT, teks({"fungsi": "rasio", "argumen_json": teks({"kode": "iku5", "a": 1, "b": 2})}),
     "Parameter yang benar"),
    (NAMA_ALAT, teks({"fungsi": "rasio", "argumen_json": teks({**RASIO_IKU5, "penyebut": 0})}), "lebih dari 0"),
])
def test_permintaan_rusak_jadi_pesan_error(nama, argumen, potongan_pesan):
    out = jalankan_alat(nama, argumen)
    assert "error" in out
    assert potongan_pesan in out["error"]


@pytest.mark.parametrize("kode, fungsi_benar", [
    # kasus asli laporan 2026-10-09: H11 (iku6), H26/H27 (iku9)
    ("iku6", "iku6"),
    ("iku9", "iku9"),
    ("IKU1", "iku1_aee_prodi"),
])
def test_rasio_untuk_iku_berfungsi_sendiri_diarahkan(kode, fungsi_benar):
    argumen = {"kode": kode, "pembilang": 200, "penyebut": 1250}
    out = jalankan_alat(NAMA_ALAT, teks({"fungsi": "rasio", "argumen_json": teks(argumen)}))
    assert "error" in out
    assert fungsi_benar in out["error"] and "Format:" in out["error"]
    assert f"- {fungsi_benar}:" in out["error"]  # contoh format argumen ikut dikirim


def test_kode_tak_dikenal_tetap_pesan_lama():
    out = jalankan_alat(NAMA_ALAT, teks({"fungsi": "rasio", "argumen_json": teks(
        {"kode": "iku99", "pembilang": 1, "penyebut": 2})}))
    assert "tidak dikenal" in out["error"]
