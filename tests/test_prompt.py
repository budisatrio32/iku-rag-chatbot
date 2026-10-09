"""
Unit test penyusunan konteks LLM (src/generation/prompt.py).

Setiap chunk IKU harus membawa nama resmi IKU-nya ke LLM. Tanpa nama itu LLM menebak
kepanjangan singkatan (kasus D13: "AEE = Angka Efisiensi Mahasiswa", seharusnya Edukasi).
"""

import json
from pathlib import Path

import pytest

from prompt import NAMA_IKU, SYSTEM_PROMPT, build_context, label_iku

PROJECT_ROOT = Path(__file__).resolve().parents[1]
CHUNKS = [json.loads(baris) for baris in
          (PROJECT_ROOT / "data" / "chunks" / "chunks.jsonl").read_text(encoding="utf-8").splitlines()]


def test_setiap_iku_id_di_chunk_punya_nama_resmi():
    tanpa_nama = sorted({c["iku_id"] for c in CHUNKS if c.get("iku_id")} - set(NAMA_IKU))
    assert not tanpa_nama, f"tambahkan nama untuk iku_id ini di data/metadata/iku_names.json: {tanpa_nama}"


@pytest.mark.parametrize("iku_id, harapan", [
    ("1", "IKU 1 – Angka Efisiensi Edukasi Perguruan Tinggi (AEE PT)"),
    ("11b", "IKU 11b – Predikat SAKIP Perguruan Tinggi (IKU 11.2)"),
    ("LLDIKTI-3", "IKU 3 LLDIKTI – Predikat SAKIP dan Zona Integritas (WBK/WBBM) LLDIKTI"),
    ("99", "IKU 99"),
])
def test_label_iku(iku_id, harapan):
    assert label_iku(iku_id) == harapan


def test_instruksi_sistem_memuat_daftar_iku_pt():
    # kasus D11: LLM harus tahu bahwa "lulusan bekerja" adalah IKU 2 walau konteksnya hanya IKU 1
    assert f"- IKU 2: {NAMA_IKU['2']}" in SYSTEM_PROMPT
    assert f"- IKU 12: {NAMA_IKU['12']}" in SYSTEM_PROMPT
    assert "LLDIKTI" not in SYSTEM_PROMPT.split("DAFTAR IKU PERGURUAN TINGGI:")[1]


def test_konteks_definisi_iku1_memuat_kepanjangan_aee():
    chunk = next(c for c in CHUNKS if c["chunk_id"] == "BUKU_0138")
    assert "Efisiensi Edukasi" not in chunk["content"], "kasus uji ini mengandaikan isi chunk tanpa nama IKU"
    assert "Angka Efisiensi Edukasi" in build_context([chunk])
