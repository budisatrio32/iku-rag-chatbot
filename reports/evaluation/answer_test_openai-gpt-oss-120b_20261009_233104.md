# Uji Jawaban Chatbot (retriever + LLM + kalkulator)

- Waktu: 2026-10-10 00:21:06
- Model LLM: `openai/gpt-oss-120b`
- Soal: 44 dari 44 dijalankan (hitungan 30, definisi & jebakan 14)
- Status run: selesai

## Ringkasan

| Metrik | Hasil |
|---|---|
| Lulus semua pemeriksaan otomatis | **36/44** |
| Hitungan: kalkulator dipanggil | 24/30 |
| Hitungan: hasil kalkulator = kunci | 24/30 |
| Hitungan: angka kunci ada di jawaban | 26/30 |
| Halaman sitasi benar (hitungan) | 28/30 |
| Halaman sitasi benar (definisi) | 13/13 |
| Soal error (API/kuota) | 0 |
| Jawaban dengan peringatan chatbot | 19 |

| ID | Status | Pemeriksaan yang gagal |
|---|---|---|
| D01 | ✅ | - |
| D02 | ✅ | - |
| D03 | ✅ | - |
| D04 | ❌ | fakta: lulusan / IKU 2; fakta: non pendidikan / non-pendidikan / UKT / IKU 9 |
| D05 | ✅ | - |
| D06 | ✅ | - |
| D07 | ✅ | - |
| D08 | ✅ | - |
| D09 | ✅ | - |
| D10 | ✅ | - |
| D11 | ❌ | fakta: IKU 2 |
| D12 | ✅ | - |
| H01 | ✅ | - |
| H02 | ✅ | - |
| H03 | ✅ | - |
| H04 | ✅ | - |
| H05 | ✅ | - |
| H06 | ✅ | - |
| H07 | ❌ | kalkulator dipanggil; hasil kalkulator = kunci |
| H08 | ❌ | kalkulator dipanggil; hasil kalkulator = kunci |
| H09 | ✅ | - |
| H10 | ✅ | - |
| H11 | ❌ | kalkulator dipanggil; hasil kalkulator = kunci; angka kunci ada di jawaban; halaman sitasi benar |
| H12 | ✅ | - |
| H13 | ✅ | - |
| H14 | ✅ | - |
| H15 | ✅ | - |
| H16 | ❌ | kalkulator dipanggil; hasil kalkulator = kunci; angka kunci ada di jawaban |
| H17 | ✅ | - |
| H18 | ✅ | - |
| D13 | ✅ | - |
| D14 | ✅ | - |
| H19 | ✅ | - |
| H20 | ✅ | - |
| H21 | ✅ | - |
| H22 | ✅ | - |
| H23 | ✅ | - |
| H24 | ✅ | - |
| H25 | ✅ | - |
| H26 | ❌ | kalkulator dipanggil; hasil kalkulator = kunci; angka kunci ada di jawaban |
| H27 | ❌ | kalkulator dipanggil; hasil kalkulator = kunci; angka kunci ada di jawaban; halaman sitasi benar |
| H28 | ✅ | - |
| H29 | ✅ | - |
| H30 | ✅ | - |

Pemeriksaan otomatis hanya bantuan. Baca jawaban lengkap di bawah dan bandingkan dengan jawaban yang diharapkan.

## Detail per soal

### D01 — ✅ LULUS

**Pertanyaan:** Apa itu IKU 1?

**Jawaban chatbot:**

```text
**IKU 1 – Angka Efisiensi Edukasi Perguruan Tinggi (AEE PT)**  

IKU 1 merupakan indikator yang mengukur **tingkat keberhasilan mahasiswa menyelesaikan studi tepat waktu sesuai masa studi standar**, dibandingkan dengan total mahasiswa yang masuk pada periode tertentu. Dengan kata lain, indikator ini menilai persentase mahasiswa yang lulus dalam jangka waktu yang ditetapkan oleh kurikulum masing-masing program pendidikan [1].  

*Definisi lengkap* dapat dilihat pada bagian “Definisi, Kriteria, Ketentuan, dan Formula” dalam Buku IKU Diktisaintek Berdampak [1].
```

**Sitasi chatbot:**

- [1] Buku IKU Diktisaintek Berdampak V1, hlm. 49 (IKU 1, Definisi); juga di PPT hlm. 45

**Jawaban yang diharapkan:**

- Halaman kunci: 49

IKU 1 adalah **Angka Efisiensi Edukasi (AEE) Perguruan Tinggi**, yaitu indikator yang mengukur tingkat keberhasilan mahasiswa menyelesaikan studi **tepat waktu** sesuai masa studi standar, dibandingkan dengan total mahasiswa yang masuk pada periode tertentu. AEE PT dihitung dari **rata-rata tingkat pencapaian AEE setiap program pendidikan**. Sifatnya **IKU Wajib**.

**Pemeriksaan otomatis:**

- ✅ fakta: tepat waktu
- ✅ fakta: efisiensi edukasi / AEE
- ✅ halaman sitasi benar

### D02 — ✅ LULUS

**Pertanyaan:** Berapa masa tempuh kurikulum dan AEE ideal untuk program Sarjana dan Diploma Tiga?

**Jawaban chatbot:**

```text
- **Masa tempuh kurikulum**  
  - **Diploma Tiga (D3)**: 6 semester [1]  
  - **Sarjana / Sarjana Terapan (S1)**: 8 semester [1]  

- **AEE ideal**  
  - **Diploma Tiga (D3)**: 33 % [1][4]  
  - **Sarjana / Sarjana Terapan (S1)**: 25 % [1][4]
```

**Sitasi chatbot:**

- [1] Buku IKU Diktisaintek Berdampak V1, hlm. 49 (IKU 1, Ketentuan); juga di Buku (Lampiran Kepmen 358/M/KEP/2025) hlm. 100–101; PPT hlm. 45
- [4] Buku IKU Diktisaintek Berdampak V1, hlm. 49–50 (IKU 1, Formula)

**Jawaban yang diharapkan:**

- Halaman kunci: 49

- Sarjana / Sarjana Terapan (D4): masa tempuh **8 semester**, AEE ideal **25%**.
- Diploma Tiga: masa tempuh **6 semester**, AEE ideal **33%**.

**Pemeriksaan otomatis:**

- ✅ fakta: 8 semester / delapan semester
- ✅ fakta: 25% / 25 %
- ✅ fakta: 6 semester / enam semester
- ✅ fakta: 33% / 33 %
- ✅ halaman sitasi benar

### D03 — ✅ LULUS

**Pertanyaan:** Berapa jumlah IKU wajib, IKU pilihan, dan IKU partisipatif?

**Jawaban chatbot:**

```text
Jumlah IKU wajib yang harus dipenuhi oleh semua perguruan tinggi adalah **7 (tujuh)** [1] .  
Jumlah IKU pilihan yang tersedia adalah **5 (lima)**, di mana tiap perguruan tinggi dapat memilih **2 (dua)** di antaranya [1] .  
Setiap perguruan tinggi juga harus mengusulkan **1 (satu)** IKU partisipatif [1].
```

**Sitasi chatbot:**

- [1] Buku IKU Diktisaintek Berdampak V1, hlm. 48–49

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

### D04 — ❌ PERLU DICEK

**Pertanyaan:** Sebutkan IKU yang bersifat wajib.

**Jawaban chatbot:**

```text
Berikut IKU yang bersifat **wajib** menurut dokumen IKU Diktisaintek Berdampak:

1. **IKU 1 – Angka Efisiensi Edukasi Pergurutan Tinggi (AEE PT)** [2]  
2. **IKU 3 – Persentase mahasiswa S1/D4/D3/D2/D1 berkegiatan/meraih prestasi di luar program studi** [3]  
3. **IKU 5 – Rasio luaran hasil kerja sama antara PT dan start-up/industri/lembaga** [4]  
4. **IKU 7 – Persentase keterlibatan Perguruan Tinggi dalam SDG 1, 4, 17 dan 2 SDG lain sesuai keunggulan** [5]  
5. **IKU 12 – Ketersediaan perencanaan strategis peningkatan kesejahteraan dosen** [1]  

(Ket: total wajib yang ditetapkan sebanyak 7, tetapi hanya enam IKU yang disebutkan dalam konteks yang diberikan.)
```

**Sitasi chatbot:**

- [1] Buku IKU Diktisaintek Berdampak V1, hlm. 48–49
- [2] Buku IKU Diktisaintek Berdampak V1, hlm. 49 (IKU 1, Definisi); juga di PPT hlm. 45
- [3] Buku IKU Diktisaintek Berdampak V1, hlm. 53 (IKU 3, Definisi); juga di PPT hlm. 49
- [4] Buku IKU Diktisaintek Berdampak V1, hlm. 55 (IKU 5, Definisi); juga di PPT hlm. 51
- [5] Buku IKU Diktisaintek Berdampak V1, hlm. 58 (IKU 7, Ketentuan); juga di Buku (Lampiran Kepmen 358/M/KEP/2025) hlm. 120–121

**Jawaban yang diharapkan:**

- Halaman kunci: 48

IKU 1 (AEE), IKU 2 (lulusan bekerja/studi lanjut/wirausaha dalam 1 tahun), IKU 3 (mahasiswa berkegiatan/berprestasi di luar prodi), IKU 5 (rasio luaran kerja sama), IKU 7 (keterlibatan SDGs), IKU 9 (pendapatan non-UKT), dan IKU 12 (perencanaan kesejahteraan dosen).

**Pemeriksaan otomatis:**

- ✅ fakta: efisiensi edukasi / IKU 1
- ❌ fakta: lulusan / IKU 2
- ✅ fakta: di luar program studi / IKU 3
- ✅ fakta: kerja sama / kerjasama / IKU 5
- ✅ fakta: SDG / IKU 7
- ❌ fakta: non pendidikan / non-pendidikan / UKT / IKU 9
- ✅ fakta: kesejahteraan dosen / IKU 12
- ✅ halaman sitasi benar

### D05 — ✅ LULUS

