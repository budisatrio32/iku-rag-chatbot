# Test Set Chatbot RAG — Buku IKU Diktisaintek Berdampak V1

Sumber: `data/input/Buku IKU Diktisaintek Berdampak_V1.pdf` (Bab V, hlm. 48–68).
Nomor halaman = nomor halaman file PDF (bukan nomor yang tercetak di dokumen).

Jumlah: **44 pertanyaan** — 14 definisi/konsep (D), 30 perhitungan (H). Soal D13–D14 dan H19–H30 adalah **soal ketahanan** (bagian C): bahasa santai, typo, dan penulisan angka/uang yang tidak baku.

Cara pakai:
- **Uji retrieval:** jalankan `python src/evaluation/eval_retrieval.py`. Sebuah chunk dianggap bukti jika memuat **semua** "Kata kunci bukti" soal tersebut (tidak peka huruf besar/kecil). Jika mengubah format file ini, pertahankan pola `### ID`, `**Pertanyaan:**`, `**Sumber:** ... hlm. N`, dan `**Kata kunci bukti:**` agar tetap terbaca script.
- **Uji jawaban:** bandingkan jawaban chatbot dengan "Jawaban benar". Untuk soal H, angka akhir harus sama (toleransi pembulatan ±0,01).
- Soal bertanda ⚠️ adalah soal jebakan: chatbot yang baik harus mengoreksi/menolak, bukan langsung menjawab.

## Ringkasan

| ID | Tipe | IKU | Topik | Hlm. |
|---|---|---|---|---|
| D01 | Definisi | 1 | Definisi AEE | 49 |
| D02 | Definisi | 1 | Masa tempuh & AEE ideal | 49 |
| D03 | Definisi | Umum | Jumlah IKU wajib/pilihan/partisipatif | 48 |
| D04 | Definisi | Umum | Daftar IKU wajib | 48 |
| D05 | Definisi | 2 | Sumber data & responden minimum | 51–52 |
| D06 | Definisi | 3 | Kegiatan di luar prodi yang diakui | 53 |
| D07 | Definisi | 7 | SDG wajib & pilihan | 58 |
| D08 | Definisi | 9 | Yang tidak termasuk pendapatan non-UKT | 59 |
| D09 | Definisi | 6 | Penerbit yang dikecualikan | 63 |
| D10 | Definisi | 11c | Arah penilaian integritas akademik | 67 |
| D11 | Jebakan ⚠️ | 1 | Salah IKU (lulusan bekerja ≠ IKU 1) | 49, 51 |
| D12 | Jebakan ⚠️ | — | Di luar cakupan dokumen | — |
| H01 | Hitung | 1 | AEE satu prodi | 49 |
| H02 | Hitung | 1 | AEE PT (rata-rata beberapa jenjang) | 49–50 |
| H03 | Hitung | 1 | AEE dengan pengecualian pindah/DO | 49 |
| H04 | Hitung | 2 | Lulusan bekerja (satu bobot) | 51–52 |
| H05 | Hitung | 2 | Lulusan dengan bobot campuran | 51–52 |
| H06 | Hitung | 2 | Responden minimum Slovin | 52 |
| H07 | Hitung | 3 | Kegiatan SKS + prestasi | 53–54 |
| H08 | Hitung | 3 | Prestasi saja | 54 |
| H09 | Hitung | 5 | Rasio luaran kerja sama | 57 |
| H10 | Hitung | 6 | Publikasi berbobot kuartil | 63 |
| H11 | Hitung | 6 | Bonus kolaborasi internasional | 63 |
| H12 | Hitung | 7 | Keterlibatan SDGs | 58 |
| H13 | Hitung | 9 | Pendapatan non-UKT | 59 |
| H14 | Hitung | 4 | Dosen rekognisi internasional | 62 |
| H15 | Hitung | 8 | SDM penyusun kebijakan | 64 |
| H16 | Hitung | 11b | Konversi nilai SAKIP ke predikat | 66 |
| H17 | Hitung | 11d | Kegiatan anti kekerasan/narkoba/korupsi | 68 |
| H18 | Hitung | 12 | Standar penghasilan dosen | 60 |
| D13 | Definisi | 1 | Ketahanan: bahasa santai | 49 |
| D14 | Definisi | 9 | Ketahanan: typo | 59 |
| H19 | Hitung | 1 | Ketahanan: typo & singkatan | 49 |
| H20 | Hitung | 1 | Ketahanan: desimal koma (22,5%) | 49–50 |
| H21 | Hitung | 2 | Ketahanan: titik ribuan (1.341) | 52 |
| H22 | Hitung | 2 | Ketahanan: "2rb" | 52 |
| H23 | Hitung | 5 | Ketahanan: typo | 57 |
| H24 | Hitung | 7 | Ketahanan: typo | 58 |
| H25 | Hitung | 9 | Ketahanan: satuan "M" (miliar) | 59 |
| H26 | Hitung | 9 | Ketahanan: campuran Rp/jt/juta | 59 |
| H27 | Hitung | 9 | Ketahanan: "milyar" & "0,2 M" | 59 |
| H28 | Hitung | 12 | Ketahanan: "3,5jt" | 60 |
| H29 | Hitung | 12 | Ketahanan: "Rp 4.250.000" | 60 |
| H30 | Hitung | 4 | Ketahanan: nomor IKU tidak disebut | 62 |

