"""
iku_formulas.py
Formula registry: rumus IKU dari Buku IKU Diktisaintek Berdampak V1 (Bab V)
ditulis sebagai fungsi Python yang deterministik.

Prinsip: LLM tidak menghitung sendiri. LLM cukup memilih fungsi dan mengisi
argumennya dari pertanyaan user; fungsi di sini yang menghitung, lalu
mengembalikan hasil, langkah perhitungan, dan sumber halaman untuk sitasi.

Setiap fungsi mengembalikan dict:
    hasil      : angka / teks akhir
    satuan     : satuan hasil
    langkah    : list langkah perhitungan yang bisa ditampilkan ke user
    sumber     : sitasi rumus di dokumen (halaman = nomor halaman file PDF)
    catatan    : keputusan tafsir untuk bagian dokumen yang ambigu (bila ada)

Bagian dokumen yang ambigu diputuskan secara eksplisit di sini (lihat CATATAN_*),
bukan ditebak ulang setiap kali.
"""

import math

BUKU = "Buku IKU Diktisaintek Berdampak V1"


def _pct(x: float) -> float:
    return round(x * 100, 2)


def _fmt(x: float) -> str:
    """Format angka gaya Indonesia: 1234.5 -> '1.234,5'."""
    s = f"{x:,.2f}".rstrip("0").rstrip(".")
    return s.replace(",", "#").replace(".", ",").replace("#", ".")


# ---------------------------------------------------------------------------
# IKU 1 — Angka Efisiensi Edukasi (AEE), hlm. 49–50
# ---------------------------------------------------------------------------

AEE_IDEAL = {   # Ketentuan d
    "D1": 100, "D2": 50, "D3": 33, "D4": 25, "S1": 25, "S2": 50, "S3": 33,
}
MASA_TEMPUH = {"D1": 2, "D2": 4, "D3": 6, "D4": 8, "S1": 8, "S2": 3, "S3": 6}   # semester


def iku1_aee_prodi(jenjang: str, lulus_tepat_waktu: int, total_mahasiswa: int,
                   pindah: int = 0, drop_out: int = 0, cuti_lebih: int = 0) -> dict:
    """AEE satu program pendidikan. Mahasiswa pindah, DO, dan cuti melebihi ketentuan
    TIDAK dihitung (Ketentuan c)."""
    jenjang = jenjang.upper()
    basis = total_mahasiswa - pindah - drop_out - cuti_lebih
    aee = lulus_tepat_waktu / basis
    ideal = AEE_IDEAL[jenjang]
    capaian = (aee * 100) / ideal
    langkah = []
    if basis != total_mahasiswa:
        langkah.append(f"Basis = {total_mahasiswa} − {pindah} pindah − {drop_out} DO − {cuti_lebih} cuti = {basis} "
                       f"(Ketentuan c: pindah/DO/cuti berlebih tidak dihitung)")
    langkah += [
        f"AEE realisasi = {lulus_tepat_waktu} / {basis} × 100% = {_fmt(_pct(aee))}%",
        f"AEE ideal {jenjang} = {ideal}% (masa tempuh {MASA_TEMPUH[jenjang]} semester)",
        f"Tingkat pencapaian = {_fmt(_pct(aee))}% / {ideal}% × 100% = {_fmt(round(capaian * 100, 2))}%",
    ]
    return {
        "hasil": {"aee_realisasi_pct": _pct(aee), "tingkat_pencapaian_pct": round(capaian * 100, 2)},
        "satuan": "%",
        "langkah": langkah,
        "sumber": f"{BUKU}, IKU 1 – Ketentuan & Formula a–b, hlm. 49",
    }


