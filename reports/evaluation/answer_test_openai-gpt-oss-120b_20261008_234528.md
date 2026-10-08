# Uji Jawaban Chatbot (retriever + LLM + kalkulator)

- Waktu: 2026-10-09 00:09:47
- Model LLM: `openai/gpt-oss-120b`
- Soal: 36 dari 44 dijalankan (hitungan 22, definisi & jebakan 14)
- Status run: berhenti: jatah harian LLM habis (429 per hari)

## Ringkasan

| Metrik | Hasil |
|---|---|
| Lulus semua pemeriksaan otomatis | **20/36** |
| Hitungan: kalkulator dipanggil | 14/21 |
| Hitungan: hasil kalkulator = kunci | 14/21 |
| Hitungan: angka kunci ada di jawaban | 15/21 |
| Halaman sitasi benar (hitungan) | 15/21 |
| Halaman sitasi benar (definisi) | 8/13 |
| Soal error (API/kuota) | 1 |
| Jawaban dengan peringatan chatbot | 19 |

| ID | Status | Pemeriksaan yang gagal |
|---|---|---|
| D01 | ✅ | - |
| D02 | ❌ | fakta: 25% / 25 %; fakta: 33% / 33 % |
| D03 | ✅ | - |
| D04 | ❌ | fakta: lulusan / IKU 2; fakta: non pendidikan / non-pendidikan / UKT / IKU 9; fakta: kesejahteraan dosen / IKU 12; halaman sitasi benar |
| D05 | ✅ | - |
| D06 | ❌ | fakta: dosen pembimbing / pendampingan |
| D07 | ❌ | fakta: SDG 1 / SDG1; fakta: SDG 4 / SDG4; fakta: SDG 17 / SDG17; fakta: 2 (dua) / dua SDG / 2 SDG / dua tujuan / 2 tujuan; halaman sitasi benar |
| D08 | ✅ | - |
| D09 | ✅ | - |
| D10 | ❌ | halaman sitasi benar |
| D11 | ❌ | fakta: IKU 2 |
| D12 | ✅ | - |
| H01 | ❌ | kalkulator dipanggil; hasil kalkulator = kunci; angka kunci ada di jawaban; halaman sitasi benar |
| H02 | ✅ | - |
| H03 | ✅ | - |
| H04 | ✅ | - |
| H05 | ✅ | - |
| H06 | ❌ | kalkulator dipanggil; hasil kalkulator = kunci; angka kunci ada di jawaban; halaman sitasi benar |
| H07 | ❌ | kalkulator dipanggil; hasil kalkulator = kunci; angka kunci ada di jawaban; halaman sitasi benar |
| H08 | ❌ | kalkulator dipanggil; hasil kalkulator = kunci |
| H09 | ✅ | - |
| H10 | ✅ | - |
| H11 | ❌ | kalkulator dipanggil; hasil kalkulator = kunci; angka kunci ada di jawaban; halaman sitasi benar |
| H12 | ✅ | - |
| H13 | ✅ | - |
| H14 | ✅ | - |
| H15 | ✅ | - |
| H16 | ❌ | kalkulator dipanggil; hasil kalkulator = kunci; angka kunci ada di jawaban; halaman sitasi benar |
| H17 | ✅ | - |
| H18 | ✅ | - |
| D13 | ❌ | halaman sitasi benar |
| D14 | ❌ | halaman sitasi benar |
| H19 | ✅ | - |
| H20 | ✅ | - |
| H21 | ❌ | kalkulator dipanggil; hasil kalkulator = kunci; angka kunci ada di jawaban; halaman sitasi benar |
| H22 | ⚠️ error | RateLimitError: Error code: 429 - {'error': {'message': 'Rate limit reached for model `openai/gpt-oss-120b` in organization `org_01m4e5peykedwrjbef346rv251` service tier `on_demand` on tokens per day (TPD): Limit 200000, Used 196151, Requested 5310. Please try again in 10m31.152s. Need more tokens? Upgrade to Dev Tier today at https://console.groq.com/settings/billing', 'type': 'tokens', 'code': 'rate_limit_exceeded'}} |

Pemeriksaan otomatis hanya bantuan. Baca jawaban lengkap di bawah dan bandingkan dengan jawaban yang diharapkan.

## Soal yang belum selesai / perlu diulang

9 soal belum dijalankan atau berakhir error: H22, H23, H24, H25, H26, H27, H28, H29, H30. Lanjutkan ke laporan ini dengan:

```powershell
python src/evaluation/run_answer_tests.py --lanjut reports/evaluation/answer_test_openai-gpt-oss-120b_20261008_234528.json --jeda 20
```

## Detail per soal

### D01 — ✅ LULUS

**Pertanyaan:** Apa itu IKU 1?

**Jawaban chatbot:**

```text
**IKU 1 – Angka Efisiensi Edukasi Perguruan Tinggi (AEE PT)**  

IKU 1 mengukur tingkat keberhasilan mahasiswa menyelesaikan studi tepat waktu sesuai masa studi standar, dibandingkan dengan total mahasiswa yang masuk pada periode tertentu. AEE PT dihitung sebagai rata‑rata nilai tingkat pencapaian AEE pada setiap program pendidikan (D1, D2, D3, D4/Sarjana, S2, S3, dll.) yang ada di perguruan tinggi [1][2].  

Kriteria utama IKU 1:  
- Mahasiswa lulus tepat waktu sesuai masa tempuh kurikulum standar (misalnya D1 = 2 semester, D4/Sarjana = 8 semester, S2 = ≥ 3 semester, dst.) [5].  
- Tidak menghitung mahasiswa yang pindah, drop‑out, atau cuti lebih dari ketentuan [4].  

Dengan kata lain, IKU 1 menunjukkan persentase mahasiswa yang berhasil menyelesaikan pendidikan sesuai jadwal yang ditetapkan, dan nilai akhir merupakan rata‑rata pencapaian tersebut di seluruh program pendidikan yang dihitung.
```

**Sitasi chatbot:**