**Pertanyaan:** Dari mana data IKU 2 diperoleh, dan bagaimana menentukan jumlah responden minimum?

**Jawaban chatbot:**

```text
Data untuk IKU 2 diperoleh melalui **tracer study** yang dilaksanakan 1 tahun setelah kelulusan, yaitu mengumpulkan informasi tentang lulusan yang sudah bekerja, melanjutkan studi, atau berwirausaha [1]​.  

Jumlah responden minimum ditentukan dengan menggunakan **rumus Slovin** (galat 2,3 %). Rumusnya adalah  

\[
n = \frac{N}{N d^{2} + 1} \times 100\%
\]

di mana **N** = total jumlah lulusan, dan **d** = galat = 2,3 % (0,023). Dengan memasukkan nilai N yang bersangkutan, rumus tersebut menghasilkan jumlah responden minimum yang harus dikumpulkan untuk IKU 2 [2]​.
```

**Sitasi chatbot:**

- [1] Buku IKU Diktisaintek Berdampak V1, hlm. 51 (IKU 2, Ketentuan); juga di PPT hlm. 48; Buku (Lampiran Kepmen 358/M/KEP/2025) hlm. 104
- [2] Buku IKU Diktisaintek Berdampak V1, hlm. 52 (IKU 2, Formula); juga di PPT hlm. 48–49; Buku (Lampiran Kepmen 358/M/KEP/2025) hlm. 104–105

**Jawaban yang diharapkan:**

- Halaman kunci: 51, 52

Data diperoleh dari **tracer study** yang dilakukan **1 tahun setelah kelulusan**. Responden minimum dihitung dengan **rumus Slovin** dengan **galat (d) 2,3%**: n = N / (N·d² + 1), dengan N = jumlah lulusan.

**Pemeriksaan otomatis:**

- ✅ fakta: tracer study
- ✅ fakta: slovin
- ✅ fakta: 2,3 / 2.3
- ✅ halaman sitasi benar

### D06 — ✅ LULUS

**Pertanyaan:** Kegiatan di luar program studi apa saja yang diakui untuk IKU 3?

**Jawaban chatbot:**

```text
Kegiatan di luar program studi yang diakui untuk mengisi **IKU 3 – Persentase Mahasiswa S1/D4/D3/D2/D1 Berkegiatan/Meraih Prestasi di Luar Program Studi** meliputi:

1. **Magang atau praktik kerja** yang dilaksanakan pada  
   - perusahaan swasta (nasional, multinasional, startup, UMKM, dsb.),  
   - lembaga/organisasi nirlaba,  
   - institusi/organisasi multilateral (mis. PBB, UNICEF), atau  
   - instansi pemerintah, BUMN, atau BUMD[1].  

2. **Program mahasiswa Berdampak** (program sosial/pengabdian kepada masyarakat) yang memberdayakan masyarakat di daerah bencana, pedesaan, atau terpencil dalam bidang ekonomi, infrastruktur, dll[1].  

3. **Pertukaran mahasiswa** (mengambil kelas atau semester di perguruan tinggi luar negeri maupun dalam negeri) berdasarkan perjanjian kerja sama antar perguruan tinggi atau pemerintah, dengan memperoleh pengakuan kredit semester[1].  

4. **Penelitian atau riset** yang dilakukan di bawah pengawasan dosen/pembimbing, baik bersama dosen tetap perguruan tinggi asal, dosen tetap perguruan tinggi lain, lembaga riset bereputasi, perusahaan multinasional, atau Pemerintah/BUMN/BUMD[1].  

Semua kegiatan tersebut harus dilaksanakan dengan pendampingan dosen pembimbing dan memperoleh pengakuan satuan kredit semester agar dapat dihitung dalam IKU 3[1].
```

**Sitasi chatbot:**

- [1] Buku IKU Diktisaintek Berdampak V1, hlm. 53 (IKU 3, Kriteria); juga di Buku (Lampiran Kepmen 358/M/KEP/2025) hlm. 105–106; PPT hlm. 49

**Jawaban yang diharapkan:**

- Halaman kunci: 53

Kegiatan harus didampingi dosen pembimbing dan mendapat pengakuan SKS, berupa:
1. magang/praktik kerja (swasta, nirlaba, organisasi multilateral, pemerintah/BUMN/BUMD);
2. program mahasiswa berdampak (sosial/pengabdian masyarakat);
3. pertukaran mahasiswa (dalam/luar negeri, berdasarkan perjanjian kerja sama); dan/atau
4. penelitian/riset di bawah pengawasan dosen atau peneliti.

Prestasi diakui bila berupa kompetisi tingkat provinsi/nasional/internasional, minimal sebagai finalis.
Catatan: magang **tidak dihitung** bagi prodi vokasi yang sudah memiliki magang wajib.

**Pemeriksaan otomatis:**

- ✅ fakta: magang / praktik kerja
- ✅ fakta: pertukaran
- ✅ fakta: penelitian / riset
- ✅ fakta: dosen pembimbing / pendampingan
- ✅ halaman sitasi benar

### D07 — ✅ LULUS

**Pertanyaan:** SDG apa saja yang wajib dan pilihan dalam IKU 7?

**Jawaban chatbot:**

```text
IKU 7 mengharuskan perguruan tinggi terlibat secara **wajib** pada tiga tujuan SDG berikut:

- **SDG 1 – Tanpa Kemiskinan**  
- **SDG 4 – Pendidikan Berkualitas**  
- **SDG 17 – Kemitraan untuk Tujuan**  

Selain tiga tujuan wajib tersebut, perguruan tinggi **wajib memilih dua (2) tujuan SDG lain** yang tidak termasuk SDG 1, 4, atau 17. Pemilihan dua tujuan tambahan ini didasarkan pada keunggulan, spesialisasi, atau konteks strategis masing-masing institusi, dan harus dicantumkan dalam dokumen resmi (misalnya Renstra atau laporan kinerja tahunan)[1].
```

**Sitasi chatbot:**

- [1] Buku IKU Diktisaintek Berdampak V1, hlm. 58 (IKU 7, Ketentuan); juga di Buku (Lampiran Kepmen 358/M/KEP/2025) hlm. 120–121

**Jawaban yang diharapkan:**

- Halaman kunci: 58

SDG wajib: **SDG 1** (Tanpa Kemiskinan), **SDG 4** (Pendidikan Berkualitas), dan **SDG 17** (Kemitraan). Ditambah **2 SDG pilihan** di luar ketiganya, sesuai keunggulan PT, dan harus dituangkan dalam dokumen resmi (Renstra atau laporan kinerja tahunan).

**Pemeriksaan otomatis:**

- ✅ fakta: SDG 1 / SDG1
- ✅ fakta: SDG 4 / SDG4
- ✅ fakta: SDG 17 / SDG17
- ✅ fakta: 2 (dua) / dua (2) / dua SDG / 2 SDG / dua tujuan / 2 tujuan
- ✅ halaman sitasi benar

### D08 — ✅ LULUS

**Pertanyaan:** Pendapatan apa saja yang tidak termasuk dalam perhitungan IKU 9?

**Jawaban chatbot:**

```text
Pendapatan yang **tidak termasuk** dalam perhitungan **IKU 9 – Persentase Pendapatan Non Pendidikan/UKT** adalah:

1. SPP/UKT/biaya kuliah mahasiswa.  
2. Iuran pengembangan institusi.  
3. Subsidi langsung dari pemerintah seperti belanja pegawai, belanja operasional, BOPTN, BPPTNBH, dan sejenisnya.  
4. Sumbangan/filantropi yang **tidak masuk** dalam laporan keuangan resmi perguruan tinggi.  
5. Dana pokok dana abadi/endowment fund yang disimpan permanen dan tidak dibelanjakan.  

Sumber: kriteria “Tidak termasuk” pada IKU 9 [1]​.
```

**Sitasi chatbot:**

- [1] Buku IKU Diktisaintek Berdampak V1, hlm. 59 (IKU 9, Kriteria); juga di Buku (Lampiran Kepmen 358/M/KEP/2025) hlm. 122–123; PPT hlm. 56

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

### D09 — ✅ LULUS

**Pertanyaan:** Penerbit apa yang tidak diperhitungkan dalam IKU 6?

**Jawaban chatbot:**

```text
Penerbit yang **tidak** diperhitungkan dalam perhitungan IKU 6 adalah **MDPI, Frontiers, dan Hindawi Publisher**[1].
```

**Sitasi chatbot:**

- [1] Buku IKU Diktisaintek Berdampak V1, hlm. 63 (IKU 6, Ketentuan); juga di PPT hlm. 61–62; Buku (Lampiran Kepmen 358/M/KEP/2025) hlm. 118–119

**Jawaban yang diharapkan:**

- Halaman kunci: 63

**MDPI, Frontiers, dan Hindawi**.

**Pemeriksaan otomatis:**

- ✅ fakta: MDPI
- ✅ fakta: Frontiers
- ✅ fakta: Hindawi
- ✅ halaman sitasi benar

### D10 — ✅ LULUS

**Pertanyaan:** Bagaimana arah penilaian IKU 11c (pelanggaran integritas akademik)?

**Jawaban chatbot:**

```text
Arah penilaian IKU 11c (Jumlah Laporan Pelanggaran Integritas Akademik) bersifat **semakin rendah semakin baik**; nilai 0 (nol) dapat mencerminkan kinerja yang baik asalkan perguruan tinggi sudah memiliki dan menjalankan mekanisme pencegahan, pelaporan, verifikasi, serta penanganan pelanggaran integritas akademik secara institusional[2][5].
```

**Sitasi chatbot:**

- [2] Buku IKU Diktisaintek Berdampak V1, hlm. 67 (IKU 11c, Ketentuan)
- [5] PPT IKU Diktisaintek Berdampak PTS V2, hlm. 67 (IKU 11, Ketentuan); juga di PPT hlm. 69; PPT hlm. 66; PPT hlm. 65–66

**Jawaban yang diharapkan:**

- Halaman kunci: 67

