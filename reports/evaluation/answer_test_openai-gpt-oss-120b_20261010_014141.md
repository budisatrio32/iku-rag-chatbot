# Uji Jawaban Chatbot (retriever + LLM + kalkulator)

- Waktu: 2026-10-10 01:46:21
- Model LLM: `openai/gpt-oss-120b`
- Soal: 2 dari 3 dijalankan (hitungan 2, definisi & jebakan 0)
- Status run: berhenti: jatah harian LLM habis (429 per hari)

## Ringkasan

| Metrik | Hasil |
|---|---|
| Lulus semua pemeriksaan otomatis | **1/2** |
| Hitungan: kalkulator dipanggil | 1/1 |
| Hitungan: hasil kalkulator = kunci | 1/1 |
| Hitungan: angka kunci ada di jawaban | 1/1 |
| Halaman sitasi benar (hitungan) | 1/1 |
| Halaman sitasi benar (definisi) | - |
| Soal error (API/kuota) | 1 |
| Jawaban dengan peringatan chatbot | 1 |

| ID | Status | Pemeriksaan yang gagal |
|---|---|---|
| H25 | ✅ | - |
| H26 | ⚠️ error | RateLimitError: Error code: 429 - {'error': {'message': 'Rate limit reached for model `openai/gpt-oss-120b` in organization `org_01m4bk7rfgeat9063z15rm7za5` service tier `on_demand` on tokens per day (TPD): Limit 200000, Used 199467, Requested 5884. Please try again in 38m31.632s. Need more tokens? Upgrade to Dev Tier today at https://console.groq.com/settings/billing', 'type': 'tokens', 'code': 'rate_limit_exceeded'}} |

Pemeriksaan otomatis hanya bantuan. Baca jawaban lengkap di bawah dan bandingkan dengan jawaban yang diharapkan.

## Soal yang belum selesai / perlu diulang

2 soal belum dijalankan atau berakhir error: H26, H27. Lanjutkan ke laporan ini dengan:

```powershell
python src/evaluation/run_answer_tests.py --lanjut reports/evaluation/answer_test_openai-gpt-oss-120b_20261010_014141.json --jeda 20
```

## Detail per soal

### H25 — ✅ LULUS

**Pertanyaan:** total pendapatan PT 500 M. rinciannya ukt 300M, boptn 80 M, hibah riset 50M, konsultasi 40 M, unit bisnis 20M, hasil dana abadi 10 M. iku 9 brp?

**Jawaban chatbot:**

```text
IKU 9 – Persentase Pendapatan Non Pendidikan/UKT = **24 %**.

Langkah perhitungannya:
- Total pendapatan PT = 500 M.  
- Pendapatan yang diakui sebagai non-mahasiswa (hibah riset 50 M + konsultasi 40 M + unit bisnis 20 M + hasil dana abadi 10 M) = 120 M.  
- Persentase = (120 M ÷ 500 M) × 100 % = **24 %**.  

Sumber: Buku IKU Diktisaintek Berdampak V1, IKU 9 – Kriteria & Formula, hlm. 59.
```

**Sumber rumus (kalkulator):**

- Buku IKU Diktisaintek Berdampak V1, IKU 9 – Kriteria & Formula, hlm. 59

**Panggilan kalkulator:**

- argumen `{"argumen_json":"{\"total_pendapatan\":\"500 M\",\"rincian\":{\"ukt\":\"300 M\",\"boptn\":\"80 M\",\"hibah_riset\":\"50 M\",\"konsultasi\":\"40 M\",\"unit_bisnis\":\"20 M\",\"hasil_dana_abadi\":\"10 M\"}}","fungsi":"iku9"}` → 24,00

**Peringatan chatbot:**

- LLM mengembalikan respons kosong; diulang otomatis.
- Panggilan alat ditolak server (nama alat 'hituk_iku' tidak dikenal); diulang otomatis.
- Jawaban tidak memuat rujukan [n] ke konteks.

**Jawaban yang diharapkan:**

- Angka kunci: **24,00**
- Halaman kunci: 59

**24%**.

*Catatan soal:* Ketahanan: satuan 'M' = miliar, ditulis rapat/berspasi ('300M', '80 M'). Argumen boleh dalam miliar asal konsisten. Sama dengan H13.

**Pemeriksaan otomatis:**

- ✅ kalkulator dipanggil
- ✅ hasil kalkulator = kunci
- ✅ angka kunci ada di jawaban
- ✅ halaman sitasi benar

### H26 — ⚠️ ERROR

**Pertanyaan:** pendapatan total Rp1.250.000.000, terdiri dr ukt rp 900jt, kontrak riset 150 juta, royalti Rp50.000.000, sisanya 150jt dari boptn. capaian iku 9?

**Jawaban chatbot:**

```text
(tidak ada jawaban: RateLimitError: Error code: 429 - {'error': {'message': 'Rate limit reached for model `openai/gpt-oss-120b` in organization `org_01m4bk7rfgeat9063z15rm7za5` service tier `on_demand` on tokens per day (TPD): Limit 200000, Used 199467, Requested 5884. Please try again in 38m31.632s. Need more tokens? Upgrade to Dev Tier today at https://console.groq.com/settings/billing', 'type': 'tokens', 'code': 'rate_limit_exceeded'}})
```

**Jawaban yang diharapkan:**

- Angka kunci: **16,00**
- Halaman kunci: 59

**16%**.

*Catatan soal:* Ketahanan: campuran 'Rp1.250.000.000', '900jt', '150 juta', 'Rp50.000.000'. Satuan harus disamakan sebelum dihitung.

**Pemeriksaan otomatis:**