- [1] Buku IKU Diktisaintek Berdampak V1, hlm. 49 (IKU 1, Definisi); juga di PPT hlm. 45
- [2] Buku IKU Diktisaintek Berdampak V1, hlm. 49–50 (IKU 1, Formula); juga di PPT hlm. 46–47; PPT hlm. 46
- [4] Buku IKU Diktisaintek Berdampak V1, hlm. 49 (IKU 1, Ketentuan); juga di PPT hlm. 45; Buku (Lampiran Kepmen 358/M/KEP/2025) hlm. 100–101
- [5] Buku IKU Diktisaintek Berdampak V1, hlm. 49 (IKU 1, Kriteria); juga di PPT hlm. 45

**Jawaban yang diharapkan:**

- Halaman kunci: 49

IKU 1 adalah **Angka Efisiensi Edukasi (AEE) Perguruan Tinggi**, yaitu indikator yang mengukur tingkat keberhasilan mahasiswa menyelesaikan studi **tepat waktu** sesuai masa studi standar, dibandingkan dengan total mahasiswa yang masuk pada periode tertentu. AEE PT dihitung dari **rata-rata tingkat pencapaian AEE setiap program pendidikan**. Sifatnya **IKU Wajib**.

**Pemeriksaan otomatis:**

- ✅ fakta: tepat waktu
- ✅ fakta: efisiensi edukasi / AEE
- ✅ halaman sitasi benar

### D02 — ❌ PERLU DICEK

**Pertanyaan:** Berapa masa tempuh kurikulum dan AEE ideal untuk program Sarjana dan Diploma Tiga?

**Jawaban chatbot:**

```text
- **Diploma Tiga (D3)**  
  - Masa tempuh kurikulum: **6 semester** [1]  
  - AEE ideal: **33 %** [1][4]  

- **Sarjana (S1)**  
  - Masa tempuh kurikulum: **8 semester** [1]  
  - AEE ideal: **25 %** [1][4]
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
- ❌ fakta: 25% / 25 %
- ✅ fakta: 6 semester / enam semester
- ❌ fakta: 33% / 33 %
- ✅ halaman sitasi benar

### D03 — ✅ LULUS

**Pertanyaan:** Berapa jumlah IKU wajib, IKU pilihan, dan IKU partisipatif?

**Jawaban chatbot:**

```text
Jumlah IKU **wajib** yang harus dipenuhi oleh seluruh perguruan tinggi adalah **7 (tujuh)** [1].  
IKU **pilihan** tersedia sebanyak **5 (lima)** indikator, dan perguruan tinggi dapat memilih **2 (dua)** di antaranya [1][3].  
Setiap perguruan tinggi juga diwajibkan mengusulkan **1 (satu)** IKU **partisipatif** [2].
```

**Sitasi chatbot:**

- [1] Buku IKU Diktisaintek Berdampak V1, hlm. 48–49
- [2] Buku IKU Diktisaintek Berdampak V1, hlm. 69
- [3] Buku IKU Diktisaintek Berdampak V1, hlm. 61

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
Berikut IKU yang disebutkan dalam dokumen sebagai **IKU wajib**:

1. **IKU 1 – Angka Efisiensi Edukasi Perguruan Tinggi (AEE PT)** [2]  
2. **IKU 3 – Persentase mahasiswa S1/D4/D3/D2/D1 berkegiatan/meraih prestasi di luar program studi** [3]  
3. **IKU 5 – Rasio luaran hasil kerja sama antara PT dan start‑up/industri/lembaga** [4]  
4. **IKU 7 – Persentase keterlibatan Perguruan Tinggi dalam SDG 1, SDG 4, SDG 17, dan dua SDG pilihan** [5]  

Dokumen menyatakan bahwa terdapat **total 7 (tujuh) IKU wajib**, namun definisi/detail untuk tiga IKU lainnya tidak disertakan dalam potongan konteks yang diberikan. Oleh karena itu, hanya keempat IKU di atas yang dapat kami sebutkan berdasarkan informasi yang tersedia.
```

**Sitasi chatbot:**

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
- ❌ fakta: kesejahteraan dosen / IKU 12
- ❌ halaman sitasi benar

### D05 — ✅ LULUS

**Pertanyaan:** Dari mana data IKU 2 diperoleh, dan bagaimana menentukan jumlah responden minimum?

**Jawaban chatbot:**

```text
**Sumber data IKU 2**  
Data untuk IKU 2 diperoleh melalui **tracer study** yang dilakukan **1 tahun setelah kelulusan** oleh lulusan program D1, D2, D3, D4/Sarjana Terapan, atau Sarjana. [1]

**Menentukan jumlah responden minimum**  
Jumlah responden minimum harus memenuhi batas yang dihitung dengan **rumus Slovin** (galat = 2,3 %). Rumusnya adalah:

\[
n = \frac{N}{N d^{2} + 1}\times 100\%
\]

* **N** = total jumlah lulusan yang menjadi populasi.  
* **d** = galat yang ditetapkan (2,3 % atau 0,023).  

Dengan memasukkan nilai N dan d ke dalam rumus di atas, diperoleh nilai n (sebagai persentase) yang merupakan **jumlah responden minimum** yang harus dikumpulkan dalam tracer study. [2]
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

### D06 — ❌ PERLU DICEK

**Pertanyaan:** Kegiatan di luar program studi apa saja yang diakui untuk IKU 3?

**Jawaban chatbot:**

```text
**IKU 3 – Persentase Mahasiswa S1 dan D4/D3/D2/D1 Berkegiatan/Meraih Prestasi di Luar Program Studi** mengakui kegiatan di luar program studi yang memenuhi kriteria berikut [1]:

1. **Magang atau praktik kerja** yang dilaksanakan pada:
   - Perusahaan swasta (nasional, multinasional, startup, UMKM, dll.);  
   - Lembaga/organisasi nirlaba;  
   - Institusi/organisasi multilateral (mis. PBB, UNICEF, dsb.); atau  
   - Instansi pemerintah, BUMN, atau BUMD.  

2. **Program mahasiswa Berdampak** berupa program sosial/pengabdian kepada masyarakat untuk pemberdayaan di daerah bencana, pedesaan, atau terpencil (mis. pembangunan ekonomi, infrastruktur, dll.).  

3. **Pertukaran mahasiswa**, yaitu mengambil kelas atau semester di perguruan tinggi lain (dalam negeri maupun luar negeri) berdasarkan perjanjian kerja sama yang sudah ada, dengan memperoleh rekognisi kredit semester.  

