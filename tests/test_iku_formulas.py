"""
Unit test kalkulator IKU (src/calculator/iku_formulas.py).

Memakai 18 soal hitungan dari data/evaluation/test_inputs_hitung.json, tanpa
retriever/GPU, sehingga bisa dijalankan di CI. Uji sitasi lengkap tetap lewat
src/evaluation/run_calc_tests.py.
"""

import json
from pathlib import Path

import pytest

from iku_formulas import REGISTRY, hitung

PROJECT_ROOT = Path(__file__).resolve().parents[1]
INPUTS_FILE = PROJECT_ROOT / "data" / "evaluation" / "test_inputs_hitung.json"
TOLERANCE = 0.01

CASES = json.loads(INPUTS_FILE.read_text(encoding="utf-8"))["cases"]


def same(actual, expected) -> bool:
    if isinstance(expected, dict):
        return isinstance(actual, dict) and all(same(actual.get(k), v) for k, v in expected.items())
    if isinstance(expected, (int, float)) and isinstance(actual, (int, float)):
        return abs(actual - expected) <= TOLERANCE
    return actual == expected


@pytest.mark.parametrize("case", CASES, ids=[c["id"] for c in CASES])
def test_hasil_sesuai_kunci(case):
    out = hitung(case["fungsi"], **case["argumen"])
    assert same(out["hasil"], case["harapan"]), f"hasil {out['hasil']!r} != kunci {case['harapan']!r}"


@pytest.mark.parametrize("case", CASES, ids=[c["id"] for c in CASES])
def test_keluaran_lengkap_untuk_sitasi(case):
    out = hitung(case["fungsi"], **case["argumen"])
    for key in ("hasil", "satuan", "langkah", "sumber"):
        assert key in out
    assert out["langkah"], "langkah perhitungan tidak boleh kosong"


def test_semua_fungsi_test_set_terdaftar():
    assert {c["fungsi"] for c in CASES} <= set(REGISTRY)


def test_fungsi_tidak_dikenal():
    with pytest.raises(KeyError):
        hitung("tidak_ada")
