# Uji Jawaban Chatbot (retriever + LLM + kalkulator)

- Waktu: 2026-10-10 01:31:45
- Model LLM: `openai/gpt-oss-120b`
- Soal: 20 dari 20 dijalankan (hitungan 13, definisi & jebakan 7)
- Status run: selesai

## Ringkasan

| Metrik | Hasil |
|---|---|
| Lulus semua pemeriksaan otomatis | **19/20** |
| Hitungan: kalkulator dipanggil | 13/13 |
| Hitungan: hasil kalkulator = kunci | 12/13 |
| Hitungan: angka kunci ada di jawaban | 12/13 |
| Halaman sitasi benar (hitungan) | 13/13 |
| Halaman sitasi benar (definisi) | 6/6 |
| Soal error (API/kuota) | 0 |
| Jawaban dengan peringatan chatbot | 10 |

| ID | Status | Pemeriksaan yang gagal |
|---|---|---|
| D01 | ✅ | - |
| D03 | ✅ | - |
| D04 | ✅ | - |
| D08 | ✅ | - |
| D11 | ✅ | - |
| D12 | ✅ | - |
| H01 | ✅ | - |
| H04 | ✅ | - |
| H07 | ✅ | - |
| H08 | ✅ | - |
| H09 | ✅ | - |
| H11 | ✅ | - |
| H12 | ✅ | - |
| H13 | ✅ | - |
| H16 | ✅ | - |
| D13 | ✅ | - |
| H21 | ✅ | - |
| H26 | ✅ | - |
| H27 | ❌ | hasil kalkulator = kunci; angka kunci ada di jawaban |
| H30 | ✅ | - |

Pemeriksaan otomatis hanya bantuan. Baca jawaban lengkap di bawah dan bandingkan dengan jawaban yang diharapkan.

## Detail per soal

### D01 — ✅ LULUS

**Pertanyaan:** Apa itu IKU 1?

**Jawaban chatbot:**

```text
IKU 1 – Angka Efisiensi Edukasi Perguruan Tinggi (AEE PT) adalah indikator yang mengukur tingkat keberhasilan mahasiswa menyelesaikan studi tepat waktu sesuai masa studi standar, dibandingkan dengan total mahasiswa yang masuk pada periode tertentu [1].  

**Kriteria**:  
- Mahasiswa harus lulus tepat waktu sesuai masa tempuh kurikulum standar.  
- Meliputi semua program pendidikan (D1, D2, D3, D4/Sarjana Terapan, S1, S2, S3, dll.) yang diterapkan di perguruan tinggi [5].

**Rumus perhitungannya**:  
1. **AEE per program** = (Jumlah mahasiswa yang lulus tepat waktu ÷ Total mahasiswa pada tahun akademik tersebut) × 100 % [2].  
2. **Tingkat Pencapaian AEE** = (AEE realisasi ÷ AEE ideal) × 100 % [2].  
3. **AEE PT** = rata-rata (Tingkat Pencapaian AEE) dari semua program pendidikan yang dihitung [2].  

Dengan demikian, AEE PT memberikan nilai persentase rata-rata keberhasilan penyelesaian studi tepat waktu di seluruh program pendidikan perguruan tinggi.
```

**Sitasi chatbot:**

- [1] Buku IKU Diktisaintek Berdampak V1, hlm. 49 (IKU 1, Definisi); juga di PPT hlm. 45
- [2] Buku IKU Diktisaintek Berdampak V1, hlm. 49–50 (IKU 1, Formula); juga di PPT hlm. 46–47; PPT hlm. 46
- [5] Buku IKU Diktisaintek Berdampak V1, hlm. 49 (IKU 1, Kriteria); juga di PPT hlm. 45

**Jawaban yang diharapkan:**

- Halaman kunci: 49

IKU 1 adalah **Angka Efisiensi Edukasi (AEE) Perguruan Tinggi**, yaitu indikator yang mengukur tingkat keberhasilan mahasiswa menyelesaikan studi **tepat waktu** sesuai masa studi standar, dibandingkan dengan total mahasiswa yang masuk pada periode tertentu. AEE PT dihitung dari **rata-rata tingkat pencapaian AEE setiap program pendidikan**. Sifatnya **IKU Wajib**.

**Pemeriksaan otomatis:**

- ✅ fakta: tepat waktu
- ✅ fakta: efisiensi edukasi / AEE
- ✅ halaman sitasi benar

### D03 — ✅ LULUS

**Pertanyaan:** Berapa jumlah IKU wajib, IKU pilihan, dan IKU partisipatif?

**Jawaban chatbot:**

```text
Jumlah IKU wajib adalah **7** indikator [1] (a. (*) IKU wajib bagi seluruh perguruan tinggi sebanyak 7 (tujuh)).  
Jumlah IKU pilihan yang tersedia adalah **5** indikator, dari mana tiap perguruan tinggi dapat memilih 2 indikator [1] (c. IKU pilihan sebanyak 5 (lima), PT dapat memilih 2 dua IKU dari 5 lima IKU pilihan).  
Untuk IKU partisipatif, setiap perguruan tinggi **harus mengusulkan 1 (satu)** IKU partisipatif [2].
```

**Sitasi chatbot:**

- [1] Buku IKU Diktisaintek Berdampak V1, hlm. 48–49
- [2] Buku IKU Diktisaintek Berdampak V1, hlm. 69

**Jawaban yang diharapkan:**

- Halaman kunci: 48

- **7 IKU wajib** bagi seluruh perguruan tinggi.
- **5 IKU pilihan**; PT memilih **2** dari 5.
- PT harus mengusulkan **1 IKU partisipatif**.
- Catatan: IKU 6 (publikasi Scopus/WoS) **wajib bagi PTN-BH**.

