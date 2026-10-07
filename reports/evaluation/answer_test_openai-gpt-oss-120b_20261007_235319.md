# Uji Jawaban Chatbot (retriever + LLM + kalkulator)

- Waktu: 2026-10-07 23:53:19
- Model LLM: `openai/gpt-oss-120b`
- Soal: 14 (hitungan 12, definisi & jebakan 2)

## Ringkasan

| Metrik | Hasil |
|---|---|
| Lulus semua pemeriksaan otomatis | **12/14** |
| Hitungan: kalkulator dipanggil | 11/11 |
| Hitungan: hasil kalkulator = kunci | 11/11 |
| Hitungan: angka kunci ada di jawaban | 11/11 |
| Halaman sitasi benar (hitungan) | 11/11 |
| Halaman sitasi benar (definisi) | 2/2 |
| Soal error (API/kuota) | 1 |
| Jawaban dengan peringatan chatbot | 4 |

| ID | Status | Pemeriksaan yang gagal |
|---|---|---|
| D13 | ❌ | fakta: efisiensi edukasi |
| D14 | ✅ | - |
| H19 | ⚠️ error | BadRequestError: Error code: 400 - {'error': {'message': "Tool call validation failed: tool call validation failed: attempted to call tool 'hit...' which was not in request.tools", 'type': 'invalid_request_error', 'code': 'tool_use_failed', 'failed_generation': '{"name": "hit...", "arguments": {\n  "argumen_json": "{\\"jenjang\\": \\"S1\\", \\"lulus_tepat_waktu\\": 40, \\"total_mahasiswa\\": 200, \\"pindah\\": 0, \\"drop_out\\": 0, \\"cuti_lebih\\": 0}",\n  "fungsi": "iku1_aee_prodi"\n}}'}} |
| H20 | ✅ | - |
| H21 | ✅ | - |
| H22 | ✅ | - |
| H23 | ✅ | - |
| H24 | ✅ | - |
| H25 | ✅ | - |
| H26 | ✅ | - |
| H27 | ✅ | - |
| H28 | ✅ | - |
| H29 | ✅ | - |
| H30 | ✅ | - |

Pemeriksaan otomatis hanya bantuan. Baca jawaban lengkap di bawah dan bandingkan dengan jawaban yang diharapkan.

## Detail per soal

### D13 — ❌ PERLU DICEK

**Pertanyaan:** aee tu apaan sih? ngukur apa?

**Jawaban chatbot:**

```text
AEE (Angka Efisiensi Mahasiswa) adalah ukuran yang mengukur **tingkat keberhasilan mahasiswa menyelesaikan studi tepat waktu sesuai masa studi standar** dibandingkan dengan total mahasiswa yang masuk pada periode yang sama [3]. Dengan kata lain, AEE menghitung persentase mahasiswa yang lulus sesuai masa tempuh kurikulum (misalnya 8 semester untuk S1) terhadap seluruh mahasiswa yang terdaftar pada tahun akademik tersebut [1].
```

**Sitasi chatbot:**

- [1] Buku IKU Diktisaintek Berdampak V1, hlm. 49–50 (IKU 1, Formula); juga di Buku (Lampiran Kepmen 358/M/KEP/2025) hlm. 101–102; Buku (Lampiran Kepmen 358/M/KEP/2025) hlm. 101–102; PPT hlm. 46; PPT hlm. 46–47
- [3] Buku IKU Diktisaintek Berdampak V1, hlm. 49 (IKU 1, Definisi); juga di Buku (Lampiran Kepmen 358/M/KEP/2025) hlm. 100; PPT hlm. 45

**Jawaban yang diharapkan:**

- Halaman kunci: 49

AEE = Angka Efisiensi Edukasi (IKU 1), mengukur keberhasilan mahasiswa menyelesaikan studi **tepat waktu** sesuai masa studi standar (sama dengan D01).

*Catatan soal:* Ketahanan: bahasa santai ('aee tu apaan sih'). 'AEE' sengaja tidak dijadikan fakta karena sudah ada di pertanyaan.

