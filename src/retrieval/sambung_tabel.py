"""
sambung_tabel.py
Tabel panjang kadang terpotong menjadi beberapa chunk saat chunking (batas 512 token).
Potongan lanjutan hanya berisi baris akhir tabel + catatan kakinya, tanpa baris awal.

Kasus D04 (laporan evaluasi 2026-10-09): tabel daftar IKU hlm. 48 terpotong menjadi
BUKU_0136 (IKU 1-9 bertanda wajib) dan BUKU_0137 (IKU 10-12 + "IKU wajib sebanyak 7").
Pertanyaan "IKU apa saja yang wajib" hanya mengambil BUKU_0137, sehingga IKU 2 dan IKU 9
tidak pernah terbaca LLM.

Solusinya di sisi retrieval (index/embedding TIDAK diubah): bila potongan lanjutan
terambil, potongan tepat sebelumnya ikut disambungkan (maksimal 1) agar LLM melihat
tabelnya utuh. Chunk tabel definisi per IKU (punya iku_id) tidak disentuh karena
potongannya sudah dikumpulkan oleh tahap dedupe di retriever.
"""

SEPARATOR_PREFIX = "| ---"


def isi_tanpa_judul(dokumen: str) -> list[str]:
    """Baris isi chunk tanpa baris judul konteks '[Buku ... | hlm. 48]' di awal."""
    baris = dokumen.splitlines()
    if baris and baris[0].startswith("["):
        baris = baris[1:]
    while baris and not baris[0].strip():
        baris = baris[1:]
    return baris


def header_tabel_terakhir(dokumen: str) -> str | None:
    """Baris judul kolom dari tabel terakhir di chunk (baris '|' yang diikuti '| --- |')."""
    baris = dokumen.splitlines()
    for i in range(len(baris) - 2, -1, -1):
        if baris[i].startswith("|") and baris[i + 1].startswith(SEPARATOR_PREFIX):
            return baris[i].strip()
    return None


def cari_lanjutan_tabel(ids: list[str], dokumen: list[str], metadata: list[dict]) -> dict[str, str]:
    """Peta id potongan lanjutan -> id potongan sebelumnya.

    Syarat: berurutan dalam dokumen yang sama, seksi sama, keduanya bukan chunk IKU,
    dan chunk kedua langsung dibuka dengan judul kolom yang sama dengan tabel terakhir
    di chunk pertama."""
    data = sorted(zip(ids, dokumen, metadata), key=lambda x: x[0])
    peta = {}
    for (id_a, dok_a, meta_a), (id_b, dok_b, meta_b) in zip(data, data[1:]):
        if id_a.split("_")[0] != id_b.split("_")[0]:
            continue
        if meta_a.get("iku_id") or meta_b.get("iku_id"):
            continue
        if meta_a.get("section_path") != meta_b.get("section_path"):
            continue
        header = header_tabel_terakhir(dok_a)
        isi_b = isi_tanpa_judul(dok_b)
        if header and isi_b and isi_b[0].strip() == header:
            peta[id_b] = id_a
    return peta


def gabung_tabel(dokumen_awal: str, dokumen_lanjutan: str) -> str:
    """Sambung dua potongan menjadi satu tabel: judul konteks dan judul kolom potongan
    lanjutan dibuang agar tabelnya terbaca sebagai satu kesatuan."""
    isi = isi_tanpa_judul(dokumen_lanjutan)
    if len(isi) >= 2 and isi[0].strip() == header_tabel_terakhir(dokumen_awal) \
            and isi[1].startswith(SEPARATOR_PREFIX):
        isi = isi[2:]
    return dokumen_awal.rstrip() + "\n" + "\n".join(isi)