def iku1_aee_pt(realisasi_per_jenjang: dict[str, float]) -> dict:
    """AEE perguruan tinggi = rata-rata tingkat pencapaian semua program pendidikan (Formula c).
    realisasi_per_jenjang: {"D3": 30, "S1": 22.5, ...} dalam persen."""
    langkah, capaian = [], []
    for jenjang, realisasi in realisasi_per_jenjang.items():
        ideal = AEE_IDEAL[jenjang.upper()]
        c = realisasi / ideal * 100
        capaian.append(c)
        langkah.append(f"Tingkat pencapaian {jenjang} = {_fmt(realisasi)}% / {ideal}% = {_fmt(round(c, 2))}%")
    hasil = sum(capaian) / len(capaian)
    langkah.append(f"AEE PT = ({' + '.join(_fmt(round(c, 2)) + '%' for c in capaian)}) / {len(capaian)} "
                   f"= {_fmt(round(hasil, 2))}%")
    return {"hasil": round(hasil, 2), "satuan": "%", "langkah": langkah,
            "sumber": f"{BUKU}, IKU 1 – Formula c & contoh perhitungan, hlm. 49–50"}


# ---------------------------------------------------------------------------
# IKU 2 — Lulusan bekerja / studi lanjut / wirausaha, hlm. 51–52
# ---------------------------------------------------------------------------

BOBOT_IKU2 = {
    # bekerja setelah lulus (Kriteria b)
    "bekerja_<6bln_>1.2ump": 1.0,
    "bekerja_<1thn_>1.2ump": 0.8,
    "bekerja_<1thn_<1.2ump": 0.6,
    # wirausaha (Kriteria c)
    "founder_<6bln_>1.2ump": 1.2, "founder_>6bln_>1.2ump": 1.0,
    "founder_<6bln_<1.2ump": 0.8, "founder_>6bln_<1.2ump": 0.6,
    "freelancer_<6bln_>1.2ump": 0.5, "freelancer_>6bln_>1.2ump": 0.4,
    "freelancer_<6bln_<1.2ump": 0.3, "freelancer_>6bln_<1.2ump": 0.2,
    # melanjutkan studi (Kriteria d)
    "studi_lanjut_<12bln": 0.6,
    # sudah bekerja / berwirausaha sebelum lulus (Kriteria e, f)
    "bekerja_sebelum_lulus_>1.2ump": 1.0,
    "wirausaha_sebelum_lulus_>1.2ump": 1.0,
    "wirausaha_sebelum_lulus_<1.2ump": 0.6,
    # belum bekerja / studi / wirausaha
    "belum": 0.0,
}


def jumlah_berbobot(kategori: dict[str, int], bobot: dict[str, float], total: int) -> tuple[float, list[str]]:
    langkah, skor = [], 0.0
    for nama, n in kategori.items():
        k = bobot[nama]
        skor += n * k
        langkah.append(f"{nama}: {n} × {_fmt(k)} = {_fmt(round(n * k, 4))}")
    langkah.append(f"Σ(n·k) = {_fmt(round(skor, 4))}")
    langkah.append(f"Capaian = {_fmt(round(skor, 4))} / {total} × 100% = {_fmt(round(skor / total * 100, 2))}%")
    return round(skor / total * 100, 2), langkah


def iku2(total_responden: int, kategori: dict[str, int]) -> dict:
    hasil, langkah = jumlah_berbobot(kategori, BOBOT_IKU2, total_responden)
    return {"hasil": hasil, "satuan": "%", "langkah": langkah,
            "sumber": f"{BUKU}, IKU 2 – Kriteria b–f & Formula, hlm. 51–52"}


def iku2_responden_minimum(jumlah_lulusan: int, galat: float = 0.023) -> dict:
    """Rumus Slovin n = N / (N·d² + 1). Dokumen menulis '× 100%', tetapi hasil yang bermakna
    adalah jumlah orang, dibulatkan ke atas."""
    n = jumlah_lulusan / (jumlah_lulusan * galat ** 2 + 1)
    return {
        "hasil": math.ceil(n),
        "satuan": "responden",
        "langkah": [f"N·d² = {jumlah_lulusan} × {galat}² = {_fmt(round(jumlah_lulusan * galat ** 2, 4))}",
                    f"n = {jumlah_lulusan} / ({_fmt(round(jumlah_lulusan * galat ** 2, 4))} + 1) = {_fmt(round(n, 2))}",
                    f"Dibulatkan ke atas = {math.ceil(n)} responden"],
        "sumber": f"{BUKU}, IKU 2 – Formula Responden Minimum, hlm. 52",
        "catatan": "Dokumen menulis '× 100%' pada rumus Slovin; hasil diperlakukan sebagai jumlah orang.",
    }