**Pemeriksaan otomatis:**

- ✅ fakta: tepat waktu
- ❌ fakta: efisiensi edukasi
- ✅ halaman sitasi benar

### D14 — ✅ LULUS

**Pertanyaan:** pendptan apa aj yg ga diitung di iku9?

**Jawaban chatbot:**

```text
Pendapatan yang **tidak dihitung** dalam perhitungan IKU 9 antara lain:

1. **SPP/UKT/biaya kuliah mahasiswa** – karena IKU 9 mengukur pendapatan non‑mahasiswa. [4]  
2. **Iuran pengembangan institusi** – tidak termasuk dalam kategori pendapatan non‑mahasiswa yang diakui. [4]  
3. **Subsidi langsung dari pemerintah**, seperti belanja pegawai, belanja operasional, BOPTN, BPPTNBH, dan sejenisnya. [4]  
4. **Sumbangan/filantropi yang tidak masuk dalam laporan keuangan resmi perguruan tinggi**. [4]  
5. **Dana pokok dana abadi/endowment fund** (yang disimpan permanen dan tidak dibelanjakan). [4]  
6. **Pendapatan yang tidak dibukukan** (misalnya pendapatan tidak tercatat, hibah barang tanpa nilai, atau dana lewat kampus tanpa pelaporan resmi). [5]  

Semua jenis pendapatan di atas tidak termasuk dalam perhitungan persentase pendapatan non‑pendidikan/UKT pada IKU 9.
```

**Sitasi chatbot:**

- [4] Buku IKU Diktisaintek Berdampak V1, hlm. 59 (IKU 9, Kriteria); juga di PPT hlm. 56; Buku (Lampiran Kepmen 358/M/KEP/2025) hlm. 122–123
- [5] Buku IKU Diktisaintek Berdampak V1, hlm. 79 (IKU 9, Kriteria dan Ketentuan); juga di PPT hlm. 81; PPT hlm. 85; PPT hlm. 86

**Jawaban yang diharapkan:**

- Halaman kunci: 59

SPP/UKT, iuran pengembangan institusi, subsidi langsung pemerintah (termasuk BOPTN/BPPTNBH), filantropi yang tidak tercatat, dan pokok dana abadi (sama dengan D08).

*Catatan soal:* Ketahanan: typo ('pendptan', 'aj', 'diitung', 'iku9'). Sama dengan D08.

**Pemeriksaan otomatis:**

- ✅ fakta: UKT / SPP
- ✅ fakta: BOPTN
- ✅ fakta: iuran pengembangan
- ✅ fakta: dana abadi / endowment
- ✅ halaman sitasi benar

### H19 — ⚠️ ERROR

**Pertanyaan:** brp aee s1 klo yg lulus tepat wktu cm 40 org dr 200 mhs?

**Jawaban chatbot:**

```text
(tidak ada jawaban: BadRequestError: Error code: 400 - {'error': {'message': "Tool call validation failed: tool call validation failed: attempted to call tool 'hit...' which was not in request.tools", 'type': 'invalid_request_error', 'code': 'tool_use_failed', 'failed_generation': '{"name": "hit...", "arguments": {\n  "argumen_json": "{\\"jenjang\\": \\"S1\\", \\"lulus_tepat_waktu\\": 40, \\"total_mahasiswa\\": 200, \\"pindah\\": 0, \\"drop_out\\": 0, \\"cuti_lebih\\": 0}",\n  "fungsi": "iku1_aee_prodi"\n}}'}})
```

**Jawaban yang diharapkan:**

- Angka kunci: **aee_realisasi_pct = 20,00, tingkat_pencapaian_pct = 80,00**
- Halaman kunci: 49

AEE realisasi **20%**, tingkat pencapaian **80%**.

*Catatan soal:* Ketahanan: typo & singkatan (brp, klo, wktu, mhs). Sama dengan H01.

**Pemeriksaan otomatis:**


### H20 — ✅ LULUS

**Pertanyaan:** realisasi aee kampus kmi: D3 30%, S1 22,5%, S2 40%. aee pt nya jd brp ya?