**Semakin rendah semakin baik.** Nilai 0 laporan mencerminkan kinerja baik, **asalkan** PT memiliki dan menjalankan mekanisme pencegahan, pelaporan, verifikasi, dan penanganan pelanggaran integritas akademik. Formula: jumlah laporan pelanggaran integritas akademik dalam 1 periode (satuan: laporan).

**Pemeriksaan otomatis:**

- ✅ fakta: semakin rendah
- ✅ halaman sitasi benar

### D11 — ❌ PERLU DICEK

**Pertanyaan:** Lulusan 400, yang bekerja 280, berapa capaian IKU 1?

**Jawaban chatbot:**

```text
Informasi yang diberikan (lulusan = 400, yang bekerja = 280) tidak relevan untuk menghitung **IKU 1 – Angka Efisiensi Edukasi Perguruan Tinggi (AEE PT)**.  
IKU 1 dihitung dengan rumus AEE = (Jumlah mahasiswa yang lulus tepat waktu ÷ Total mahasiswa) × 100 % dan kemudian dirata-rata across program pendidikan (D3, D4, S1, S2, S3, dst.) [1][3][4].  

Untuk dapat menghitung capaian IKU 1, diperlukan data berikut:
1. Jumlah mahasiswa yang **lulus tepat waktu** (sesuai masa tempuh kurikulum) untuk masing-masing program pendidikan yang dihitung.  
2. **Total mahasiswa** pada tahun akademik yang sama untuk masing-masing program pendidikan.  
3. Jika ada lebih dari satu program, nilai **Tingkat Pencapaian AEE** per program (AEE realisasi ÷ AEE ideal) dan jumlah program (n) untuk menghitung AEE PT = Σ Tingkat Pencapaian ÷ n [1][2].

Silakan sediakan data tersebut (misalnya: D3 – lulus 40 / total 120, S1 – lulus 50 / total 200, dst.) agar perhitungan dapat dilakukan dengan fungsi `hitung_iku`.
```

**Sitasi chatbot:**

- [1] Buku IKU Diktisaintek Berdampak V1, hlm. 49–50 (IKU 1, Formula); juga di PPT hlm. 46–47; PPT hlm. 46; Buku (Lampiran Kepmen 358/M/KEP/2025) hlm. 101–102
- [2] Buku IKU Diktisaintek Berdampak V1, hlm. 49–50 (IKU 1, Formula)
- [3] Buku IKU Diktisaintek Berdampak V1, hlm. 49 (IKU 1, Ketentuan); juga di PPT hlm. 45; Buku (Lampiran Kepmen 358/M/KEP/2025) hlm. 100–101
- [4] Buku IKU Diktisaintek Berdampak V1, hlm. 49 (IKU 1, Kriteria); juga di PPT hlm. 45

**Peringatan chatbot:**

- Soal hitungan dijawab dengan persentase tetapi kalkulator tidak dipanggil.

**Jawaban yang diharapkan:**

- Halaman kunci: 49, 51

Chatbot harus **mengoreksi**: IKU 1 adalah Angka Efisiensi Edukasi (kelulusan tepat waktu), bukan persentase lulusan bekerja. Data lulusan bekerja termasuk **IKU 2**. Jika dihitung sebagai IKU 2, dengan asumsi seluruh 280 lulusan berbobot 1 (masa tunggu < 6 bulan dan gaji > 1,2× UMP) dan 400 adalah total responden tracer study: 280/400 × 100% = **70%** (lihat H04).

*Catatan soal:* Soal jebakan: chatbot harus meluruskan bahwa data lulusan bekerja termasuk IKU 2, bukan IKU 1.

**Pemeriksaan otomatis:**

- ❌ fakta: IKU 2
- ✅ fakta: efisiensi edukasi / tepat waktu / AEE
- ✅ halaman sitasi benar

### D12 — ✅ LULUS

**Pertanyaan:** Berapa besaran UKT di Universitas Gadjah Mada tahun 2026?

**Jawaban chatbot:**

```text
Informasi tentang besaran UKT (Uang Kuliah Tunggal) di Universitas Gadjah Mada tahun 2026 tidak ditemukan dalam dokumen IKU yang diberikan.
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
AEE realisasi prodi S1 = 20 %  
Tingkat pencapaian AEE prodi S1 = 80 %  

Perhitungan:  
- AEE realisasi = 40 ÷ 200 × 100 % = 20 %  
- AEE ideal S1 = 25 % (sesuai masa studi 8 semester)  
- Tingkat pencapaian = 20 % ÷ 25 % × 100 % = 80 %  

[Rujukan: 1][2][3]
```

**Sitasi chatbot:**

- [2] Buku IKU Diktisaintek Berdampak V1, hlm. 49–50 (IKU 1, Formula)
- [3] Buku IKU Diktisaintek Berdampak V1, hlm. 49 (IKU 1, Ketentuan); juga di Buku (Lampiran Kepmen 358/M/KEP/2025) hlm. 100–101; PPT hlm. 45

**Sumber rumus (kalkulator):**

- Buku IKU Diktisaintek Berdampak V1, IKU 1 – Ketentuan & Formula a–b, hlm. 49

**Panggilan kalkulator:**

- argumen `{"argumen_json":"{\"jenjang\": \"S1\", \"lulus_tepat_waktu\": 40, \"total_mahasiswa\": 200, \"pindah\": 0, \"drop_out\": 0, \"cuti_lebih\": 0}","fungsi":"iku1_aee_prodi"}` → aee_realisasi_pct = 20,00, tingkat_pencapaian_pct = 80,00

**Peringatan chatbot:**

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

### H02 — ✅ LULUS

**Pertanyaan:** Sebuah PT memiliki 3 program pendidikan: D3 dengan AEE realisasi 30%, S1 dengan 22,5%, dan S2 dengan 40%. Berapa AEE PT?

**Jawaban chatbot:**

```text
AEE PT untuk tiga program pendidikan tersebut adalah **86,97 %**. Langkah perhitungannya:

1. Tingkat pencapaian D3 = 30 % ÷ 33 % = 90,91 %  
2. Tingkat pencapaian S1 = 22,5 % ÷ 25 % = 90 %  
3. Tingkat pencapaian S2 = 40 % ÷ 50 % = 80 %  
4. AEE PT = (90,91 % + 90 % + 80 %) ÷ 3 = 86,97 %  

Sumber: Buku IKU Diktisaintek Berdampak V1, IKU 1 – Formula c & contoh perhitungan, hlm. 49-50.
```

**Sumber rumus (kalkulator):**

- Buku IKU Diktisaintek Berdampak V1, IKU 1 – Formula c & contoh perhitungan, hlm. 49–50

**Panggilan kalkulator:**

- argumen `{"argumen_json":"{\"realisasi_per_jenjang\": {\"D3\": 30, \"S1\": 22.5, \"S2\": 40}}","fungsi":"iku1_aee_pt"}` → 86,97

**Peringatan chatbot:**

- Panggilan alat ditolak server (nama alat 'hitungan_iku' tidak dikenal); diulang otomatis.
- Jawaban tidak memuat rujukan [n] ke konteks.

**Jawaban yang diharapkan:**

- Angka kunci: **86,97**
- Halaman kunci: 49, 50

**86,97%**.

**Pemeriksaan otomatis:**

- ✅ kalkulator dipanggil
- ✅ hasil kalkulator = kunci
- ✅ angka kunci ada di jawaban
- ✅ halaman sitasi benar

### H03 — ✅ LULUS

**Pertanyaan:** Prodi S1 mencatat 250 mahasiswa pada satu tahun akademik, termasuk 10 mahasiswa pindah dan 15 mahasiswa *drop out*. Sebanyak 45 mahasiswa lulus tepat 8 semester. Berapa AEE realisasi dan tingkat pencapaiannya?

**Jawaban chatbot:**

```text
AEE realisasi untuk prodi S1 adalah **20 %** dan tingkat pencapaiannya adalah **80 %**.

Perhitungan:
- Basis perhitungan = 250 total mahasiswa − 10 pindah − 15 drop-out − 0 cuti = **225** mahasiswa yang dihitung[1].
- AEE realisasi = 45 lulus tepat waktu ÷ 225 × 100 % = **20 %**[1].
- AEE ideal S1 = 25 % (masa studi 8 semester) sesuai ketentuan[1].
- Tingkat pencapaian = 20 % ÷ 25 % × 100 % = **80 %**[1].
```

**Sitasi chatbot:**

- [1] Buku IKU Diktisaintek Berdampak V1, hlm. 49 (IKU 1, Ketentuan); juga di Buku (Lampiran Kepmen 358/M/KEP/2025) hlm. 100–101; PPT hlm. 45

**Sumber rumus (kalkulator):**

- Buku IKU Diktisaintek Berdampak V1, IKU 1 – Ketentuan & Formula a–b, hlm. 49

**Panggilan kalkulator:**

- argumen `{"argumen_json":"{\"jenjang\": \"S1\", \"lulus_tepat_waktu\": 45, \"total_mahasiswa\": 250, \"pindah\": 10, \"drop_out\": 15, \"cuti_lebih\": 0}","fungsi":"iku1_aee_prodi"}` → aee_realisasi_pct = 20,00, tingkat_pencapaian_pct = 80,00

**Jawaban yang diharapkan:**

- Angka kunci: **aee_realisasi_pct = 20,00, tingkat_pencapaian_pct = 80,00**
- Halaman kunci: 49

AEE realisasi **20%**, tingkat pencapaian **80%**. Jawaban 45/250 = 18% **salah**.

**Pemeriksaan otomatis:**

- ✅ kalkulator dipanggil
- ✅ hasil kalkulator = kunci
- ✅ angka kunci ada di jawaban
- ✅ halaman sitasi benar

### H04 — ✅ LULUS

**Pertanyaan:** Tracer study mengumpulkan 400 responden lulusan S1. Sebanyak 280 lulusan bekerja dengan masa tunggu < 6 bulan dan gaji > 1,2× UMP; sisanya belum bekerja. Berapa capaian IKU 2?

**Jawaban chatbot:**