---

## A. Pertanyaan Definisi / Konsep

### D01 — Apa itu IKU 1?
**Jawaban benar:** IKU 1 adalah **Angka Efisiensi Edukasi (AEE) Perguruan Tinggi**, yaitu indikator yang mengukur tingkat keberhasilan mahasiswa menyelesaikan studi **tepat waktu** sesuai masa studi standar, dibandingkan dengan total mahasiswa yang masuk pada periode tertentu. AEE PT dihitung dari **rata-rata tingkat pencapaian AEE setiap program pendidikan**. Sifatnya **IKU Wajib**.
**Sumber:** IKU 1, hlm. 49.
**Kata kunci bukti:** `tepat waktu`, `masa studi standar`

### D02 — Berapa masa tempuh kurikulum dan AEE ideal untuk program Sarjana dan Diploma Tiga?
**Jawaban benar:**
- Sarjana / Sarjana Terapan (D4): masa tempuh **8 semester**, AEE ideal **25%**.
- Diploma Tiga: masa tempuh **6 semester**, AEE ideal **33%**.

**Sumber:** IKU 1 — Ketentuan a & d, hlm. 49.
**Kata kunci bukti:** `aee ideal`, `8 semester`, `25%`

### D03 — Berapa jumlah IKU wajib, IKU pilihan, dan IKU partisipatif?
**Jawaban benar:**
- **7 IKU wajib** bagi seluruh perguruan tinggi.
- **5 IKU pilihan**; PT memilih **2** dari 5.
- PT harus mengusulkan **1 IKU partisipatif**.
- Catatan: IKU 6 (publikasi Scopus/WoS) **wajib bagi PTN-BH**.

**Sumber:** Tabel 5.3 dan catatan a–d, hlm. 48.
**Kata kunci bukti:** `sebanyak 7 (tujuh)`, `partisipatif`

### D04 — Sebutkan IKU yang bersifat wajib.
**Jawaban benar:** IKU 1 (AEE), IKU 2 (lulusan bekerja/studi lanjut/wirausaha dalam 1 tahun), IKU 3 (mahasiswa berkegiatan/berprestasi di luar prodi), IKU 5 (rasio luaran kerja sama), IKU 7 (keterlibatan SDGs), IKU 9 (pendapatan non-UKT), dan IKU 12 (perencanaan kesejahteraan dosen).
**Sumber:** Tabel 5.3, hlm. 48.
**Kata kunci bukti:** `angka efisiensi edukasi`, `kesejahteraan dosen`, `pendapatan non pendidikan`

### D05 — Dari mana data IKU 2 diperoleh, dan bagaimana menentukan jumlah responden minimum?
**Jawaban benar:** Data diperoleh dari **tracer study** yang dilakukan **1 tahun setelah kelulusan**. Responden minimum dihitung dengan **rumus Slovin** dengan **galat (d) 2,3%**: n = N / (N·d² + 1), dengan N = jumlah lulusan.
**Sumber:** IKU 2 — Ketentuan & Formula, hlm. 51–52.
**Kata kunci bukti:** `tracer study`, `slovin`

### D06 — Kegiatan di luar program studi apa saja yang diakui untuk IKU 3?
**Jawaban benar:** Kegiatan harus didampingi dosen pembimbing dan mendapat pengakuan SKS, berupa:
1. magang/praktik kerja (swasta, nirlaba, organisasi multilateral, pemerintah/BUMN/BUMD);
2. program mahasiswa berdampak (sosial/pengabdian masyarakat);
3. pertukaran mahasiswa (dalam/luar negeri, berdasarkan perjanjian kerja sama); dan/atau
4. penelitian/riset di bawah pengawasan dosen atau peneliti.