**Pemeriksaan otomatis:**

- ✅ fakta: 7 (tujuh) / tujuh / 7 IKU / 7 indikator / sebanyak 7
- ✅ fakta: 5 (lima) / lima / 5 IKU / 5 indikator
- ✅ fakta: 2 (dua) / dua / memilih 2
- ✅ fakta: partisipatif
- ✅ halaman sitasi benar

### D04 — ✅ LULUS

**Pertanyaan:** Sebutkan IKU yang bersifat wajib.

**Jawaban chatbot:**

```text
Berikut adalah **IKU yang bersifat wajib** (ditandai dengan ✔ pada kolom “Wajib” dalam tabel IKU) :

1. **IKU 1 – Angka Efisiensi Edukasi Perguruan Tinggi (AEE PT)**[1]  
2. **IKU 2 – Persentase lulusan pendidikan tinggi & vokasi yang langsung bekerja/melanjutkan jenjang pendidikan berikutnya dalam jangka waktu 1 tahun setelah kelulusan**[1]  
3. **IKU 3 – Persentase mahasiswa S1/D4/D3/D2/D1 berkegiatan/meraih prestasi di luar program studi**[1]  
4. **IKU 5 – Rasio luaran hasil kerja sama antara PT dan start-up/industri/Lembaga**[1]  
5. **IKU 7 – Persentase keterlibatan Perguruan Tinggi dalam SDG 1, SDG 4, SDG 17, serta dua (2) SDG lain sesuai keunggulan**[1]  
6. **IKU 9 – Persentase Pendapatan Non Pendidikan/UKT**[1]  
7. **IKU 12 – Ketersediaan perencanaan strategis peningkatan kesejahteraan dosen**[1]

Jumlahnya memang **tujuh (7) indikator wajib** sebagaimana dijelaskan pada bagian 5.3.1 [1].
```

**Sitasi chatbot:**

- [1] Buku IKU Diktisaintek Berdampak V1, hlm. 48–49

**Jawaban yang diharapkan:**

- Halaman kunci: 48

IKU 1 (AEE), IKU 2 (lulusan bekerja/studi lanjut/wirausaha dalam 1 tahun), IKU 3 (mahasiswa berkegiatan/berprestasi di luar prodi), IKU 5 (rasio luaran kerja sama), IKU 7 (keterlibatan SDGs), IKU 9 (pendapatan non-UKT), dan IKU 12 (perencanaan kesejahteraan dosen).

**Pemeriksaan otomatis:**

- ✅ fakta: efisiensi edukasi / IKU 1
- ✅ fakta: lulusan / IKU 2
- ✅ fakta: di luar program studi / IKU 3
- ✅ fakta: kerja sama / kerjasama / IKU 5
- ✅ fakta: SDG / IKU 7
- ✅ fakta: non pendidikan / non-pendidikan / UKT / IKU 9
- ✅ fakta: kesejahteraan dosen / IKU 12
- ✅ halaman sitasi benar

### D08 — ✅ LULUS

**Pertanyaan:** Pendapatan apa saja yang tidak termasuk dalam perhitungan IKU 9?

**Jawaban chatbot:**

```text
Pendapatan yang **tidak termasuk** dalam perhitungan IKU 9 – Persentase Pendapatan Non Pendidikan/UKT adalah:

1. **SPP/UKT/biaya kuliah mahasiswa**[1]  
2. **Iuran pengembangan institusi**[1]  
3. **Subsidi langsung dari pemerintah**, seperti belanja pegawai, belanja operasional, BOPTN, BPPTNBH, dan sejenisnya[1]  
4. **Sumbangan/filantropi yang tidak masuk laporan keuangan resmi perguruan tinggi**[1]  
5. **Dana pokok dana abadi/endowment fund** yang disimpan permanen dan tidak dibelanjakan[1]  
6. **Pendapatan yang tidak dibukukan**, termasuk hibah barang tanpa nilai, serta **dana yang lewat kampus tanpa pelaporan resmi**[5].
```

**Sitasi chatbot:**

- [1] Buku IKU Diktisaintek Berdampak V1, hlm. 59 (IKU 9, Kriteria); juga di Buku (Lampiran Kepmen 358/M/KEP/2025) hlm. 122–123; PPT hlm. 56
- [5] Buku IKU Diktisaintek Berdampak V1, hlm. 79 (IKU 9, Kriteria dan Ketentuan); juga di PPT hlm. 81; PPT hlm. 85; PPT hlm. 86

**Jawaban yang diharapkan:**

- Halaman kunci: 59

1. SPP/UKT/biaya kuliah mahasiswa;
2. iuran pengembangan institusi;
3. subsidi langsung pemerintah (belanja pegawai, operasional, BOPTN, BPPTNBH, dan sejenisnya);
4. sumbangan/filantropi yang tidak masuk laporan keuangan resmi; dan
5. dana pokok dana abadi (*endowment fund*).

**Pemeriksaan otomatis:**

- ✅ fakta: UKT / SPP
- ✅ fakta: BOPTN
- ✅ fakta: iuran pengembangan
- ✅ fakta: dana abadi / endowment
- ✅ halaman sitasi benar

### D11 — ✅ LULUS

**Pertanyaan:** Lulusan 400, yang bekerja 280, berapa capaian IKU 1?

**Jawaban chatbot:**