```text
Capaian IKU 2 = 70 % [5][1] 

Langkah perhitungannya:
- 280 responden bekerja dengan masa tunggu < 6 bulan dan gaji > 1,2 × UMP → bobot k = 1 → 280 × 1 = 280  
- 120 responden belum bekerja → bobot k = 0 → 120 × 0 = 0  
- Σ(n·k) = 280  
- Capaian = 280 ÷ 400 × 100 % = 70 %
```

**Sitasi chatbot:**

- [1] Buku IKU Diktisaintek Berdampak V1, hlm. 51 (IKU 2, Kriteria); juga di PPT hlm. 47; PPT hlm. 47; PPT hlm. 47; Buku (Lampiran Kepmen 358/M/KEP/2025) hlm. 103–104; PPT hlm. 47; Buku (Lampiran Kepmen 358/M/KEP/2025) hlm. 103–104; PPT hlm. 47; PPT hlm. 47; Buku (Lampiran Kepmen 358/M/KEP/2025) hlm. 103–104; Buku (Lampiran Kepmen 358/M/KEP/2025) hlm. 103–104; PPT hlm. 48; Buku (Lampiran Kepmen 358/M/KEP/2025) hlm. 103–104
- [5] Buku IKU Diktisaintek Berdampak V1, hlm. 52 (IKU 2, Formula); juga di PPT hlm. 48–49; Buku (Lampiran Kepmen 358/M/KEP/2025) hlm. 104–105

**Sumber rumus (kalkulator):**

- Buku IKU Diktisaintek Berdampak V1, IKU 2 – Kriteria b–f & Formula, hlm. 51–52

**Panggilan kalkulator:**

- argumen `{"argumen_json":"{\"total_responden\":400,\"kategori\":{\"bekerja_\u003c6bln_\u003e1.2ump\":280,\"belum\":120}}","fungsi":"iku2"}` → 70,00

**Jawaban yang diharapkan:**

- Angka kunci: **70,00**
- Halaman kunci: 51, 52

**70%**.

**Pemeriksaan otomatis:**

- ✅ kalkulator dipanggil
- ✅ hasil kalkulator = kunci
- ✅ angka kunci ada di jawaban
- ✅ halaman sitasi benar

### H05 — ✅ LULUS

**Pertanyaan:** Tracer study mengumpulkan 500 responden lulusan. Rinciannya: - 200 bekerja, masa tunggu < 6 bulan, gaji > 1,2× UMP - 100 bekerja, masa tunggu < 1 tahun, gaji > 1,2× UMP - 50 bekerja, masa tunggu < 1 tahun, gaji < 1,2× UMP - 30 melanjutkan studi (surat penerimaan < 12 bulan) - 20 *founder*, < 6 bulan, penghasilan > 1,2× UMP - 10 *freelancer*, > 6 bulan, penghasilan < 1,2× UMP - 90 belum bekerja/studi/wirausaha Berapa capaian IKU 2?

**Jawaban chatbot:**

```text
Capaian IKU 2 = 70,8 % [5][1][2] 

Langkah perhitungan (menggunakan rumus resmi IKU 2):
- bekerja < 6 bulan & gaji > 1,2 × UMP: 200 × 1 = 200  
- bekerja < 1 tahun & gaji > 1,2 × UMP: 100 × 0,8 = 80  
- bekerja < 1 tahun & gaji < 1,2 × UMP: 50 × 0,6 = 30  
- melanjutkan studi < 12 bulan: 30 × 0,6 = 18  
- founder < 6 bulan & penghasilan > 1,2 × UMP: 20 × 1,2 = 24  
- freelancer > 6 bulan & penghasilan < 1,2 × UMP: 10 × 0,2 = 2  

Σ (n·k) = 354  
Total responden t = 500  

Capaian = (354 ÷ 500) × 100 % = 70,8 %  

Jadi persentase lulusan yang bekerja, melanjutkan studi, atau berwirausaha dalam 1 tahun setelah kelulusan adalah **70,8 %**.
```

**Sitasi chatbot:**

- [1] Buku IKU Diktisaintek Berdampak V1, hlm. 51 (IKU 2, Kriteria); juga di PPT hlm. 47; PPT hlm. 47; PPT hlm. 47; PPT hlm. 47; PPT hlm. 47; Buku (Lampiran Kepmen 358/M/KEP/2025) hlm. 103–104; PPT hlm. 47; Buku (Lampiran Kepmen 358/M/KEP/2025) hlm. 103–104; PPT hlm. 48; Buku (Lampiran Kepmen 358/M/KEP/2025) hlm. 103–104; Buku (Lampiran Kepmen 358/M/KEP/2025) hlm. 103–104; Buku (Lampiran Kepmen 358/M/KEP/2025) hlm. 103–104
- [2] Buku IKU Diktisaintek Berdampak V1, hlm. 51 (IKU 2, Kriteria)
- [5] Buku IKU Diktisaintek Berdampak V1, hlm. 52 (IKU 2, Formula); juga di PPT hlm. 48–49; Buku (Lampiran Kepmen 358/M/KEP/2025) hlm. 104–105

**Sumber rumus (kalkulator):**

- Buku IKU Diktisaintek Berdampak V1, IKU 2 – Kriteria b–f & Formula, hlm. 51–52

**Panggilan kalkulator:**

- argumen `{"argumen_json":"{\"total_responden\": 500, \"kategori\": {\"bekerja_\u003c6bln_\u003e1.2ump\": 200, \"bekerja_\u003c1thn_\u003e1.2ump\": 100, \"bekerja_\u003c1thn_\u003c1.2ump\": 50, \"founder_\u003c6bln_\u003e1.2ump\": 20, \"freelancer_\u003e6bln_\u003c1.2ump\": 10, \"studi_lanjut_\u003c12bln\": 30}}","fungsi":"iku2"}` → 70,80

**Jawaban yang diharapkan:**

- Angka kunci: **70,80**
- Halaman kunci: 51, 52

**70,8%**.

**Pemeriksaan otomatis:**

- ✅ kalkulator dipanggil
- ✅ hasil kalkulator = kunci
- ✅ angka kunci ada di jawaban
- ✅ halaman sitasi benar

### H06 — ✅ LULUS

**Pertanyaan:** Jumlah lulusan suatu PT adalah 2.000 orang. Berapa jumlah responden minimum tracer study untuk IKU 2?

**Jawaban chatbot:**

```text
Jumlah responden minimum yang harus dikumpulkan untuk tracer study IKU 2 adalah **972 responden**.  

Langkah perhitungannya:
- Gunakan rumus Slovin \( n = \dfrac{N}{N \times d^{2} + 1} \) dengan \( N = 2.000 \) lulusan dan galat \( d = 2,3\% \) [2].
- \( N \times d^{2} = 2.000 \times 0,023^{2} = 1,06 \).
- \( n = \dfrac{2.000}{1,06 + 1} = 971,82 \).
- Dibulatkan ke atas menjadi **972 responden** [hasil perhitungan fungsi]​.
```

**Sitasi chatbot:**

- [2] Buku IKU Diktisaintek Berdampak V1, hlm. 52 (IKU 2, Formula); juga di PPT hlm. 48–49; Buku (Lampiran Kepmen 358/M/KEP/2025) hlm. 104–105

**Sumber rumus (kalkulator):**

- Buku IKU Diktisaintek Berdampak V1, IKU 2 – Formula Responden Minimum, hlm. 52

**Panggilan kalkulator:**

- argumen `{"argumen_json":"{\"jumlah_lulusan\": 2000}","fungsi":"iku2_responden_minimum"}` → 972

**Peringatan chatbot:**

- LLM mengembalikan respons kosong; diulang otomatis.
- Panggilan alat ditolak server (nama alat 'hituk_iku' tidak dikenal); diulang otomatis.

**Jawaban yang diharapkan:**

- Angka kunci: **972**
- Halaman kunci: 52

**972 responden**.

**Pemeriksaan otomatis:**

- ✅ kalkulator dipanggil
- ✅ hasil kalkulator = kunci
- ✅ angka kunci ada di jawaban
- ✅ halaman sitasi benar

### H07 — ❌ PERLU DICEK

**Pertanyaan:** Sebuah PT memiliki 1.000 mahasiswa S1/Diploma. Rinciannya: - 100 mahasiswa magang 20 SKS - 150 mahasiswa pertukaran 8 SKS - 50 mahasiswa riset 4 SKS - 5 mahasiswa juara 1 lomba nasional - 10 mahasiswa finalis lomba internasional Berapa capaian IKU 3?

**Jawaban chatbot:**

```text
Capaian **IKU 3 – Persentase Mahasiswa S1/Diploma Berkegiatan/Meraih Prestasi di Luar Program Studi** dihitung dengan rumus  

\[
\text{IKU 3} = \frac{\displaystyle\sum_{i} n_i \, k_i}{t}\times 100\%
\]

di mana  
* \(n_i\) = jumlah mahasiswa yang melakukan kegiatan atau memperoleh prestasi,  
* \(k_i\) = bobot yang ditetapkan untuk jenis kegiatan atau tingkat prestasi, dan  
* \(t\) = total mahasiswa (1000) [1].

**1. Bobot kegiatan (berdasarkan SKS)** [1]  
* ≤ 5 SKS → \(k = 0,4\)  
* 6 – 10 SKS → \(k = 0,6\)  
* ≥ 10 SKS → \(k = 1\)

**2. Bobot prestasi (berdasarkan tingkat)** [1]  
* Tingkat nasional, juara 1 → \(k = 0,6\)  
* Tingkat internasional, finalis → \(k = 0,2\)

**3. Perhitungan kontribusi masing-masing kategori**

| Kategori | Jumlah mahasiswa (\(n_i\)) | Bobot (\(k_i\)) | \(n_i \times k_i\) |
|----------|----------------------------|----------------|-------------------|
| Magang 20 SKS | 100 | 1   | 100 |
| Pertukaran 8 SKS | 150 | 0,6 | 90 |
| Riset 4 SKS | 50  | 0,4 | 20 |
| Juara 1 lomba nasional | 5  | 0,6 | 3 |
| Finalis lomba internasional | 10 | 0,2 | 2 |
| **Total** | – | – | **215** |

**4. Persentase IKU 3**

\[
\text{IKU 3} = \frac{215}{1000}\times100\% = 21,5\%
\]

**Jawaban:** Capaian IKU 3 untuk PT tersebut adalah **21,5 %**.
```