Prestasi diakui bila berupa kompetisi tingkat provinsi/nasional/internasional, minimal sebagai finalis.
Catatan: magang **tidak dihitung** bagi prodi vokasi yang sudah memiliki magang wajib.
**Sumber:** IKU 3 — Kriteria & Ketentuan, hlm. 53.
**Kata kunci bukti:** `magang`, `pertukaran mahasiswa`, `dosen pembimbing`

### D07 — SDG apa saja yang wajib dan pilihan dalam IKU 7?
**Jawaban benar:** SDG wajib: **SDG 1** (Tanpa Kemiskinan), **SDG 4** (Pendidikan Berkualitas), dan **SDG 17** (Kemitraan). Ditambah **2 SDG pilihan** di luar ketiganya, sesuai keunggulan PT, dan harus dituangkan dalam dokumen resmi (Renstra atau laporan kinerja tahunan).
**Sumber:** IKU 7 — Ketentuan, hlm. 58.
**Kata kunci bukti:** `sdg 17`, `2 (dua) tujuan sdgs lain`

### D08 — Pendapatan apa saja yang tidak termasuk dalam perhitungan IKU 9?
**Jawaban benar:**
1. SPP/UKT/biaya kuliah mahasiswa;
2. iuran pengembangan institusi;
3. subsidi langsung pemerintah (belanja pegawai, operasional, BOPTN, BPPTNBH, dan sejenisnya);
4. sumbangan/filantropi yang tidak masuk laporan keuangan resmi; dan
5. dana pokok dana abadi (*endowment fund*).

**Sumber:** IKU 9 — Kriteria b, hlm. 59.
**Kata kunci bukti:** `boptn`, `iuran pengembangan institusi`

### D09 — Penerbit apa yang tidak diperhitungkan dalam IKU 6?
**Jawaban benar:** **MDPI, Frontiers, dan Hindawi**.
**Sumber:** IKU 6 — Ketentuan f, hlm. 63.
**Kata kunci bukti:** `mdpi`, `hindawi`

### D10 — Bagaimana arah penilaian IKU 11c (pelanggaran integritas akademik)?
**Jawaban benar:** **Semakin rendah semakin baik.** Nilai 0 laporan mencerminkan kinerja baik, **asalkan** PT memiliki dan menjalankan mekanisme pencegahan, pelaporan, verifikasi, dan penanganan pelanggaran integritas akademik. Formula: jumlah laporan pelanggaran integritas akademik dalam 1 periode (satuan: laporan).
**Sumber:** IKU 11c, hlm. 67.
**Kata kunci bukti:** `semakin rendah semakin baik`

### D11 ⚠️ — "Lulusan 400, yang bekerja 280, berapa capaian IKU 1?"
**Jawaban benar:** Chatbot harus **mengoreksi**: IKU 1 adalah Angka Efisiensi Edukasi (kelulusan tepat waktu), bukan persentase lulusan bekerja. Data lulusan bekerja termasuk **IKU 2**. Jika dihitung sebagai IKU 2, dengan asumsi seluruh 280 lulusan berbobot 1 (masa tunggu < 6 bulan dan gaji > 1,2× UMP) dan 400 adalah total responden tracer study: 280/400 × 100% = **70%** (lihat H04).
**Sumber:** IKU 1 hlm. 49; IKU 2 hlm. 51.
**Kata kunci bukti:** `tepat waktu`, `masa studi standar`

### D12 ⚠️ — Berapa besaran UKT di Universitas Gadjah Mada tahun 2026?
**Jawaban benar:** Informasi ini **tidak ada** di Buku IKU. Chatbot harus menyatakan tidak menemukan jawabannya di dokumen, bukan mengarang angka.
**Sumber:** — (di luar cakupan).
**Kata kunci bukti:** — (di luar cakupan, tidak ada chunk bukti)

---

## B. Pertanyaan Perhitungan

### H01 — IKU 1: AEE satu program studi
**Pertanyaan:** Prodi S1 memiliki 200 mahasiswa dalam satu tahun akademik. Sebanyak 40 mahasiswa lulus tepat 8 semester. Berapa AEE realisasi dan tingkat pencapaian AEE prodi tersebut?
**Perhitungan:**
- AEE realisasi = 40 / 200 × 100% = 20%
- Tingkat pencapaian = AEE realisasi / AEE ideal S1 = 20% / 25% × 100% = 80%