4. **Penelitian atau riset** yang dilakukan di bawah pengawasan dosen atau peneliti, baik di dalam maupun di luar perguruan tinggi (mis. kolaborasi dengan dosen tetap PT asal, dosen PT lain, lembaga riset, perusahaan multinasional, atau pemerintah/BUMN/BUMD).   [1]
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
- ❌ fakta: dosen pembimbing / pendampingan
- ✅ halaman sitasi benar

### D07 — ❌ PERLU DICEK

**Pertanyaan:** SDG apa saja yang wajib dan pilihan dalam IKU 7?

**Jawaban chatbot:**

```text
Dalam **IKU 7**, keterlibatan perguruan tinggi terbagi menjadi:

* **SDG wajib**:  
  1. **SDG 1 – Tanpa Kemiskinan**  
  2. **SDG 4 – Pendidikan Berkualitas**  
  3. **SDG 17 – Kemitraan**  

* **SDG pilihan**:  
  Perguruan tinggi wajib memilih **dua (2) tujuan SDG lain** di luar SDG 1, SDG 4, dan SDG 17, yang ditetapkan berdasarkan keunggulan, bidang spesialisasi, atau konteks strategis institusi masing‑masing【1】【4】.
```

**Peringatan chatbot:**

- Jawaban tidak memuat rujukan [n] ke konteks.

**Jawaban yang diharapkan:**

- Halaman kunci: 58

SDG wajib: **SDG 1** (Tanpa Kemiskinan), **SDG 4** (Pendidikan Berkualitas), dan **SDG 17** (Kemitraan). Ditambah **2 SDG pilihan** di luar ketiganya, sesuai keunggulan PT, dan harus dituangkan dalam dokumen resmi (Renstra atau laporan kinerja tahunan).

**Pemeriksaan otomatis:**

- ❌ fakta: SDG 1 / SDG1
- ❌ fakta: SDG 4 / SDG4
- ❌ fakta: SDG 17 / SDG17
- ❌ fakta: 2 (dua) / dua SDG / 2 SDG / dua tujuan / 2 tujuan
- ❌ halaman sitasi benar

### D08 — ✅ LULUS

**Pertanyaan:** Pendapatan apa saja yang tidak termasuk dalam perhitungan IKU 9?

**Jawaban chatbot:**

```text
Pendapatan yang **tidak termasuk** dalam perhitungan **IKU 9 – Persentase Pendapatan Non Pendidikan/UKT** adalah:

1. **SPP/UKT/biaya kuliah mahasiswa**.  
2. **Iuran pengembangan institusi**.  
3. **Subsidi langsung dari pemerintah**, seperti belanja pegawai, belanja operasional, BOPTN, BPPTNBH, dan sejenisnya.  
4. **Sumbangan/filantropi yang tidak masuk dalam laporan keuangan resmi perguruan tinggi**.  
5. **Dana pokok dana abadi/endowment fund** yang disimpan secara permanen dan tidak dibelanjakan.  
6. **Pendapatan yang tidak dibukukan**, termasuk hibah barang tanpa nilai dan dana yang masuk lewat kampus tanpa pelaporan resmi.  

*(Sumber: Kriteria tidak termasuk pada IKU 9 [1]; tambahan “Tidak termasuk” pada Kriteria dan Ketentuan Sub‑Indikator IKU 9 [5]).*
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

### D09 — ✅ LULUS

**Pertanyaan:** Penerbit apa yang tidak diperhitungkan dalam IKU 6?

**Jawaban chatbot:**

```text
Penerbit yang **tidak** diperhitungkan dalam perhitungan IKU 6 adalah:

- **MDPI**  
- **Frontiers**  
- **Hindawi Publisher**  

[1]
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

### D10 — ❌ PERLU DICEK

**Pertanyaan:** Bagaimana arah penilaian IKU 11c (pelanggaran integritas akademik)?

**Jawaban chatbot:**

```text
Arah penilaian IKU 11c adalah **semakin rendah semakin baik**; nilai 0 (nol) dapat mencerminkan kinerja yang baik, dengan catatan perguruan tinggi sudah memiliki dan menjalankan mekanisme pencegahan, pelaporan, verifikasi, dan penanganan pelanggaran integritas akademik secara institusional【2†L1-L3】.
```

**Peringatan chatbot:**

- Jawaban tidak memuat rujukan [n] ke konteks.

**Jawaban yang diharapkan:**

- Halaman kunci: 67

**Semakin rendah semakin baik.** Nilai 0 laporan mencerminkan kinerja baik, **asalkan** PT memiliki dan menjalankan mekanisme pencegahan, pelaporan, verifikasi, dan penanganan pelanggaran integritas akademik. Formula: jumlah laporan pelanggaran integritas akademik dalam 1 periode (satuan: laporan).

**Pemeriksaan otomatis:**

- ✅ fakta: semakin rendah
- ❌ halaman sitasi benar

### D11 — ❌ PERLU DICEK

**Pertanyaan:** Lulusan 400, yang bekerja 280, berapa capaian IKU 1?

**Jawaban chatbot:**

```text
Informasi yang diberikan (jumlah lulusan = 400 dan yang bekerja = 280) tidak berkaitan dengan perhitungan **IKU 1 – Angka Efisiensi Edukasi Perguruan Tinggi (AEE PT)**.  
IKU 1 menghitung persentase mahasiswa yang lulus tepat waktu dibandingkan total mahasiswa pada tahun akademik yang bersangkutan, sebagaimana dijelaskan dalam definisi, kriteria, dan formula pada potongan [1]‑[4].  

Untuk menghitung capaian IKU 1 diperlukan data:

* Jumlah mahasiswa yang lulus tepat waktu (sesuai masa tempuh kurikulum).  
* Total mahasiswa pada tahun akademik tersebut.  

Karena data tersebut tidak tersedia dalam konteks yang diberikan, **capaian IKU 1 tidak dapat dihitung**. Silakan sampaikan data yang diperlukan agar perhitungan dapat dilakukan.
```

**Sitasi chatbot:**