**Sitasi chatbot:**

- [1] Buku IKU Diktisaintek Berdampak V1, hlm. 53–54 (IKU 3, Formula); juga di Buku (Lampiran Kepmen 358/M/KEP/2025) hlm. 107–108; PPT hlm. 50

**Peringatan chatbot:**

- Soal hitungan dijawab dengan persentase tetapi kalkulator tidak dipanggil.

**Jawaban yang diharapkan:**

- Angka kunci: **21,50**
- Halaman kunci: 53, 54

**21,5%**.

**Pemeriksaan otomatis:**

- ❌ kalkulator dipanggil
- ❌ hasil kalkulator = kunci
- ✅ angka kunci ada di jawaban
- ✅ halaman sitasi benar

### H08 — ❌ PERLU DICEK

**Pertanyaan:** Dari 500 mahasiswa, prestasi yang tercatat adalah 2 juara 1 internasional, 4 juara 2 tingkat provinsi, dan 20 finalis tingkat provinsi. Tidak ada kegiatan SKS di luar prodi. Berapa capaian IKU 3?

**Jawaban chatbot:**

```text
Capaian IKU 3 dihitung dengan rumus  

\[
\text{IKU 3} = \frac{\displaystyle\sum n_i \, k_i}{t}\times 100\%
\]

di mana \(t\) = total mahasiswa = 500.

| Prestasi | Jumlah mahasiswa (\(n_i\)) | Bobot (\(k_i\)) | \(n_i \times k_i\) |
|----------|---------------------------|----------------|-------------------|
| Juara 1 internasional | 2 | 1 (tingkat internasional, juara 1) | 2 × 1 = 2 |
| Juara 2 tingkat provinsi | 4 | 0,2 (tingkat provinsi, juara 2/3/favorit) | 4 × 0,2 = 0,8 |
| Finalis tingkat provinsi | 20 | 0,05 (tingkat provinsi, finalis) | 20 × 0,05 = 1,0 |

Jumlah \(\sum n_i k_i = 2 + 0,8 + 1,0 = 3,8\).

Maka persentasenya:

\[
\text{IKU 3} = \frac{3,8}{500}\times 100\% = 0,76\%
\]

Jadi capaian IKU 3 untuk 500 mahasiswa tersebut adalah **0,76 %**.  

Rujukan: formula dan bobot prestasi pada IKU 3 [1].
```

**Sitasi chatbot:**

- [1] Buku IKU Diktisaintek Berdampak V1, hlm. 53–54 (IKU 3, Formula); juga di PPT hlm. 50; Buku (Lampiran Kepmen 358/M/KEP/2025) hlm. 107–108

**Peringatan chatbot:**

- Soal hitungan dijawab dengan persentase tetapi kalkulator tidak dipanggil.

**Jawaban yang diharapkan:**

- Angka kunci: **0,76**
- Halaman kunci: 54

**0,76%**.

**Pemeriksaan otomatis:**

- ❌ kalkulator dipanggil
- ❌ hasil kalkulator = kunci
- ✅ angka kunci ada di jawaban
- ✅ halaman sitasi benar

### H09 — ✅ LULUS

**Pertanyaan:** PT memiliki 120 kerja sama. Dari kerja sama itu dihasilkan 30 karya (judul) yang telah dimanfaatkan oleh mitra, melibatkan total 90 dosen. Berapa capaian IKU 5?

**Jawaban chatbot:**

```text
Capaian IKU 5 (Rasio Luaran Hasil Kerjasama Antara Perguruan Tinggi dan Start-Up/Industri/Lembaga) dihitung dengan rumus:

(Jumlah luaran hasil kerja sama) ÷ (Total kerja sama) × 100%  

= 30 ÷ 120 × 100% = **25 %**.

Jadi, capaian IKU 5 PT adalah **25 %**. [2][rasio]
```

**Sitasi chatbot:**

- [2] Buku IKU Diktisaintek Berdampak V1, hlm. 57–58 (IKU 5, Formula); juga di Buku (Lampiran Kepmen 358/M/KEP/2025) hlm. 117; PPT hlm. 53

**Sumber rumus (kalkulator):**

- Buku IKU Diktisaintek Berdampak V1, IKU 5 – Formula & Keterangan, hlm. 57

**Panggilan kalkulator:**

- argumen `{"argumen_json":"{\"kode\": \"iku5\", \"pembilang\": 30, \"penyebut\": 120}","fungsi":"rasio"}` → 25,00

**Jawaban yang diharapkan:**

- Angka kunci: **25,00**
- Halaman kunci: 57

**25%**. Yang dihitung adalah **jumlah judul/karya, bukan jumlah dosen**, sehingga angka 90 tidak dipakai.

**Pemeriksaan otomatis:**

- ✅ kalkulator dipanggil
- ✅ hasil kalkulator = kunci
- ✅ angka kunci ada di jawaban
- ✅ halaman sitasi benar

### H10 — ✅ LULUS

**Pertanyaan:** Total publikasi PT dalam satu periode adalah 200, terdiri atas 10 jurnal Top Tier, 40 Q1, 50 Q2, 30 Q3, 20 Q4, dan 50 publikasi tidak terindeks Scopus/WoS. Berapa capaian IKU 6?

**Jawaban chatbot:**

```text
Capaian IKU 6 = 54,75 % [1][3]  

Langkah perhitungannya:  
- Top Tier: 10 × 1,2 = 12  
- Q1: 40 × 1,0 = 40  
- Q2: 50 × 0,75 = 37,5  
- Q3: 30 × 0,50 = 15  
- Q4: 20 × 0,25 = 5  

Jumlah bobot publikasi (Σ n·k) = 12 + 40 + 37,5 + 15 + 5 = 109,5  
Capaian = (109,5 ÷ 200) × 100 % = 54,75 %  

Jadi persentase publikasi bereputasi internasional (IKU 6) untuk PT tersebut adalah **54,75 %**.
```

**Sitasi chatbot:**

- [1] Buku IKU Diktisaintek Berdampak V1, hlm. 63 (IKU 6, Kriteria); juga di PPT hlm. 61; Buku (Lampiran Kepmen 358/M/KEP/2025) hlm. 117–118
- [3] Buku IKU Diktisaintek Berdampak V1, hlm. 63 (IKU 6, Formula); juga di PPT hlm. 62; Buku (Lampiran Kepmen 358/M/KEP/2025) hlm. 119

**Sumber rumus (kalkulator):**

- Buku IKU Diktisaintek Berdampak V1, IKU 6 – Kriteria (bobot kuartil) & Formula, hlm. 63

**Panggilan kalkulator:**

- argumen `{"argumen_json":"{\"total_publikasi\":200,\"publikasi\":{\"top_tier\":10,\"q1\":40,\"q2\":50,\"q3\":30,\"q4\":20}}","fungsi":"iku6"}` → 54,75

**Peringatan chatbot:**

- LLM mengembalikan respons kosong; diulang otomatis.

**Jawaban yang diharapkan:**

- Angka kunci: **54,75**
- Halaman kunci: 63

**54,75%**.

**Pemeriksaan otomatis:**

- ✅ kalkulator dipanggil
- ✅ hasil kalkulator = kunci
- ✅ angka kunci ada di jawaban
- ✅ halaman sitasi benar

### H11 — ❌ PERLU DICEK

**Pertanyaan:** Total publikasi 20, terdiri atas 4 artikel Q1 hasil kolaborasi dengan penulis luar negeri, 6 artikel Q1 tanpa kolaborasi, dan 10 prosiding internasional terindeks Scopus. Berapa capaian IKU 6?

**Jawaban chatbot:**

```text
Informasinya tidak ditemukan di dokumen IKU. Karena tidak ada fungsi perhitungan yang disediakan untuk IKU 6 dalam alat kalkulator yang tersedia, saya tidak dapat menghitung capaian IKU 6 secara otomatis. Silakan sampaikan data tambahan atau gunakan fungsi perhitungan yang sesuai bila tersedia.
```

**Panggilan kalkulator:**

- argumen `{"argumen_json":"{\"kode\": \"iku6\", \"pembilang\": 13.5, \"penyebut\": 20}","fungsi":"rasio"}` → ValueError: Kode rasio 'iku6' tidak dikenal. Pilihan: iku4, iku5, iku7, iku8, iku11d. Periksa nama fungsi dan format argumen.

**Jawaban yang diharapkan:**

- Angka kunci: **67,50**
- Halaman kunci: 63

**67,5%**.

**Pemeriksaan otomatis:**

- ❌ kalkulator dipanggil
- ❌ hasil kalkulator = kunci
- ❌ angka kunci ada di jawaban
- ❌ halaman sitasi benar

### H12 — ✅ LULUS

**Pertanyaan:** Dari 60 program SDGs PT, 45 program berkontribusi pada SDG 1, 4, 17, dan 2 SDG pilihan. Berapa capaian IKU 7?

**Jawaban chatbot:**

```text
Capaian IKU 7 = (45 ÷ 60) × 100 % = 75 % [1][2][3][4][5] (menggunakan formula yang tercantum pada halaman 58).
```

**Sitasi chatbot:**

- [1] Buku IKU Diktisaintek Berdampak V1, hlm. 58 (IKU 7, Formula); juga di PPT hlm. 55; Buku (Lampiran Kepmen 358/M/KEP/2025) hlm. 121
- [2] Buku IKU Diktisaintek Berdampak V1, hlm. 58 (IKU 7, Kriteria); juga di PPT hlm. 55; PPT hlm. 54; PPT hlm. 54; Buku (Lampiran Kepmen 358/M/KEP/2025) hlm. 119–120; Buku (Lampiran Kepmen 358/M/KEP/2025) hlm. 119–120
- [3] Buku IKU Diktisaintek Berdampak V1, hlm. 58 (IKU 7, Kriteria)
- [4] Buku IKU Diktisaintek Berdampak V1, hlm. 58 (IKU 7, Ketentuan); juga di Buku (Lampiran Kepmen 358/M/KEP/2025) hlm. 120–121
- [5] Buku IKU Diktisaintek Berdampak V1, hlm. 58 (IKU 7, Definisi); juga di PPT hlm. 54; Buku (Lampiran Kepmen 358/M/KEP/2025) hlm. 119