**Jawaban benar:** AEE realisasi **20%**, tingkat pencapaian **80%**.
**Sumber:** IKU 1 — Formula a & b, hlm. 49.
**Kata kunci bukti:** `aee ideal`, `tingkat pencapaian aee`

### H02 — IKU 1: AEE perguruan tinggi
**Pertanyaan:** Sebuah PT memiliki 3 program pendidikan: D3 dengan AEE realisasi 30%, S1 dengan 22,5%, dan S2 dengan 40%. Berapa AEE PT?
**Perhitungan:**
- D3: 30% / 33% = 90,91%
- S1: 22,5% / 25% = 90,00%
- S2: 40% / 50% = 80,00%
- AEE PT = (90,91% + 90% + 80%) / 3 = **86,97%**

**Jawaban benar:** **86,97%**.
**Sumber:** IKU 1 — Formula c dan contoh perhitungan, hlm. 49–50.
**Kata kunci bukti:** `aee pt`, `tingkat pencapaian`

### H03 — IKU 1: Pengecualian mahasiswa pindah dan DO
**Pertanyaan:** Prodi S1 mencatat 250 mahasiswa pada satu tahun akademik, termasuk 10 mahasiswa pindah dan 15 mahasiswa *drop out*. Sebanyak 45 mahasiswa lulus tepat 8 semester. Berapa AEE realisasi dan tingkat pencapaiannya?
**Perhitungan:**
- Basis = 250 − 10 − 15 = 225 (mahasiswa pindah dan DO tidak dihitung)
- AEE realisasi = 45 / 225 × 100% = 20%
- Tingkat pencapaian = 20% / 25% = 80%

**Jawaban benar:** AEE realisasi **20%**, tingkat pencapaian **80%**. Jawaban 45/250 = 18% **salah**.
**Sumber:** IKU 1 — Ketentuan c, hlm. 49.
**Kata kunci bukti:** `drop out`, `mahasiswa pindah`

### H04 — IKU 2: Lulusan bekerja (satu kategori)
**Pertanyaan:** Tracer study mengumpulkan 400 responden lulusan S1. Sebanyak 280 lulusan bekerja dengan masa tunggu < 6 bulan dan gaji > 1,2× UMP; sisanya belum bekerja. Berapa capaian IKU 2?
**Perhitungan:** (280 × 1) / 400 × 100% = 70%
**Jawaban benar:** **70%**.
**Sumber:** IKU 2 — Kriteria b & Formula, hlm. 51–52.
**Kata kunci bukti:** `masa tunggu`, `1.2x ump`

### H05 — IKU 2: Bobot campuran
**Pertanyaan:** Tracer study mengumpulkan 500 responden lulusan. Rinciannya:
- 200 bekerja, masa tunggu < 6 bulan, gaji > 1,2× UMP
- 100 bekerja, masa tunggu < 1 tahun, gaji > 1,2× UMP
- 50 bekerja, masa tunggu < 1 tahun, gaji < 1,2× UMP
- 30 melanjutkan studi (surat penerimaan < 12 bulan)
- 20 *founder*, < 6 bulan, penghasilan > 1,2× UMP
- 10 *freelancer*, > 6 bulan, penghasilan < 1,2× UMP
- 90 belum bekerja/studi/wirausaha

Berapa capaian IKU 2?
**Perhitungan:**

| Kategori | n | Bobot k | n × k |
|---|---|---|---|
| Bekerja < 6 bln, > 1,2 UMP | 200 | 1 | 200 |
| Bekerja < 1 thn, > 1,2 UMP | 100 | 0,8 | 80 |
| Bekerja < 1 thn, < 1,2 UMP | 50 | 0,6 | 30 |
| Lanjut studi | 30 | 0,6 | 18 |
| Founder < 6 bln, > 1,2 UMP | 20 | 1,2 | 24 |
| Freelancer > 6 bln, < 1,2 UMP | 10 | 0,2 | 2 |
| Belum bekerja | 90 | 0 | 0 |
| **Total** | **500** | | **354** |

Capaian = 354 / 500 × 100% = 70,8%
**Jawaban benar:** **70,8%**.
**Sumber:** IKU 2 — Kriteria b–d & Formula, hlm. 51–52.
**Kata kunci bukti:** `freelancer`, `bobot = 0,8`

### H06 — IKU 2: Responden minimum (Slovin)
**Pertanyaan:** Jumlah lulusan suatu PT adalah 2.000 orang. Berapa jumlah responden minimum tracer study untuk IKU 2?
**Perhitungan:**
- n = N / (N·d² + 1), dengan d = 2,3% = 0,023
- N·d² = 2.000 × 0,000529 = 1,058
- n = 2.000 / 2,058 = 971,8 → dibulatkan ke atas