**Jawaban chatbot:**

```text
AEE PT kampus KMI adalah **86,97 %**.  
Langkah perhitungannya:  

1. Tingkat pencapaian D3 = 30 % ÷ 33 % = 90,91 %  
2. Tingkat pencapaian S1 = 22,5 % ÷ 25 % = 90,00 %  
3. Tingkat pencapaian S2 = 40 % ÷ 50 % = 80,00 %  
4. AEE PT = (90,91 % + 90,00 % + 80,00 %) ÷ 3 = **86,97 %**  

Sumber: Buku IKU Diktisaintek Berdampak V1, IKU 1 – Formula (c) & contoh perhitungan, hlm. 49–50.
```

**Sumber rumus (kalkulator):**

- Buku IKU Diktisaintek Berdampak V1, IKU 1 – Formula c & contoh perhitungan, hlm. 49–50

**Panggilan kalkulator:**

- argumen `{"argumen_json":"{\"realisasi_per_jenjang\": {\"D3\": 30, \"S1\": 22.5, \"S2\": 40}}","fungsi":"iku1_aee_pt"}` → 86,97

**Peringatan chatbot:**

- Jawaban tidak memuat rujukan [n] ke konteks.

**Jawaban yang diharapkan:**

- Angka kunci: **86,97**
- Halaman kunci: 49, 50

**86,97%**.

*Catatan soal:* Ketahanan: desimal koma '22,5%' harus dibaca 22.5. Sama dengan H02.

**Pemeriksaan otomatis:**

- ✅ kalkulator dipanggil
- ✅ hasil kalkulator = kunci
- ✅ angka kunci ada di jawaban
- ✅ halaman sitasi benar

### H21 — ✅ LULUS

**Pertanyaan:** lulusan kampus kami 1.341 org, minimal responden tracer study nya brp?

**Jawaban chatbot:**

```text
Berdasarkan rumus Slovin untuk responden minimum (IKU 2) dengan galat 2,3 % dan jumlah lulusan = 1 341, diperlukan **785 responden** minimum. [2]
```

**Sitasi chatbot:**

- [2] Buku IKU Diktisaintek Berdampak V1, hlm. 52 (IKU 2, Formula); juga di Buku (Lampiran Kepmen 358/M/KEP/2025) hlm. 104–105; PPT hlm. 48–49

**Sumber rumus (kalkulator):**

- Buku IKU Diktisaintek Berdampak V1, IKU 2 – Formula Responden Minimum, hlm. 52

**Panggilan kalkulator:**

- argumen `{"argumen_json":"{\"jumlah_lulusan\": 1341}","fungsi":"iku2_responden_minimum"}` → 785

**Jawaban yang diharapkan:**

- Angka kunci: **785**
- Halaman kunci: 52

**785 responden**.

*Catatan soal:* Ketahanan: titik pemisah ribuan '1.341' = 1341 (bukan 1,341).

**Pemeriksaan otomatis:**

- ✅ kalkulator dipanggil
- ✅ hasil kalkulator = kunci
- ✅ angka kunci ada di jawaban
- ✅ halaman sitasi benar

### H22 — ✅ LULUS

**Pertanyaan:** klo lulusannya 2rb orang, responden minimum tracer studi brp

**Jawaban chatbot:**

```text
Berdasarkan rumus Slovin dengan galat 2,3 % (d = 0,023) untuk jumlah lulusan N = 2 000 orang, responden minimum yang harus dikumpulkan dalam tracer study adalah **972 responden**. [2][1]
```

**Sitasi chatbot:**

- [1] Buku IKU Diktisaintek Berdampak V1, hlm. 51 (IKU 2, Ketentuan); juga di Buku (Lampiran Kepmen 358/M/KEP/2025) hlm. 104; PPT hlm. 48
- [2] Buku IKU Diktisaintek Berdampak V1, hlm. 52 (IKU 2, Formula); juga di PPT hlm. 48–49; Buku (Lampiran Kepmen 358/M/KEP/2025) hlm. 104–105

**Sumber rumus (kalkulator):**

