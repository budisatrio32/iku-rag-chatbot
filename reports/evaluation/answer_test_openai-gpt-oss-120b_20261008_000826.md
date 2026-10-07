# Uji Jawaban Chatbot (retriever + LLM + kalkulator)

- Waktu: 2026-10-08 00:08:26
- Model LLM: `openai/gpt-oss-120b`
- Soal: 1 (hitungan 1, definisi & jebakan 0)

## Ringkasan

| Metrik | Hasil |
|---|---|
| Lulus semua pemeriksaan otomatis | **1/1** |
| Hitungan: kalkulator dipanggil | 1/1 |
| Hitungan: hasil kalkulator = kunci | 1/1 |
| Hitungan: angka kunci ada di jawaban | 1/1 |
| Halaman sitasi benar (hitungan) | 1/1 |
| Halaman sitasi benar (definisi) | - |
| Soal error (API/kuota) | 0 |
| Jawaban dengan peringatan chatbot | 0 |

| ID | Status | Pemeriksaan yang gagal |
|---|---|---|
| H19 | ✅ | - |

Pemeriksaan otomatis hanya bantuan. Baca jawaban lengkap di bawah dan bandingkan dengan jawaban yang diharapkan.

## Detail per soal

### H19 — ✅ LULUS

**Pertanyaan:** brp aee s1 klo yg lulus tepat wktu cm 40 org dr 200 mhs?

**Jawaban chatbot:**

```text
AEE untuk program S1 adalah **20 %** (AEE realisasi) dengan tingkat pencapaian **80 %** dibandingkan AEE ideal 25 % % [1][2].  Langkah perhitungannya:  
- AEE realisasi = 40 / 200 × 100 % = 20 %  
- AEE ideal S1 = 25 % (sesuai masa tempuh kurikulum 8 semester)  
- Tingkat pencapaian = 20 % / 25 % × 100 % = 80 %   (hasil dari fungsi hitung_iku).
```

**Sitasi chatbot:**

- [1] Buku IKU Diktisaintek Berdampak V1, hlm. 49 (IKU 1, Kriteria); juga di Buku (Lampiran Kepmen 358/M/KEP/2025) hlm. 100; PPT hlm. 45
- [2] Buku IKU Diktisaintek Berdampak V1, hlm. 49–50 (IKU 1, Formula); juga di Buku (Lampiran Kepmen 358/M/KEP/2025) hlm. 101–102; Buku (Lampiran Kepmen 358/M/KEP/2025) hlm. 101–102; PPT hlm. 46; PPT hlm. 46–47

**Sumber rumus (kalkulator):**

- Buku IKU Diktisaintek Berdampak V1, IKU 1 – Ketentuan & Formula a–b, hlm. 49

**Panggilan kalkulator:**

- argumen `{"argumen_json":"{\"jenjang\": \"S1\", \"lulus_tepat_waktu\": 40, \"total_mahasiswa\": 200, \"pindah\": 0, \"drop_out\": 0, \"cuti_lebih\": 0}","fungsi":"iku1_aee_prodi"}` → aee_realisasi_pct = 20,00, tingkat_pencapaian_pct = 80,00

**Jawaban yang diharapkan:**

- Angka kunci: **aee_realisasi_pct = 20,00, tingkat_pencapaian_pct = 80,00**
- Halaman kunci: 49

AEE realisasi **20%**, tingkat pencapaian **80%**.

*Catatan soal:* Ketahanan: typo & singkatan (brp, klo, wktu, mhs). Sama dengan H01.

**Pemeriksaan otomatis:**

- ✅ kalkulator dipanggil
- ✅ hasil kalkulator = kunci
- ✅ angka kunci ada di jawaban
- ✅ halaman sitasi benar
