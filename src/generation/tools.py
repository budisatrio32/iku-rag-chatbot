"""
tools.py
Alat (tool) yang boleh dipanggil LLM. Hanya satu: `hitung_iku`, yaitu jembatan ke
kalkulator IKU (src/calculator/iku_formulas.py). LLM tidak menghitung sendiri;
ia memilih fungsi dan mengisi argumennya, lalu kalkulator yang menghitung.

Daftar kunci (kategori IKU 2, bobot prestasi, jenis publikasi, dst.) diambil
langsung dari kalkulator, jadi petunjuk untuk LLM selalu sama dengan kodenya.
"""

import json
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(PROJECT_ROOT / "src" / "calculator"))

import iku_formulas as calc  # noqa: E402


def _daftar(items) -> str:
    return ", ".join(f'"{x}"' for x in items)


def panduan_argumen() -> str:
    """Contoh format argumen untuk setiap fungsi kalkulator."""
    tingkat = sorted({t for t, _ in calc.BOBOT_PRESTASI})
    peringkat = sorted({p for _, p in calc.BOBOT_PRESTASI})
    return "\n".join([
        '- iku1_aee_prodi: {"jenjang": "S1", "lulus_tepat_waktu": 40, "total_mahasiswa": 200, '
        '"pindah": 0, "drop_out": 0, "cuti_lebih": 0}  (jenjang: ' + _daftar(calc.AEE_IDEAL) + ")",
        '- iku1_aee_pt: {"realisasi_per_jenjang": {"D3": 30, "S1": 22.5}}  (nilai AEE realisasi dalam persen)',
        '- iku2: {"total_responden": 500, "kategori": {"<kunci>": jumlah, ...}}  (kunci: '
        + _daftar(calc.BOBOT_IKU2) + ")",
        '- iku2_responden_minimum: {"jumlah_lulusan": 2000}',
        '- iku3: {"total_mahasiswa": 1000, "kegiatan": [{"jumlah": 100, "sks": 20}], '
        '"prestasi": [{"jumlah": 5, "tingkat": "nasional", "peringkat": "juara1"}]}  '
        f"(tingkat: {_daftar(tingkat)}; peringkat: {_daftar(peringkat)})",
        '- iku6: {"total_publikasi": 200, "publikasi": {"q1": 40}, "kolaborasi": {"q1": 4}}  (jenis: '
        + _daftar(calc.BOBOT_PUBLIKASI) + "; kolaborasi = publikasi dengan penulis luar negeri)",
        '- rasio: {"kode": "iku5", "pembilang": 30, "penyebut": 120}  (kode: '
        + "; ".join(f'"{k}" = {a} / {b}' for k, (a, b, _) in calc.RASIO.items()) + ")",
        '- iku9: {"total_pendapatan": 500, "rincian": {"<pos>": nilai, ...}}  (pos yang dihitung: '
        + _daftar(sorted(calc.PENDAPATAN_DIAKUI)) + "; pos yang tidak dihitung: "
        + _daftar(sorted(calc.PENDAPATAN_TIDAK_DIAKUI)) + ")",
        '- iku11b_predikat: {"nilai_akhir": 82}',
        '- iku12_penghasilan_minimum: {"ump": 3000000, "jabatan": ["lektor"]}  (jabatan: '
        + _daftar(calc.KELIPATAN_UMP) + ")",
    ])


TOOL_HITUNG_IKU = {
    "type": "function",
    "function": {
        "name": "hitung_iku",
        "description": (
            "Menghitung capaian IKU dengan rumus resmi Buku IKU Diktisaintek Berdampak. "
            "WAJIB dipakai untuk setiap perhitungan angka; jangan menghitung sendiri. "
            "Mengembalikan hasil, langkah perhitungan, dan sumber halaman rumus.\n"
            "Format argumen per fungsi:\n" + panduan_argumen()
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "fungsi": {
                    "type": "string",
                    "enum": sorted(calc.REGISTRY),
                    "description": "Nama fungsi kalkulator yang dipakai.",
                },
                # argumen dikirim sebagai teks JSON agar skemanya sederhana dan diterima
                # semua penyedia (Gemini, Ollama, OpenAI)
                "argumen_json": {
                    "type": "string",
                    "description": "Argumen fungsi dalam bentuk teks JSON, sesuai contoh format di atas.",
                },
            },
            "required": ["fungsi", "argumen_json"],
        },
    },
}


def jalankan_alat(nama: str, argumen_teks: str) -> dict:
    """Jalankan alat yang diminta LLM. Kesalahan dikembalikan sebagai pesan, bukan crash,
    supaya LLM bisa memperbaiki argumennya di putaran berikutnya."""
    if nama != "hitung_iku":
        return {"error": f"Alat '{nama}' tidak dikenal. Alat yang tersedia: hitung_iku."}
    try:
        permintaan = json.loads(argumen_teks or "{}")
        argumen = permintaan.get("argumen_json", {})
        if isinstance(argumen, str):
            argumen = json.loads(argumen)
        return calc.hitung(permintaan["fungsi"], **argumen)
    except json.JSONDecodeError as e:
        return {"error": f"argumen_json bukan JSON yang valid: {e}"}
    except (KeyError, TypeError, ValueError, ZeroDivisionError) as e:
        return {"error": f"{type(e).__name__}: {e}. Periksa nama fungsi dan format argumen."}