- Buku IKU Diktisaintek Berdampak V1, IKU 2 – Formula Responden Minimum, hlm. 52

**Panggilan kalkulator:**

- argumen `{"argumen_json":"{\"jumlah_lulusan\": 2000}","fungsi":"iku2_responden_minimum"}` → 972

**Jawaban yang diharapkan:**

- Angka kunci: **972**
- Halaman kunci: 52

**972 responden**.

*Catatan soal:* Ketahanan: '2rb' = 2000. Sama dengan H06.

**Pemeriksaan otomatis:**

- ✅ kalkulator dipanggil
- ✅ hasil kalkulator = kunci
- ✅ angka kunci ada di jawaban
- ✅ halaman sitasi benar

### H23 — ✅ LULUS

**Pertanyaan:** kerjsama PT kita ada 120, luaran nya 30 judul. capaian iku5 brp persen?

**Jawaban chatbot:**

```text
Capaian IKU 5 = (Jumlah luaran / Total kerja sama) × 100 %  
= 30 / 120 × 100 % = 25 % [1] 

Jadi, rasio luaran hasil kerja sama perguruan tinggi dengan start‑up/industri/lembaga adalah **25 %**.
```

**Sitasi chatbot:**

- [1] Buku IKU Diktisaintek Berdampak V1, hlm. 57–58 (IKU 5, Formula); juga di Buku (Lampiran Kepmen 358/M/KEP/2025) hlm. 117; PPT hlm. 53

**Sumber rumus (kalkulator):**

- Buku IKU Diktisaintek Berdampak V1, IKU 5 – Formula & Keterangan, hlm. 57

**Panggilan kalkulator:**

- argumen `{"argumen_json":"{\"kode\":\"iku5\",\"pembilang\":30,\"penyebut\":120}","fungsi":"rasio"}` → 25,00

**Jawaban yang diharapkan:**

- Angka kunci: **25,00**
- Halaman kunci: 57

**25%**.

*Catatan soal:* Ketahanan: typo 'kerjsama', 'iku5' tanpa spasi. Sama dengan H09.

**Pemeriksaan otomatis:**

- ✅ kalkulator dipanggil
- ✅ hasil kalkulator = kunci
- ✅ angka kunci ada di jawaban
- ✅ halaman sitasi benar

### H24 — ✅ LULUS

**Pertanyaan:** dr 50 progam sdgs, 25 yg kontribusi ke sdg 1,4,17 + 2 sdg pilihan. capaian iku 7 brapa

**Jawaban chatbot:**

```text
Berdasarkan formula IKU 7 (“(Jumlah program atau kegiatan PT yang berkontribusi pada SDGs 1, 4, 17 dan 2 SDGs lainnya) / (Total program SDGs PT) × 100%”) [4], capaian persentase keterlibatan adalah:

\[
\frac{25}{50}\times 100\% = 50\%
\]

Jadi, IKU 7 tercapai **50 %**.
```

**Sitasi chatbot:**

- [4] Buku IKU Diktisaintek Berdampak V1, hlm. 58 (IKU 7, Formula); juga di Buku (Lampiran Kepmen 358/M/KEP/2025) hlm. 121; PPT hlm. 55

**Sumber rumus (kalkulator):**

- Buku IKU Diktisaintek Berdampak V1, IKU 7 – Formula, hlm. 58

**Panggilan kalkulator:**

- argumen `{"argumen_json":"{\"kode\":\"iku7\",\"pembilang\":25,\"penyebut\":50}","fungsi":"rasio"}` → 50,00

**Jawaban yang diharapkan:**

- Angka kunci: **50,00**
- Halaman kunci: 58

**50%**.

*Catatan soal:* Ketahanan: typo 'progam', 'brapa'.

**Pemeriksaan otomatis:**

- ✅ kalkulator dipanggil
- ✅ hasil kalkulator = kunci
- ✅ angka kunci ada di jawaban
- ✅ halaman sitasi benar

### H25 — ✅ LULUS