- [1] Buku IKU Diktisaintek Berdampak V1, hlm. 49–50 (IKU 1, Formula); juga di PPT hlm. 46–47; PPT hlm. 46; Buku (Lampiran Kepmen 358/M/KEP/2025) hlm. 101–102
- [4] Buku IKU Diktisaintek Berdampak V1, hlm. 49 (IKU 1, Kriteria); juga di PPT hlm. 45

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
Informasinya tidak ditemukan di dokumen IKU yang tersedia.
```

**Jawaban yang diharapkan:**

- Halaman kunci: -

Informasi ini **tidak ada** di Buku IKU. Chatbot harus menyatakan tidak menemukan jawabannya di dokumen, bukan mengarang angka.

*Catatan soal:* Soal di luar cakupan: chatbot harus menolak, bukan mengarang angka UKT.

**Pemeriksaan otomatis:**

- ✅ fakta: tidak ditemukan / tidak terdapat / tidak tersedia / tidak ada informasi / tidak dijelaskan / tidak memuat
- ✅ tidak mengarang sitasi

### H01 — ❌ PERLU DICEK

**Pertanyaan:** Prodi S1 memiliki 200 mahasiswa dalam satu tahun akademik. Sebanyak 40 mahasiswa lulus tepat 8 semester. Berapa AEE realisasi dan tingkat pencapaian AEE prodi tersebut?

**Jawaban chatbot:**

```text
(tidak ada jawaban: None)
```

**Peringatan chatbot:**

- Jawaban tidak memuat rujukan [n] ke konteks.

**Jawaban yang diharapkan:**

- Angka kunci: **aee_realisasi_pct = 20,00, tingkat_pencapaian_pct = 80,00**
- Halaman kunci: 49

AEE realisasi **20%**, tingkat pencapaian **80%**.

**Pemeriksaan otomatis:**

- ❌ kalkulator dipanggil
- ❌ hasil kalkulator = kunci
- ❌ angka kunci ada di jawaban
- ❌ halaman sitasi benar

### H02 — ✅ LULUS

**Pertanyaan:** Sebuah PT memiliki 3 program pendidikan: D3 dengan AEE realisasi 30%, S1 dengan 22,5%, dan S2 dengan 40%. Berapa AEE PT?

**Jawaban chatbot:**

```text
AEE PT = 86,97 % [1][2] 

Langkah perhitungannya:
- Tingkat pencapaian D3 = 30 % ÷ 33 % = 90,91 %
- Tingkat pencapaian S1 = 22,5 % ÷ 25 % = 90 %
- Tingkat pencapaian S2 = 40 % ÷ 50 % = 80 %
- AEE PT = (90,91 % + 90 % + 80 %) ÷ 3 = 86,97 % 

(Perhitungan menggunakan fungsi **hitung_iku** sesuai rumus resmi pada Buku IKU Diktisaintek Berdampak).
```

**Sitasi chatbot:**

- [1] Buku IKU Diktisaintek Berdampak V1, hlm. 49–50 (IKU 1, Formula); juga di Buku (Lampiran Kepmen 358/M/KEP/2025) hlm. 101–102; PPT hlm. 46; Buku (Lampiran Kepmen 358/M/KEP/2025) hlm. 101–102; PPT hlm. 46–47
- [2] Buku IKU Diktisaintek Berdampak V1, hlm. 49–50 (IKU 1, Formula)

**Sumber rumus (kalkulator):**

- Buku IKU Diktisaintek Berdampak V1, IKU 1 – Formula c & contoh perhitungan, hlm. 49–50

**Panggilan kalkulator:**

- argumen `{"argumen_json":"{\"realisasi_per_jenjang\": {\"D3\": 30, \"S1\": 22.5, \"S2\": 40}}","fungsi":"iku1_aee_pt"}` → 86,97

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
**IKU 1 – Angka Efisiensi Edukasi Perguruan Tinggi (AEE PT)**  

- **AEE realisasi** = 20 %  [1][2]  
- **Tingkat pencapaian AEE** = 80 %  [1][2]  

*Langkah perhitungan (berdasarkan rumus resmi):*  
1. Basis = 250 mahasiswa – 10 pindah – 15 drop‑out – 0 cuti lebih = **225** mahasiswa [c. Ketentuan].  
2. AEE realisasi = 45 lulus tepat / 225 × 100 % = **20 %**.  
3. AEE ideal untuk jenjang S1 = **25 %** (8 semester) [a. Ketentuan].  
4. Tingkat pencapaian = 20 % / 25 % × 100 % = **80 %**.  

Jadi, prodi S1 mencatat AEE realisasi 20 % dengan tingkat pencapaian 80 %.
```

**Sitasi chatbot:**

- [1] Buku IKU Diktisaintek Berdampak V1, hlm. 49 (IKU 1, Ketentuan); juga di Buku (Lampiran Kepmen 358/M/KEP/2025) hlm. 100–101; PPT hlm. 45
- [2] Buku IKU Diktisaintek Berdampak V1, hlm. 49–50 (IKU 1, Formula); juga di Buku (Lampiran Kepmen 358/M/KEP/2025) hlm. 101–102; PPT hlm. 46; Buku (Lampiran Kepmen 358/M/KEP/2025) hlm. 101–102

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
Capaian IKU 2 = 70 % [5][1]  

**Langkah perhitungan (menggunakan fungsi hitung_iku):**  
1. bekerja < 6 bulan & > 1,2 × UMP: 280 × 1 = 280  
2. belum bekerja: 120 × 0 = 0  
3. Σ (n·k) = 280  
4. Capaian = 280 ÷ 400 × 100 % = 70 %  