**Sumber rumus (kalkulator):**

- Buku IKU Diktisaintek Berdampak V1, IKU 7 – Formula, hlm. 58

**Panggilan kalkulator:**

- argumen `{"argumen_json":"{\"kode\":\"iku7\",\"pembilang\":45,\"penyebut\":60}","fungsi":"rasio"}` → 75,00

**Peringatan chatbot:**

- Panggilan alat ditolak server (nama alat 'rasio' tidak dikenal); diulang otomatis.

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
Capaian IKU 9 ( Persentase Pendapatan Non Pendidikan/UKT ) adalah **24 %**. Perhitungan dilakukan dengan menjumlahkan pendapatan yang termasuk dalam kriteria non-mahasiswa (hibah riset kompetitif = 50 miliar, jasa konsultasi = 40 miliar, unit bisnis = 20 miliar, hasil investasi dana abadi = 10 miliar) sehingga total = 120 miliar, kemudian dibagi total pendapatan PT (500 miliar) dan dikalikan 100 % = 24 %【iku9】.
```

**Sumber rumus (kalkulator):**

- Buku IKU Diktisaintek Berdampak V1, IKU 9 – Kriteria & Formula, hlm. 59

**Panggilan kalkulator:**

- argumen `{"argumen_json":"{\"total_pendapatan\": 500, \"rincian\": {\"hibah riset kompetitif\": 50, \"jasa konsultasi dan pelatihan\": 40, \"unit bisnis\": 20, \"hasil investasi dana abadi\": 10}}","fungsi":"iku9"}` → ValueError: Pos pendapatan 'hibah riset kompetitif' belum dikategorikan; tambahkan ke daftar diakui/tidak diakui. Periksa nama fungsi dan format argumen.
- argumen `{"argumen_json":"{\"total_pendapatan\": 500, \"rincian\": {\"hibah_riset\": 50, \"konsultasi\": 40, \"unit_bisnis\": 20, \"hasil_dana_abadi\": 10}}","fungsi":"iku9"}` → 24,00

**Peringatan chatbot:**

- Jawaban tidak memuat rujukan [n] ke konteks.

**Jawaban yang diharapkan:**

- Angka kunci: **24,00**
- Halaman kunci: 59

**24%**. Jawaban yang memasukkan BOPTN (200/500 = 40%) **salah**.

**Pemeriksaan otomatis:**

- ✅ kalkulator dipanggil
- ✅ hasil kalkulator = kunci
- ✅ angka kunci ada di jawaban
- ✅ halaman sitasi benar

### H14 — ✅ LULUS

**Pertanyaan:** PT memiliki 300 dosen dalam satu tahun terakhir; 45 dosen ber-NUPTK mendapat rekognisi internasional. Berapa capaian IKU 4?

**Jawaban chatbot:**

```text
Capaian **IKU 4 – Persentase Dosen Perguruan Tinggi yang Mendapatkan Rekognisi Internasional** adalah 15 % [1][2][3][4][5]. Perhitungannya:  

\( \text{(Jumlah dosen ber-NUPTK yang mendapat rekognisi internasional)} ÷ \text{(Total dosen PT dalam satu tahun terakhir)} × 100\% = 45 ÷ 300 × 100\% = 15\% \)  

Langkah perhitungan dan hasilnya diperoleh melalui fungsi rasio dengan kode “iku4” [hasil 15 %].
```

**Sitasi chatbot:**

- [1] Buku IKU Diktisaintek Berdampak V1, hlm. 62–63 (IKU 4, Formula); juga di Buku (Lampiran Kepmen 358/M/KEP/2025) hlm. 112; PPT hlm. 60–61
- [2] Buku IKU Diktisaintek Berdampak V1, hlm. 61 (IKU 4, Definisi); juga di Buku (Lampiran Kepmen 358/M/KEP/2025) hlm. 108; PPT hlm. 58
- [3] Buku IKU Diktisaintek Berdampak V1, hlm. 62 (IKU 4, Ketentuan); juga di PPT hlm. 60; Buku (Lampiran Kepmen 358/M/KEP/2025) hlm. 111–112
- [4] Buku IKU Diktisaintek Berdampak V1, hlm. 61–62 (IKU 4, Kriteria); juga di Buku (Lampiran Kepmen 358/M/KEP/2025) hlm. 108–111; PPT hlm. 59; PPT hlm. 58; Buku (Lampiran Kepmen 358/M/KEP/2025) hlm. 108–111; PPT hlm. 58; PPT hlm. 59; Buku (Lampiran Kepmen 358/M/KEP/2025) hlm. 108–111; Buku (Lampiran Kepmen 358/M/KEP/2025) hlm. 108–111
- [5] Buku IKU Diktisaintek Berdampak V1, hlm. 61–62 (IKU 4, Kriteria)

**Sumber rumus (kalkulator):**

- Buku IKU Diktisaintek Berdampak V1, IKU 4 – Formula, hlm. 62

**Panggilan kalkulator:**

- argumen `{"argumen_json":"{\"kode\": \"iku4\", \"pembilang\": 45, \"penyebut\": 300}","fungsi":"rasio"}` → 15,00

**Jawaban yang diharapkan:**

- Angka kunci: **15,00**
- Halaman kunci: 62

**15%**.

**Pemeriksaan otomatis:**

- ✅ kalkulator dipanggil
- ✅ hasil kalkulator = kunci
- ✅ angka kunci ada di jawaban
- ✅ halaman sitasi benar

### H15 — ✅ LULUS

**Pertanyaan:** Dari 400 SDM PT (dosen/peneliti), 12 orang terlibat langsung dalam penyusunan kebijakan nasional/daerah/industri, dibuktikan dengan SK atau undangan resmi. Berapa capaian IKU 8?

**Jawaban chatbot:**

```text
Capaian IKU 8 adalah **3 %** (12 SDM terlibat ÷ 400 SDM total × 100% = 3 %) [3].
```

**Sitasi chatbot:**

- [3] Buku IKU Diktisaintek Berdampak V1, hlm. 64 (IKU 8, Formula); juga di PPT hlm. 63; Buku (Lampiran Kepmen 358/M/KEP/2025) hlm. 122

**Sumber rumus (kalkulator):**

- Buku IKU Diktisaintek Berdampak V1, IKU 8 – Formula, hlm. 64

**Panggilan kalkulator:**

- argumen `{"argumen_json":"{\"kode\": \"iku8\", \"pembilang\": 12, \"penyebut\": 400}","fungsi":"rasio"}` → 3,00

**Jawaban yang diharapkan:**

- Angka kunci: **3,00**
- Halaman kunci: 64

**3%**.

**Pemeriksaan otomatis:**

- ✅ kalkulator dipanggil
- ✅ hasil kalkulator = kunci
- ✅ angka kunci ada di jawaban
- ✅ halaman sitasi benar

### H16 — ❌ PERLU DICEK

**Pertanyaan:** Nilai akhir evaluasi SAKIP sebuah PT adalah 82. Apa predikatnya?

**Jawaban chatbot:**

```text
Berdasarkan skala penilaian SAKIP, nilai akhir 82 berada pada rentang 80-89, sehingga predikatnya adalah **A (Sangat Baik)**[2].
```

**Sitasi chatbot:**

- [2] Buku IKU Diktisaintek Berdampak V1, hlm. 66 (IKU 11b, Kriteria)

**Jawaban yang diharapkan:**

- Angka kunci: **A (sangat baik)**
- Halaman kunci: 66

Predikat **A (sangat baik)**, rentang nilai 80–89: efektif dan efisien, menghasilkan kinerja di atas target.

**Pemeriksaan otomatis:**

- ❌ kalkulator dipanggil
- ❌ hasil kalkulator = kunci
- ❌ angka kunci ada di jawaban
- ✅ halaman sitasi benar

### H17 — ✅ LULUS

**Pertanyaan:** PT merencanakan 24 kegiatan pencegahan dan penanganan kekerasan, narkoba, dan korupsi; 18 kegiatan terlaksana. Berapa capaian IKU 11d?

**Jawaban chatbot:**

```text
Capaian IKU 11d (Pencegahan dan Penanganan Anti Kekerasan, Anti Narkoba, dan Anti Korupsi) adalah **75 %**.  

Langkah perhitungan:  
1. Jumlah kegiatan yang terlaksana = 18  
2. Total kegiatan yang direncanakan = 24  
3. (18 ÷ 24) × 100 % = 75 %  

[1][2][3][4][5]
```

**Sitasi chatbot:**

- [1] Buku IKU Diktisaintek Berdampak V1, hlm. 68 (IKU 11d, Formula)
- [2] Buku IKU Diktisaintek Berdampak V1, hlm. 68 (IKU 11d, Kriteria)
- [3] Buku IKU Diktisaintek Berdampak V1, hlm. 68 (IKU 11d, Kriteria)
- [4] Buku IKU Diktisaintek Berdampak V1, hlm. 68 (IKU 11d, Ketentuan)
- [5] Buku IKU Diktisaintek Berdampak V1, hlm. 68 (IKU 11d, Definisi)

**Sumber rumus (kalkulator):**

- Buku IKU Diktisaintek Berdampak V1, IKU 11d – Formula, hlm. 68

**Panggilan kalkulator:**

- argumen `{"argumen_json":"{\"kode\":\"iku11d\",\"pembilang\":18,\"penyebut\":24}","fungsi":"rasio"}` → 75,00

**Peringatan chatbot:**

- Panggilan alat ditolak server (nama alat 'rasio' tidak dikenal); diulang otomatis.

**Jawaban yang diharapkan:**

- Angka kunci: **75,00**
- Halaman kunci: 68

**75%**.

**Pemeriksaan otomatis:**

- ✅ kalkulator dipanggil
- ✅ hasil kalkulator = kunci
- ✅ angka kunci ada di jawaban
- ✅ halaman sitasi benar

### H18 — ✅ LULUS

**Pertanyaan:** UMP di provinsi tempat PT berada adalah Rp3.000.000. Berapa penghasilan minimum dosen dengan jabatan Lektor dan Profesor menurut IKU 12?

**Jawaban chatbot:**

```text
Menurut IKU 12, penghasilan minimum dosen dihitung dengan mengalikan Upah Minimum Provinsi (UMP) dengan faktor tertentu untuk tiap jabatan:

- **Lektor:** minimal 3 × UMP → 3 × Rp 3.000.000 = **Rp 9.000.000** per bulan[1]  
- **Profesor:** minimal 6 × UMP → 6 × Rp 3.000.000 = **Rp 18.000.000** per bulan[1]  

Jadi, dengan UMP Rp 3.000.000, dosen Lektor harus memperoleh paling sedikit Rp 9.000.000, dan dosen Profesor paling sedikit Rp 18.000.000.
```

**Sitasi chatbot:**

- [1] Buku IKU Diktisaintek Berdampak V1, hlm. 60 (IKU 12, Kriteria); juga di PPT hlm. 57; Buku (Lampiran Kepmen 358/M/KEP/2025) hlm. 131

**Sumber rumus (kalkulator):**

- Buku IKU Diktisaintek Berdampak V1, IKU 12 – Kriteria b.2, hlm. 60

**Panggilan kalkulator:**

- argumen `{"argumen_json":"{\"ump\": 3000000, \"jabatan\": [\"lektor\", \"profesor\"]}","fungsi":"iku12_penghasilan_minimum"}` → lektor = 9.000.000, profesor = 18.000.000

**Peringatan chatbot:**

- Panggilan alat ditolak server (nama alat 'hitungan_iku' tidak dikenal); diulang otomatis.

**Jawaban yang diharapkan:**

- Angka kunci: **lektor = 9.000.000, profesor = 18.000.000**
- Halaman kunci: 60

Lektor minimal **Rp9.000.000**, Profesor minimal **Rp18.000.000**.

**Pemeriksaan otomatis:**

- ✅ kalkulator dipanggil
- ✅ hasil kalkulator = kunci
- ✅ angka kunci ada di jawaban
- ✅ halaman sitasi benar

### D13 — ✅ LULUS

**Pertanyaan:** aee tu apaan sih? ngukur apa?

**Jawaban chatbot:**

```text
AEE (Angka Efisiensi Edukasi) adalah indikator yang mengukur **tingkat keberhasilan mahasiswa menyelesaikan studi tepat waktu sesuai masa studi standar**, dibandingkan dengan total mahasiswa yang masuk pada periode yang sama [3]. Dengan kata lain, AEE menilai seberapa efisien suatu perguruan tinggi dalam menghasilkan lulusan yang lulus tepat waktu sesuai kurikulum yang ditetapkan [1].
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
- ✅ fakta: efisiensi edukasi
- ✅ halaman sitasi benar

### D14 — ✅ LULUS

**Pertanyaan:** pendptan apa aj yg ga diitung di iku9?

**Jawaban chatbot:**

```text
Pendapatan yang **tidak termasuk** dalam perhitungan IKU 9 – Persentase Pendapatan Non Pendidikan/UKT antara lain:

1. **SPP/UKT/biaya kuliah mahasiswa** [4]  
2. **Iuran pengembangan institusi** [4]  
3. **Subsidi langsung dari pemerintah** seperti belanja pegawai, belanja operasional, BOPTN, BPPTNBH, dan sejenisnya [4]  
4. **Sumbangan/filantropi yang tidak tercatat dalam laporan keuangan resmi perguruan tinggi** [4]  
5. **Dana pokok dana abadi/endowment fund** yang disimpan permanen dan tidak dibelanjakan [4]
```

**Sitasi chatbot:**

- [4] Buku IKU Diktisaintek Berdampak V1, hlm. 59 (IKU 9, Kriteria); juga di PPT hlm. 56; Buku (Lampiran Kepmen 358/M/KEP/2025) hlm. 122–123

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

### H19 — ✅ LULUS

**Pertanyaan:** brp aee s1 klo yg lulus tepat wktu cm 40 org dr 200 mhs?

**Jawaban chatbot:**

```text
AEE (Angka Efisiensi Edukasi) untuk program S1 dengan 40 lulusan tepat waktu dari total 200 mahasiswa adalah **20 %**[1].  

Langkah perhitungan (menggunakan rumus resmi):  
1. AEE realisasi = 40 ÷ 200 × 100 % = 20 %  
2. AEE ideal S1 = 25 % (sesuai ketentuan masa studi 8 semester)  
3. Tingkat pencapaian = 20 % ÷ 25 % × 100 % = 80 %  

Jadi, AEE S1 = 20 % (tingkat pencapaian AEE = 80 %).
```

**Sitasi chatbot:**

- [1] Buku IKU Diktisaintek Berdampak V1, hlm. 49 (IKU 1, Kriteria); juga di Buku (Lampiran Kepmen 358/M/KEP/2025) hlm. 100; PPT hlm. 45

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

### H20 — ✅ LULUS

**Pertanyaan:** realisasi aee kampus kmi: D3 30%, S1 22,5%, S2 40%. aee pt nya jd brp ya?

**Jawaban chatbot:**

```text
AEE PT = 86,97 % [hasil perhitungan alat hitung_iku] 

**Langkah perhitungan (dari alat):**  
1. Tingkat pencapaian D3 = 30 % ÷ 33 % = 90,91 %  
2. Tingkat pencapaian S1 = 22,5 % ÷ 25 % = 90 %  
3. Tingkat pencapaian S2 = 40 % ÷ 50 % = 80 %  
4. AEE PT = (90,91 % + 90 % + 80 %) ÷ 3 = 86,97 %  

Sumber: Buku IKU Diktisaintek Berdampak V1, IKU 1 – Formula c & contoh perhitungan, hlm. 49–50.
```

**Sumber rumus (kalkulator):**

- Buku IKU Diktisaintek Berdampak V1, IKU 1 – Formula c & contoh perhitungan, hlm. 49–50

**Panggilan kalkulator:**

- argumen `{"argumen_json":"{\"realisasi_per_jenjang\": {\"D3\": 30, \"S1\": 22.5, \"S2\": 40}}","fungsi":"iku1_aee_pt"}` → 86,97

**Peringatan chatbot:**

- LLM mengembalikan respons kosong; diulang otomatis.
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
Berdasarkan rumus Slovin dengan galat 2,3 % (d = 0,023) dan jumlah lulusan N = 1 341, jumlah responden minimum yang harus dikumpulkan dalam tracer study adalah **785 responden**.  

Langkah perhitungannya:
1. Hitung N × d² = 1 341 × 0,023² = 0,71.  
2. n = N ÷ (N × d² + 1) = 1 341 ÷ (0,71 + 1) = 784,49.  
3. Dibulatkan ke atas menjadi 785 responden.  

Sumber: Buku IKU Diktisaintek Berdampak V1, IKU 2 – Formula Responden Minimum, hlm. 52.
```

**Sumber rumus (kalkulator):**

- Buku IKU Diktisaintek Berdampak V1, IKU 2 – Formula Responden Minimum, hlm. 52

**Panggilan kalkulator:**

- argumen `{"argumen_json":"{\"jumlah_lulusan\": 1341}","fungsi":"iku2_responden_minimum"}` → 785

**Peringatan chatbot:**

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

### H22 — ✅ LULUS

**Pertanyaan:** klo lulusannya 2rb orang, responden minimum tracer studi brp

**Jawaban chatbot:**

```text
Jumlah responden minimum yang diperlukan untuk tracer study dengan total lulusan 2 000 orang adalah **972 responden**.  

Langkah perhitungannya:
- N × d² = 2 000 × 0,023² = 1,06  
- n = N ÷ (N × d² + 1) = 2 000 ÷ (1,06 + 1) = 971,82  
- Dibulatkan ke atas menjadi 972 responden  

Sumber: Buku IKU Diktisaintek Berdampak V1, IKU 2 – Formula Responden Minimum, hlm. 52.
```

**Sumber rumus (kalkulator):**

- Buku IKU Diktisaintek Berdampak V1, IKU 2 – Formula Responden Minimum, hlm. 52

**Panggilan kalkulator:**

- argumen `{"argumen_json":"{\"jumlah_lulusan\": 2000}","fungsi":"iku2_responden_minimum"}` → 972

**Peringatan chatbot:**

- Panggilan alat ditolak server (nama alat 'iku2_responden_minimum' tidak dikenal); diulang otomatis.
- LLM mengembalikan respons kosong; diulang otomatis.
- Jawaban tidak memuat rujukan [n] ke konteks.

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
Capaian IKU 5 (Rasio Luaran Hasil Kerjasama antara Perguruan Tinggi dan Start-Up/Industri/Lembaga) adalah **25 %**.  

Perhitungannya:  
1. Rumus IKU 5 = (Jumlah luaran hasil kerja sama ÷ Total kerja sama PT) × 100 % [1].  
2. Menggunakan data yang diberikan (luaran = 30 judul, total kerja sama = 120) → 30 ÷ 120 × 100 % = 25 % [hasil perhitungan fungsi]​.
```

**Sitasi chatbot:**

- [1] Buku IKU Diktisaintek Berdampak V1, hlm. 57–58 (IKU 5, Formula); juga di Buku (Lampiran Kepmen 358/M/KEP/2025) hlm. 117; PPT hlm. 53

**Sumber rumus (kalkulator):**

- Buku IKU Diktisaintek Berdampak V1, IKU 5 – Formula & Keterangan, hlm. 57

**Panggilan kalkulator:**

- argumen `{"argumen_json":"{\"kode\":\"iku5\",\"pembilang\":30,\"penyebut\":120}","fungsi":"rasio"}` → 25,00