**Jawaban benar:** **972 responden**.
**Sumber:** IKU 2 — Formula Responden Minimum, hlm. 52.
**Kata kunci bukti:** `responden minimum`, `galat`
**Catatan:** rumus di buku tertulis "× 100%", tetapi hasil yang bermakna adalah jumlah orang, bukan persentase.

### H07 — IKU 3: Kegiatan SKS dan prestasi
**Pertanyaan:** Sebuah PT memiliki 1.000 mahasiswa S1/Diploma. Rinciannya:
- 100 mahasiswa magang 20 SKS
- 150 mahasiswa pertukaran 8 SKS
- 50 mahasiswa riset 4 SKS
- 5 mahasiswa juara 1 lomba nasional
- 10 mahasiswa finalis lomba internasional

Berapa capaian IKU 3?
**Perhitungan:**

| Kategori | n | Bobot k | n × k |
|---|---|---|---|
| Kegiatan ≥ 10 SKS | 100 | 1 | 100 |
| Kegiatan 6–10 SKS | 150 | 0,6 | 90 |
| Kegiatan ≤ 5 SKS | 50 | 0,4 | 20 |
| Juara 1 nasional | 5 | 0,6 | 3 |
| Finalis internasional | 10 | 0,2 | 2 |
| **Total** | | | **215** |

Capaian = 215 / 1.000 × 100% = 21,5%
**Jawaban benar:** **21,5%**.
**Sumber:** IKU 3 — Formula & Ketentuan Bobot, hlm. 53–54.
**Kata kunci bukti:** `5 sks, bobot = 0,4`, `finalis, bobot = 0,2`

### H08 — IKU 3: Prestasi saja
**Pertanyaan:** Dari 500 mahasiswa, prestasi yang tercatat adalah 2 juara 1 internasional, 4 juara 2 tingkat provinsi, dan 20 finalis tingkat provinsi. Tidak ada kegiatan SKS di luar prodi. Berapa capaian IKU 3?
**Perhitungan:**
- (2 × 1) + (4 × 0,2) + (20 × 0,05) = 2 + 0,8 + 1 = 3,8
- 3,8 / 500 × 100% = 0,76%

**Jawaban benar:** **0,76%**.
**Sumber:** IKU 3 — Ketentuan Bobot Prestasi, hlm. 54.
**Kata kunci bukti:** `juara harapan`, `finalis, bobot = 0,05`

### H09 — IKU 5: Rasio luaran kerja sama
**Pertanyaan:** PT memiliki 120 kerja sama. Dari kerja sama itu dihasilkan 30 karya (judul) yang telah dimanfaatkan oleh mitra, melibatkan total 90 dosen. Berapa capaian IKU 5?
**Perhitungan:** 30 / 120 × 100% = 25%
**Jawaban benar:** **25%**. Yang dihitung adalah **jumlah judul/karya, bukan jumlah dosen**, sehingga angka 90 tidak dipakai.
**Sumber:** IKU 5 — Formula & Keterangan, hlm. 57.
**Kata kunci bukti:** `total kerjasama perguruan tinggi`, `bukan jumlah dosen`

### H10 — IKU 6: Publikasi berbobot kuartil
**Pertanyaan:** Total publikasi PT dalam satu periode adalah 200, terdiri atas 10 jurnal Top Tier, 40 Q1, 50 Q2, 30 Q3, 20 Q4, dan 50 publikasi tidak terindeks Scopus/WoS. Berapa capaian IKU 6?
**Perhitungan:**
- (10 × 1,2) + (40 × 1) + (50 × 0,75) + (30 × 0,5) + (20 × 0,25)
- = 12 + 40 + 37,5 + 15 + 5 = 109,5
- 109,5 / 200 × 100% = 54,75%

**Jawaban benar:** **54,75%**.
**Sumber:** IKU 6 — Kriteria a & Formula, hlm. 63.
**Kata kunci bukti:** `top tier`, `bobot 1,2`, `q4`

### H11 — IKU 6: Bonus kolaborasi internasional
**Pertanyaan:** Total publikasi 20, terdiri atas 4 artikel Q1 hasil kolaborasi dengan penulis luar negeri, 6 artikel Q1 tanpa kolaborasi, dan 10 prosiding internasional terindeks Scopus. Berapa capaian IKU 6?
**Perhitungan:**
- Q1 kolaborasi: 4 × (1 + 0,25) = 5
- Q1 biasa: 6 × 1 = 6
- Prosiding: 10 × 0,25 = 2,5
- Total = 13,5 → 13,5 / 20 × 100% = 67,5%