# ---------------------------------------------------------------------------
# IKU 3 — Mahasiswa berkegiatan / berprestasi di luar prodi, hlm. 53–54
# ---------------------------------------------------------------------------

BOBOT_PRESTASI = {
    ("internasional", "juara1"): 1.0, ("internasional", "juara2_3_favorit"): 0.5,
    ("internasional", "harapan"): 0.3, ("internasional", "finalis"): 0.2,
    ("nasional", "juara1"): 0.6, ("nasional", "juara2_3_favorit"): 0.3,
    ("nasional", "harapan"): 0.2, ("nasional", "finalis"): 0.1,
    ("provinsi", "juara1"): 0.4, ("provinsi", "juara2_3_favorit"): 0.2,
    ("provinsi", "harapan"): 0.1, ("provinsi", "finalis"): 0.05,
}
CATATAN_SKS = ("Dokumen menulis '6 – 10 SKS = 0,6' dan '≥ 10 SKS = 1' sehingga 10 SKS tumpang-tindih; "
               "di sini 10 SKS diberi bobot 1.")


def bobot_sks(sks: int) -> float:
    if sks <= 5:
        return 0.4
    if sks < 10:
        return 0.6
    return 1.0


def iku3(total_mahasiswa: int, kegiatan: list[dict] | None = None, prestasi: list[dict] | None = None) -> dict:
    """kegiatan: [{"jumlah": 100, "sks": 20}, ...]
    prestasi: [{"jumlah": 5, "tingkat": "nasional", "peringkat": "juara1"}, ...]"""
    langkah, skor = [], 0.0
    for k in kegiatan or []:
        b = bobot_sks(k["sks"])
        skor += k["jumlah"] * b
        langkah.append(f"Kegiatan {k['sks']} SKS: {k['jumlah']} × {_fmt(b)} = {_fmt(round(k['jumlah'] * b, 4))}")
    for p in prestasi or []:
        b = BOBOT_PRESTASI[(p["tingkat"], p["peringkat"])]
        skor += p["jumlah"] * b
        langkah.append(f"Prestasi {p['peringkat']} {p['tingkat']}: {p['jumlah']} × {_fmt(b)} = "
                       f"{_fmt(round(p['jumlah'] * b, 4))}")
    hasil = skor / total_mahasiswa * 100
    langkah += [f"Σ(n·k) = {_fmt(round(skor, 4))}",
                f"Capaian = {_fmt(round(skor, 4))} / {total_mahasiswa} × 100% = {_fmt(round(hasil, 2))}%"]
    return {"hasil": round(hasil, 2), "satuan": "%", "langkah": langkah,
            "sumber": f"{BUKU}, IKU 3 – Formula & Ketentuan Bobot, hlm. 53–54",
            "catatan": CATATAN_SKS}


# ---------------------------------------------------------------------------
# IKU 6 — Publikasi bereputasi internasional, hlm. 63
# ---------------------------------------------------------------------------

BOBOT_PUBLIKASI = {"top_tier": 1.2, "q1": 1.0, "q2": 0.75, "q3": 0.5, "q4": 0.25,
                   "prosiding": 0.25, "tidak_terindeks": 0.0}
BONUS_KOLABORASI = 0.25
CATATAN_KOLABORASI = ("Dokumen: 'tambahan bobot sebesar 0,25 dari bobot dasar'. Di sini ditafsirkan +0,25 "
                      "(ditambahkan ke bobot dasar). Untuk Q1 (bobot dasar 1) kedua tafsiran (+0,25 dan +25%) sama.")