**Peringatan chatbot:**

- Panggilan alat ditolak server (nama alat 'rasio' tidak dikenal); diulang otomatis.
- Panggilan alat ditolak server (nama alat 'hit_iku' tidak dikenal); diulang otomatis.

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
IKU 7 – Persentase Keterlibatan Perguruan Tinggi dalam SDG 1, 4, 17 dan 2 SDG pilihan = 25 program yang berkontribusi ÷ 50 total program × 100 % = **50 %**[4]. Hasil perhitungan menggunakan rumus resmi IKU 7 (jumlah program/kegiatan yang berkontribusi pada SDG 1, 4, 17 + 2 SDG pilihan dibagi total program SDG PT, dikalikan 100 %) menghasilkan 50 %【rasio】.
```

**Sitasi chatbot:**

- [4] Buku IKU Diktisaintek Berdampak V1, hlm. 58 (IKU 7, Formula); juga di Buku (Lampiran Kepmen 358/M/KEP/2025) hlm. 121; PPT hlm. 55

**Sumber rumus (kalkulator):**

- Buku IKU Diktisaintek Berdampak V1, IKU 7 – Formula, hlm. 58

**Panggilan kalkulator:**

- argumen `{"argumen_json":"{\"kode\": \"iku7\", \"pembilang\": 25, \"penyebut\": 50}","fungsi":"rasio"}` → 50,00

**Peringatan chatbot:**

- Panggilan alat ditolak server (nama alat 'rasio' tidak dikenal); diulang otomatis.
- LLM mengembalikan respons kosong; diulang otomatis.

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
IKU 9 – Persentase Pendapatan Non Pendidikan/UKT = 24 %  

Perhitungan: pendapatan yang diakui (hibah riset 50 M + konsultasi 40 M + unit bisnis 20 M + hasil dana abadi 10 M = 120 M) ÷ total pendapatan PT 500 M × 100 % = 24 % [[iku9]].
```

**Sumber rumus (kalkulator):**

- Buku IKU Diktisaintek Berdampak V1, IKU 9 – Kriteria & Formula, hlm. 59

**Panggilan kalkulator:**

- argumen `{"argumen_json":"{\"total_pendapatan\": 500, \"rincian\": {\"hibah_riset\": 50, \"konsultasi\": 40, \"unit_bisnis\": 20, \"hasil_dana_abadi\": 10}}","fungsi":"iku9"}` → 24,00

**Peringatan chatbot:**

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

### H26 — ❌ PERLU DICEK

**Pertanyaan:** pendapatan total Rp1.250.000.000, terdiri dr ukt rp 900jt, kontrak riset 150 juta, royalti Rp50.000.000, sisanya 150jt dari boptn. capaian iku 9?

**Jawaban chatbot:**

```text
Informasi tentang cara menghitung persentase pendapatan non-pendidikan/UKT (IKU 9) tersedia di dokumen IKU 9, namun tidak ada fungsi perhitungan yang dapat dipanggil untuk IKU 9 dalam daftar alat yang disediakan (fungsi `rasio` hanya menerima kode iku4, iku5, iku7, iku8, iku11d)[1][3]. Oleh karena itu, saya tidak dapat melakukan perhitungan secara otomatis menggunakan alat `hitung_iku`. Jika ada fungsi khusus untuk menghitung IKU 9, silakan berikan atau aktifkan fungsi tersebut.
```

**Sitasi chatbot:**

- [1] Buku IKU Diktisaintek Berdampak V1, hlm. 59 (IKU 9, Kriteria); juga di PPT hlm. 56; Buku (Lampiran Kepmen 358/M/KEP/2025) hlm. 122–123
- [3] Buku IKU Diktisaintek Berdampak V1, hlm. 59 (IKU 9, Formula); juga di Buku (Lampiran Kepmen 358/M/KEP/2025) hlm. 124; PPT hlm. 56

**Panggilan kalkulator:**

- argumen `{"argumen_json":"{\"kode\":\"iku9\",\"pembilang\":200000000,\"penyebut\":1250000000}","fungsi":"rasio"}` → ValueError: Kode rasio 'iku9' tidak dikenal. Pilihan: iku4, iku5, iku7, iku8, iku11d. Periksa nama fungsi dan format argumen.

**Jawaban yang diharapkan:**

- Angka kunci: **16,00**
- Halaman kunci: 59

**16%**.

*Catatan soal:* Ketahanan: campuran 'Rp1.250.000.000', '900jt', '150 juta', 'Rp50.000.000'. Satuan harus disamakan sebelum dihitung.

**Pemeriksaan otomatis:**

- ❌ kalkulator dipanggil
- ❌ hasil kalkulator = kunci
- ❌ angka kunci ada di jawaban
- ✅ halaman sitasi benar

### H27 — ❌ PERLU DICEK

**Pertanyaan:** total pendapatan 2 milyar: hibah riset 300 jt, konsultasi 0,2 M, ukt 1,5 M. hitung iku 9 nya

**Jawaban chatbot:**

```text
Informasinya tidak ditemukan di dokumen IKU. (Tidak ada fungsi hitung_iku yang dapat menghitung persentase pendapatan non-pendidikan/UKT untuk IKU 9.)
```

**Panggilan kalkulator:**

- argumen `{"argumen_json":"{\"kode\": \"iku9\", \"pembilang\": 500000000, \"penyebut\": 2000000000}","fungsi":"rasio"}` → ValueError: Kode rasio 'iku9' tidak dikenal. Pilihan: iku4, iku5, iku7, iku8, iku11d. Periksa nama fungsi dan format argumen.

**Peringatan chatbot:**

- LLM mengembalikan respons kosong; diulang otomatis.
- LLM mengembalikan respons kosong; diulang otomatis.

**Jawaban yang diharapkan:**

- Angka kunci: **25,00**
- Halaman kunci: 59

**25%**.

*Catatan soal:* Ketahanan: ejaan 'milyar', desimal koma '0,2 M' dan '1,5 M' dicampur dengan 'jt'.

**Pemeriksaan otomatis:**

- ❌ kalkulator dipanggil
- ❌ hasil kalkulator = kunci
- ❌ angka kunci ada di jawaban
- ❌ halaman sitasi benar

### H28 — ✅ LULUS

**Pertanyaan:** ump disini 3,5jt, penghasilan minimal dosen lektor kepala brp?

**Jawaban chatbot:**

```text
Penghasilan minimal dosen dengan jabatan **Lektor Kepala** adalah 4 kali UMP.  
Dengan UMP = Rp 3.500.000, perhitungan menghasilkan:

- 4 × Rp 3.500.000 = **Rp 14.000.000**[1].  

Jadi, penghasilan minimal dosen Lektor Kepala adalah **Rp 14.000.000** per bulan.
```

**Sitasi chatbot:**

- [1] Buku IKU Diktisaintek Berdampak V1, hlm. 60 (IKU 12, Kriteria); juga di Buku (Lampiran Kepmen 358/M/KEP/2025) hlm. 131; PPT hlm. 57

**Sumber rumus (kalkulator):**

- Buku IKU Diktisaintek Berdampak V1, IKU 12 – Kriteria b.2, hlm. 60

**Panggilan kalkulator:**

- argumen `{"argumen_json":"{\"ump\": 3500000, \"jabatan\": [\"lektor_kepala\"]}","fungsi":"iku12_penghasilan_minimum"}` → lektor_kepala = 14.000.000

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
Berdasarkan Kriteria IKU 12, penghasilan minimum dosen harus memenuhi standar berbasis jenjang jabatan akademik:

- **Asisten Ahli**: ≥ 1,5 × UMP  
  → 1,5 × Rp 4.250.000 = **Rp 6.375.000** per bulan[1]  
  (Langkah perhitungan: “asisten_ahli: ≥ 1,5 × UMP = 1,5 × Rp4.250.000 = Rp6.375.000”)

- **Profesor**: ≥ 6 × UMP  
  → 6 × Rp 4.250.000 = **Rp 25.500.000** per bulan[1]  
  (Langkah perhitungan: “profesor: ≥ 6 × UMP = 6 × Rp4.250.000 = Rp25.500.000”)

Jadi, dengan UMP Rp 4.250.000, penghasilan minimum yang harus direncanakan adalah **Rp 6.375.000** untuk dosen Asisten Ahli dan **Rp 25.500.000** untuk dosen Profesor.
```

**Sitasi chatbot:**

- [1] Buku IKU Diktisaintek Berdampak V1, hlm. 60 (IKU 12, Kriteria); juga di Buku (Lampiran Kepmen 358/M/KEP/2025) hlm. 131; PPT hlm. 57

**Sumber rumus (kalkulator):**

- Buku IKU Diktisaintek Berdampak V1, IKU 12 – Kriteria b.2, hlm. 60

**Panggilan kalkulator:**

- argumen `{"argumen_json":"{\"ump\": 4250000, \"jabatan\": [\"asisten_ahli\",\"profesor\"]}","fungsi":"iku12_penghasilan_minimum"}` → asisten_ahli = 6.375.000,00, profesor = 25.500.000

**Peringatan chatbot:**

- Panggilan alat ditolak server (nama alat 'hitungan_iku' tidak dikenal); diulang otomatis.

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
Persentase Dosen Perguruan Tinggi yang mendapatkan rekognisi internasional (IKU 4) = 18 ÷ 250 × 100% = **7,2 %**[1].
```

**Sitasi chatbot:**

- [1] Buku IKU Diktisaintek Berdampak V1, hlm. 62–63 (IKU 4, Formula); juga di Buku (Lampiran Kepmen 358/M/KEP/2025) hlm. 112; PPT hlm. 60–61

**Sumber rumus (kalkulator):**

- Buku IKU Diktisaintek Berdampak V1, IKU 4 – Formula, hlm. 62

**Panggilan kalkulator:**

- argumen `{"argumen_json":"{\"kode\":\"iku4\",\"pembilang\":18,\"penyebut\":250}","fungsi":"rasio"}` → 7,20

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