```text
Informasi yang diperlukan untuk menghitung **IKU 1 – Angka Efisiensi Edukasi Perguruan Tinggi (AEE PT)** tidak terdapat dalam pertanyaan. IKU 1 menghitung persentase mahasiswa yang **lulus tepat waktu sesuai masa tempuh kurikulum** (lihat definisi dan rumus pada konteks [1]–[4]), bukan persentase lulusan yang bekerja. Data yang Anda berikan (lulusan = 400, yang bekerja = 280) relevan untuk **IKU 2 – Persentase lulusan pendidikan tinggi & vokasi yang langsung bekerja/melanjutkan jenjang pendidikan**.

Untuk dapat menghitung IKU 1 diperlukan data, misalnya:
- Jumlah mahasiswa tahun akademik yang lulus sesuai masa tempuh kurikulum per program (D1, D2, D3, D4/Sarjana, S2, S3, dll.).
- Total mahasiswa tahun akademik per program.
- (Tidak termasuk mahasiswa pindah, DO, atau cuti lebih dari ketentuan) [3].

Silakan sediakan data tersebut atau ajukan pertanyaan mengenai **IKU 2**, sehingga perhitungan yang tepat dapat dilakukan.
```

**Sitasi chatbot:**

- [1] Buku IKU Diktisaintek Berdampak V1, hlm. 49–50 (IKU 1, Formula); juga di PPT hlm. 46–47; PPT hlm. 46; Buku (Lampiran Kepmen 358/M/KEP/2025) hlm. 101–102
- [3] Buku IKU Diktisaintek Berdampak V1, hlm. 49 (IKU 1, Ketentuan); juga di PPT hlm. 45; Buku (Lampiran Kepmen 358/M/KEP/2025) hlm. 100–101
- [4] Buku IKU Diktisaintek Berdampak V1, hlm. 49 (IKU 1, Kriteria); juga di PPT hlm. 45

**Jawaban yang diharapkan:**

- Halaman kunci: 49, 51

Chatbot harus **mengoreksi**: IKU 1 adalah Angka Efisiensi Edukasi (kelulusan tepat waktu), bukan persentase lulusan bekerja. Data lulusan bekerja termasuk **IKU 2**. Jika dihitung sebagai IKU 2, dengan asumsi seluruh 280 lulusan berbobot 1 (masa tunggu < 6 bulan dan gaji > 1,2× UMP) dan 400 adalah total responden tracer study: 280/400 × 100% = **70%** (lihat H04).

*Catatan soal:* Soal jebakan: chatbot harus meluruskan bahwa data lulusan bekerja termasuk IKU 2, bukan IKU 1.

**Pemeriksaan otomatis:**

- ✅ fakta: IKU 2
- ✅ fakta: efisiensi edukasi / tepat waktu / AEE
- ✅ halaman sitasi benar

### D12 — ✅ LULUS

**Pertanyaan:** Berapa besaran UKT di Universitas Gadjah Mada tahun 2026?

**Jawaban chatbot:**

```text
Informasi mengenai besaran UKT (Uang Kuliah Tunggal) di Universitas Gadjah Mada tahun 2026 tidak ditemukan dalam dokumen IKU yang diberikan.
```

**Jawaban yang diharapkan:**

- Halaman kunci: -

Informasi ini **tidak ada** di Buku IKU. Chatbot harus menyatakan tidak menemukan jawabannya di dokumen, bukan mengarang angka.

*Catatan soal:* Soal di luar cakupan: chatbot harus menolak, bukan mengarang angka UKT.

**Pemeriksaan otomatis:**

- ✅ fakta: tidak ditemukan / tidak terdapat / tidak tersedia / tidak ada informasi / tidak dijelaskan / tidak memuat
- ✅ tidak mengarang sitasi

### H01 — ✅ LULUS

**Pertanyaan:** Prodi S1 memiliki 200 mahasiswa dalam satu tahun akademik. Sebanyak 40 mahasiswa lulus tepat 8 semester. Berapa AEE realisasi dan tingkat pencapaian AEE prodi tersebut?

**Jawaban chatbot:**

```text
AEE realisasi prodi S1 = 20 % [1]  
Tingkat pencapaian AEE prodi S1 = 80 % [1]
```

**Sitasi chatbot:**

- [1] Buku IKU Diktisaintek Berdampak V1, hlm. 49–50 (IKU 1, Formula); juga di Buku (Lampiran Kepmen 358/M/KEP/2025) hlm. 101–102; Buku (Lampiran Kepmen 358/M/KEP/2025) hlm. 101–102; PPT hlm. 46; PPT hlm. 46–47

**Sumber rumus (kalkulator):**

- Buku IKU Diktisaintek Berdampak V1, IKU 1 – Ketentuan & Formula a–b, hlm. 49

**Panggilan kalkulator:**

- argumen `{"argumen_json":"{\"jenjang\":\"S1\",\"lulus_tepat_waktu\":40,\"total_mahasiswa\":200,\"pindah\":0,\"drop_out\":0,\"cuti_lebih\":0}","fungsi":"iku1_aee_prodi"}` → aee_realisasi_pct = 20,00, tingkat_pencapaian_pct = 80,00

**Peringatan chatbot:**