**Pertanyaan:** total pendapatan PT 500 M. rinciannya ukt 300M, boptn 80 M, hibah riset 50M, konsultasi 40 M, unit bisnis 20M, hasil dana abadi 10 M. iku 9 brp?

**Jawaban chatbot:**

```text
IKU 9 = 24 % [2][3]  

**Perhitungan**  
- Pendapatan yang diakui (non‑pendidikan/UKT):  
  - Hibah riset = 50 M  
  - Konsultasi = 40 M  
  - Unit bisnis = 20 M  
  - Hasil dana abadi = 10 M  
  - **Total = 120 M**  

- Total pendapatan PT = 500 M  

- Persentase = (120 M ÷ 500 M) × 100 % = 24 %  

Pendapatan UKT (300 M) dan BOPTN (80 M) tidak termasuk dalam perhitungan karena tidak termasuk dalam kriteria pendapatan non‑mahasiswa.  

*Catatan*: Rumus dan kriteria diambil dari Buku IKU Diktisaintek Berdampak V1, bab IKU 9 (hlm. 59).
```

**Sitasi chatbot:**

- [2] Buku IKU Diktisaintek Berdampak V1, hlm. 59 (IKU 9, Kriteria); juga di Buku (Lampiran Kepmen 358/M/KEP/2025) hlm. 122–123; PPT hlm. 56
- [3] Buku IKU Diktisaintek Berdampak V1, hlm. 79 (IKU 9, Kriteria dan Ketentuan); juga di PPT hlm. 83; PPT hlm. 85

**Sumber rumus (kalkulator):**

- Buku IKU Diktisaintek Berdampak V1, IKU 9 – Kriteria & Formula, hlm. 59

**Panggilan kalkulator:**

- argumen `{"argumen_json":"{\"total_pendapatan\": 500, \"rincian\": {\"hibah_riset\": 50, \"konsultasi\": 40, \"unit_bisnis\": 20, \"hasil_dana_abadi\": 10, \"ukt\": 300, \"boptn\": 80}}","fungsi":"iku9"}` → 24,00

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

### H26 — ✅ LULUS

**Pertanyaan:** pendapatan total Rp1.250.000.000, terdiri dr ukt rp 900jt, kontrak riset 150 juta, royalti Rp50.000.000, sisanya 150jt dari boptn. capaian iku 9?

**Jawaban chatbot:**

```text
Capaian IKU 9 = 16 % [1][3]  

Perhitungan:  
- Pendapatan non‑mahasiswa yang diakui: kontrak riset Rp 150 jt + royalti Rp 50 jt = **Rp 200 jt**.  
- Total pendapatan PT: **Rp 1 250 jt**.  
- Persentase = (200 jt ÷ 1 250 jt) × 100 % = **16 %**.  

Pendapatan BOPTN tidak dihitung karena tidak termasuk dalam kriteria pendapatan non‑mahasiswa [1].
```

**Sitasi chatbot:**

- [1] Buku IKU Diktisaintek Berdampak V1, hlm. 59 (IKU 9, Kriteria); juga di PPT hlm. 56; Buku (Lampiran Kepmen 358/M/KEP/2025) hlm. 122–123
- [3] Buku IKU Diktisaintek Berdampak V1, hlm. 59 (IKU 9, Formula); juga di Buku (Lampiran Kepmen 358/M/KEP/2025) hlm. 124; PPT hlm. 56

**Sumber rumus (kalkulator):**

- Buku IKU Diktisaintek Berdampak V1, IKU 9 – Kriteria & Formula, hlm. 59

**Panggilan kalkulator:**

- argumen `{"argumen_json":"{\"total_pendapatan\":1250000000,\"rincian\":{\"kontrak_riset\":150000000,\"royalti\":50000000}}","fungsi":"iku9"}` → 16,00

**Jawaban yang diharapkan:**

- Angka kunci: **16,00**
- Halaman kunci: 59

**16%**.

*Catatan soal:* Ketahanan: campuran 'Rp1.250.000.000', '900jt', '150 juta', 'Rp50.000.000'. Satuan harus disamakan sebelum dihitung.

**Pemeriksaan otomatis:**