**Jawaban benar:** **67,5%**.
**Sumber:** IKU 6 — Kriteria b & c, hlm. 63.
**Kata kunci bukti:** `kolaborasi internasional`, `prosiding internasional`
**Catatan:** frasa "tambahan bobot sebesar 0,25 dari bobot dasar" bisa dibaca +0,25 atau +25%. Soal ini sengaja memakai Q1 (bobot dasar 1) sehingga kedua tafsiran menghasilkan angka yang sama.

### H12 — IKU 7: Keterlibatan SDGs
**Pertanyaan:** Dari 60 program SDGs PT, 45 program berkontribusi pada SDG 1, 4, 17, dan 2 SDG pilihan. Berapa capaian IKU 7?
**Perhitungan:** 45 / 60 × 100% = 75%
**Jawaban benar:** **75%**.
**Sumber:** IKU 7 — Formula, hlm. 58.
**Kata kunci bukti:** `total program sdg`

### H13 — IKU 9: Pendapatan non-UKT
**Pertanyaan:** Total pendapatan PT dalam satu tahun anggaran adalah Rp500 miliar, terdiri atas:
- UKT Rp300 miliar
- BOPTN Rp80 miliar
- hibah riset kompetitif Rp50 miliar
- jasa konsultasi dan pelatihan Rp40 miliar
- unit bisnis (hotel, penerbitan) Rp20 miliar
- hasil investasi dana abadi Rp10 miliar

Berapa capaian IKU 9?
**Perhitungan:**
- Non-mahasiswa = 50 + 40 + 20 + 10 = Rp120 miliar (UKT dan BOPTN tidak dihitung)
- 120 / 500 × 100% = 24%

**Jawaban benar:** **24%**. Jawaban yang memasukkan BOPTN (200/500 = 40%) **salah**.
**Sumber:** IKU 9 — Kriteria & Formula, hlm. 59.
**Kata kunci bukti:** `boptn`, `dana abadi`

### H14 — IKU 4: Dosen rekognisi internasional
**Pertanyaan:** PT memiliki 300 dosen dalam satu tahun terakhir; 45 dosen ber-NUPTK mendapat rekognisi internasional. Berapa capaian IKU 4?
**Perhitungan:** 45 / 300 × 100% = 15%
**Jawaban benar:** **15%**.
**Sumber:** IKU 4 — Formula, hlm. 62.
**Kata kunci bukti:** `nuptk`, `rekognisi internasional`

### H15 — IKU 8: SDM penyusun kebijakan
**Pertanyaan:** Dari 400 SDM PT (dosen/peneliti), 12 orang terlibat langsung dalam penyusunan kebijakan nasional/daerah/industri, dibuktikan dengan SK atau undangan resmi. Berapa capaian IKU 8?
**Perhitungan:** 12 / 400 × 100% = 3%
**Jawaban benar:** **3%**.
**Sumber:** IKU 8 — Formula, hlm. 64.
**Kata kunci bukti:** `penyusunan kebijakan`, `total sdm pt`

### H16 — IKU 11b: Predikat SAKIP
**Pertanyaan:** Nilai akhir evaluasi SAKIP sebuah PT adalah 82. Apa predikatnya?
**Jawaban benar:** Predikat **A (sangat baik)**, rentang nilai 80–89: efektif dan efisien, menghasilkan kinerja di atas target.
**Sumber:** IKU 11b — Skala dan Predikat, hlm. 66.
**Kata kunci bukti:** `sakip`, `sangat baik`

### H17 — IKU 11d: Pencegahan dan penanganan
**Pertanyaan:** PT merencanakan 24 kegiatan pencegahan dan penanganan kekerasan, narkoba, dan korupsi; 18 kegiatan terlaksana. Berapa capaian IKU 11d?
**Perhitungan:** 18 / 24 × 100% = 75%
**Jawaban benar:** **75%**.
**Sumber:** IKU 11d — Formula, hlm. 68.
**Kata kunci bukti:** `total kegiatan yang direncanakan`