- Panggilan alat ditolak server (Error code: 400 - {'error': {'message': "Tool call validation failed: tool call validation failed: parameters for tool h); diulang otomatis.
- LLM mengembalikan respons kosong; diulang otomatis.

**Jawaban yang diharapkan:**

- Angka kunci: **aee_realisasi_pct = 20,00, tingkat_pencapaian_pct = 80,00**
- Halaman kunci: 49

AEE realisasi **20%**, tingkat pencapaian **80%**.

**Pemeriksaan otomatis:**

- ✅ kalkulator dipanggil
- ✅ hasil kalkulator = kunci
- ✅ angka kunci ada di jawaban
- ✅ halaman sitasi benar

### H04 — ✅ LULUS

**Pertanyaan:** Tracer study mengumpulkan 400 responden lulusan S1. Sebanyak 280 lulusan bekerja dengan masa tunggu < 6 bulan dan gaji > 1,2× UMP; sisanya belum bekerja. Berapa capaian IKU 2?

**Jawaban chatbot:**

```text
Capaian IKU 2 (Persentase lulusan pendidikan tinggi & vokasi yang langsung bekerja/melanjutkan jenjang pendidikan berikutnya dalam jangka waktu 1 tahun setelah kelulusan) adalah **70 %**.  

Langkah perhitungannya:  
- Responden yang bekerja dengan masa tunggu < 6 bulan dan gaji > 1,2 × UMP: 280 orang, bobot = 1 → 280 × 1 = 280.  
- Total responden yang dikumpulkan: 400 orang.  
- Capaian = (280 ÷ 400) × 100 % = 70 %【iku2】.
```

**Sumber rumus (kalkulator):**

- Buku IKU Diktisaintek Berdampak V1, IKU 2 – Kriteria b–f & Formula, hlm. 51–52

**Panggilan kalkulator:**

- argumen `{"argumen_json":"{\"total_responden\": 400, \"kategori\": {\"bekerja_\u003c6bln_\u003e1.2ump\": 280}}","fungsi":"iku2"}` → 70,00

**Peringatan chatbot:**

- Jawaban tidak memuat rujukan [n] ke konteks.

**Jawaban yang diharapkan:**

- Angka kunci: **70,00**
- Halaman kunci: 51, 52

**70%**.

**Pemeriksaan otomatis:**

- ✅ kalkulator dipanggil
- ✅ hasil kalkulator = kunci
- ✅ angka kunci ada di jawaban
- ✅ halaman sitasi benar

### H07 — ✅ LULUS

**Pertanyaan:** Sebuah PT memiliki 1.000 mahasiswa S1/Diploma. Rinciannya: - 100 mahasiswa magang 20 SKS - 150 mahasiswa pertukaran 8 SKS - 50 mahasiswa riset 4 SKS - 5 mahasiswa juara 1 lomba nasional - 10 mahasiswa finalis lomba internasional Berapa capaian IKU 3?

**Jawaban chatbot:**

```text
Capaian IKU 3 = 21,5 % [1][2][3] 

Langkah perhitungannya:
- Kegiatan magang 20 SKS: 100 mahasiswa × 1 = 100  
- Kegiatan pertukaran 8 SKS: 150 mahasiswa × 0,6 = 90  
- Kegiatan riset 4 SKS: 50 mahasiswa × 0,4 = 20  
- Prestasi juara 1 lomba nasional: 5 mahasiswa × 0,6 = 3  
- Prestasi finalis lomba internasional: 10 mahasiswa × 0,2 = 2  

Total bobot Σ(n·k) = 215  
Capaian = 215 ÷ 1 000 × 100 % = **21,5 %**.
```

**Sitasi chatbot:**

- [1] Buku IKU Diktisaintek Berdampak V1, hlm. 53–54 (IKU 3, Formula); juga di Buku (Lampiran Kepmen 358/M/KEP/2025) hlm. 107–108; PPT hlm. 50
- [2] Buku IKU Diktisaintek Berdampak V1, hlm. 53 (IKU 3, Ketentuan); juga di Buku (Lampiran Kepmen 358/M/KEP/2025) hlm. 106–107; PPT hlm. 50; PPT hlm. 49
- [3] Buku IKU Diktisaintek Berdampak V1, hlm. 53 (IKU 3, Kriteria); juga di Buku (Lampiran Kepmen 358/M/KEP/2025) hlm. 105–106; PPT hlm. 49

**Sumber rumus (kalkulator):**

- Buku IKU Diktisaintek Berdampak V1, IKU 3 – Formula & Ketentuan Bobot, hlm. 53–54

**Panggilan kalkulator:**

- argumen `{"argumen_json":"{\"kode\": \"iku3\", \"pembilang\": 0, \"penyebut\": 0}","fungsi":"rasio"}` → 'iku3' bukan kode rasio: IKU ini punya fungsi sendiri (iku3). Panggil ulang hitung_iku dengan fungsi tersebut dan data asli dari pertanyaan (jangan dihitung dulu). Format: - iku3: {"total_mahasiswa": 1000, "kegiatan": [{"jumlah": 100, "sks": 20}], "prestasi": [{"jumlah": 5, "tingkat": "nasional", "peringkat": "juara1"}]}  (tingkat: "internasional", "nasional", "provinsi"; peringkat: "finalis", "harapan", "juara1", "juara2_3_favorit")
- argumen `{"argumen_json":"{\"total_mahasiswa\": 1000, \"kegiatan\": [{\"jumlah\": 100, \"sks\": 20}, {\"jumlah\": 150, \"sks\": 8}, {\"jumlah\": 50, \"sks\": 4}], \"prestasi\": [{\"jumlah\": 5, \"tingkat\": \"nasional\", \"peringkat\": \"juara1\"}, {\"jumlah\": 10, \"tingkat\": \"internasional\", \"peringkat\": \"finalis\"}]}","fungsi":"iku3"}` → 21,50

**Peringatan chatbot:**

- LLM mengembalikan respons kosong; diulang otomatis.
- Panggilan alat ditolak server (nama alat 'hituk_iku' tidak dikenal); diulang otomatis.

**Jawaban yang diharapkan:**

- Angka kunci: **21,50**
- Halaman kunci: 53, 54

**21,5%**.

**Pemeriksaan otomatis:**

- ✅ kalkulator dipanggil
- ✅ hasil kalkulator = kunci
- ✅ angka kunci ada di jawaban
- ✅ halaman sitasi benar

### H08 — ✅ LULUS

**Pertanyaan:** Dari 500 mahasiswa, prestasi yang tercatat adalah 2 juara 1 internasional, 4 juara 2 tingkat provinsi, dan 20 finalis tingkat provinsi. Tidak ada kegiatan SKS di luar prodi. Berapa capaian IKU 3?

**Jawaban chatbot:**

```text
Capaian IKU 3 sebesar **0,76 %**.  

Langkah perhitungan (diperoleh dari alat hitung_iku):
- Prestasi juara 1 internasional: 2 × 1 = 2  
- Prestasi juara 2/3/favorit tingkat provinsi: 4 × 0,2 = 0,8  
- Prestasi finalis tingkat provinsi: 20 × 0,05 = 1  
- Σ(n·k) = 3,8  
- Capaian = 3,8 ÷ 500 × 100 % = **0,76 %**  

Sumber: Buku IKU Diktisaintek Berdampak V1, IKU 3 – Formula & Ketentuan Bobot, hlm. 53-54.
```

**Sumber rumus (kalkulator):**

- Buku IKU Diktisaintek Berdampak V1, IKU 3 – Formula & Ketentuan Bobot, hlm. 53–54

**Panggilan kalkulator:**

- argumen `{"argumen_json":"{\"total_mahasiswa\":500,\"kegiatan\":[],\"prestasi\":[{\"jumlah\":2,\"tingkat\":\"internasional\",\"peringkat\":\"juara1\"},{\"jumlah\":4,\"tingkat\":\"provinsi\",\"peringkat\":\"juara2\"},{\"jumlah\":20,\"tingkat\":\"provinsi\",\"peringkat\":\"finalis\"}]}","fungsi":"iku3"}` → ValueError: Prestasi (tingkat, peringkat) ('provinsi', 'juara2') tidak dikenal. Pilihan: ('internasional', 'juara1'), ('internasional', 'juara2_3_favorit'), ('internasional', 'harapan'), ('internasional', 'finalis'), ('nasional', 'juara1'), ('nasional', 'juara2_3_favorit'), ('nasional', 'harapan'), ('nasional', 'finalis'), ('provinsi', 'juara1'), ('provinsi', 'juara2_3_favorit'), ('provinsi', 'harapan'), ('provinsi', 'finalis'). Periksa nama fungsi dan format argumen.
- argumen `{"argumen_json":"{\"total_mahasiswa\":500,\"kegiatan\":[],\"prestasi\":[{\"jumlah\":2,\"tingkat\":\"internasional\",\"peringkat\":\"juara1\"},{\"jumlah\":4,\"tingkat\":\"provinsi\",\"peringkat\":\"juara2_3_favorit\"},{\"jumlah\":20,\"tingkat\":\"provinsi\",\"peringkat\":\"finalis\"}]}","fungsi":"iku3"}` → 0,76

**Peringatan chatbot:**

- LLM mengembalikan respons kosong; diulang otomatis.
- LLM mengembalikan respons kosong; diulang otomatis.
- Panggilan alat ditolak server (nama alat 'hitungan_iku' tidak dikenal); diulang otomatis.
- Panggilan alat ditolak server (nama alat 'hitungan_iku' tidak dikenal); diulang otomatis.
- Jawaban tidak memuat rujukan [n] ke konteks.

**Jawaban yang diharapkan:**

- Angka kunci: **0,76**
- Halaman kunci: 54

**0,76%**.

**Pemeriksaan otomatis:**

- ✅ kalkulator dipanggil
- ✅ hasil kalkulator = kunci
- ✅ angka kunci ada di jawaban
- ✅ halaman sitasi benar

### H09 — ✅ LULUS

**Pertanyaan:** PT memiliki 120 kerja sama. Dari kerja sama itu dihasilkan 30 karya (judul) yang telah dimanfaatkan oleh mitra, melibatkan total 90 dosen. Berapa capaian IKU 5?

**Jawaban chatbot:**

```text
Capaian IKU 5 (Rasio luaran hasil kerja sama antara PT dan start-up/industri/lembaga) adalah:

30 (luaran/judul) ÷ 120 (total kerja sama) × 100 % = **25 %**【iku5】.
```

**Sumber rumus (kalkulator):**

- Buku IKU Diktisaintek Berdampak V1, IKU 5 – Formula & Keterangan, hlm. 57

**Panggilan kalkulator:**

- argumen `{"argumen_json":"{\"kode\": \"iku5\", \"pembilang\": 30, \"penyebut\": 120}","fungsi":"rasio"}` → 25,00

**Peringatan chatbot:**

- Panggilan alat ditolak server (nama alat 'hitungan_iku' tidak dikenal); diulang otomatis.
- Jawaban tidak memuat rujukan [n] ke konteks.

**Jawaban yang diharapkan:**

- Angka kunci: **25,00**
- Halaman kunci: 57

**25%**. Yang dihitung adalah **jumlah judul/karya, bukan jumlah dosen**, sehingga angka 90 tidak dipakai.

**Pemeriksaan otomatis:**

- ✅ kalkulator dipanggil
- ✅ hasil kalkulator = kunci
- ✅ angka kunci ada di jawaban
- ✅ halaman sitasi benar

### H11 — ✅ LULUS

**Pertanyaan:** Total publikasi 20, terdiri atas 4 artikel Q1 hasil kolaborasi dengan penulis luar negeri, 6 artikel Q1 tanpa kolaborasi, dan 10 prosiding internasional terindeks Scopus. Berapa capaian IKU 6?

**Jawaban chatbot:**

```text
Capaian IKU 6 = 67,5 % [4][1] 

Langkah perhitungan (menggunakan fungsi hitung_iku):
- Q1 tanpa kolaborasi: 6 × 1 = 6  
- Prosiding internasional: 10 × 0,25 = 2,5  
- Q1 dengan kolaborasi internasional: 4 × (1 + 0,25) = 5  
- Σ (n × k) = 13,5  
- Capaian = 13,5 ÷ 20 × 100 % = 67,5 %  

Jadi, persentase publikasi bereputasi internasional yang tercapai adalah 67,5 %.
```

**Sitasi chatbot:**

- [1] Buku IKU Diktisaintek Berdampak V1, hlm. 63 (IKU 6, Kriteria); juga di Buku (Lampiran Kepmen 358/M/KEP/2025) hlm. 117–118; PPT hlm. 61
- [4] Buku IKU Diktisaintek Berdampak V1, hlm. 63 (IKU 6, Formula); juga di Buku (Lampiran Kepmen 358/M/KEP/2025) hlm. 119

**Sumber rumus (kalkulator):**

- Buku IKU Diktisaintek Berdampak V1, IKU 6 – Kriteria (bobot kuartil) & Formula, hlm. 63

**Panggilan kalkulator:**

- argumen `{"argumen_json":"{\"total_publikasi\": 20, \"publikasi\": {\"q1\": 10, \"prosiding\": 10}, \"kolaborasi\": {\"q1\": 4}}","fungsi":"iku6"}` → ValueError: Jumlah publikasi per jenis (24) melebihi total publikasi (20). Periksa nama fungsi dan format argumen.
- argumen `{"argumen_json":"{\"total_publikasi\": 20, \"publikasi\": {\"q1\": 6, \"prosiding\": 10}, \"kolaborasi\": {\"q1\": 4}}","fungsi":"iku6"}` → 67,50

**Peringatan chatbot:**

- Panggilan alat ditolak server (nama alat 'hitungan_iku' tidak dikenal); diulang otomatis.

**Jawaban yang diharapkan:**

- Angka kunci: **67,50**
- Halaman kunci: 63

**67,5%**.

**Pemeriksaan otomatis:**

- ✅ kalkulator dipanggil
- ✅ hasil kalkulator = kunci
- ✅ angka kunci ada di jawaban
- ✅ halaman sitasi benar

### H12 — ✅ LULUS

**Pertanyaan:** Dari 60 program SDGs PT, 45 program berkontribusi pada SDG 1, 4, 17, dan 2 SDG pilihan. Berapa capaian IKU 7?

**Jawaban chatbot:**

```text
Capaian IKU 7 = 45 ÷ 60 × 100% = 75 %[1]. Ini menunjukkan bahwa 75 % program perguruan tinggi berkontribusi pada SDG 1, SDG 4, SDG 17, dan dua SDG pilihan sesuai ketentuan.
```

**Sitasi chatbot:**

- [1] Buku IKU Diktisaintek Berdampak V1, hlm. 58 (IKU 7, Formula); juga di PPT hlm. 55; Buku (Lampiran Kepmen 358/M/KEP/2025) hlm. 121

**Sumber rumus (kalkulator):**

- Buku IKU Diktisaintek Berdampak V1, IKU 7 – Formula, hlm. 58

**Panggilan kalkulator:**

- argumen `{"argumen_json":"{\"kode\": \"iku7\", \"pembilang\": 45, \"penyebut\": 60}","fungsi":"rasio"}` → 75,00

**Jawaban yang diharapkan:**

- Angka kunci: **75,00**
- Halaman kunci: 58

**75%**.

**Pemeriksaan otomatis:**

- ✅ kalkulator dipanggil
- ✅ hasil kalkulator = kunci
- ✅ angka kunci ada di jawaban
- ✅ halaman sitasi benar

### H13 — ✅ LULUS

**Pertanyaan:** Total pendapatan PT dalam satu tahun anggaran adalah Rp500 miliar, terdiri atas: - UKT Rp300 miliar - BOPTN Rp80 miliar - hibah riset kompetitif Rp50 miliar - jasa konsultasi dan pelatihan Rp40 miliar - unit bisnis (hotel, penerbitan) Rp20 miliar - hasil investasi dana abadi Rp10 miliar Berapa capaian IKU 9?

**Jawaban chatbot:**

```text
Capaian IKU 9 = (hibah riset + jasa konsultasi + unit bisnis + hasil investasi dana abadi) ÷ total pendapatan PT × 100 %  
= (50 + 40 + 20 + 10) ÷ 500 × 100 %  
= 120 ÷ 500 × 100 % = 24 % [3][1] 

Jadi, persentase pendapatan non-pendidikan/UKT yang tercapai oleh perguruan tinggi tersebut adalah **24 %**.
```

**Sitasi chatbot:**

- [1] Buku IKU Diktisaintek Berdampak V1, hlm. 59 (IKU 9, Kriteria); juga di PPT hlm. 56; Buku (Lampiran Kepmen 358/M/KEP/2025) hlm. 122–123
- [3] Buku IKU Diktisaintek Berdampak V1, hlm. 59 (IKU 9, Formula); juga di Buku (Lampiran Kepmen 358/M/KEP/2025) hlm. 124; PPT hlm. 56

**Sumber rumus (kalkulator):**

- Buku IKU Diktisaintek Berdampak V1, IKU 9 – Kriteria & Formula, hlm. 59

**Panggilan kalkulator:**

- argumen `{"argumen_json":"{\"total_pendapatan\":500,\"rincian\":{\"hibah_riset\":50,\"konsultasi\":40,\"unit_bisnis\":20,\"hasil_dana_abadi\":10}}","fungsi":"iku9"}` → 24,00

**Peringatan chatbot:**

- LLM mengembalikan respons kosong; diulang otomatis.

**Jawaban yang diharapkan:**

- Angka kunci: **24,00**
- Halaman kunci: 59

**24%**. Jawaban yang memasukkan BOPTN (200/500 = 40%) **salah**.

**Pemeriksaan otomatis:**

- ✅ kalkulator dipanggil
- ✅ hasil kalkulator = kunci
- ✅ angka kunci ada di jawaban
- ✅ halaman sitasi benar

### H16 — ✅ LULUS

**Pertanyaan:** Nilai akhir evaluasi SAKIP sebuah PT adalah 82. Apa predikatnya?

**Jawaban chatbot:**

```text
Berdasarkan perhitungan dengan alat hitung_iku, nilai akhir 82 termasuk dalam rentang 80-89 pada tabel predikat SAKIP, sehingga predikatnya adalah **A (sangat baik)**. Langkah perhitungannya: nilai akhir 82 → lihat tabel predikat SAKIP (AA ≥ 90, A ≥ 80, BB ≥ 70, B ≥ 60, CC-C < 60) → predikat A (sangat baik)[2].
```

**Sitasi chatbot:**

- [2] Buku IKU Diktisaintek Berdampak V1, hlm. 66 (IKU 11b, Kriteria)

**Sumber rumus (kalkulator):**

- Buku IKU Diktisaintek Berdampak V1, IKU 11b – Skala dan Predikat, hlm. 66

**Panggilan kalkulator:**

- argumen `{"argumen_json":"{\"nilai_akhir\": 82}","fungsi":"iku11b_predikat"}` → A (sangat baik)

**Peringatan chatbot:**

- LLM menghitung sendiri tanpa kalkulator; diminta mengulang dengan alat.

**Jawaban yang diharapkan:**

- Angka kunci: **A (sangat baik)**
- Halaman kunci: 66

Predikat **A (sangat baik)**, rentang nilai 80–89: efektif dan efisien, menghasilkan kinerja di atas target.

**Pemeriksaan otomatis:**

- ✅ kalkulator dipanggil
- ✅ hasil kalkulator = kunci
- ✅ angka kunci ada di jawaban
- ✅ halaman sitasi benar

### D13 — ✅ LULUS

**Pertanyaan:** aee tu apaan sih? ngukur apa?

**Jawaban chatbot:**

```text
AEE (Angka Efisiensi Edukasi) adalah indikator yang mengukur **tingkat keberhasilan mahasiswa menyelesaikan studinya tepat waktu sesuai masa studi standar** dibandingkan dengan total mahasiswa yang masuk pada periode tersebut. AEE menghitung proporsi mahasiswa yang lulus dalam jangka waktu yang ditetapkan (misalnya 8 semester untuk program Sarjana) terhadap seluruh mahasiswa yang terdaftar, kemudian dirata-rata across setiap program pendidikan di perguruan tinggi untuk menghasilkan AEE PT % [3][4]​.
```

**Sitasi chatbot:**

- [3] Buku IKU Diktisaintek Berdampak V1, hlm. 49 (IKU 1, Definisi); juga di Buku (Lampiran Kepmen 358/M/KEP/2025) hlm. 100; PPT hlm. 45
- [4] Buku IKU Diktisaintek Berdampak V1, hlm. 49 (IKU 1, Ketentuan); juga di Buku (Lampiran Kepmen 358/M/KEP/2025) hlm. 100–101; PPT hlm. 45

**Jawaban yang diharapkan:**

- Halaman kunci: 49

AEE = Angka Efisiensi Edukasi (IKU 1), mengukur keberhasilan mahasiswa menyelesaikan studi **tepat waktu** sesuai masa studi standar (sama dengan D01).

*Catatan soal:* Ketahanan: bahasa santai ('aee tu apaan sih'). 'AEE' sengaja tidak dijadikan fakta karena sudah ada di pertanyaan.

**Pemeriksaan otomatis:**

- ✅ fakta: tepat waktu
- ✅ fakta: efisiensi edukasi
- ✅ halaman sitasi benar

### H21 — ✅ LULUS

**Pertanyaan:** lulusan kampus kami 1.341 org, minimal responden tracer study nya brp?

**Jawaban chatbot:**

```text
Berdasarkan rumus Slovin pada IKU 2, dengan jumlah lulusan N = 1.341 dan galat d = 2,3 % (0,023), jumlah responden minimum yang harus diperoleh adalah **785 orang**.  

Langkah perhitungan:  
1. N·d² = 1.341 × 0,023² = 0,71  
2. n = 1.341 ÷ (0,71 + 1) = 784,49  
3. Dibulatkan ke atas = 785 responden [iku2_responden_minimum]
```

**Sumber rumus (kalkulator):**

- Buku IKU Diktisaintek Berdampak V1, IKU 2 – Formula Responden Minimum, hlm. 52

**Panggilan kalkulator:**

- argumen `{"argumen_json":"{\"jumlah_lulusan\": 1341}","fungsi":"iku2_responden_minimum"}` → 785

**Peringatan chatbot:**

- LLM mengembalikan respons kosong; diulang otomatis.
- LLM mengembalikan respons kosong; diulang otomatis.
- Panggilan alat ditolak server (nama alat 'hit\u200bung_iku' tidak dikenal); diulang otomatis.
- Jawaban tidak memuat rujukan [n] ke konteks.

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

### H26 — ✅ LULUS

**Pertanyaan:** pendapatan total Rp1.250.000.000, terdiri dr ukt rp 900jt, kontrak riset 150 juta, royalti Rp50.000.000, sisanya 150jt dari boptn. capaian iku 9?

**Jawaban chatbot:**

```text
Capaian IKU 9 = 16 % [3][1] 

Perhitungan:
- Pendapatan non-mahasiswa yang diakui: kontrak riset Rp 150 juta + royalti Rp 50 juta = Rp 200 juta.  
- Total pendapatan PT: Rp 1.250 juta.  
- Persentase = (200 juta ÷ 1.250 juta) × 100 % = 16 % (hasil dari alat hitung_iku).
```

**Sitasi chatbot:**

- [1] Buku IKU Diktisaintek Berdampak V1, hlm. 59 (IKU 9, Kriteria); juga di PPT hlm. 56; Buku (Lampiran Kepmen 358/M/KEP/2025) hlm. 122–123
- [3] Buku IKU Diktisaintek Berdampak V1, hlm. 59 (IKU 9, Formula); juga di Buku (Lampiran Kepmen 358/M/KEP/2025) hlm. 124; PPT hlm. 56

**Sumber rumus (kalkulator):**

- Buku IKU Diktisaintek Berdampak V1, IKU 9 – Kriteria & Formula, hlm. 59

**Panggilan kalkulator:**

- argumen `{"argumen_json":"{\"total_pendapatan\": 1250000000, \"rincian\": {\"kontrak_riset\": 150000000, \"royalti\": 50000000}}","fungsi":"iku9"}` → 16,00

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

### H27 — ❌ PERLU DICEK

**Pertanyaan:** total pendapatan 2 milyar: hibah riset 300 jt, konsultasi 0,2 M, ukt 1,5 M. hitung iku 9 nya

**Jawaban chatbot:**

```text
Persentase Pendapatan Non Pendidikan/UKT (IKU 9) = 15,01 % [1][2][3]  

Langkah perhitungannya:  
- Pendapatan non-mahasiswa yang diakui = hibah riset 300 jt + konsultasi 0,2 jt = 300,2 jt.  
- Total pendapatan PT dalam satu periode = 2 000 jt.  
- Persentase = (300,2 ÷ 2 000) × 100 % = 15,01 %  

(Perhitungan dilakukan dengan fungsi **hitung_iku** sesuai rumus resmi).
```

**Sitasi chatbot:**

- [1] Buku IKU Diktisaintek Berdampak V1, hlm. 59 (IKU 9, Kriteria); juga di Buku (Lampiran Kepmen 358/M/KEP/2025) hlm. 122–123; PPT hlm. 56
- [2] Buku IKU Diktisaintek Berdampak V1, hlm. 59 (IKU 9, Formula); juga di Buku (Lampiran Kepmen 358/M/KEP/2025) hlm. 124; PPT hlm. 56
- [3] Buku IKU Diktisaintek Berdampak V1, hlm. 59 (IKU 9, Definisi); juga di Buku (Lampiran Kepmen 358/M/KEP/2025) hlm. 122; PPT hlm. 56

**Sumber rumus (kalkulator):**

- Buku IKU Diktisaintek Berdampak V1, IKU 9 – Kriteria & Formula, hlm. 59

**Panggilan kalkulator:**

- argumen `{"argumen_json":"{\"total_pendapatan\": 2000, \"rincian\": {\"hibah_riset\": 300, \"konsultasi\": 0.2}}","fungsi":"iku9"}` → 15,01

**Peringatan chatbot:**

- LLM mengembalikan respons kosong; diulang otomatis.

**Jawaban yang diharapkan:**

- Angka kunci: **25,00**
- Halaman kunci: 59

**25%**.

*Catatan soal:* Ketahanan: ejaan 'milyar', desimal koma '0,2 M' dan '1,5 M' dicampur dengan 'jt'.

**Pemeriksaan otomatis:**

- ✅ kalkulator dipanggil
- ❌ hasil kalkulator = kunci
- ❌ angka kunci ada di jawaban
- ✅ halaman sitasi benar

### H30 — ✅ LULUS

**Pertanyaan:** dosen kami 250 org setahun terakhir, yg ber-NUPTK & dpt rekognisi internasional 18 org. capaiannya brp?

**Jawaban chatbot:**

```text
Persentase Dosen PT yang mendapatkan rekognisi internasional = (18 ÷ 250) × 100% = 7,2 %[1]. Langkah perhitungannya: (Dosen ber-NUPTK yang mendapat rekognisi internasional) ÷ (Total dosen PT setahun terakhir) × 100% = 18 ÷ 250 × 100% = 7,2 %[1].
```

**Sitasi chatbot:**

- [1] Buku IKU Diktisaintek Berdampak V1, hlm. 62–63 (IKU 4, Formula); juga di Buku (Lampiran Kepmen 358/M/KEP/2025) hlm. 112; PPT hlm. 60–61

**Sumber rumus (kalkulator):**

- Buku IKU Diktisaintek Berdampak V1, IKU 4 – Formula, hlm. 62

**Panggilan kalkulator:**

- argumen `{"argumen_json":"{\"kode\": \"iku4\", \"pembilang\": 18, \"penyebut\": 250}","fungsi":"rasio"}` → 7,20

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