- ✅ kalkulator dipanggil
- ✅ hasil kalkulator = kunci
- ✅ angka kunci ada di jawaban
- ✅ halaman sitasi benar

### H27 — ✅ LULUS

**Pertanyaan:** total pendapatan 2 milyar: hibah riset 300 jt, konsultasi 0,2 M, ukt 1,5 M. hitung iku 9 nya

**Jawaban chatbot:**

```text
IKU 9 = Persentase Pendapatan Non‑Pendidikan/UKT  

**Perhitungan**  
- Pendapatan non‑mahasiswa yang diakui:  
  - Hibah riset = 300 jt  
  - Konsultasi = 0,2 jt = 200 jt  
  - Total = 300 jt + 200 jt = 500 jt  

- Total pendapatan PT = 2 milyar  

\[
\text{IKU 9} = \frac{500\,\text{jt}}{2\,000\,\text{jt}} \times 100\% = 25\%
\]

**Hasil:** 25 % [2][3] (menggunakan rumus pada dokumen IKU 9, hlm. 59).
```

**Sitasi chatbot:**

- [2] Buku IKU Diktisaintek Berdampak V1, hlm. 59 (IKU 9, Formula); juga di Buku (Lampiran Kepmen 358/M/KEP/2025) hlm. 124; PPT hlm. 56
- [3] Buku IKU Diktisaintek Berdampak V1, hlm. 59 (IKU 9, Definisi); juga di Buku (Lampiran Kepmen 358/M/KEP/2025) hlm. 122; PPT hlm. 56

**Sumber rumus (kalkulator):**

- Buku IKU Diktisaintek Berdampak V1, IKU 9 – Kriteria & Formula, hlm. 59

**Panggilan kalkulator:**

- argumen `{"argumen_json":"{\"total_pendapatan\": 2000000000, \"rincian\": {\"hibah_riset\": 300000000, \"konsultasi\": 200000000}}","fungsi":"iku9"}` → 25,00

**Jawaban yang diharapkan:**

- Angka kunci: **25,00**
- Halaman kunci: 59

**25%**.

*Catatan soal:* Ketahanan: ejaan 'milyar', desimal koma '0,2 M' dan '1,5 M' dicampur dengan 'jt'.

**Pemeriksaan otomatis:**

- ✅ kalkulator dipanggil
- ✅ hasil kalkulator = kunci
- ✅ angka kunci ada di jawaban
- ✅ halaman sitasi benar

### H28 — ✅ LULUS

**Pertanyaan:** ump disini 3,5jt, penghasilan minimal dosen lektor kepala brp?

**Jawaban chatbot:**

```text
Penghasilan minimal dosen Lektor Kepala adalah 4 × UMP. Dengan UMP = Rp 3.500.000, maka:

- Penghasilan minimal Lektor Kepala = 4 × Rp 3.500.000 = **Rp 14.000.000**【1】. 

Hasil perhitungan: Rp 14.000.000 per bulan (atau sesuai periode yang ditetapkan).
```

**Sumber rumus (kalkulator):**

- Buku IKU Diktisaintek Berdampak V1, IKU 12 – Kriteria b.2, hlm. 60

**Panggilan kalkulator:**

- argumen `{"argumen_json":"{\"ump\": 3500000, \"jabatan\": [\"lektor_kepala\"]}","fungsi":"iku12_penghasilan_minimum"}` → lektor_kepala = 14.000.000

**Peringatan chatbot:**

- Jawaban tidak memuat rujukan [n] ke konteks.

**Jawaban yang diharapkan:**

- Angka kunci: **lektor_kepala = 14.000.000**
- Halaman kunci: 60

Lektor kepala minimal **Rp14.000.000**.

*Catatan soal:* Ketahanan: '3,5jt' = Rp3.500.000. Argumen ump harus rupiah penuh, bukan 3.5.

**Pemeriksaan otomatis:**

- ✅ kalkulator dipanggil
- ✅ hasil kalkulator = kunci
- ✅ angka kunci ada di jawaban
- ✅ halaman sitasi benar

### H29 — ✅ LULUS