### H18 — IKU 12: Standar penghasilan dosen
**Pertanyaan:** UMP di provinsi tempat PT berada adalah Rp3.000.000. Berapa penghasilan minimum dosen dengan jabatan Lektor dan Profesor menurut IKU 12?
**Perhitungan:**
- Lektor: ≥ 3 × UMP = 3 × Rp3.000.000 = Rp9.000.000
- Profesor: ≥ 6 × UMP = 6 × Rp3.000.000 = Rp18.000.000

**Jawaban benar:** Lektor minimal **Rp9.000.000**, Profesor minimal **Rp18.000.000**.
**Sumber:** IKU 12 — Kriteria b.2, hlm. 60.
**Kata kunci bukti:** `lektor kepala`, `ump`

---

## C. Pertanyaan Ketahanan (bahasa santai, typo, format angka/uang tidak baku)

Soal di bagian ini menanyakan hal yang sama dengan soal A/B, tetapi ditulis seperti user sungguhan: singkatan, salah ketik, dan angka/uang yang tidak baku. Yang diuji bukan rumusnya, melainkan apakah chatbot **membaca angka dengan benar** dan tetap memilih rumus yang tepat.

Aturan baca angka Indonesia yang harus dipatuhi chatbot:
- Titik = pemisah ribuan (`1.341` = 1341, `Rp1.250.000.000` = 1,25 miliar); koma = desimal (`22,5%`, `0,2 M`).
- `rb` = ribu; `jt` = juta; `M`, `miliar`, `milyar` = miliar (bukan *million*).
- Untuk rasio, satuan boleh apa saja asal **konsisten** di pembilang dan penyebut. Untuk IKU 12 (rupiah), hasil harus dalam rupiah penuh.

### D13 — Definisi IKU 1 dengan bahasa santai
**Pertanyaan:** aee tu apaan sih? ngukur apa?
**Jawaban benar:** AEE = Angka Efisiensi Edukasi (IKU 1), mengukur keberhasilan mahasiswa menyelesaikan studi **tepat waktu** sesuai masa studi standar (sama dengan D01).
**Sumber:** IKU 1, hlm. 49.
**Kata kunci bukti:** `tepat waktu`, `masa studi standar`

### D14 — Pendapatan yang tidak dihitung IKU 9 (typo)
**Pertanyaan:** pendptan apa aj yg ga diitung di iku9?
**Jawaban benar:** SPP/UKT, iuran pengembangan institusi, subsidi langsung pemerintah (termasuk BOPTN/BPPTNBH), filantropi yang tidak tercatat, dan pokok dana abadi (sama dengan D08).
**Sumber:** IKU 9 — Kriteria b, hlm. 59.
**Kata kunci bukti:** `boptn`, `iuran pengembangan institusi`

### H19 — IKU 1: typo & singkatan
**Pertanyaan:** brp aee s1 klo yg lulus tepat wktu cm 40 org dr 200 mhs?
**Perhitungan:** sama dengan H01: 40 / 200 = 20%; 20% / 25% = 80%.
**Jawaban benar:** AEE realisasi **20%**, tingkat pencapaian **80%**.
**Sumber:** IKU 1 — Formula a & b, hlm. 49.
**Kata kunci bukti:** `aee ideal`, `tingkat pencapaian aee`

### H20 — IKU 1: desimal koma
**Pertanyaan:** realisasi aee kampus kmi: D3 30%, S1 22,5%, S2 40%. aee pt nya jd brp ya?
**Perhitungan:** sama dengan H02; "22,5%" harus dibaca 22.5, bukan 225 atau 22.
**Jawaban benar:** **86,97%**.
**Sumber:** IKU 1 — Formula c dan contoh perhitungan, hlm. 49–50.
**Kata kunci bukti:** `aee pt`, `tingkat pencapaian`

### H21 — IKU 2: titik pemisah ribuan
**Pertanyaan:** lulusan kampus kami 1.341 org, minimal responden tracer study nya brp?
**Perhitungan:** "1.341" = 1341. N·d² = 1341 × 0,000529 = 0,7094; n = 1341 / 1,7094 = 784,5 → dibulatkan ke atas.
**Jawaban benar:** **785 responden**.
**Sumber:** IKU 2 — Formula Responden Minimum, hlm. 52.
**Kata kunci bukti:** `responden minimum`, `galat`

### H22 — IKU 2: singkatan "rb"
**Pertanyaan:** klo lulusannya 2rb orang, responden minimum tracer studi brp
**Perhitungan:** "2rb" = 2000; sama dengan H06.
**Jawaban benar:** **972 responden**.
**Sumber:** IKU 2 — Formula Responden Minimum, hlm. 52.
**Kata kunci bukti:** `responden minimum`, `galat`

