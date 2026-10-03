# Laporan Evaluasi Retrieval

- Waktu: 2026-10-03 20:05:47
- Test set: `data\evaluation\test_set_buku_iku.md` (30 soal, 29 dalam cakupan, 1 di luar cakupan)
- Model embedding: `BAAI/bge-m3` | Koleksi: `pmpt_qa_v2` (605 chunk)
- top_k: 5 | ambang di luar cakupan: distance ≥ 0.45

Definisi: sebuah soal **HIT** jika ada chunk yang memuat semua *kata kunci bukti* soal tersebut di 5 hasil teratas `Retriever.search()`.

## Ringkasan

| Metrik | Nilai |
|---|---|
| Hit@1 | 19/29 (65.5%) |
| Hit@3 | 26/29 (89.7%) |
| Hit@5 | 26/29 (89.7%) |
| MRR@5 | 0.764 |
| Halaman sitasi benar (chunk bukti dari Buku) | 13/24 (54.2%) |
| Hasil #1 berasal dari PPT (bukan Buku) | 8/29 |
| Chunk bukti pertama berasal dari PPT | 6 soal |
| Bukti tidak ada di corpus (masalah chunking) | 1 ['D04'] |
| Nyaris kena (bukti di top-20 tapi tidak di top-5) | 1 ['H15'] |
| Soal di luar cakupan lolos | 0/1 |
| Rata-rata distance #1 (soal HIT / MISS) | 0.32 / 0.3061 |
| Distance #1 tertinggi soal dalam cakupan | 0.4319 |
| Distance #1 soal di luar cakupan | {'D12': 0.3727} |
| Rata-rata waktu per query | 0.031 s |

### Per tipe soal

| Tipe | n | Hit@1 | Hit@3 | Hit@5 | MRR |
|---|---|---|---|---|---|
| Definisi | 10 | 70.0% | 90.0% | 90.0% | 0.783 |
| Jebakan ⚠️ | 1 | 0.0% | 0.0% | 0.0% | 0.0 |
| Hitung | 18 | 66.7% | 94.4% | 94.4% | 0.796 |

### Per IKU

| IKU | n | Hit@1 | Hit@5 | MRR |
|---|---|---|---|---|
| 1 | 6 | 4/6 | 5/6 | 0.75 |
| 11b | 1 | 1/1 | 1/1 | 1.0 |
| 11c | 1 | 0/1 | 1/1 | 0.333 |
| 11d | 1 | 1/1 | 1/1 | 1.0 |
| 12 | 1 | 0/1 | 1/1 | 0.5 |
| 2 | 4 | 3/4 | 4/4 | 0.875 |
| 3 | 3 | 3/3 | 3/3 | 1.0 |
| 4 | 1 | 1/1 | 1/1 | 1.0 |
| 5 | 1 | 0/1 | 1/1 | 0.5 |
| 6 | 3 | 1/3 | 3/3 | 0.611 |
| 7 | 2 | 2/2 | 2/2 | 1.0 |
| 8 | 1 | 0/1 | 0/1 | 0.0 |
| 9 | 2 | 2/2 | 2/2 | 1.0 |
| Umum | 2 | 1/2 | 1/2 | 0.5 |

## Hasil per soal

| ID | IKU | Status | Sumber bukti | Hlm. bukti (Buku) | Hlm. benar | Rank mentah | Distance #1 | Sumber #1 |
|---|---|---|---|---|---|---|---|---|
| D01 | 1 | HIT @1 | Buku | 49 ✅ | 49 | 1 | 0.3565 | Buku |
| D02 | 1 | HIT @1 | Buku | 100–101 ❌ | 49 | 1 | 0.3277 | Buku |
| D03 | Umum | HIT @1 | Buku | 48–49 ✅ | 48 | 1 | 0.3311 | Buku |
| D04 | Umum | MISS - bukti tidak ada di corpus | - | - | 48 | - | 0.3476 | Buku |
| D05 | 2 | HIT @1 | Buku | 51 ✅ | 51, 52 | 1 | 0.4091 | Buku |
| D06 | 3 | HIT @1 | Buku | 53 ✅ | 53 | 1 | 0.2737 | Buku |
| D07 | 7 | HIT @1 | Buku | 58 ✅ | 58 | 1 | 0.2403 | Buku |
| D08 | 9 | HIT @1 | Buku | 122–123 ❌ | 59 | 1 | 0.3021 | Buku |
| D09 | 6 | HIT @2 | Buku | 63 ✅ | 63 | 2 | 0.4319 | Buku |
| D10 | 11c | HIT @3 | Buku | 67 ✅ | 67 | 3 | 0.2792 | Buku |
| D11 | 1 | MISS - bukti tidak masuk top-20 | - | - | 49, 51 | - | 0.3407 | PPT |
| D12 | — | GAGAL (di luar cakupan) | - | - | - | - | 0.3727 | PPT |
| H01 | 1 | HIT @2 | Buku | 101–102 ❌ | 49 | 2 | 0.3543 | Buku |
| H02 | 1 | HIT @1 | Buku | 101–102 ❌ | 49, 50 | 1 | 0.2946 | Buku |
| H03 | 1 | HIT @1 | Buku | 100–101 ❌ | 49 | 1 | 0.3368 | Buku |
| H04 | 2 | HIT @1 | PPT | 103–104 ❌ | 51, 52 | 1 | 0.2834 | PPT |
| H05 | 2 | HIT @2 | PPT | - | 51, 52 | 2 | 0.2473 | PPT |
| H06 | 2 | HIT @1 | PPT | - | 52 | 1 | 0.3538 | PPT |
| H07 | 3 | HIT @1 | Buku | 107–108 ❌ | 53, 54 | 1 | 0.3249 | Buku |
| H08 | 3 | HIT @1 | Buku | 53–54 ✅ | 54 | 1 | 0.3073 | Buku |
| H09 | 5 | HIT @2 | Buku | 57–58 ✅ | 57 | 2 | 0.308 | Buku |
| H10 | 6 | HIT @1 | PPT | 75 ❌ | 63 | 1 | 0.2906 | PPT |
| H11 | 6 | HIT @3 | Buku | 117–118 ❌ | 63 | 3 | 0.3096 | Buku |
| H12 | 7 | HIT @1 | PPT | 58 ✅ | 58 | 1 | 0.2854 | PPT |
| H13 | 9 | HIT @1 | Buku | 59 ✅ | 59 | 1 | 0.3208 | Buku |
| H14 | 4 | HIT @1 | Buku | 112 ❌ | 62 | 1 | 0.2516 | Buku |
| H15 | 8 | MISS - bukti di rank mentah 6 | - | - | 64 | 6 | 0.2299 | PPT |
| H16 | 11b | HIT @1 | Buku | 135 ❌ | 66 | 1 | 0.396 | Buku |
| H17 | 11d | HIT @1 | Buku | 68 ✅ | 68 | 1 | 0.3472 | Buku |
| H18 | 12 | HIT @2 | PPT | 60 ✅ | 60 | 2 | 0.3568 | PPT |

## Detail per soal

<details><summary>✅ <b>D01</b> — HIT @1 — Apa itu IKU 1?</summary>

**Pertanyaan:** Apa itu IKU 1?

**Kata kunci bukti:** `tepat waktu`, `masa studi standar`

**Halaman benar:** 49 | **Chunk bukti di corpus:** 3 (Buku hlm.49, Buku hlm.100, PPT hlm.45)