**Pertanyaan:** UMP prov kami Rp 4.250.000 , brp penghasilan min dosen asisten ahli sm profesor?

**Jawaban chatbot:**

```text
Berdasarkan kriteria IKU 12, penghasilan minimum dosen per jenjang jabatan adalah:

- **Asisten Ahli:** ≥ 1,5 × UMP = 1,5 × Rp 4.250.000 = **Rp 6.375.000**【1】  
- **Lektor:** ≥ 3 × UMP = 3 × Rp 4.250.000 = **Rp 12.750.000**【1】  
- **Lektor Kepala:** ≥ 4 × UMP = 4 × Rp 4.250.000 = **Rp 17.000.000**【1】  
- **Profesor:** ≥ 6 × UMP = 6 × Rp 4.250.000 = **Rp 25.500.000**【1】

Hasil perhitungan diperoleh melalui fungsi **iku12_penghasilan_minimum** dengan UMP = Rp 4.250.000 dan jenjang jabatan yang diminta【fungsi】.
```

**Sumber rumus (kalkulator):**

- Buku IKU Diktisaintek Berdampak V1, IKU 12 – Kriteria b.2, hlm. 60

**Panggilan kalkulator:**

- argumen `{"argumen_json":"{\"ump\":4250000,\"jabatan\":[\"asisten_ahli\",\"lektor\",\"lektor_kepala\",\"profesor\"]}","fungsi":"iku12_penghasilan_minimum"}` → asisten_ahli = 6.375.000,00, lektor = 12.750.000, lektor_kepala = 17.000.000, profesor = 25.500.000

**Peringatan chatbot:**

- Jawaban tidak memuat rujukan [n] ke konteks.

**Jawaban yang diharapkan:**

- Angka kunci: **asisten_ahli = 6.375.000, profesor = 25.500.000**
- Halaman kunci: 60

Asisten ahli minimal **Rp6.375.000**, profesor minimal **Rp25.500.000**.

*Catatan soal:* Ketahanan: 'Rp 4.250.000' dengan spasi setelah Rp dan titik ribuan.

**Pemeriksaan otomatis:**

- ✅ kalkulator dipanggil
- ✅ hasil kalkulator = kunci
- ✅ angka kunci ada di jawaban
- ✅ halaman sitasi benar

### H30 — ✅ LULUS

**Pertanyaan:** dosen kami 250 org setahun terakhir, yg ber-NUPTK & dpt rekognisi internasional 18 org. capaiannya brp?

**Jawaban chatbot:**

```text
Persentase dosen yang memiliki NUPTK dan memperoleh rekognisi internasional adalah **7,2 %**.  

Perhitungan (menggunakan rumus IKU 4):  

1. \( \frac{\text{Dosen ber‑NUPTK yang mendapat rekognisi internasional}}{\text{Total dosen PT setahun terakhir}} \times 100\% \)  
2. \( = \frac{18}{250} \times 100\% = 7,2\% \)  【rasio】.  



*Rujukan: definisi, kriteria, dan formula IKU 4 terdapat pada Buku IKU Diktisaintek Berdampak V1, hlm. 61‑63.*
```

**Sumber rumus (kalkulator):**

- Buku IKU Diktisaintek Berdampak V1, IKU 4 – Formula, hlm. 62

**Panggilan kalkulator:**

- argumen `{"argumen_json":"{\"kode\":\"iku4\",\"pembilang\":18,\"penyebut\":250}","fungsi":"rasio"}` → 7,20

**Peringatan chatbot:**

- Jawaban tidak memuat rujukan [n] ke konteks.

**Jawaban yang diharapkan:**

- Angka kunci: **7,20**
- Halaman kunci: 62

**7,2%** (IKU 4).

*Catatan soal:* Ketahanan: nomor IKU tidak disebut; chatbot harus mengenali IKU 4 dari isi soal.

**Pemeriksaan otomatis:**

- ✅ kalkulator dipanggil
- ✅ hasil kalkulator = kunci
- ✅ angka kunci ada di jawaban
- ✅ halaman sitasi benar