### H23 — IKU 5: typo
**Pertanyaan:** kerjsama PT kita ada 120, luaran nya 30 judul. capaian iku5 brp persen?
**Perhitungan:** 30 / 120 × 100% = 25% (sama dengan H09).
**Jawaban benar:** **25%**.
**Sumber:** IKU 5 — Formula & Keterangan, hlm. 57.
**Kata kunci bukti:** `total kerjasama perguruan tinggi`, `bukan jumlah dosen`

### H24 — IKU 7: typo
**Pertanyaan:** dr 50 progam sdgs, 25 yg kontribusi ke sdg 1,4,17 + 2 sdg pilihan. capaian iku 7 brapa
**Perhitungan:** 25 / 50 × 100% = 50%.
**Jawaban benar:** **50%**.
**Sumber:** IKU 7 — Formula, hlm. 58.
**Kata kunci bukti:** `total program sdg`

### H25 — IKU 9: satuan "M" (miliar)
**Pertanyaan:** total pendapatan PT 500 M. rinciannya ukt 300M, boptn 80 M, hibah riset 50M, konsultasi 40 M, unit bisnis 20M, hasil dana abadi 10 M. iku 9 brp?
**Perhitungan:** sama dengan H13 (dalam miliar): diakui = 50 + 40 + 20 + 10 = 120; 120 / 500 × 100% = 24%.
**Jawaban benar:** **24%**.
**Sumber:** IKU 9 — Kriteria & Formula, hlm. 59.
**Kata kunci bukti:** `boptn`, `dana abadi`

### H26 — IKU 9: campuran Rp, "jt", dan "juta"
**Pertanyaan:** pendapatan total Rp1.250.000.000, terdiri dr ukt rp 900jt, kontrak riset 150 juta, royalti Rp50.000.000, sisanya 150jt dari boptn. capaian iku 9?
**Perhitungan:** semua dalam juta: total 1.250; diakui = kontrak riset 150 + royalti 50 = 200 (UKT & BOPTN tidak dihitung); 200 / 1.250 × 100% = 16%.
**Jawaban benar:** **16%**.
**Sumber:** IKU 9 — Kriteria & Formula, hlm. 59.
**Kata kunci bukti:** `boptn`, `dana abadi`

### H27 — IKU 9: "milyar" dan desimal koma "0,2 M"
**Pertanyaan:** total pendapatan 2 milyar: hibah riset 300 jt, konsultasi 0,2 M, ukt 1,5 M. hitung iku 9 nya
**Perhitungan:** dalam juta: total 2.000; diakui = 300 + 200 = 500; 500 / 2.000 × 100% = 25%.
**Jawaban benar:** **25%**.
**Sumber:** IKU 9 — Kriteria & Formula, hlm. 59.
**Kata kunci bukti:** `boptn`, `dana abadi`

### H28 — IKU 12: "3,5jt"
**Pertanyaan:** ump disini 3,5jt, penghasilan minimal dosen lektor kepala brp?
**Perhitungan:** 4 × Rp3.500.000 = Rp14.000.000.
**Jawaban benar:** Lektor kepala minimal **Rp14.000.000**.
**Sumber:** IKU 12 — Kriteria b.2, hlm. 60.
**Kata kunci bukti:** `lektor kepala`, `ump`

### H29 — IKU 12: "Rp 4.250.000" dengan spasi
**Pertanyaan:** UMP prov kami Rp 4.250.000 , brp penghasilan min dosen asisten ahli sm profesor?
**Perhitungan:** asisten ahli 1,5 × Rp4.250.000 = Rp6.375.000; profesor 6 × Rp4.250.000 = Rp25.500.000.
**Jawaban benar:** Asisten ahli minimal **Rp6.375.000**, profesor minimal **Rp25.500.000**.
**Sumber:** IKU 12 — Kriteria b.2, hlm. 60.
**Kata kunci bukti:** `lektor kepala`, `ump`

### H30 — IKU 4: nomor IKU tidak disebut
**Pertanyaan:** dosen kami 250 org setahun terakhir, yg ber-NUPTK & dpt rekognisi internasional 18 org. capaiannya brp?
**Perhitungan:** chatbot harus mengenali ini sebagai IKU 4: 18 / 250 × 100% = 7,2%.
**Jawaban benar:** **7,2%** (IKU 4).
**Sumber:** IKU 4 — Formula, hlm. 62.
**Kata kunci bukti:** `nuptk`, `rekognisi internasional`