Jadi, persentase lulusan yang langsung bekerja dengan kriteria paling tinggi dalam 1 tahun setelah kelulusan adalah **70 %**.
```

**Sitasi chatbot:**

- [1] Buku IKU Diktisaintek Berdampak V1, hlm. 51 (IKU 2, Kriteria); juga di PPT hlm. 47; PPT hlm. 47; PPT hlm. 47; Buku (Lampiran Kepmen 358/M/KEP/2025) hlm. 103–104; PPT hlm. 47; Buku (Lampiran Kepmen 358/M/KEP/2025) hlm. 103–104; PPT hlm. 47; PPT hlm. 47; Buku (Lampiran Kepmen 358/M/KEP/2025) hlm. 103–104; Buku (Lampiran Kepmen 358/M/KEP/2025) hlm. 103–104; PPT hlm. 48; Buku (Lampiran Kepmen 358/M/KEP/2025) hlm. 103–104
- [5] Buku IKU Diktisaintek Berdampak V1, hlm. 52 (IKU 2, Formula); juga di PPT hlm. 48–49; Buku (Lampiran Kepmen 358/M/KEP/2025) hlm. 104–105

**Sumber rumus (kalkulator):**

- Buku IKU Diktisaintek Berdampak V1, IKU 2 – Kriteria b–f & Formula, hlm. 51–52

**Panggilan kalkulator:**

- argumen `{"argumen_json":"{\"total_responden\": 400, \"kategori\": {\"bekerja_\u003c6bln_\u003e1.2ump\": 280, \"belum\": 120}}","fungsi":"iku2"}` → 70,00

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
Capaian **IKU 2 – Persentase Lulusan Pendidikan Tinggi & Vokasi yang Langsung Bekerja / Melanjutkan Studi / Berwirausaha** adalah **70,8 %**.

**Perhitungan** (menggunakan rumus resmi IKU 2 = Σ (nᵢ × kᵢ) ÷ t × 100 %):

- **bekerja, < 6 bulan, gaji > 1,2 × UMP**: 200 × 1 = 200  
- **bekerja, < 1 tahun, gaji > 1,2 × UMP**: 100 × 0,8 = 80  
- **bekerja, < 1 tahun, gaji < 1,2 × UMP**: 50 × 0,6 = 30  
- **melanjutkan studi (surat penerimaan < 12 bulan)**: 30 × 0,6 = 18  
- **founder, < 6 bulan, penghasilan > 1,2 × UMP**: 20 × 1,2 = 24  
- **freelancer, > 6 bulan, penghasilan < 1,2 × UMP**: 10 × 0,2 = 2  
- **belum bekerja / studi / wirausaha**: 90 × 0 = 0  

Total Σ (n·k) = 354  

Capaian = 354 ÷ 500 × 100 % = **70,8 %**.

*Rujukan*: Kriteria bobot (b‑f) dan formula IKU 2 pada Buku IKU Diktisaintek Berdampak V1, hlm. 51‑52.
```

**Sumber rumus (kalkulator):**

- Buku IKU Diktisaintek Berdampak V1, IKU 2 – Kriteria b–f & Formula, hlm. 51–52

**Panggilan kalkulator:**

- argumen `{"argumen_json":"{\"total_responden\":500,\"kategori\":{\"bekerja_\u003c6bln_\u003e1.2ump\":200,\"bekerja_\u003c1thn_\u003e1.2ump\":100,\"bekerja_\u003c1thn_\u003c1.2ump\":50,\"studi_lanjut_\u003c12bln\":30,\"founder_\u003c6bln_\u003e1.2ump\":20,\"freelancer_\u003e6bln_\u003c1.2ump\":10,\"belum\":90}}","fungsi":"iku2"}` → 70,80

**Peringatan chatbot:**

- Jawaban tidak memuat rujukan [n] ke konteks.

**Jawaban yang diharapkan:**

- Angka kunci: **70,80**
- Halaman kunci: 51, 52

**70,8%**.

**Pemeriksaan otomatis:**

- ✅ kalkulator dipanggil
- ✅ hasil kalkulator = kunci
- ✅ angka kunci ada di jawaban
- ✅ halaman sitasi benar

### H06 — ❌ PERLU DICEK

**Pertanyaan:** Jumlah lulusan suatu PT adalah 2.000 orang. Berapa jumlah responden minimum tracer study untuk IKU 2?

**Jawaban chatbot:**

```text
(tidak ada jawaban: None)
```

**Peringatan chatbot:**

- Jawaban tidak memuat rujukan [n] ke konteks.

**Jawaban yang diharapkan:**

- Angka kunci: **972**
- Halaman kunci: 52

**972 responden**.

**Pemeriksaan otomatis:**

- ❌ kalkulator dipanggil
- ❌ hasil kalkulator = kunci
- ❌ angka kunci ada di jawaban
- ❌ halaman sitasi benar

### H07 — ❌ PERLU DICEK

**Pertanyaan:** Sebuah PT memiliki 1.000 mahasiswa S1/Diploma. Rinciannya: - 100 mahasiswa magang 20 SKS - 150 mahasiswa pertukaran 8 SKS - 50 mahasiswa riset 4 SKS - 5 mahasiswa juara 1 lomba nasional - 10 mahasiswa finalis lomba internasional Berapa capaian IKU 3?

**Jawaban chatbot:**

```text
(tidak ada jawaban: None)
```

**Peringatan chatbot:**

- Jawaban tidak memuat rujukan [n] ke konteks.

**Jawaban yang diharapkan:**

- Angka kunci: **21,50**
- Halaman kunci: 53, 54

**21,5%**.

**Pemeriksaan otomatis:**

- ❌ kalkulator dipanggil
- ❌ hasil kalkulator = kunci
- ❌ angka kunci ada di jawaban
- ❌ halaman sitasi benar

### H08 — ❌ PERLU DICEK

**Pertanyaan:** Dari 500 mahasiswa, prestasi yang tercatat adalah 2 juara 1 internasional, 4 juara 2 tingkat provinsi, dan 20 finalis tingkat provinsi. Tidak ada kegiatan SKS di luar prodi. Berapa capaian IKU 3?

**Jawaban chatbot:**

```text
Capaian IKU 3 =  

\[
\frac{\displaystyle 
(2 \times 1) \;+\; (4 \times 0,2) \;+\; (20 \times 0,05)
}{500}\times 100\%
= \frac{3,8}{500}\times100\% = 0,76\%
\]

Jadi, persentase mahasiswa yang memiliki prestasi di luar program studi adalah **0,76 %**.  

Rujukan: definisi, formula, bobot prestasi, dan ketentuan pada IKU 3 [1][2][3][4].
```

**Sitasi chatbot:**