| # | Bukti | Sumber | Hlm. | Distance | Section | Cuplikan |
|---|---|---|---|---|---|---|
| 1 | ✅ | Buku | 49 | 0.3565 | …U) Diktisaintek Berdampak > 5.3.1. Indikator Kinerja Utama (IKU) Wajib | [Buku IKU Diktisaintek Berdampak V1 / BAB - V > 5.3. Indikator Kinerja Utama (IKU) Diktisaintek Berdampak > 5.3.1. Indikator Kinerja Utama (IKU) Wajib > IKU 1 / |
| 2 |  | Buku | 86 | 0.3583 | … Lembaga Layanan Pendidikan Tinggi > IKU 1: Keunggulan layanan LLDIKTI | [Buku IKU Diktisaintek Berdampak V1 / BAB - VI > 5.5. Indikator Kinerja Utama (IKU) Lembaga Layanan Pendidikan Tinggi > IKU 1: Keunggulan layanan LLDIKTI / Bagi |
| 3 | ✅ | PPT | 45 | 0.3674 | …ja Utama (IKU) Wajib > IKU 1: Angka Efisiensi Edukasi Perguruan Tinggi | [PPT IKU Diktisaintek Berdampak PTS V2 / BAB - V > 5.3. INDIKATOR KINERJA UTAMA (IKU) DIKTISAINTEK BERDAMPAK > 5.3.1. Indikator Kinerja Utama (IKU) Wajib > IKU  |
| 4 |  | Buku | 49 | 0.3727 | …U) Diktisaintek Berdampak > 5.3.1. Indikator Kinerja Utama (IKU) Wajib | [Buku IKU Diktisaintek Berdampak V1 / BAB - V > 5.3. Indikator Kinerja Utama (IKU) Diktisaintek Berdampak > 5.3.1. Indikator Kinerja Utama (IKU) Wajib > IKU 1 / |
| 5 |  | Buku | 58 | 0.3748 | …Berkualitas), SDG17 (Kemitraan), dan 2(dua)SDGs Lain Sesuai Keunggulan | [Buku IKU Diktisaintek Berdampak V1 / BAB - V > 5.3. Indikator Kinerja Utama (IKU) Diktisaintek Berdampak > 5.3.1. Indikator Kinerja Utama (IKU) Wajib > IKU 7:  |

</details>

<details><summary>✅ <b>D02</b> — HIT @1 — Berapa masa tempuh kurikulum dan AEE ideal untuk program Sarjana dan Diploma Tiga?</summary>

**Pertanyaan:** Berapa masa tempuh kurikulum dan AEE ideal untuk program Sarjana dan Diploma Tiga?

**Kata kunci bukti:** `aee ideal`, `8 semester`, `25%`

**Halaman benar:** 49 | **Chunk bukti di corpus:** 3 (Buku hlm.49, Buku hlm.100–101, PPT hlm.45)

| # | Bukti | Sumber | Hlm. | Distance | Section | Cuplikan |
|---|---|---|---|---|---|---|
| 1 | ✅ | Buku | 100–101 | 0.3277 | …LAMPIRAN Kepmen 358/M/KEP/2025 > 1. IKU BAGI PERGURUAN TINGGI | [Buku IKU Diktisaintek Berdampak V1 (Lampiran Kepmen 358/M/KEP/2025) / LAMPIRAN Kepmen 358/M/KEP/2025 > 1. IKU BAGI PERGURUAN TINGGI > IKU 1. Angka Efisiensi Ed |
| 2 | ✅ | Buku | 49 | 0.3376 | …U) Diktisaintek Berdampak > 5.3.1. Indikator Kinerja Utama (IKU) Wajib | [Buku IKU Diktisaintek Berdampak V1 / BAB - V > 5.3. Indikator Kinerja Utama (IKU) Diktisaintek Berdampak > 5.3.1. Indikator Kinerja Utama (IKU) Wajib > IKU 1 / |
| 3 | ✅ | PPT | 45 | 0.3802 | …ja Utama (IKU) Wajib > IKU 1: Angka Efisiensi Edukasi Perguruan Tinggi | [PPT IKU Diktisaintek Berdampak PTS V2 / BAB - V > 5.3. INDIKATOR KINERJA UTAMA (IKU) DIKTISAINTEK BERDAMPAK > 5.3.1. Indikator Kinerja Utama (IKU) Wajib > IKU  |
| 4 |  | Buku | 100 | 0.4054 | …LAMPIRAN Kepmen 358/M/KEP/2025 > 1. IKU BAGI PERGURUAN TINGGI | [Buku IKU Diktisaintek Berdampak V1 (Lampiran Kepmen 358/M/KEP/2025) / LAMPIRAN Kepmen 358/M/KEP/2025 > 1. IKU BAGI PERGURUAN TINGGI > IKU 1. Angka Efisiensi Ed |
| 5 |  | Buku | 101–102 | 0.4117 | …LAMPIRAN Kepmen 358/M/KEP/2025 > 1. IKU BAGI PERGURUAN TINGGI | [Buku IKU Diktisaintek Berdampak V1 (Lampiran Kepmen 358/M/KEP/2025) / LAMPIRAN Kepmen 358/M/KEP/2025 > 1. IKU BAGI PERGURUAN TINGGI > IKU 1. Angka Efisiensi Ed |

</details>

<details><summary>✅ <b>D03</b> — HIT @1 — Berapa jumlah IKU wajib, IKU pilihan, dan IKU partisipatif?</summary>

**Pertanyaan:** Berapa jumlah IKU wajib, IKU pilihan, dan IKU partisipatif?

**Kata kunci bukti:** `sebanyak 7 (tujuh)`, `partisipatif`

**Halaman benar:** 48 | **Chunk bukti di corpus:** 1 (Buku hlm.48–49)

| # | Bukti | Sumber | Hlm. | Distance | Section | Cuplikan |
|---|---|---|---|---|---|---|
| 1 | ✅ | Buku | 48–49 | 0.3311 | …BAB - V > 5.3. Indikator Kinerja Utama (IKU) Diktisaintek Berdampak | [Buku IKU Diktisaintek Berdampak V1 / BAB - V > 5.3. Indikator Kinerja Utama (IKU) Diktisaintek Berdampak / hlm. 48–49] / No / Sasaran / Indikator Kinerja Utama |
| 2 |  | PPT | 44 | 0.3377 | …BAB - V > 5.3. INDIKATOR KINERJA UTAMA (IKU) DIKTISAINTEK BERDAMPAK | [PPT IKU Diktisaintek Berdampak PTS V2 / BAB - V > 5.3. INDIKATOR KINERJA UTAMA (IKU) DIKTISAINTEK BERDAMPAK / hlm. 44] / No. / Sasaran / Indikator Kinerja Utam |
| 3 |  | Buku | 61 | 0.3453 | … Diktisaintek Berdampak > 5.3.2. Indikator Kinerja Utama (IKU) Pilihan | [Buku IKU Diktisaintek Berdampak V1 / BAB - V > 5.3. Indikator Kinerja Utama (IKU) Diktisaintek Berdampak > 5.3.2. Indikator Kinerja Utama (IKU) Pilihan / hlm.  |
| 4 |  | Buku | 49 | 0.3486 | …U) Diktisaintek Berdampak > 5.3.1. Indikator Kinerja Utama (IKU) Wajib | [Buku IKU Diktisaintek Berdampak V1 / BAB - V > 5.3. Indikator Kinerja Utama (IKU) Diktisaintek Berdampak > 5.3.1. Indikator Kinerja Utama (IKU) Wajib > IKU 1 / |
| 5 |  | PPT | 45 | 0.3525 | …ja Utama (IKU) Wajib > IKU 1: Angka Efisiensi Edukasi Perguruan Tinggi | [PPT IKU Diktisaintek Berdampak PTS V2 / BAB - V > 5.3. INDIKATOR KINERJA UTAMA (IKU) DIKTISAINTEK BERDAMPAK > 5.3.1. Indikator Kinerja Utama (IKU) Wajib > IKU  |

</details>

<details><summary>❌ <b>D04</b> — MISS - bukti tidak ada di corpus — Sebutkan IKU yang bersifat wajib.</summary>

**Pertanyaan:** Sebutkan IKU yang bersifat wajib.

**Kata kunci bukti:** `angka efisiensi edukasi`, `kesejahteraan dosen`, `pendapatan non pendidikan`

**Halaman benar:** 48 | **Chunk bukti di corpus:** 0 

| # | Bukti | Sumber | Hlm. | Distance | Section | Cuplikan |
|---|---|---|---|---|---|---|
| 1 |  | Buku | 49 | 0.3476 | …U) Diktisaintek Berdampak > 5.3.1. Indikator Kinerja Utama (IKU) Wajib | [Buku IKU Diktisaintek Berdampak V1 / BAB - V > 5.3. Indikator Kinerja Utama (IKU) Diktisaintek Berdampak > 5.3.1. Indikator Kinerja Utama (IKU) Wajib > IKU 1 / |
| 2 |  | Buku | 53 | 0.3538 | …a S1 dan D4/D3/D2/D1 Berkegiatan/Meraih Prestasi di Luar Program Studi | [Buku IKU Diktisaintek Berdampak V1 / BAB - V > 5.3. Indikator Kinerja Utama (IKU) Diktisaintek Berdampak > 5.3.1. Indikator Kinerja Utama (IKU) Wajib > 3 IKU 3 |
| 3 |  | PPT | 44 | 0.3541 | …BAB - V > 5.3. INDIKATOR KINERJA UTAMA (IKU) DIKTISAINTEK BERDAMPAK | [PPT IKU Diktisaintek Berdampak PTS V2 / BAB - V > 5.3. INDIKATOR KINERJA UTAMA (IKU) DIKTISAINTEK BERDAMPAK / hlm. 44] / No. / Sasaran / Indikator Kinerja Utam |
| 4 |  | Buku | 48–49 | 0.3565 | …BAB - V > 5.3. Indikator Kinerja Utama (IKU) Diktisaintek Berdampak | [Buku IKU Diktisaintek Berdampak V1 / BAB - V > 5.3. Indikator Kinerja Utama (IKU) Diktisaintek Berdampak / hlm. 48–49] / No / Sasaran / Indikator Kinerja Utama |
| 5 |  | PPT | 49 | 0.3596 | …kutnya/ Berwirausaha dalam Jangka Waktu 1 Tahun Setelah Kelulusan. (2) | [PPT IKU Diktisaintek Berdampak PTS V2 / BAB - V > 5.3. INDIKATOR KINERJA UTAMA (IKU) DIKTISAINTEK BERDAMPAK > 5.3.1. Indikator Kinerja Utama (IKU) Wajib > IKU  |

</details>

<details><summary>✅ <b>D05</b> — HIT @1 — Dari mana data IKU 2 diperoleh, dan bagaimana menentukan jumlah responden minimum?</summary>

**Pertanyaan:** Dari mana data IKU 2 diperoleh, dan bagaimana menentukan jumlah responden minimum?

**Kata kunci bukti:** `tracer study`, `slovin`

**Halaman benar:** 51, 52 | **Chunk bukti di corpus:** 3 (Buku hlm.51, Buku hlm.104, PPT hlm.48)

| # | Bukti | Sumber | Hlm. | Distance | Section | Cuplikan |
|---|---|---|---|---|---|---|
| 1 | ✅ | Buku | 51 | 0.4091 | …Berikutnya/ Berwirausaha dalam Jangka Waktu 1 Tahun Setelah Kelulusan. | [Buku IKU Diktisaintek Berdampak V1 / BAB - V > 5.3. Indikator Kinerja Utama (IKU) Diktisaintek Berdampak > 5.3.1. Indikator Kinerja Utama (IKU) Wajib > 2 IKU 2 |
| 2 | ✅ | PPT | 48 | 0.4138 | …kutnya/ Berwirausaha dalam Jangka Waktu 1 Tahun Setelah Kelulusan. (2) | [PPT IKU Diktisaintek Berdampak PTS V2 / BAB - V > 5.3. INDIKATOR KINERJA UTAMA (IKU) DIKTISAINTEK BERDAMPAK > 5.3.1. Indikator Kinerja Utama (IKU) Wajib > IKU  |
| 3 |  | Buku | 52 | 0.4173 | …Berikutnya/ Berwirausaha dalam Jangka Waktu 1 Tahun Setelah Kelulusan. | [Buku IKU Diktisaintek Berdampak V1 / BAB - V > 5.3. Indikator Kinerja Utama (IKU) Diktisaintek Berdampak > 5.3.1. Indikator Kinerja Utama (IKU) Wajib > 2 IKU 2 |
| 4 |  | PPT | 48–49 | 0.4235 | …kutnya/ Berwirausaha dalam Jangka Waktu 1 Tahun Setelah Kelulusan. (2) | [PPT IKU Diktisaintek Berdampak PTS V2 / BAB - V > 5.3. INDIKATOR KINERJA UTAMA (IKU) DIKTISAINTEK BERDAMPAK > 5.3.1. Indikator Kinerja Utama (IKU) Wajib > IKU  |
| 5 |  | Buku | 87 | 0.4242 | …an Pendidikan Tinggi > IKU 2: Arsitektur Perguruan Tinggi Swasta (PTS) | [Buku IKU Diktisaintek Berdampak V1 / BAB - VI > 5.5. Indikator Kinerja Utama (IKU) Lembaga Layanan Pendidikan Tinggi > IKU 2: Arsitektur Perguruan Tinggi Swast |

</details>

<details><summary>✅ <b>D06</b> — HIT @1 — Kegiatan di luar program studi apa saja yang diakui untuk IKU 3?</summary>

**Pertanyaan:** Kegiatan di luar program studi apa saja yang diakui untuk IKU 3?

**Kata kunci bukti:** `magang`, `pertukaran mahasiswa`, `dosen pembimbing`

**Halaman benar:** 53 | **Chunk bukti di corpus:** 5 (Buku hlm.53, Buku hlm.53, Buku hlm.105–106, Buku hlm.106–107, PPT hlm.49)

| # | Bukti | Sumber | Hlm. | Distance | Section | Cuplikan |
|---|---|---|---|---|---|---|
| 1 | ✅ | Buku | 53 | 0.2737 | …a S1 dan D4/D3/D2/D1 Berkegiatan/Meraih Prestasi di Luar Program Studi | [Buku IKU Diktisaintek Berdampak V1 / BAB - V > 5.3. Indikator Kinerja Utama (IKU) Diktisaintek Berdampak > 5.3.1. Indikator Kinerja Utama (IKU) Wajib > 3 IKU 3 |
| 2 | ✅ | Buku | 53 | 0.2754 | …a S1 dan D4/D3/D2/D1 Berkegiatan/Meraih Prestasi di Luar Program Studi | [Buku IKU Diktisaintek Berdampak V1 / BAB - V > 5.3. Indikator Kinerja Utama (IKU) Diktisaintek Berdampak > 5.3.1. Indikator Kinerja Utama (IKU) Wajib > 3 IKU 3 |
| 3 | ✅ | Buku | 105–106 | 0.3126 | …LAMPIRAN Kepmen 358/M/KEP/2025 > 1. IKU BAGI PERGURUAN TINGGI | [Buku IKU Diktisaintek Berdampak V1 (Lampiran Kepmen 358/M/KEP/2025) / LAMPIRAN Kepmen 358/M/KEP/2025 > 1. IKU BAGI PERGURUAN TINGGI > IKU 3. Persentase mahasis |
| 4 | ✅ | Buku | 106–107 | 0.3138 | …LAMPIRAN Kepmen 358/M/KEP/2025 > 1. IKU BAGI PERGURUAN TINGGI | [Buku IKU Diktisaintek Berdampak V1 (Lampiran Kepmen 358/M/KEP/2025) / LAMPIRAN Kepmen 358/M/KEP/2025 > 1. IKU BAGI PERGURUAN TINGGI > IKU 3. Persentase mahasis |
| 5 |  | Buku | 53 | 0.314 | …a S1 dan D4/D3/D2/D1 Berkegiatan/Meraih Prestasi di Luar Program Studi | [Buku IKU Diktisaintek Berdampak V1 / BAB - V > 5.3. Indikator Kinerja Utama (IKU) Diktisaintek Berdampak > 5.3.1. Indikator Kinerja Utama (IKU) Wajib > 3 IKU 3 |

</details>

<details><summary>✅ <b>D07</b> — HIT @1 — SDG apa saja yang wajib dan pilihan dalam IKU 7?</summary>

**Pertanyaan:** SDG apa saja yang wajib dan pilihan dalam IKU 7?

**Kata kunci bukti:** `sdg 17`, `2 (dua) tujuan sdgs lain`

**Halaman benar:** 58 | **Chunk bukti di corpus:** 3 (Buku hlm.58, Buku hlm.120–121, PPT hlm.55)

| # | Bukti | Sumber | Hlm. | Distance | Section | Cuplikan |
|---|---|---|---|---|---|---|
| 1 | ✅ | Buku | 58 | 0.2403 | …Berkualitas), SDG17 (Kemitraan), dan 2(dua)SDGs Lain Sesuai Keunggulan | [Buku IKU Diktisaintek Berdampak V1 / BAB - V > 5.3. Indikator Kinerja Utama (IKU) Diktisaintek Berdampak > 5.3.1. Indikator Kinerja Utama (IKU) Wajib > IKU 7:  |
| 2 | ✅ | PPT | 55 | 0.2461 | …ualitas), SDG17 (Kemitraan), dan 2(dua)SDGs Lain Sesuai Keunggulan (2) | [PPT IKU Diktisaintek Berdampak PTS V2 / BAB - V > 5.3. INDIKATOR KINERJA UTAMA (IKU) DIKTISAINTEK BERDAMPAK > 5.3.1. Indikator Kinerja Utama (IKU) Wajib > IKU  |
| 3 |  | Buku | 58 | 0.2726 | …Berkualitas), SDG17 (Kemitraan), dan 2(dua)SDGs Lain Sesuai Keunggulan | [Buku IKU Diktisaintek Berdampak V1 / BAB - V > 5.3. Indikator Kinerja Utama (IKU) Diktisaintek Berdampak > 5.3.1. Indikator Kinerja Utama (IKU) Wajib > IKU 7:  |
| 4 |  | PPT | 54 | 0.2783 | …rkualitas), SDG17 (Kemitraan), dan 2 (dua) SDGs Lain Sesuai Keunggulan | [PPT IKU Diktisaintek Berdampak PTS V2 / BAB - V > 5.3. INDIKATOR KINERJA UTAMA (IKU) DIKTISAINTEK BERDAMPAK > 5.3.1. Indikator Kinerja Utama (IKU) Wajib > IKU  |
| 5 |  | PPT | 54 | 0.2865 | …rkualitas), SDG17 (Kemitraan), dan 2 (dua) SDGs Lain Sesuai Keunggulan | [PPT IKU Diktisaintek Berdampak PTS V2 / BAB - V > 5.3. INDIKATOR KINERJA UTAMA (IKU) DIKTISAINTEK BERDAMPAK > 5.3.1. Indikator Kinerja Utama (IKU) Wajib > IKU  |

</details>

<details><summary>✅ <b>D08</b> — HIT @1 — Pendapatan apa saja yang tidak termasuk dalam perhitungan IKU 9?</summary>

**Pertanyaan:** Pendapatan apa saja yang tidak termasuk dalam perhitungan IKU 9?

**Kata kunci bukti:** `boptn`, `iuran pengembangan institusi`

**Halaman benar:** 59 | **Chunk bukti di corpus:** 3 (Buku hlm.59, Buku hlm.122–123, PPT hlm.56)

| # | Bukti | Sumber | Hlm. | Distance | Section | Cuplikan |
|---|---|---|---|---|---|---|
| 1 | ✅ | Buku | 122–123 | 0.3021 | …LAMPIRAN Kepmen 358/M/KEP/2025 > 1. IKU BAGI PERGURUAN TINGGI | [Buku IKU Diktisaintek Berdampak V1 (Lampiran Kepmen 358/M/KEP/2025) / LAMPIRAN Kepmen 358/M/KEP/2025 > 1. IKU BAGI PERGURUAN TINGGI > IKU 9. Persentase pendapa |
| 2 | ✅ | Buku | 59 | 0.3045 | … Utama (IKU) Wajib > 6 IKU 9: Persentase Pendapatan Non Pendidikan/UKT | [Buku IKU Diktisaintek Berdampak V1 / BAB - V > 5.3. Indikator Kinerja Utama (IKU) Diktisaintek Berdampak > 5.3.1. Indikator Kinerja Utama (IKU) Wajib > 6 IKU 9 |
| 3 |  | Buku | 122 | 0.3077 | …LAMPIRAN Kepmen 358/M/KEP/2025 > 1. IKU BAGI PERGURUAN TINGGI | [Buku IKU Diktisaintek Berdampak V1 (Lampiran Kepmen 358/M/KEP/2025) / LAMPIRAN Kepmen 358/M/KEP/2025 > 1. IKU BAGI PERGURUAN TINGGI > IKU 9. Persentase pendapa |
| 4 | ✅ | PPT | 56 | 0.3157 | …Utama (IKU) Wajib > 6 IKU 9 : Persentase Pendapatan Non Pendidikan/UKT | [PPT IKU Diktisaintek Berdampak PTS V2 / BAB - V > 5.3. INDIKATOR KINERJA UTAMA (IKU) DIKTISAINTEK BERDAMPAK > 5.3.1. Indikator Kinerja Utama (IKU) Wajib > 6 IK |
| 5 |  | Buku | 59 | 0.3208 | … Utama (IKU) Wajib > 6 IKU 9: Persentase Pendapatan Non Pendidikan/UKT | [Buku IKU Diktisaintek Berdampak V1 / BAB - V > 5.3. Indikator Kinerja Utama (IKU) Diktisaintek Berdampak > 5.3.1. Indikator Kinerja Utama (IKU) Wajib > 6 IKU 9 |

</details>

<details><summary>✅ <b>D09</b> — HIT @2 — Penerbit apa yang tidak diperhitungkan dalam IKU 6?</summary>

**Pertanyaan:** Penerbit apa yang tidak diperhitungkan dalam IKU 6?

**Kata kunci bukti:** `mdpi`, `hindawi`

**Halaman benar:** 63 | **Chunk bukti di corpus:** 9 (Buku hlm.63, Buku hlm.73, Buku hlm.74, Buku hlm.75, Buku hlm.118–119, PPT hlm.61–62)

| # | Bukti | Sumber | Hlm. | Distance | Section | Cuplikan |
|---|---|---|---|---|---|---|
| 1 |  | Buku | 63 | 0.4319 | …an > IKU 6: Persentase Publikasi Bereputasi Internasional (Scopus/WoS) | [Buku IKU Diktisaintek Berdampak V1 / BAB - V > 5.3. Indikator Kinerja Utama (IKU) Diktisaintek Berdampak > 5.3.2. Indikator Kinerja Utama (IKU) Pilihan > IKU 6 |
| 2 | ✅ | Buku | 63 | 0.4332 | …an > IKU 6: Persentase Publikasi Bereputasi Internasional (Scopus/WoS) | [Buku IKU Diktisaintek Berdampak V1 / BAB - V > 5.3. Indikator Kinerja Utama (IKU) Diktisaintek Berdampak > 5.3.2. Indikator Kinerja Utama (IKU) Pilihan > IKU 6 |
| 3 | ✅ | PPT | 61–62 | 0.4351 | …an > IKU 6: Persentase Publikasi Bereputasi Internasional (Scopus/WoS) | [PPT IKU Diktisaintek Berdampak PTS V2 / BAB - V > 5.3. INDIKATOR KINERJA UTAMA (IKU) DIKTISAINTEK BERDAMPAK > 5.3.2. Indikator Kinerja Utama (IKU) Pilihan > IK |
| 4 |  | Buku | 63 | 0.441 | …an > IKU 6: Persentase Publikasi Bereputasi Internasional (Scopus/WoS) | [Buku IKU Diktisaintek Berdampak V1 / BAB - V > 5.3. Indikator Kinerja Utama (IKU) Diktisaintek Berdampak > 5.3.2. Indikator Kinerja Utama (IKU) Pilihan > IKU 6 |
| 5 |  | PPT | 61 | 0.4427 | …an > IKU 6: Persentase Publikasi Bereputasi Internasional (Scopus/WoS) | [PPT IKU Diktisaintek Berdampak PTS V2 / BAB - V > 5.3. INDIKATOR KINERJA UTAMA (IKU) DIKTISAINTEK BERDAMPAK > 5.3.2. Indikator Kinerja Utama (IKU) Pilihan > IK |

</details>

<details><summary>✅ <b>D10</b> — HIT @3 — Bagaimana arah penilaian IKU 11c (pelanggaran integritas akademik)?</summary>

**Pertanyaan:** Bagaimana arah penilaian IKU 11c (pelanggaran integritas akademik)?

**Kata kunci bukti:** `semakin rendah semakin baik`

**Halaman benar:** 67 | **Chunk bukti di corpus:** 3 (Buku hlm.67, Buku hlm.126–130, PPT hlm.67)

| # | Bukti | Sumber | Hlm. | Distance | Section | Cuplikan |
|---|---|---|---|---|---|---|
| 1 |  | Buku | 67 | 0.2792 | … IKU 11: (c) Pencegahan dan Penanganan Pelanggaran Integritas Akademik | [Buku IKU Diktisaintek Berdampak V1 / BAB - V > 5.3. Indikator Kinerja Utama (IKU) Diktisaintek Berdampak > 5.3.2. Indikator Kinerja Utama (IKU) Pilihan > IKU 1 |
| 2 |  | Buku | 67 | 0.288 | … IKU 11: (c) Pencegahan dan Penanganan Pelanggaran Integritas Akademik | [Buku IKU Diktisaintek Berdampak V1 / BAB - V > 5.3. Indikator Kinerja Utama (IKU) Diktisaintek Berdampak > 5.3.2. Indikator Kinerja Utama (IKU) Pilihan > IKU 1 |
| 3 | ✅ | Buku | 67 | 0.2892 | … IKU 11: (c) Pencegahan dan Penanganan Pelanggaran Integritas Akademik | [Buku IKU Diktisaintek Berdampak V1 / BAB - V > 5.3. Indikator Kinerja Utama (IKU) Diktisaintek Berdampak > 5.3.2. Indikator Kinerja Utama (IKU) Pilihan > IKU 1 |
| 4 |  | Buku | 125–130 | 0.3107 | …LAMPIRAN Kepmen 358/M/KEP/2025 > 1. IKU BAGI PERGURUAN TINGGI | [Buku IKU Diktisaintek Berdampak V1 (Lampiran Kepmen 358/M/KEP/2025) / LAMPIRAN Kepmen 358/M/KEP/2025 > 1. IKU BAGI PERGURUAN TINGGI > IKU 11. a. Hasil audit at |
| 5 |  | PPT | 67 | 0.3192 | …K/WBBM > IKU 11.1 : Hasil audit atas Laporan Keuangan Perguruan Tinggi | [PPT IKU Diktisaintek Berdampak PTS V2 / BAB - V > 5.3. INDIKATOR KINERJA UTAMA (IKU) DIKTISAINTEK BERDAMPAK > 5.3.2. Indikator Kinerja Utama (IKU) Pilihan > 4  |

</details>

<details><summary>❌ <b>D11</b> — MISS - bukti tidak masuk top-20 — Lulusan 400, yang bekerja 280, berapa capaian IKU 1?</summary>

**Pertanyaan:** Lulusan 400, yang bekerja 280, berapa capaian IKU 1?

**Kata kunci bukti:** `tepat waktu`, `masa studi standar`

**Halaman benar:** 49, 51 | **Chunk bukti di corpus:** 3 (Buku hlm.49, Buku hlm.100, PPT hlm.45)

| # | Bukti | Sumber | Hlm. | Distance | Section | Cuplikan |
|---|---|---|---|---|---|---|
| 1 |  | PPT | 45 | 0.3407 | …ja Utama (IKU) Wajib > IKU 1: Angka Efisiensi Edukasi Perguruan Tinggi | [PPT IKU Diktisaintek Berdampak PTS V2 / BAB - V > 5.3. INDIKATOR KINERJA UTAMA (IKU) DIKTISAINTEK BERDAMPAK > 5.3.1. Indikator Kinerja Utama (IKU) Wajib > IKU  |
| 2 |  | Buku | 104–105 | 0.3414 | …LAMPIRAN Kepmen 358/M/KEP/2025 > 1. IKU BAGI PERGURUAN TINGGI | [Buku IKU Diktisaintek Berdampak V1 (Lampiran Kepmen 358/M/KEP/2025) / LAMPIRAN Kepmen 358/M/KEP/2025 > 1. IKU BAGI PERGURUAN TINGGI > IKU 2. Persentase lulusan |
| 3 |  | Buku | 49 | 0.3449 | …U) Diktisaintek Berdampak > 5.3.1. Indikator Kinerja Utama (IKU) Wajib | [Buku IKU Diktisaintek Berdampak V1 / BAB - V > 5.3. Indikator Kinerja Utama (IKU) Diktisaintek Berdampak > 5.3.1. Indikator Kinerja Utama (IKU) Wajib > IKU 1 / |
| 4 |  | Buku | 104 | 0.3472 | …LAMPIRAN Kepmen 358/M/KEP/2025 > 1. IKU BAGI PERGURUAN TINGGI | [Buku IKU Diktisaintek Berdampak V1 (Lampiran Kepmen 358/M/KEP/2025) / LAMPIRAN Kepmen 358/M/KEP/2025 > 1. IKU BAGI PERGURUAN TINGGI > IKU 2. Persentase lulusan |
| 5 |  | Buku | 102–103 | 0.3489 | …LAMPIRAN Kepmen 358/M/KEP/2025 > 1. IKU BAGI PERGURUAN TINGGI | [Buku IKU Diktisaintek Berdampak V1 (Lampiran Kepmen 358/M/KEP/2025) / LAMPIRAN Kepmen 358/M/KEP/2025 > 1. IKU BAGI PERGURUAN TINGGI > IKU 2. Persentase lulusan |

</details>

<details><summary>❌ <b>D12</b> — GAGAL (di luar cakupan) — Berapa besaran UKT di Universitas Gadjah Mada tahun 2026?</summary>

**Pertanyaan:** Berapa besaran UKT di Universitas Gadjah Mada tahun 2026?

**Kata kunci bukti:** — (di luar cakupan)

**Halaman benar:** - | **Chunk bukti di corpus:** 0 

| # | Bukti | Sumber | Hlm. | Distance | Section | Cuplikan |
|---|---|---|---|---|---|---|
| 1 |  | PPT | 39 | 0.3727 | …BAB - IV > 4.11. DANA ABADI > Skenario 1 | [PPT IKU Diktisaintek Berdampak PTS V2 / BAB - IV > 4.11. DANA ABADI > Skenario 1 / hlm. 39] Analisis (Dalam Miliar Rp) / PERGURUAN TINGGI / DANA ABADI 2024 (A) |
| 2 |  | PPT | 28 | 0.3783 | …3. PROYEKSI PERTUMBUHAN MAHASISWA ASING 2030 > Universitas Gadjah Mada | [PPT IKU Diktisaintek Berdampak PTS V2 / BAB - IV > 4.3. PROYEKSI PERTUMBUHAN MAHASISWA ASING 2030 > Universitas Gadjah Mada / hlm. 28] / Tahun 2025 / Target IK |
| 3 |  | PPT | 39 | 0.3815 | …BAB - IV > 4.11. DANA ABADI > Hasil Perbandingan 2 Skenario | [PPT IKU Diktisaintek Berdampak PTS V2 / BAB - IV > 4.11. DANA ABADI > Hasil Perbandingan 2 Skenario / hlm. 39] (Dalam Miliar Rp) Tabel: Hasil Perbandingan 2 Sk |
| 4 |  | Buku | 33 | 0.3902 | …BAB - IV > 4.3. PROYEKSI PERTUMBUHAN MAHASISWA ASING 2030 | [Buku IKU Diktisaintek Berdampak V1 / BAB - IV > 4.3. PROYEKSI PERTUMBUHAN MAHASISWA ASING 2030 / hlm. 33] Sebagai ilustrasi implementasi kebijakan peningkatan  |
| 5 |  | Buku | 43 | 0.3939 | …BAB - IV > 4.10. DANA ABADI > Latar Belakang | [Buku IKU Diktisaintek Berdampak V1 / BAB - IV > 4.10. DANA ABADI > Latar Belakang / hlm. 43] **Dana Abadi Top 7 PTN-BH 2024** (Dalam Miliar Rp) / PERGURUAN TIN |

</details>

<details><summary>✅ <b>H01</b> — HIT @2 — Prodi S1 memiliki 200 mahasiswa dalam satu tahun akademik. Sebanyak 40 mahasiswa lulus tep</summary>

**Pertanyaan:** Prodi S1 memiliki 200 mahasiswa dalam satu tahun akademik. Sebanyak 40 mahasiswa lulus tepat 8 semester. Berapa AEE realisasi dan tingkat pencapaian AEE prodi tersebut?

**Kata kunci bukti:** `aee ideal`, `tingkat pencapaian aee`

**Halaman benar:** 49 | **Chunk bukti di corpus:** 5 (Buku hlm.49–50, Buku hlm.49–50, Buku hlm.101–102, Buku hlm.101–102, PPT hlm.46)

| # | Bukti | Sumber | Hlm. | Distance | Section | Cuplikan |
|---|---|---|---|---|---|---|
| 1 |  | Buku | 100–101 | 0.3543 | …LAMPIRAN Kepmen 358/M/KEP/2025 > 1. IKU BAGI PERGURUAN TINGGI | [Buku IKU Diktisaintek Berdampak V1 (Lampiran Kepmen 358/M/KEP/2025) / LAMPIRAN Kepmen 358/M/KEP/2025 > 1. IKU BAGI PERGURUAN TINGGI > IKU 1. Angka Efisiensi Ed |
| 2 | ✅ | Buku | 101–102 | 0.4025 | …LAMPIRAN Kepmen 358/M/KEP/2025 > 1. IKU BAGI PERGURUAN TINGGI | [Buku IKU Diktisaintek Berdampak V1 (Lampiran Kepmen 358/M/KEP/2025) / LAMPIRAN Kepmen 358/M/KEP/2025 > 1. IKU BAGI PERGURUAN TINGGI > IKU 1. Angka Efisiensi Ed |
| 3 |  | Buku | 49 | 0.4029 | …U) Diktisaintek Berdampak > 5.3.1. Indikator Kinerja Utama (IKU) Wajib | [Buku IKU Diktisaintek Berdampak V1 / BAB - V > 5.3. Indikator Kinerja Utama (IKU) Diktisaintek Berdampak > 5.3.1. Indikator Kinerja Utama (IKU) Wajib > IKU 1 / |
| 4 | ✅ | Buku | 49–50 | 0.4089 | …U) Diktisaintek Berdampak > 5.3.1. Indikator Kinerja Utama (IKU) Wajib | [Buku IKU Diktisaintek Berdampak V1 / BAB - V > 5.3. Indikator Kinerja Utama (IKU) Diktisaintek Berdampak > 5.3.1. Indikator Kinerja Utama (IKU) Wajib > IKU 1 / |
| 5 | ✅ | Buku | 101–102 | 0.4115 | …LAMPIRAN Kepmen 358/M/KEP/2025 > 1. IKU BAGI PERGURUAN TINGGI | [Buku IKU Diktisaintek Berdampak V1 (Lampiran Kepmen 358/M/KEP/2025) / LAMPIRAN Kepmen 358/M/KEP/2025 > 1. IKU BAGI PERGURUAN TINGGI > IKU 1. Angka Efisiensi Ed |

</details>

<details><summary>✅ <b>H02</b> — HIT @1 — Sebuah PT memiliki 3 program pendidikan: D3 dengan AEE realisasi 30%, S1 dengan 22,5%, dan</summary>

**Pertanyaan:** Sebuah PT memiliki 3 program pendidikan: D3 dengan AEE realisasi 30%, S1 dengan 22,5%, dan S2 dengan 40%. Berapa AEE PT?

**Kata kunci bukti:** `aee pt`, `tingkat pencapaian`

**Halaman benar:** 49, 50 | **Chunk bukti di corpus:** 7 (Buku hlm.49–50, Buku hlm.49–50, Buku hlm.100, Buku hlm.101–102, Buku hlm.101–102, PPT hlm.46)

| # | Bukti | Sumber | Hlm. | Distance | Section | Cuplikan |
|---|---|---|---|---|---|---|
| 1 | ✅ | Buku | 101–102 | 0.2946 | …LAMPIRAN Kepmen 358/M/KEP/2025 > 1. IKU BAGI PERGURUAN TINGGI | [Buku IKU Diktisaintek Berdampak V1 (Lampiran Kepmen 358/M/KEP/2025) / LAMPIRAN Kepmen 358/M/KEP/2025 > 1. IKU BAGI PERGURUAN TINGGI > IKU 1. Angka Efisiensi Ed |
| 2 | ✅ | Buku | 101–102 | 0.3012 | …LAMPIRAN Kepmen 358/M/KEP/2025 > 1. IKU BAGI PERGURUAN TINGGI | [Buku IKU Diktisaintek Berdampak V1 (Lampiran Kepmen 358/M/KEP/2025) / LAMPIRAN Kepmen 358/M/KEP/2025 > 1. IKU BAGI PERGURUAN TINGGI > IKU 1. Angka Efisiensi Ed |
| 3 |  | Buku | 100–101 | 0.3293 | …LAMPIRAN Kepmen 358/M/KEP/2025 > 1. IKU BAGI PERGURUAN TINGGI | [Buku IKU Diktisaintek Berdampak V1 (Lampiran Kepmen 358/M/KEP/2025) / LAMPIRAN Kepmen 358/M/KEP/2025 > 1. IKU BAGI PERGURUAN TINGGI > IKU 1. Angka Efisiensi Ed |
| 4 |  | Buku | 100 | 0.3396 | …LAMPIRAN Kepmen 358/M/KEP/2025 > 1. IKU BAGI PERGURUAN TINGGI | [Buku IKU Diktisaintek Berdampak V1 (Lampiran Kepmen 358/M/KEP/2025) / LAMPIRAN Kepmen 358/M/KEP/2025 > 1. IKU BAGI PERGURUAN TINGGI > IKU 1. Angka Efisiensi Ed |
| 5 | ✅ | PPT | 46 | 0.3439 | …ma (IKU) Wajib > 1 IKU 1: Angka Efisiensi Edukasi Perguruan Tinggi (2) | [PPT IKU Diktisaintek Berdampak PTS V2 / BAB - V > 5.3. INDIKATOR KINERJA UTAMA (IKU) DIKTISAINTEK BERDAMPAK > 5.3.1. Indikator Kinerja Utama (IKU) Wajib > 1 IK |

</details>

<details><summary>✅ <b>H03</b> — HIT @1 — Prodi S1 mencatat 250 mahasiswa pada satu tahun akademik, termasuk 10 mahasiswa pindah dan</summary>

**Pertanyaan:** Prodi S1 mencatat 250 mahasiswa pada satu tahun akademik, termasuk 10 mahasiswa pindah dan 15 mahasiswa *drop out*. Sebanyak 45 mahasiswa lulus tepat 8 semester. Berapa AEE realisasi dan tingkat pencapaiannya?

**Kata kunci bukti:** `drop out`, `mahasiswa pindah`

**Halaman benar:** 49 | **Chunk bukti di corpus:** 3 (Buku hlm.49, Buku hlm.100–101, PPT hlm.45)

| # | Bukti | Sumber | Hlm. | Distance | Section | Cuplikan |
|---|---|---|---|---|---|---|
| 1 | ✅ | Buku | 100–101 | 0.3368 | …LAMPIRAN Kepmen 358/M/KEP/2025 > 1. IKU BAGI PERGURUAN TINGGI | [Buku IKU Diktisaintek Berdampak V1 (Lampiran Kepmen 358/M/KEP/2025) / LAMPIRAN Kepmen 358/M/KEP/2025 > 1. IKU BAGI PERGURUAN TINGGI > IKU 1. Angka Efisiensi Ed |
| 2 |  | Buku | 101–102 | 0.3781 | …LAMPIRAN Kepmen 358/M/KEP/2025 > 1. IKU BAGI PERGURUAN TINGGI | [Buku IKU Diktisaintek Berdampak V1 (Lampiran Kepmen 358/M/KEP/2025) / LAMPIRAN Kepmen 358/M/KEP/2025 > 1. IKU BAGI PERGURUAN TINGGI > IKU 1. Angka Efisiensi Ed |
| 3 |  | Buku | 25 | 0.3824 | …EMENTERIAN > INDIKATOR KINERJA DIKTISAINTEK BERDAMPAK PERGURUAN TINGGI | [Buku IKU Diktisaintek Berdampak V1 / BAB - III > 3.7. KETERKAITAN IKU DIKTISAINTEK BERDAMPAK DENGAN IKU KEMENTERIAN > INDIKATOR KINERJA DIKTISAINTEK BERDAMPAK  |
| 4 | ✅ | Buku | 49 | 0.3883 | …U) Diktisaintek Berdampak > 5.3.1. Indikator Kinerja Utama (IKU) Wajib | [Buku IKU Diktisaintek Berdampak V1 / BAB - V > 5.3. Indikator Kinerja Utama (IKU) Diktisaintek Berdampak > 5.3.1. Indikator Kinerja Utama (IKU) Wajib > IKU 1 / |
| 5 |  | Buku | 49–50 | 0.3915 | …U) Diktisaintek Berdampak > 5.3.1. Indikator Kinerja Utama (IKU) Wajib | [Buku IKU Diktisaintek Berdampak V1 / BAB - V > 5.3. Indikator Kinerja Utama (IKU) Diktisaintek Berdampak > 5.3.1. Indikator Kinerja Utama (IKU) Wajib > IKU 1 / |

</details>

<details><summary>✅ <b>H04</b> — HIT @1 — Tracer study mengumpulkan 400 responden lulusan S1. Sebanyak 280 lulusan bekerja dengan ma</summary>

**Pertanyaan:** Tracer study mengumpulkan 400 responden lulusan S1. Sebanyak 280 lulusan bekerja dengan masa tunggu < 6 bulan dan gaji > 1,2× UMP; sisanya belum bekerja. Berapa capaian IKU 2?

**Kata kunci bukti:** `masa tunggu`, `1.2x ump`

**Halaman benar:** 51, 52 | **Chunk bukti di corpus:** 9 (Buku hlm.51, Buku hlm.103–104, Buku hlm.103–104, PPT hlm.47, PPT hlm.47, PPT hlm.47)

| # | Bukti | Sumber | Hlm. | Distance | Section | Cuplikan |
|---|---|---|---|---|---|---|
| 1 | ✅ | PPT | 47 | 0.2834 | …ma (IKU) Wajib > 1 IKU 1: Angka Efisiensi Edukasi Perguruan Tinggi (2) | [PPT IKU Diktisaintek Berdampak PTS V2 / BAB - V > 5.3. INDIKATOR KINERJA UTAMA (IKU) DIKTISAINTEK BERDAMPAK > 5.3.1. Indikator Kinerja Utama (IKU) Wajib > 1 IK |
| 2 | ✅ | PPT | 47 | 0.2947 | …ma (IKU) Wajib > 1 IKU 1: Angka Efisiensi Edukasi Perguruan Tinggi (2) | [PPT IKU Diktisaintek Berdampak PTS V2 / BAB - V > 5.3. INDIKATOR KINERJA UTAMA (IKU) DIKTISAINTEK BERDAMPAK > 5.3.1. Indikator Kinerja Utama (IKU) Wajib > 1 IK |
| 3 | ✅ | Buku | 103–104 | 0.2949 | …LAMPIRAN Kepmen 358/M/KEP/2025 > 1. IKU BAGI PERGURUAN TINGGI | [Buku IKU Diktisaintek Berdampak V1 (Lampiran Kepmen 358/M/KEP/2025) / LAMPIRAN Kepmen 358/M/KEP/2025 > 1. IKU BAGI PERGURUAN TINGGI > IKU 2. Persentase lulusan |
| 4 | ✅ | PPT | 47 | 0.2974 | …ma (IKU) Wajib > 1 IKU 1: Angka Efisiensi Edukasi Perguruan Tinggi (2) | [PPT IKU Diktisaintek Berdampak PTS V2 / BAB - V > 5.3. INDIKATOR KINERJA UTAMA (IKU) DIKTISAINTEK BERDAMPAK > 5.3.1. Indikator Kinerja Utama (IKU) Wajib > 1 IK |
| 5 | ✅ | Buku | 103–104 | 0.2979 | …LAMPIRAN Kepmen 358/M/KEP/2025 > 1. IKU BAGI PERGURUAN TINGGI | [Buku IKU Diktisaintek Berdampak V1 (Lampiran Kepmen 358/M/KEP/2025) / LAMPIRAN Kepmen 358/M/KEP/2025 > 1. IKU BAGI PERGURUAN TINGGI > IKU 2. Persentase lulusan |

</details>

<details><summary>✅ <b>H05</b> — HIT @2 — Tracer study mengumpulkan 500 responden lulusan. Rinciannya: - 200 bekerja, masa tunggu < </summary>

**Pertanyaan:** Tracer study mengumpulkan 500 responden lulusan. Rinciannya: - 200 bekerja, masa tunggu < 6 bulan, gaji > 1,2× UMP - 100 bekerja, masa tunggu < 1 tahun, gaji > 1,2× UMP - 50 bekerja, masa tunggu < 1 tahun, gaji < 1,2× UMP - 30 melanjutkan studi (surat penerimaan < 12 bulan) - 20 *founder*, < 6 bulan, penghasilan > 1,2× UMP - 10 *freelancer*, > 6 bulan, penghasilan < 1,2× UMP - 90 belum bekerja/studi/wirausaha Berapa capaian IKU 2?

**Kata kunci bukti:** `freelancer`, `bobot = 0,8`

**Halaman benar:** 51, 52 | **Chunk bukti di corpus:** 2 (PPT hlm.47, PPT hlm.47)

| # | Bukti | Sumber | Hlm. | Distance | Section | Cuplikan |
|---|---|---|---|---|---|---|
| 1 |  | PPT | 47 | 0.2473 | …ma (IKU) Wajib > 1 IKU 1: Angka Efisiensi Edukasi Perguruan Tinggi (2) | [PPT IKU Diktisaintek Berdampak PTS V2 / BAB - V > 5.3. INDIKATOR KINERJA UTAMA (IKU) DIKTISAINTEK BERDAMPAK > 5.3.1. Indikator Kinerja Utama (IKU) Wajib > 1 IK |
| 2 | ✅ | PPT | 47 | 0.2605 | …ma (IKU) Wajib > 1 IKU 1: Angka Efisiensi Edukasi Perguruan Tinggi (2) | [PPT IKU Diktisaintek Berdampak PTS V2 / BAB - V > 5.3. INDIKATOR KINERJA UTAMA (IKU) DIKTISAINTEK BERDAMPAK > 5.3.1. Indikator Kinerja Utama (IKU) Wajib > 1 IK |
| 3 |  | PPT | 47 | 0.2627 | …ma (IKU) Wajib > 1 IKU 1: Angka Efisiensi Edukasi Perguruan Tinggi (2) | [PPT IKU Diktisaintek Berdampak PTS V2 / BAB - V > 5.3. INDIKATOR KINERJA UTAMA (IKU) DIKTISAINTEK BERDAMPAK > 5.3.1. Indikator Kinerja Utama (IKU) Wajib > 1 IK |
| 4 |  | Buku | 51 | 0.2634 | …Berikutnya/ Berwirausaha dalam Jangka Waktu 1 Tahun Setelah Kelulusan. | [Buku IKU Diktisaintek Berdampak V1 / BAB - V > 5.3. Indikator Kinerja Utama (IKU) Diktisaintek Berdampak > 5.3.1. Indikator Kinerja Utama (IKU) Wajib > 2 IKU 2 |
| 5 |  | Buku | 103–104 | 0.2641 | …LAMPIRAN Kepmen 358/M/KEP/2025 > 1. IKU BAGI PERGURUAN TINGGI | [Buku IKU Diktisaintek Berdampak V1 (Lampiran Kepmen 358/M/KEP/2025) / LAMPIRAN Kepmen 358/M/KEP/2025 > 1. IKU BAGI PERGURUAN TINGGI > IKU 2. Persentase lulusan |

</details>

<details><summary>✅ <b>H06</b> — HIT @1 — Jumlah lulusan suatu PT adalah 2.000 orang. Berapa jumlah responden minimum tracer study u</summary>

**Pertanyaan:** Jumlah lulusan suatu PT adalah 2.000 orang. Berapa jumlah responden minimum tracer study untuk IKU 2?

**Kata kunci bukti:** `responden minimum`, `galat`

**Halaman benar:** 52 | **Chunk bukti di corpus:** 3 (Buku hlm.52, Buku hlm.104–105, PPT hlm.48–49)

| # | Bukti | Sumber | Hlm. | Distance | Section | Cuplikan |
|---|---|---|---|---|---|---|
| 1 | ✅ | PPT | 48–49 | 0.3538 | …kutnya/ Berwirausaha dalam Jangka Waktu 1 Tahun Setelah Kelulusan. (2) | [PPT IKU Diktisaintek Berdampak PTS V2 / BAB - V > 5.3. INDIKATOR KINERJA UTAMA (IKU) DIKTISAINTEK BERDAMPAK > 5.3.1. Indikator Kinerja Utama (IKU) Wajib > IKU  |
| 2 |  | PPT | 48 | 0.357 | …kutnya/ Berwirausaha dalam Jangka Waktu 1 Tahun Setelah Kelulusan. (2) | [PPT IKU Diktisaintek Berdampak PTS V2 / BAB - V > 5.3. INDIKATOR KINERJA UTAMA (IKU) DIKTISAINTEK BERDAMPAK > 5.3.1. Indikator Kinerja Utama (IKU) Wajib > IKU  |
| 3 |  | Buku | 104 | 0.3666 | …LAMPIRAN Kepmen 358/M/KEP/2025 > 1. IKU BAGI PERGURUAN TINGGI | [Buku IKU Diktisaintek Berdampak V1 (Lampiran Kepmen 358/M/KEP/2025) / LAMPIRAN Kepmen 358/M/KEP/2025 > 1. IKU BAGI PERGURUAN TINGGI > IKU 2. Persentase lulusan |
| 4 |  | PPT | 47 | 0.3703 | …ma (IKU) Wajib > 1 IKU 1: Angka Efisiensi Edukasi Perguruan Tinggi (2) | [PPT IKU Diktisaintek Berdampak PTS V2 / BAB - V > 5.3. INDIKATOR KINERJA UTAMA (IKU) DIKTISAINTEK BERDAMPAK > 5.3.1. Indikator Kinerja Utama (IKU) Wajib > 1 IK |
| 5 |  | PPT | 47 | 0.3717 | …ma (IKU) Wajib > 1 IKU 1: Angka Efisiensi Edukasi Perguruan Tinggi (2) | [PPT IKU Diktisaintek Berdampak PTS V2 / BAB - V > 5.3. INDIKATOR KINERJA UTAMA (IKU) DIKTISAINTEK BERDAMPAK > 5.3.1. Indikator Kinerja Utama (IKU) Wajib > 1 IK |

</details>

<details><summary>✅ <b>H07</b> — HIT @1 — Sebuah PT memiliki 1.000 mahasiswa S1/Diploma. Rinciannya: - 100 mahasiswa magang 20 SKS -</summary>

**Pertanyaan:** Sebuah PT memiliki 1.000 mahasiswa S1/Diploma. Rinciannya: - 100 mahasiswa magang 20 SKS - 150 mahasiswa pertukaran 8 SKS - 50 mahasiswa riset 4 SKS - 5 mahasiswa juara 1 lomba nasional - 10 mahasiswa finalis lomba internasional Berapa capaian IKU 3?

**Kata kunci bukti:** `5 sks, bobot = 0,4`, `finalis, bobot = 0,2`

**Halaman benar:** 53, 54 | **Chunk bukti di corpus:** 3 (Buku hlm.53–54, Buku hlm.107–108, PPT hlm.50)

| # | Bukti | Sumber | Hlm. | Distance | Section | Cuplikan |
|---|---|---|---|---|---|---|
| 1 | ✅ | Buku | 107–108 | 0.3249 | …LAMPIRAN Kepmen 358/M/KEP/2025 > 1. IKU BAGI PERGURUAN TINGGI | [Buku IKU Diktisaintek Berdampak V1 (Lampiran Kepmen 358/M/KEP/2025) / LAMPIRAN Kepmen 358/M/KEP/2025 > 1. IKU BAGI PERGURUAN TINGGI > IKU 3. Persentase mahasis |
| 2 | ✅ | PPT | 50 | 0.3272 | … dan D4/D3/D2/D1 Berkegiatan/Meraih Prestasi di Luar Program Studi (2) | [PPT IKU Diktisaintek Berdampak PTS V2 / BAB - V > 5.3. INDIKATOR KINERJA UTAMA (IKU) DIKTISAINTEK BERDAMPAK > 5.3.1. Indikator Kinerja Utama (IKU) Wajib > 3 IK |
| 3 | ✅ | Buku | 53–54 | 0.3276 | …a S1 dan D4/D3/D2/D1 Berkegiatan/Meraih Prestasi di Luar Program Studi | [Buku IKU Diktisaintek Berdampak V1 / BAB - V > 5.3. Indikator Kinerja Utama (IKU) Diktisaintek Berdampak > 5.3.1. Indikator Kinerja Utama (IKU) Wajib > 3 IKU 3 |
| 4 |  | Buku | 53 | 0.3301 | …a S1 dan D4/D3/D2/D1 Berkegiatan/Meraih Prestasi di Luar Program Studi | [Buku IKU Diktisaintek Berdampak V1 / BAB - V > 5.3. Indikator Kinerja Utama (IKU) Diktisaintek Berdampak > 5.3.1. Indikator Kinerja Utama (IKU) Wajib > 3 IKU 3 |
| 5 |  | Buku | 53 | 0.3311 | …a S1 dan D4/D3/D2/D1 Berkegiatan/Meraih Prestasi di Luar Program Studi | [Buku IKU Diktisaintek Berdampak V1 / BAB - V > 5.3. Indikator Kinerja Utama (IKU) Diktisaintek Berdampak > 5.3.1. Indikator Kinerja Utama (IKU) Wajib > 3 IKU 3 |

</details>

<details><summary>✅ <b>H08</b> — HIT @1 — Dari 500 mahasiswa, prestasi yang tercatat adalah 2 juara 1 internasional, 4 juara 2 tingk</summary>

**Pertanyaan:** Dari 500 mahasiswa, prestasi yang tercatat adalah 2 juara 1 internasional, 4 juara 2 tingkat provinsi, dan 20 finalis tingkat provinsi. Tidak ada kegiatan SKS di luar prodi. Berapa capaian IKU 3?

**Kata kunci bukti:** `juara harapan`, `finalis, bobot = 0,05`

**Halaman benar:** 54 | **Chunk bukti di corpus:** 3 (Buku hlm.53–54, Buku hlm.107–108, PPT hlm.50)

| # | Bukti | Sumber | Hlm. | Distance | Section | Cuplikan |
|---|---|---|---|---|---|---|
| 1 | ✅ | Buku | 53–54 | 0.3073 | …a S1 dan D4/D3/D2/D1 Berkegiatan/Meraih Prestasi di Luar Program Studi | [Buku IKU Diktisaintek Berdampak V1 / BAB - V > 5.3. Indikator Kinerja Utama (IKU) Diktisaintek Berdampak > 5.3.1. Indikator Kinerja Utama (IKU) Wajib > 3 IKU 3 |
| 2 | ✅ | PPT | 50 | 0.3222 | … dan D4/D3/D2/D1 Berkegiatan/Meraih Prestasi di Luar Program Studi (2) | [PPT IKU Diktisaintek Berdampak PTS V2 / BAB - V > 5.3. INDIKATOR KINERJA UTAMA (IKU) DIKTISAINTEK BERDAMPAK > 5.3.1. Indikator Kinerja Utama (IKU) Wajib > 3 IK |
| 3 | ✅ | Buku | 107–108 | 0.3262 | …LAMPIRAN Kepmen 358/M/KEP/2025 > 1. IKU BAGI PERGURUAN TINGGI | [Buku IKU Diktisaintek Berdampak V1 (Lampiran Kepmen 358/M/KEP/2025) / LAMPIRAN Kepmen 358/M/KEP/2025 > 1. IKU BAGI PERGURUAN TINGGI > IKU 3. Persentase mahasis |
| 4 |  | Buku | 53 | 0.3358 | …a S1 dan D4/D3/D2/D1 Berkegiatan/Meraih Prestasi di Luar Program Studi | [Buku IKU Diktisaintek Berdampak V1 / BAB - V > 5.3. Indikator Kinerja Utama (IKU) Diktisaintek Berdampak > 5.3.1. Indikator Kinerja Utama (IKU) Wajib > 3 IKU 3 |
| 5 |  | Buku | 53 | 0.3403 | …a S1 dan D4/D3/D2/D1 Berkegiatan/Meraih Prestasi di Luar Program Studi | [Buku IKU Diktisaintek Berdampak V1 / BAB - V > 5.3. Indikator Kinerja Utama (IKU) Diktisaintek Berdampak > 5.3.1. Indikator Kinerja Utama (IKU) Wajib > 3 IKU 3 |

</details>

<details><summary>✅ <b>H09</b> — HIT @2 — PT memiliki 120 kerja sama. Dari kerja sama itu dihasilkan 30 karya (judul) yang telah dim</summary>

**Pertanyaan:** PT memiliki 120 kerja sama. Dari kerja sama itu dihasilkan 30 karya (judul) yang telah dimanfaatkan oleh mitra, melibatkan total 90 dosen. Berapa capaian IKU 5?

**Kata kunci bukti:** `total kerjasama perguruan tinggi`, `bukan jumlah dosen`

**Halaman benar:** 57 | **Chunk bukti di corpus:** 3 (Buku hlm.57–58, Buku hlm.117, PPT hlm.53)

| # | Bukti | Sumber | Hlm. | Distance | Section | Cuplikan |
|---|---|---|---|---|---|---|
| 1 |  | Buku | 56–57 | 0.308 | … Hasil Kerjasama Antara Perguruan Tinggi dan Start-Up/Industri/Lembaga | [Buku IKU Diktisaintek Berdampak V1 / BAB - V > 5.3. Indikator Kinerja Utama (IKU) Diktisaintek Berdampak > 5.3.1. Indikator Kinerja Utama (IKU) Wajib > 4 IKU 5 |
| 2 | ✅ | Buku | 57–58 | 0.3089 | … Hasil Kerjasama Antara Perguruan Tinggi dan Start-Up/Industri/Lembaga | [Buku IKU Diktisaintek Berdampak V1 / BAB - V > 5.3. Indikator Kinerja Utama (IKU) Diktisaintek Berdampak > 5.3.1. Indikator Kinerja Utama (IKU) Wajib > 4 IKU 5 |
| 3 |  | PPT | 52 | 0.309 | …il Kerjasama Antara Perguruan Tinggi dan Start-Up/Industri/Lembaga (2) | [PPT IKU Diktisaintek Berdampak PTS V2 / BAB - V > 5.3. INDIKATOR KINERJA UTAMA (IKU) DIKTISAINTEK BERDAMPAK > 5.3.1. Indikator Kinerja Utama (IKU) Wajib > IKU  |
| 4 | ✅ | PPT | 53 | 0.309 | …il Kerjasama Antara Perguruan Tinggi dan Start-Up/Industri/Lembaga (3) | [PPT IKU Diktisaintek Berdampak PTS V2 / BAB - V > 5.3. INDIKATOR KINERJA UTAMA (IKU) DIKTISAINTEK BERDAMPAK > 5.3.1. Indikator Kinerja Utama (IKU) Wajib > 4 IK |
| 5 | ✅ | Buku | 117 | 0.3091 | …LAMPIRAN Kepmen 358/M/KEP/2025 > 1. IKU BAGI PERGURUAN TINGGI | [Buku IKU Diktisaintek Berdampak V1 (Lampiran Kepmen 358/M/KEP/2025) / LAMPIRAN Kepmen 358/M/KEP/2025 > 1. IKU BAGI PERGURUAN TINGGI > IKU 5. Persentase luaran  |

</details>

<details><summary>✅ <b>H10</b> — HIT @1 — Total publikasi PT dalam satu periode adalah 200, terdiri atas 10 jurnal Top Tier, 40 Q1, </summary>

**Pertanyaan:** Total publikasi PT dalam satu periode adalah 200, terdiri atas 10 jurnal Top Tier, 40 Q1, 50 Q2, 30 Q3, 20 Q4, dan 50 publikasi tidak terindeks Scopus/WoS. Berapa capaian IKU 6?

**Kata kunci bukti:** `top tier`, `q4`

**Halaman benar:** 63 | **Chunk bukti di corpus:** 8 (Buku hlm.63, Buku hlm.75, Buku hlm.76, Buku hlm.117–118, PPT hlm.61, PPT hlm.76)

| # | Bukti | Sumber | Hlm. | Distance | Section | Cuplikan |
|---|---|---|---|---|---|---|
| 1 | ✅ | PPT | 76 | 0.2906 | …rnasional (Scopus/WoS) > c. Persentase Publikasi Bereputasi Quartile 1 | [PPT IKU Diktisaintek Berdampak PTS V2 / BAB - V > 5.4. Sub Indikator Kinerja Utama (IKU) > 5.4.3. Sub Indikator (IKU 6): Persentase Publikasi Bereputasi Intern |
| 2 |  | PPT | 75 | 0.2909 | …ternasional (Scopus/WoS) > b. Persentase Publikasi Bereputasi Top Tier | [PPT IKU Diktisaintek Berdampak PTS V2 / BAB - V > 5.4. Sub Indikator Kinerja Utama (IKU) > 5.4.3. Sub Indikator (IKU 6): Persentase Publikasi Bereputasi Intern |
| 3 |  | Buku | 74 | 0.304 | …ternasional (Scopus/WoS) > b. Persentase Publikasi Bereputasi Top Tier | [Buku IKU Diktisaintek Berdampak V1 / BAB - V > 5.4. Sub Indikator Kinerja Utama (IKU) > 5.4.3. Sub Indikator (IKU 6): Persentase Publikasi Bereputasi Internasi |
| 4 | ✅ | Buku | 75 | 0.3098 | …rnasional (Scopus/WoS) > c. Persentase Publikasi Bereputasi Quartile 1 | [Buku IKU Diktisaintek Berdampak V1 / BAB - V > 5.4. Sub Indikator Kinerja Utama (IKU) > 5.4.3. Sub Indikator (IKU 6): Persentase Publikasi Bereputasi Internasi |
| 5 |  | PPT | 74 | 0.3137 | …reputasi Internasional (Scopus/WoS) > a. Total Publikasi Internasional | [PPT IKU Diktisaintek Berdampak PTS V2 / BAB - V > 5.4. Sub Indikator Kinerja Utama (IKU) > 5.4.3. Sub Indikator (IKU 6): Persentase Publikasi Bereputasi Intern |

</details>

<details><summary>✅ <b>H11</b> — HIT @3 — Total publikasi 20, terdiri atas 4 artikel Q1 hasil kolaborasi dengan penulis luar negeri,</summary>

**Pertanyaan:** Total publikasi 20, terdiri atas 4 artikel Q1 hasil kolaborasi dengan penulis luar negeri, 6 artikel Q1 tanpa kolaborasi, dan 10 prosiding internasional terindeks Scopus. Berapa capaian IKU 6?

**Kata kunci bukti:** `kolaborasi internasional`, `prosiding internasional`

**Halaman benar:** 63 | **Chunk bukti di corpus:** 6 (Buku hlm.63, Buku hlm.63, Buku hlm.117–118, Buku hlm.118–119, PPT hlm.61, PPT hlm.61–62)

| # | Bukti | Sumber | Hlm. | Distance | Section | Cuplikan |
|---|---|---|---|---|---|---|
| 1 |  | Buku | 76 | 0.3096 | …al (Scopus/WoS) > d. Persentase Penelitian Berkolaborasi Internasional | [Buku IKU Diktisaintek Berdampak V1 / BAB - V > 5.4. Sub Indikator Kinerja Utama (IKU) > 5.4.3. Sub Indikator (IKU 6): Persentase Publikasi Bereputasi Internasi |
| 2 |  | PPT | 77 | 0.3146 | …al (Scopus/WoS) > d. Persentase Penelitian Berkolaborasi Internasional | [PPT IKU Diktisaintek Berdampak PTS V2 / BAB - V > 5.4. Sub Indikator Kinerja Utama (IKU) > 5.4.3. Sub Indikator (IKU 6): Persentase Publikasi Bereputasi Intern |
| 3 | ✅ | Buku | 117–118 | 0.3225 | …LAMPIRAN Kepmen 358/M/KEP/2025 > 1. IKU BAGI PERGURUAN TINGGI | [Buku IKU Diktisaintek Berdampak V1 (Lampiran Kepmen 358/M/KEP/2025) / LAMPIRAN Kepmen 358/M/KEP/2025 > 1. IKU BAGI PERGURUAN TINGGI > IKU 6. Persentase publika |
| 4 | ✅ | Buku | 63 | 0.3226 | …an > IKU 6: Persentase Publikasi Bereputasi Internasional (Scopus/WoS) | [Buku IKU Diktisaintek Berdampak V1 / BAB - V > 5.3. Indikator Kinerja Utama (IKU) Diktisaintek Berdampak > 5.3.2. Indikator Kinerja Utama (IKU) Pilihan > IKU 6 |
| 5 |  | Buku | 73 | 0.3239 | …reputasi Internasional (Scopus/WoS) > a. Total Publikasi Internasional | [Buku IKU Diktisaintek Berdampak V1 / BAB - V > 5.4. Sub Indikator Kinerja Utama (IKU) > 5.4.3. Sub Indikator (IKU 6): Persentase Publikasi Bereputasi Internasi |

</details>

<details><summary>✅ <b>H12</b> — HIT @1 — Dari 60 program SDGs PT, 45 program berkontribusi pada SDG 1, 4, 17, dan 2 SDG pilihan. Be</summary>

**Pertanyaan:** Dari 60 program SDGs PT, 45 program berkontribusi pada SDG 1, 4, 17, dan 2 SDG pilihan. Berapa capaian IKU 7?

**Kata kunci bukti:** `total program sdg`

**Halaman benar:** 58 | **Chunk bukti di corpus:** 3 (Buku hlm.58, Buku hlm.121, PPT hlm.55)

| # | Bukti | Sumber | Hlm. | Distance | Section | Cuplikan |
|---|---|---|---|---|---|---|
| 1 | ✅ | PPT | 55 | 0.2854 | …ualitas), SDG17 (Kemitraan), dan 2(dua)SDGs Lain Sesuai Keunggulan (2) | [PPT IKU Diktisaintek Berdampak PTS V2 / BAB - V > 5.3. INDIKATOR KINERJA UTAMA (IKU) DIKTISAINTEK BERDAMPAK > 5.3.1. Indikator Kinerja Utama (IKU) Wajib > IKU  |
| 2 |  | PPT | 55 | 0.2904 | …ualitas), SDG17 (Kemitraan), dan 2(dua)SDGs Lain Sesuai Keunggulan (2) | [PPT IKU Diktisaintek Berdampak PTS V2 / BAB - V > 5.3. INDIKATOR KINERJA UTAMA (IKU) DIKTISAINTEK BERDAMPAK > 5.3.1. Indikator Kinerja Utama (IKU) Wajib > IKU  |
| 3 | ✅ | Buku | 58 | 0.2928 | …Berkualitas), SDG17 (Kemitraan), dan 2(dua)SDGs Lain Sesuai Keunggulan | [Buku IKU Diktisaintek Berdampak V1 / BAB - V > 5.3. Indikator Kinerja Utama (IKU) Diktisaintek Berdampak > 5.3.1. Indikator Kinerja Utama (IKU) Wajib > IKU 7:  |
| 4 |  | Buku | 58 | 0.2937 | …Berkualitas), SDG17 (Kemitraan), dan 2(dua)SDGs Lain Sesuai Keunggulan | [Buku IKU Diktisaintek Berdampak V1 / BAB - V > 5.3. Indikator Kinerja Utama (IKU) Diktisaintek Berdampak > 5.3.1. Indikator Kinerja Utama (IKU) Wajib > IKU 7:  |
| 5 | ✅ | Buku | 121 | 0.3091 | …LAMPIRAN Kepmen 358/M/KEP/2025 > 1. IKU BAGI PERGURUAN TINGGI | [Buku IKU Diktisaintek Berdampak V1 (Lampiran Kepmen 358/M/KEP/2025) / LAMPIRAN Kepmen 358/M/KEP/2025 > 1. IKU BAGI PERGURUAN TINGGI > IKU 7. Persentase keterli |

</details>

<details><summary>✅ <b>H13</b> — HIT @1 — Total pendapatan PT dalam satu tahun anggaran adalah Rp500 miliar, terdiri atas: - UKT Rp3</summary>

**Pertanyaan:** Total pendapatan PT dalam satu tahun anggaran adalah Rp500 miliar, terdiri atas: - UKT Rp300 miliar - BOPTN Rp80 miliar - hibah riset kompetitif Rp50 miliar - jasa konsultasi dan pelatihan Rp40 miliar - unit bisnis (hotel, penerbitan) Rp20 miliar - hasil investasi dana abadi Rp10 miliar Berapa capaian IKU 9?

**Kata kunci bukti:** `boptn`, `dana abadi`

**Halaman benar:** 59 | **Chunk bukti di corpus:** 3 (Buku hlm.59, Buku hlm.122–123, PPT hlm.56)

| # | Bukti | Sumber | Hlm. | Distance | Section | Cuplikan |
|---|---|---|---|---|---|---|
| 1 | ✅ | Buku | 59 | 0.3208 | … Utama (IKU) Wajib > 6 IKU 9: Persentase Pendapatan Non Pendidikan/UKT | [Buku IKU Diktisaintek Berdampak V1 / BAB - V > 5.3. Indikator Kinerja Utama (IKU) Diktisaintek Berdampak > 5.3.1. Indikator Kinerja Utama (IKU) Wajib > 6 IKU 9 |
| 2 | ✅ | Buku | 122–123 | 0.3263 | …LAMPIRAN Kepmen 358/M/KEP/2025 > 1. IKU BAGI PERGURUAN TINGGI | [Buku IKU Diktisaintek Berdampak V1 (Lampiran Kepmen 358/M/KEP/2025) / LAMPIRAN Kepmen 358/M/KEP/2025 > 1. IKU BAGI PERGURUAN TINGGI > IKU 9. Persentase pendapa |
| 3 | ✅ | PPT | 56 | 0.3298 | …Utama (IKU) Wajib > 6 IKU 9 : Persentase Pendapatan Non Pendidikan/UKT | [PPT IKU Diktisaintek Berdampak PTS V2 / BAB - V > 5.3. INDIKATOR KINERJA UTAMA (IKU) DIKTISAINTEK BERDAMPAK > 5.3.1. Indikator Kinerja Utama (IKU) Wajib > 6 IK |
| 4 |  | Buku | 79 | 0.3327 | …an/UKT > 1. Persentase Pendapatan terhadap Total Aset Perguruan Tinggi | [Buku IKU Diktisaintek Berdampak V1 / BAB - V > 5.4. Sub Indikator Kinerja Utama (IKU) > 5.4.5. Sub Indikator (IKU 9): Persentase Pendapatan Non Pendidikan/UKT  |
| 5 |  | Buku | 59 | 0.3472 | … Utama (IKU) Wajib > 6 IKU 9: Persentase Pendapatan Non Pendidikan/UKT | [Buku IKU Diktisaintek Berdampak V1 / BAB - V > 5.3. Indikator Kinerja Utama (IKU) Diktisaintek Berdampak > 5.3.1. Indikator Kinerja Utama (IKU) Wajib > 6 IKU 9 |

</details>

<details><summary>✅ <b>H14</b> — HIT @1 — PT memiliki 300 dosen dalam satu tahun terakhir; 45 dosen ber-NUPTK mendapat rekognisi int</summary>

**Pertanyaan:** PT memiliki 300 dosen dalam satu tahun terakhir; 45 dosen ber-NUPTK mendapat rekognisi internasional. Berapa capaian IKU 4?

**Kata kunci bukti:** `nuptk`, `rekognisi internasional`

**Halaman benar:** 62 | **Chunk bukti di corpus:** 3 (Buku hlm.62–63, Buku hlm.112, PPT hlm.60–61)

| # | Bukti | Sumber | Hlm. | Distance | Section | Cuplikan |
|---|---|---|---|---|---|---|
| 1 | ✅ | Buku | 112 | 0.2516 | …LAMPIRAN Kepmen 358/M/KEP/2025 > 1. IKU BAGI PERGURUAN TINGGI | [Buku IKU Diktisaintek Berdampak V1 (Lampiran Kepmen 358/M/KEP/2025) / LAMPIRAN Kepmen 358/M/KEP/2025 > 1. IKU BAGI PERGURUAN TINGGI > IKU 4. Jumlah Dosen pergu |
| 2 | ✅ | PPT | 60–61 | 0.255 | …se Dosen Perguruan Tinggi yang Mendapatkan Rekognisi Internasional (3) | [PPT IKU Diktisaintek Berdampak PTS V2 / BAB - V > 5.3. INDIKATOR KINERJA UTAMA (IKU) DIKTISAINTEK BERDAMPAK > 5.3.2. Indikator Kinerja Utama (IKU) Pilihan > IK |
| 3 | ✅ | Buku | 62–63 | 0.267 | …entase Dosen Perguruan Tinggi yang Mendapatkan Rekognisi Internasional | [Buku IKU Diktisaintek Berdampak V1 / BAB - V > 5.3. Indikator Kinerja Utama (IKU) Diktisaintek Berdampak > 5.3.2. Indikator Kinerja Utama (IKU) Pilihan > IKU 4 |
| 4 |  | Buku | 108 | 0.2768 | …LAMPIRAN Kepmen 358/M/KEP/2025 > 1. IKU BAGI PERGURUAN TINGGI | [Buku IKU Diktisaintek Berdampak V1 (Lampiran Kepmen 358/M/KEP/2025) / LAMPIRAN Kepmen 358/M/KEP/2025 > 1. IKU BAGI PERGURUAN TINGGI > IKU 4. Jumlah Dosen pergu |
| 5 |  | PPT | 58 | 0.2827 | …entase Dosen Perguruan Tinggi yang Mendapatkan Rekognisi Internasional | [PPT IKU Diktisaintek Berdampak PTS V2 / BAB - V > 5.3. INDIKATOR KINERJA UTAMA (IKU) DIKTISAINTEK BERDAMPAK > 5.3.2. Indikator Kinerja Utama (IKU) Pilihan > IK |

</details>

<details><summary>❌ <b>H15</b> — MISS - bukti di rank mentah 6 — Dari 400 SDM PT (dosen/peneliti), 12 orang terlibat langsung dalam penyusunan kebijakan na</summary>

**Pertanyaan:** Dari 400 SDM PT (dosen/peneliti), 12 orang terlibat langsung dalam penyusunan kebijakan nasional/daerah/industri, dibuktikan dengan SK atau undangan resmi. Berapa capaian IKU 8?

**Kata kunci bukti:** `penyusunan kebijakan`, `total sdm pt`

**Halaman benar:** 64 | **Chunk bukti di corpus:** 3 (Buku hlm.64, Buku hlm.122, PPT hlm.63)

| # | Bukti | Sumber | Hlm. | Distance | Section | Cuplikan |
|---|---|---|---|---|---|---|
| 1 |  | PPT | 63 | 0.2299 | …erlibat Langsung dalam Penyusunan Kebijakan (Nasional/Daerah/Industri) | [PPT IKU Diktisaintek Berdampak PTS V2 / BAB - V > 5.3. INDIKATOR KINERJA UTAMA (IKU) DIKTISAINTEK BERDAMPAK > 5.3.2. Indikator Kinerja Utama (IKU) Pilihan > 3  |
| 2 |  | PPT | 63 | 0.2326 | …erlibat Langsung dalam Penyusunan Kebijakan (Nasional/Daerah/Industri) | [PPT IKU Diktisaintek Berdampak PTS V2 / BAB - V > 5.3. INDIKATOR KINERJA UTAMA (IKU) DIKTISAINTEK BERDAMPAK > 5.3.2. Indikator Kinerja Utama (IKU) Pilihan > 3  |
| 3 |  | Buku | 64 | 0.2335 | …erlibat Langsung dalam Penyusunan Kebijakan (Nasional/Daerah/Industri) | [Buku IKU Diktisaintek Berdampak V1 / BAB - V > 5.3. Indikator Kinerja Utama (IKU) Diktisaintek Berdampak > 5.3.2. Indikator Kinerja Utama (IKU) Pilihan > IKU 8 |
| 4 |  | Buku | 64 | 0.2346 | …erlibat Langsung dalam Penyusunan Kebijakan (Nasional/Daerah/Industri) | [Buku IKU Diktisaintek Berdampak V1 / BAB - V > 5.3. Indikator Kinerja Utama (IKU) Diktisaintek Berdampak > 5.3.2. Indikator Kinerja Utama (IKU) Pilihan > IKU 8 |
| 5 |  | Buku | 121 | 0.2403 | …LAMPIRAN Kepmen 358/M/KEP/2025 > 1. IKU BAGI PERGURUAN TINGGI | [Buku IKU Diktisaintek Berdampak V1 (Lampiran Kepmen 358/M/KEP/2025) / LAMPIRAN Kepmen 358/M/KEP/2025 > 1. IKU BAGI PERGURUAN TINGGI > IKU 8. Persentase Sumber  |

</details>

<details><summary>✅ <b>H16</b> — HIT @1 — Nilai akhir evaluasi SAKIP sebuah PT adalah 82. Apa predikatnya?</summary>

**Pertanyaan:** Nilai akhir evaluasi SAKIP sebuah PT adalah 82. Apa predikatnya?

**Kata kunci bukti:** `sakip`, `sangat baik`

**Halaman benar:** 66 | **Chunk bukti di corpus:** 6 (Buku hlm.66, Buku hlm.87, Buku hlm.125–130, Buku hlm.134, Buku hlm.135, PPT hlm.66)

| # | Bukti | Sumber | Hlm. | Distance | Section | Cuplikan |
|---|---|---|---|---|---|---|
| 1 | ✅ | Buku | 135 | 0.396 | … Kepmen 358/M/KEP/2025 > 2. IKU BAGI LEMBAGA LAYANAN PENDIDIKAN TINGGI | [Buku IKU Diktisaintek Berdampak V1 (Lampiran Kepmen 358/M/KEP/2025) / LAMPIRAN Kepmen 358/M/KEP/2025 > 2. IKU BAGI LEMBAGA LAYANAN PENDIDIKAN TINGGI / hlm. 135 |
| 2 | ✅ | Buku | 66 | 0.4065 | …tem Akuntabilitas Kinerja Instansi Pemerintah (SAKIP) Perguruan Tinggi | [Buku IKU Diktisaintek Berdampak V1 / BAB - V > 5.3. Indikator Kinerja Utama (IKU) Diktisaintek Berdampak > 5.3.2. Indikator Kinerja Utama (IKU) Pilihan > IKU 1 |
| 3 | ✅ | Buku | 87 | 0.433 | …Tinggi > IKU 3: Tata kelola LLDIKTI yang berkualitas dan berintegritas | [Buku IKU Diktisaintek Berdampak V1 / BAB - VI > 5.5. Indikator Kinerja Utama (IKU) Lembaga Layanan Pendidikan Tinggi > IKU 3: Tata kelola LLDIKTI yang berkuali |
| 4 |  | Buku | 66 | 0.4374 | …tem Akuntabilitas Kinerja Instansi Pemerintah (SAKIP) Perguruan Tinggi | [Buku IKU Diktisaintek Berdampak V1 / BAB - V > 5.3. Indikator Kinerja Utama (IKU) Diktisaintek Berdampak > 5.3.2. Indikator Kinerja Utama (IKU) Pilihan > IKU 1 |
| 5 | ✅ | Buku | 125–130 | 0.4385 | …LAMPIRAN Kepmen 358/M/KEP/2025 > 1. IKU BAGI PERGURUAN TINGGI | [Buku IKU Diktisaintek Berdampak V1 (Lampiran Kepmen 358/M/KEP/2025) / LAMPIRAN Kepmen 358/M/KEP/2025 > 1. IKU BAGI PERGURUAN TINGGI > IKU 11. a. Hasil audit at |

</details>

<details><summary>✅ <b>H17</b> — HIT @1 — PT merencanakan 24 kegiatan pencegahan dan penanganan kekerasan, narkoba, dan korupsi; 18 </summary>

**Pertanyaan:** PT merencanakan 24 kegiatan pencegahan dan penanganan kekerasan, narkoba, dan korupsi; 18 kegiatan terlaksana. Berapa capaian IKU 11d?

**Kata kunci bukti:** `total kegiatan yang direncanakan`

**Halaman benar:** 68 | **Chunk bukti di corpus:** 3 (Buku hlm.68, Buku hlm.126–131, PPT hlm.69)

| # | Bukti | Sumber | Hlm. | Distance | Section | Cuplikan |
|---|---|---|---|---|---|---|
| 1 | ✅ | Buku | 68 | 0.3472 | …ka dan Bahan Adiktif berbahaya lainnya (narkoba); dan (3) Anti Korupsi | [Buku IKU Diktisaintek Berdampak V1 / BAB - V > 5.3. Indikator Kinerja Utama (IKU) Diktisaintek Berdampak > 5.3.2. Indikator Kinerja Utama (IKU) Pilihan > IKU 1 |
| 2 |  | Buku | 68 | 0.3496 | …ka dan Bahan Adiktif berbahaya lainnya (narkoba); dan (3) Anti Korupsi | [Buku IKU Diktisaintek Berdampak V1 / BAB - V > 5.3. Indikator Kinerja Utama (IKU) Diktisaintek Berdampak > 5.3.2. Indikator Kinerja Utama (IKU) Pilihan > IKU 1 |
| 3 |  | Buku | 68 | 0.351 | …ka dan Bahan Adiktif berbahaya lainnya (narkoba); dan (3) Anti Korupsi | [Buku IKU Diktisaintek Berdampak V1 / BAB - V > 5.3. Indikator Kinerja Utama (IKU) Diktisaintek Berdampak > 5.3.2. Indikator Kinerja Utama (IKU) Pilihan > IKU 1 |
| 4 |  | Buku | 68 | 0.3553 | …ka dan Bahan Adiktif berbahaya lainnya (narkoba); dan (3) Anti Korupsi | [Buku IKU Diktisaintek Berdampak V1 / BAB - V > 5.3. Indikator Kinerja Utama (IKU) Diktisaintek Berdampak > 5.3.2. Indikator Kinerja Utama (IKU) Pilihan > IKU 1 |
| 5 |  | Buku | 68 | 0.3584 | …ka dan Bahan Adiktif berbahaya lainnya (narkoba); dan (3) Anti Korupsi | [Buku IKU Diktisaintek Berdampak V1 / BAB - V > 5.3. Indikator Kinerja Utama (IKU) Diktisaintek Berdampak > 5.3.2. Indikator Kinerja Utama (IKU) Pilihan > IKU 1 |

</details>

<details><summary>✅ <b>H18</b> — HIT @2 — UMP di provinsi tempat PT berada adalah Rp3.000.000. Berapa penghasilan minimum dosen deng</summary>

**Pertanyaan:** UMP di provinsi tempat PT berada adalah Rp3.000.000. Berapa penghasilan minimum dosen dengan jabatan Lektor dan Profesor menurut IKU 12?

**Kata kunci bukti:** `lektor kepala`, `ump`

**Halaman benar:** 60 | **Chunk bukti di corpus:** 3 (Buku hlm.60, Buku hlm.131, PPT hlm.57)

| # | Bukti | Sumber | Hlm. | Distance | Section | Cuplikan |
|---|---|---|---|---|---|---|
| 1 |  | PPT | 23 | 0.3568 | …BAB - III > 3.8. PROFIL DAN DAMPAK PT INDONESIA > Kontribusi ekonomi | [PPT IKU Diktisaintek Berdampak PTS V2 / BAB - III > 3.8. PROFIL DAN DAMPAK PT INDONESIA > Kontribusi ekonomi / hlm. 23] **±Rp. 390 T*** (exc. riset dan pengmas |
| 2 | ✅ | PPT | 57 | 0.3829 | …2 : Ketersediaan perencanaan strategis peningkatan kesejahteraan dosen | [PPT IKU Diktisaintek Berdampak PTS V2 / BAB - V > 5.3. INDIKATOR KINERJA UTAMA (IKU) DIKTISAINTEK BERDAMPAK > 5.3.1. Indikator Kinerja Utama (IKU) Wajib > 7 IK |
| 3 | ✅ | Buku | 60 | 0.3951 | …12: Ketersediaan perencanaan strategis peningkatan kesejahteraan dosen | [Buku IKU Diktisaintek Berdampak V1 / BAB - V > 5.3. Indikator Kinerja Utama (IKU) Diktisaintek Berdampak > 5.3.1. Indikator Kinerja Utama (IKU) Wajib > IKU 12: |
| 4 | ✅ | Buku | 131 | 0.3956 | …LAMPIRAN Kepmen 358/M/KEP/2025 > 1. IKU BAGI PERGURUAN TINGGI | [Buku IKU Diktisaintek Berdampak V1 (Lampiran Kepmen 358/M/KEP/2025) / LAMPIRAN Kepmen 358/M/KEP/2025 > 1. IKU BAGI PERGURUAN TINGGI > IKU 12. Ketersediaan pere |
| 5 |  | PPT | 30 | 0.4051 | …BAB - IV > 4.4. PENINGKATAN DOSEN BERKUALIFIKASI DOKTOR (2) > Asumsi: | [PPT IKU Diktisaintek Berdampak PTS V2 / BAB - IV > 4.4. PENINGKATAN DOSEN BERKUALIFIKASI DOKTOR (2) > Asumsi: / hlm. 30] * Apabila di alokasikan dana dari Dana |

</details>
