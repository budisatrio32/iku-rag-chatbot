"""
postproses.py
Merapikan teks jawaban LLM sebelum diperiksa dan ditampilkan.

Beberapa model (mis. openai/gpt-oss) punya kebiasaan bawaan yang merusak format kita:
- rujukan ditulis 【3】 atau 【2†L1-L3】, bukan [3], sehingga sitasi halaman tidak terbaca;
- spasi khusus (narrow no-break space U+202F, no-break space U+00A0) di antara angka dan
  satuan ("33 %", "SDG 1"), dan tanda hubung khusus (U+2011) yang menyulitkan pencarian teks.
Perapian di sini tidak mengubah isi jawaban, hanya bentuk tulisannya.
"""

import re

RUJUKAN_BAWAAN = re.compile(r"【\s*(\d+)\s*(?:†[^】]*)?】")
SPASI_KHUSUS = str.maketrans({" ": " ", " ": " ", " ": " ", "‑": "-"})


def rapikan_jawaban(teks: str) -> str:
    """'… tepat waktu【3†L1-L4】, 33 %' -> '… tepat waktu[3], 33 %'."""
    return RUJUKAN_BAWAAN.sub(r"[\1]", teks.translate(SPASI_KHUSUS))