- [1] Buku IKU Diktisaintek Berdampak V1, hlm. 53–54 (IKU 3, Formula); juga di PPT hlm. 50; Buku (Lampiran Kepmen 358/M/KEP/2025) hlm. 107–108
- [2] Buku IKU Diktisaintek Berdampak V1, hlm. 53 (IKU 3, Kriteria); juga di Buku (Lampiran Kepmen 358/M/KEP/2025) hlm. 105–106; PPT hlm. 49
- [3] Buku IKU Diktisaintek Berdampak V1, hlm. 53 (IKU 3, Ketentuan); juga di Buku (Lampiran Kepmen 358/M/KEP/2025) hlm. 106–107; PPT hlm. 50; PPT hlm. 49
- [4] Buku IKU Diktisaintek Berdampak V1, hlm. 53 (IKU 3, Definisi); juga di Buku (Lampiran Kepmen 358/M/KEP/2025) hlm. 105

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
Capaian **IKU 5 – Rasio Luaran Hasil Kerja Sama antara Perguruan Tinggi dan Start‑Up/Industri/Lembaga** adalah **25 %**.

- Definisi dan kriteria IKU 5 dijelaskan pada [1] dan [3][4][5].
- Formula perhitungannya terdapat pada [2]:  
  \[
  \text{Rasio} = \frac{\text{Jumlah luaran (judul/karya) hasil kerja sama}}{\text{Total kerja sama PT}} \times 100\%
  \]

Dengan data yang diberikan:
- Jumlah luaran (judul/karya) yang dimanfaatkan = 30  
- Total kerja sama = 120  

Perhitungan menggunakan fungsi resmi **rasio** menghasilkan 25 % (langkah perhitungan: 30 ÷ 120 × 100 = 25 %)【hasil:25.0%】.  

Jadi, IKU 5 tercapai sebesar **25 %**.
```

**Sitasi chatbot:**

- [1] Buku IKU Diktisaintek Berdampak V1, hlm. 56–57 (IKU 5, Ketentuan); juga di PPT hlm. 53; Buku (Lampiran Kepmen 358/M/KEP/2025) hlm. 116–117
- [2] Buku IKU Diktisaintek Berdampak V1, hlm. 57–58 (IKU 5, Formula); juga di Buku (Lampiran Kepmen 358/M/KEP/2025) hlm. 117; PPT hlm. 53
- [3] Buku IKU Diktisaintek Berdampak V1, hlm. 55–56 (IKU 5, Kriteria); juga di Buku (Lampiran Kepmen 358/M/KEP/2025) hlm. 112–116; PPT hlm. 52; PPT hlm. 51; Buku (Lampiran Kepmen 358/M/KEP/2025) hlm. 112–116; Buku (Lampiran Kepmen 358/M/KEP/2025) hlm. 112–116; Buku (Lampiran Kepmen 358/M/KEP/2025) hlm. 112–116; PPT hlm. 51; Buku (Lampiran Kepmen 358/M/KEP/2025) hlm. 112–116; PPT hlm. 52; PPT hlm. 52; PPT hlm. 53
- [4] Buku IKU Diktisaintek Berdampak V1, hlm. 55–56 (IKU 5, Kriteria)
- [5] Buku IKU Diktisaintek Berdampak V1, hlm. 55–56 (IKU 5, Kriteria)

**Sumber rumus (kalkulator):**

- Buku IKU Diktisaintek Berdampak V1, IKU 5 – Formula & Keterangan, hlm. 57

**Panggilan kalkulator:**

- argumen `{"argumen_json":"{\"kode\":\"iku5\",\"pembilang\":30,\"penyebut\":120}","fungsi":"rasio"}` → 25,00

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
Capaian IKU 6 = 54,75 %  

Perhitungan:  
- Top Tier: 10 × 1,2 = 12  
- Q1: 40 × 1,00 = 40  
- Q2: 50 × 0,75 = 37,5  
- Q3: 30 × 0,50 = 15  
- Q4: 20 × 0,25 = 5  

Jumlah bobot publikasi = 12 + 40 + 37,5 + 15 + 5 = 109,5  

Persentase = (109,5 ÷ 200) × 100 % = 54,75 %  

Rujukan: definisi, kriteria bobot kuartil, dan formula IKU 6 pada Buku IKU Diktisaintek Berdampak V1, hlm. 63.
```

**Sumber rumus (kalkulator):**

- Buku IKU Diktisaintek Berdampak V1, IKU 6 – Kriteria (bobot kuartil) & Formula, hlm. 63

**Panggilan kalkulator:**

- argumen `{"argumen_json":"{\"total_publikasi\":200,\"publikasi\":{\"top_tier\":10,\"q1\":40,\"q2\":50,\"q3\":30,\"q4\":20},\"kolaborasi\":{}}","fungsi":"iku6"}` → 54,75

**Peringatan chatbot:**

- Jawaban tidak memuat rujukan [n] ke konteks.

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
(tidak ada jawaban: None)
```

**Peringatan chatbot:**

- Jawaban tidak memuat rujukan [n] ke konteks.

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
Capaian IKU 7 adalah **75 %**. Perhitungan menggunakan formula IKU 7:  

\[
\text{Capaian} = \frac{\text{Program/kegiatan berkontribusi pada SDG 1, 4, 17 + 2 SDG pilihan}}{\text{Total program SDG PT}} \times 100\% = \frac{45}{60}\times100\% = 75\%
\]  

Hasil ini sesuai dengan rumusan pada dokumen IKU (Buku IKU Diktisaintek Berdampak V1, halaman 58)【1】.
```

**Sumber rumus (kalkulator):**

- Buku IKU Diktisaintek Berdampak V1, IKU 7 – Formula, hlm. 58

**Panggilan kalkulator:**

- argumen `{"argumen_json":"{\"kode\":\"iku7\",\"pembilang\":45,\"penyebut\":60}","fungsi":"rasio"}` → 75,00

**Peringatan chatbot:**

- Panggilan alat ditolak server (nama alat 'rasio' tidak dikenal); diulang otomatis.
- Jawaban tidak memuat rujukan [n] ke konteks.

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
Capaian IKU 9 = 24 % [[1][3]]