def iku6(total_publikasi: int, publikasi: dict[str, int], kolaborasi: dict[str, int] | None = None) -> dict:
    """publikasi: {"q1": 40, ...} (tanpa kolaborasi internasional)
    kolaborasi: {"q1": 4, ...} publikasi dengan penulis luar negeri (mendapat bonus)."""
    langkah, skor = [], 0.0
    for jenis, n in publikasi.items():
        k = BOBOT_PUBLIKASI[jenis]
        skor += n * k
        langkah.append(f"{jenis}: {n} × {_fmt(k)} = {_fmt(round(n * k, 4))}")
    for jenis, n in (kolaborasi or {}).items():
        k = BOBOT_PUBLIKASI[jenis] + BONUS_KOLABORASI
        skor += n * k
        langkah.append(f"{jenis} + kolaborasi internasional: {n} × ({_fmt(BOBOT_PUBLIKASI[jenis])} + "
                       f"{_fmt(BONUS_KOLABORASI)}) = {_fmt(round(n * k, 4))}")
    hasil = skor / total_publikasi * 100
    langkah += [f"Σ(n·k) = {_fmt(round(skor, 4))}",
                f"Capaian = {_fmt(round(skor, 4))} / {total_publikasi} × 100% = {_fmt(round(hasil, 2))}%"]
    out = {"hasil": round(hasil, 2), "satuan": "%", "langkah": langkah,
           "sumber": f"{BUKU}, IKU 6 – Kriteria (bobot kuartil) & Formula, hlm. 63"}
    if kolaborasi:
        out["catatan"] = CATATAN_KOLABORASI
    return out


# ---------------------------------------------------------------------------
# IKU dengan rumus rasio (a / b × 100%)
# ---------------------------------------------------------------------------

RASIO = {
    "iku4": ("Dosen ber-NUPTK yang mendapat rekognisi internasional", "Total dosen PT setahun terakhir",
             "IKU 4 – Formula, hlm. 62"),
    "iku5": ("Jumlah luaran (judul/karya) hasil kerja sama", "Total kerja sama PT",
             "IKU 5 – Formula & Keterangan, hlm. 57"),
    "iku7": ("Program/kegiatan berkontribusi pada SDG 1, 4, 17 + 2 SDG pilihan", "Total program SDGs PT",
             "IKU 7 – Formula, hlm. 58"),
    "iku8": ("SDM yang terlibat penyusunan kebijakan", "Total SDM PT dalam satu periode",
             "IKU 8 – Formula, hlm. 64"),
    "iku11d": ("Kegiatan pencegahan & penanganan yang terlaksana", "Total kegiatan yang direncanakan",
               "IKU 11d – Formula, hlm. 68"),
}


def rasio(kode: str, pembilang: float, penyebut: float) -> dict:
    nama_a, nama_b, sumber = RASIO[kode]
    hasil = pembilang / penyebut * 100
    return {"hasil": round(hasil, 2), "satuan": "%",
            "langkah": [f"({nama_a}) / ({nama_b}) × 100%",
                        f"= {_fmt(pembilang)} / {_fmt(penyebut)} × 100% = {_fmt(round(hasil, 2))}%"],
            "sumber": f"{BUKU}, {sumber}"}


# ---------------------------------------------------------------------------
# IKU 9 — Pendapatan non pendidikan/UKT, hlm. 59
# ---------------------------------------------------------------------------

PENDAPATAN_DIAKUI = {"hibah_riset", "kontrak_riset", "royalti", "komersialisasi", "inkubasi",
                     "konsultasi", "pelatihan", "kerja_sama", "layanan_profesional",
                     "unit_bisnis", "aset_produktif", "filantropi_tercatat", "hasil_dana_abadi"}
