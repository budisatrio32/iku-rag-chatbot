"""
Unit test penyambungan potongan tabel (src/retrieval/sambung_tabel.py), memakai chunk asli.

Kasus D04: tabel daftar IKU hlm. 48 terpotong menjadi BUKU_0136 (IKU 1-9) dan BUKU_0137
(IKU 10-12 + "IKU wajib sebanyak 7"). Saat BUKU_0137 terambil, BUKU_0136 harus ikut.
"""

import json
from pathlib import Path

from sambung_tabel import cari_lanjutan_tabel, gabung_tabel

PROJECT_ROOT = Path(__file__).resolve().parents[1]
CHUNKS = [json.loads(baris) for baris in
          (PROJECT_ROOT / "data" / "chunks" / "chunks.jsonl").read_text(encoding="utf-8").splitlines()]
PER_ID = {c["chunk_id"]: c for c in CHUNKS}
PETA = cari_lanjutan_tabel([c["chunk_id"] for c in CHUNKS], [c["text"] for c in CHUNKS], CHUNKS)


def test_tabel_daftar_iku_hlm48_dikenali_sebagai_lanjutan():
    assert PETA["BUKU_0137"] == "BUKU_0136"
    assert PETA["PPT_0104"] == "PPT_0103"


def test_chunk_iku_dan_chunk_biasa_tidak_disambung():
    assert not any(PER_ID[b].get("iku_id") or PER_ID[a].get("iku_id") for b, a in PETA.items())
    assert "BUKU_0136" not in PETA  # awal tabel, bukan lanjutan
    assert "BUKU_0138" not in PETA  # definisi IKU 1 sesudah tabel


def test_gabungan_memuat_tabel_utuh_dengan_satu_judul_kolom():
    gabungan = gabung_tabel(PER_ID["BUKU_0136"]["text"], PER_ID["BUKU_0137"]["text"])
    for isi in ("2. Persentase lulusan", "9. Persentase Pendapatan Non Pendidikan/UKT",
                "12. Ketersediaan perencanaan strategis", "sebanyak 7 (tujuh)"):
        assert isi in gabungan
    assert gabungan.count("| No | Sasaran |") == 1
    assert gabungan.count("[Buku IKU") == 1


def test_teks_tanpa_tabel_tidak_berubah_bentuk():
    awal = "[Buku | hlm. 1]\n| A | B |\n| --- | --- |\n| 1 | 2 |"
    lanjutan = "[Buku | hlm. 2]\nCatatan biasa."
    assert gabung_tabel(awal, lanjutan) == awal + "\nCatatan biasa."