**Penjelasan singkat**  
Pendapatan non‑mahasiswa yang diakui (hibah riset 50 miliar + jasa konsultasi 40 miliar + unit bisnis 20 miliar + hasil investasi dana abadi 10 miliar = 120 miliar) dibagi total pendapatan PT (500 miliar) kemudian dikalikan 100 % → 24 % [[1][3]].
```

**Sitasi chatbot:**

- [1] Buku IKU Diktisaintek Berdampak V1, hlm. 59 (IKU 9, Kriteria); juga di PPT hlm. 56; Buku (Lampiran Kepmen 358/M/KEP/2025) hlm. 122–123
- [3] Buku IKU Diktisaintek Berdampak V1, hlm. 59 (IKU 9, Formula); juga di Buku (Lampiran Kepmen 358/M/KEP/2025) hlm. 124; PPT hlm. 56

**Sumber rumus (kalkulator):**

- Buku IKU Diktisaintek Berdampak V1, IKU 9 – Kriteria & Formula, hlm. 59

**Panggilan kalkulator:**

- argumen `{"argumen_json":"{\"total_pendapatan\":500,\"rincian\":{\"hibah_riset\":50,\"konsultasi\":40,\"unit_bisnis\":20,\"hasil_dana_abadi\":10}}","fungsi":"iku9"}` → 24,00

**Peringatan chatbot:**

- Panggilan alat ditolak server (nama alat 'hit_iku' tidak dikenal); diulang otomatis.

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
Capaian **IKU 4 – Persentase Dosen Perguruan Tinggi yang Mendapatkan Rekognisi Internasional** adalah:

**15 %**  

Perhitungan: (45 dosen ber‑NUPTK yang mendapat rekognisi internasional ÷ 300 dosen total dalam satu tahun terakhir) × 100 % = 15 % [1][2][3][4][5] (rumus pada halaman 62‑63).
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
Capaian **IKU 8 – Persentase SDM PT (dosen/peneliti) yang Terlibat Langsung dalam Penyusunan Kebijakan (Nasional/Daerah/Industri)** dapat dihitung dengan rumus pada [3]:

\[
\text{Persentase} = \frac{\text{Jumlah SDM yang terlibat}}{\text{Total SDM PT}} \times 100\%
\]

Dengan data:
- Jumlah SDM yang terlibat = 12 orang  
- Total SDM PT = 400 orang  

Menggunakan fungsi **rasio** untuk menghitung:

\[
\frac{12}{400} \times 100\% = 3\%
\]

**Hasil:** 3 % [3]  

Jadi, capaian IKU 8 adalah **3 %**.
```

**Sitasi chatbot:**

- [3] Buku IKU Diktisaintek Berdampak V1, hlm. 64 (IKU 8, Formula); juga di PPT hlm. 63; Buku (Lampiran Kepmen 358/M/KEP/2025) hlm. 122

**Sumber rumus (kalkulator):**

- Buku IKU Diktisaintek Berdampak V1, IKU 8 – Formula, hlm. 64

**Panggilan kalkulator:**

- argumen `{"argumen_json":"{\"kode\":\"iku8\",\"pembilang\":12,\"penyebut\":400}","fungsi":"rasio"}` → 3,00

**Peringatan chatbot:**

- Panggilan alat ditolak server (nama alat 'hitungan_iku' tidak dikenal); diulang otomatis.

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
Berdasarkan skala penilaian SAKIP pada IKU 11 b (dan juga pada IKU 3), nilai akhir 82 masuk dalam rentang **80–89**, yang diberikan predikat **A (Sangat Baik)**【1†L1-L4】【2†L1-L4】.
```

**Peringatan chatbot:**

- Jawaban tidak memuat rujukan [n] ke konteks.

**Jawaban yang diharapkan:**

- Angka kunci: **A (sangat baik)**
- Halaman kunci: 66

Predikat **A (sangat baik)**, rentang nilai 80–89: efektif dan efisien, menghasilkan kinerja di atas target.

**Pemeriksaan otomatis:**

- ❌ kalkulator dipanggil
- ❌ hasil kalkulator = kunci
- ❌ angka kunci ada di jawaban
- ❌ halaman sitasi benar

### H17 — ✅ LULUS

**Pertanyaan:** PT merencanakan 24 kegiatan pencegahan dan penanganan kekerasan, narkoba, dan korupsi; 18 kegiatan terlaksana. Berapa capaian IKU 11d?

**Jawaban chatbot:**

```text
Capaian IKU 11d (Pencegahan dan Penanganan Anti Kekerasan, Anti Narkoba, dan Anti Korupsi) adalah **75 %**.  
Perhitungannya: (jumlah kegiatan yang terlaksana ÷ total kegiatan yang direncanakan) × 100 % = 18 ÷ 24 × 100 % = 75 %【1】.
```

**Sumber rumus (kalkulator):**

- Buku IKU Diktisaintek Berdampak V1, IKU 11d – Formula, hlm. 68

**Panggilan kalkulator:**

- argumen `{"argumen_json":"{\"kode\":\"iku11d\",\"pembilang\":18,\"penyebut\":24}","fungsi":"rasio"}` → 75,00

**Peringatan chatbot:**

- Jawaban tidak memuat rujukan [n] ke konteks.

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
Penghasilan minimum dosen menurut IKU 12:

- **Lektor:** ≥ 3 × UMP = 3 × Rp 3.000.000 = **Rp 9.000.000** per bulan [1]  
- **Profesor:** ≥ 6 × UMP = 6 × Rp 3.000.000 = **Rp 18.000.000** per bulan [1]
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

### D13 — ❌ PERLU DICEK

**Pertanyaan:** aee tu apaan sih? ngukur apa?

**Jawaban chatbot:**

```text
AEE (Angka Efisiensi Edukasi) adalah indikator yang mengukur **tingkat keberhasilan mahasiswa menyelesaikan studinya tepat waktu** sesuai dengan masa studi standar yang ditetapkan untuk setiap program pendidikan (misalnya D1 = 2 semester, D4/S1 = 8 semester, S2 = 3 semester, dst.) dibandingkan dengan **total mahasiswa yang masuk** pada tahun akademik yang bersangkutan【3】. Dengan kata lain, AEE menunjukkan persentase mahasiswa yang lulus tepat waktu terhadap seluruh mahasiswa yang terdaftar pada periode tersebut【3】.
```

**Peringatan chatbot:**

- Jawaban tidak memuat rujukan [n] ke konteks.

**Jawaban yang diharapkan:**

- Halaman kunci: 49

AEE = Angka Efisiensi Edukasi (IKU 1), mengukur keberhasilan mahasiswa menyelesaikan studi **tepat waktu** sesuai masa studi standar (sama dengan D01).

*Catatan soal:* Ketahanan: bahasa santai ('aee tu apaan sih'). 'AEE' sengaja tidak dijadikan fakta karena sudah ada di pertanyaan.

**Pemeriksaan otomatis:**

- ✅ fakta: tepat waktu
- ✅ fakta: efisiensi edukasi
- ❌ halaman sitasi benar

### D14 — ❌ PERLU DICEK

**Pertanyaan:** pendptan apa aj yg ga diitung di iku9?

**Jawaban chatbot:**

```text
Pendapatan yang **tidak termasuk** dalam perhitungan IKU 9 – Persentase Pendapatan Non Pendidikan/UKT adalah:

1. **SPP/UKT/biaya kuliah mahasiswa** (biaya pendidikan mahasiswa)【4】  
2. **Iuran pengembangan institusi**【4】  
3. **Subsidi langsung dari pemerintah**, meliputi:
   - belanja pegawai,
   - belanja operasional,
   - BOPTN,
   - BPPTNBH, dan sejenisnya【4】  
4. **Sumbangan/filantropi yang tidak masuk laporan keuangan resmi perguruan tinggi**【4】  
5. **Dana pokok dana abadi/endowment fund** yang disimpan permanen dan tidak dibelanjakan【4】

Semua pendapatan di atas dikecualikan karena tidak termasuk dalam kategori “pendapatan non‑mahasiswa” yang diakui untuk IKU 9.
```

**Peringatan chatbot:**

- Jawaban tidak memuat rujukan [n] ke konteks.

**Jawaban yang diharapkan:**

- Halaman kunci: 59

SPP/UKT, iuran pengembangan institusi, subsidi langsung pemerintah (termasuk BOPTN/BPPTNBH), filantropi yang tidak tercatat, dan pokok dana abadi (sama dengan D08).

*Catatan soal:* Ketahanan: typo ('pendptan', 'aj', 'diitung', 'iku9'). Sama dengan D08.

**Pemeriksaan otomatis:**

- ✅ fakta: UKT / SPP
- ✅ fakta: BOPTN
- ✅ fakta: iuran pengembangan
- ✅ fakta: dana abadi / endowment
- ❌ halaman sitasi benar

### H19 — ✅ LULUS

**Pertanyaan:** brp aee s1 klo yg lulus tepat wktu cm 40 org dr 200 mhs?

**Jawaban chatbot:**

```text
AEE (Angka Efisiensi Edukasi) untuk program S1 dihitung dengan rumus:

\[
\text{AEE realisasi} = \frac{\text{jumlah mahasiswa lulus tepat waktu}}{\text{total mahasiswa}} \times 100\%
\]

\[
\text{Tingkat pencapaian} = \frac{\text{AEE realisasi}}{\text{AEE ideal}} \times 100\%
\]

Dengan data yang diberikan (40 mahasiswa lulus tepat waktu dari 200 mahasiswa), hasil perhitungannya adalah:

- **AEE realisasi** = 20 %  
- **AEE ideal S1** = 25 % (sesuai standar masa studi 8 semester)  
- **Tingkat pencapaian AEE S1** = 80 %  

Jadi, AEE S1 = **80 %**.  

Rujukan: formula dan ketentuan AEE PT pada Buku IKU Diktisaintek Berdampak V1, bagian IKU 1 – Formula & Ketentuan, hlm. 49‑50. [2][4]
```

**Sitasi chatbot:**

- [2] Buku IKU Diktisaintek Berdampak V1, hlm. 49–50 (IKU 1, Formula); juga di Buku (Lampiran Kepmen 358/M/KEP/2025) hlm. 101–102; Buku (Lampiran Kepmen 358/M/KEP/2025) hlm. 101–102; PPT hlm. 46; PPT hlm. 46–47
- [4] Buku IKU Diktisaintek Berdampak V1, hlm. 49 (IKU 1, Ketentuan); juga di Buku (Lampiran Kepmen 358/M/KEP/2025) hlm. 100–101; PPT hlm. 45

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
AEE PT kampus KMI = **86,97 %**【1】.  

Langkah perhitungan (menggunakan rumus resmi IKU 1):
- Tingkat pencapaian D3 = 30 % ÷ 33 % = 90,91 %
- Tingkat pencapaian S1 = 22,5 % ÷ 25 % = 90,00 %
- Tingkat pencapaian S2 = 40 % ÷ 50 % = 80,00 %
- AEE PT = (90,91 % + 90,00 % + 80,00 %) ÷ 3 = 86,97 %  

Sumber: Buku IKU Diktisaintek Berdampak V1, IKU 1 – Formula c & contoh perhitungan, hlm. 49‑50.
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

### H21 — ❌ PERLU DICEK

**Pertanyaan:** lulusan kampus kami 1.341 org, minimal responden tracer study nya brp?

**Jawaban chatbot:**

```text
(tidak ada jawaban: None)
```

**Peringatan chatbot:**

- Jawaban tidak memuat rujukan [n] ke konteks.

**Jawaban yang diharapkan:**

- Angka kunci: **785**
- Halaman kunci: 52

**785 responden**.

*Catatan soal:* Ketahanan: titik pemisah ribuan '1.341' = 1341 (bukan 1,341).

**Pemeriksaan otomatis:**

- ❌ kalkulator dipanggil
- ❌ hasil kalkulator = kunci
- ❌ angka kunci ada di jawaban
- ❌ halaman sitasi benar

### H22 — ⚠️ ERROR

**Pertanyaan:** klo lulusannya 2rb orang, responden minimum tracer studi brp

**Jawaban chatbot:**

```text
(tidak ada jawaban: RateLimitError: Error code: 429 - {'error': {'message': 'Rate limit reached for model `openai/gpt-oss-120b` in organization `org_01m4e5peykedwrjbef346rv251` service tier `on_demand` on tokens per day (TPD): Limit 200000, Used 196151, Requested 5310. Please try again in 10m31.152s. Need more tokens? Upgrade to Dev Tier today at https://console.groq.com/settings/billing', 'type': 'tokens', 'code': 'rate_limit_exceeded'}})
```

**Jawaban yang diharapkan:**

- Angka kunci: **972**
- Halaman kunci: 52

**972 responden**.

*Catatan soal:* Ketahanan: '2rb' = 2000. Sama dengan H06.

**Pemeriksaan otomatis:**