PENDAPATAN_TIDAK_DIAKUI = {"ukt", "iuran_pengembangan", "boptn", "bpptnbh", "subsidi_pemerintah",
                           "filantropi_tidak_tercatat", "pokok_dana_abadi"}


def iku9(total_pendapatan: float, rincian: dict[str, float]) -> dict:
    langkah, diakui = [], 0.0
    for pos, nilai in rincian.items():
        if pos in PENDAPATAN_DIAKUI:
            diakui += nilai
            langkah.append(f"{pos}: {_fmt(nilai)} → DIHITUNG (Kriteria a)")
        elif pos in PENDAPATAN_TIDAK_DIAKUI:
            langkah.append(f"{pos}: {_fmt(nilai)} → TIDAK dihitung (Kriteria b)")
        else:
            raise ValueError(f"Pos pendapatan '{pos}' belum dikategorikan; tambahkan ke daftar diakui/tidak diakui.")
    hasil = diakui / total_pendapatan * 100
    langkah.append(f"Capaian = {_fmt(diakui)} / {_fmt(total_pendapatan)} × 100% = {_fmt(round(hasil, 2))}%")
    return {"hasil": round(hasil, 2), "satuan": "%", "langkah": langkah,
            "sumber": f"{BUKU}, IKU 9 – Kriteria & Formula, hlm. 59"}


# ---------------------------------------------------------------------------
# IKU 11b — Predikat SAKIP, hlm. 66 ; IKU 12 — standar penghasilan dosen, hlm. 60
# ---------------------------------------------------------------------------

PREDIKAT_SAKIP = [(90, "AA (memuaskan)"), (80, "A (sangat baik)"), (70, "BB (baik)"),
                  (60, "B (cukup baik)"), (0, "CC-C (kurang)")]


def iku11b_predikat(nilai_akhir: float) -> dict:
    predikat = next(p for batas, p in PREDIKAT_SAKIP if nilai_akhir >= batas)
    return {"hasil": predikat, "satuan": "predikat",
            "langkah": [f"Nilai akhir {_fmt(nilai_akhir)} → rentang tabel predikat SAKIP → {predikat}"],
            "sumber": f"{BUKU}, IKU 11b – Skala dan Predikat, hlm. 66"}


KELIPATAN_UMP = {"asisten_ahli": 1.5, "lektor": 3, "lektor_kepala": 4, "profesor": 6}


def iku12_penghasilan_minimum(ump: float, jabatan: list[str]) -> dict:
    hasil, langkah = {}, []
    for j in jabatan:
        nilai = KELIPATAN_UMP[j] * ump
        hasil[j] = nilai
        langkah.append(f"{j}: ≥ {_fmt(KELIPATAN_UMP[j])} × UMP = {_fmt(KELIPATAN_UMP[j])} × Rp{_fmt(ump)} = Rp{_fmt(nilai)}")
    return {"hasil": hasil, "satuan": "Rp", "langkah": langkah,
            "sumber": f"{BUKU}, IKU 12 – Kriteria b.2, hlm. 60"}


# ---------------------------------------------------------------------------
# Daftar fungsi yang boleh dipanggil (nanti dipakai LLM lewat tool calling)
# ---------------------------------------------------------------------------

REGISTRY = {
    "iku1_aee_prodi": iku1_aee_prodi,
    "iku1_aee_pt": iku1_aee_pt,
    "iku2": iku2,
    "iku2_responden_minimum": iku2_responden_minimum,
    "iku3": iku3,
    "iku6": iku6,
    "rasio": rasio,
    "iku9": iku9,
    "iku11b_predikat": iku11b_predikat,
    "iku12_penghasilan_minimum": iku12_penghasilan_minimum,
}


def hitung(fungsi: str, **argumen) -> dict:
    if fungsi not in REGISTRY:
        raise KeyError(f"Fungsi '{fungsi}' tidak ada di registry: {sorted(REGISTRY)}")
    return REGISTRY[fungsi](**argumen)
