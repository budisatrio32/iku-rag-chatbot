# Uji Jawaban Chatbot (retriever + LLM + kalkulator)

- Waktu: 2026-10-05 19:03:20
- Model LLM: `gemini-3.8-flash`
- Soal: 3 (hitungan 1, definisi & jebakan 2)

## Ringkasan

| Metrik | Hasil |
|---|---|
| Lulus semua pemeriksaan otomatis | **3/3** |
| Hitungan: kalkulator dipanggil | 1/1 |
| Hitungan: hasil kalkulator = kunci | 1/1 |
| Hitungan: angka kunci ada di jawaban | 1/1 |
| Halaman sitasi benar (hitungan) | 1/1 |
| Halaman sitasi benar (definisi) | 1/1 |
| Soal error (API/kuota) | 0 |
| Jawaban dengan peringatan chatbot | 0 |

| ID | Status | Pemeriksaan yang gagal |
|---|---|---|
| D09 | ✅ | - |
| D12 | ✅ | - |
| H07 | ✅ | - |

Pemeriksaan otomatis hanya bantuan. Baca jawaban lengkap di bawah dan bandingkan dengan jawaban yang diharapkan.

## Detail per soal

### D09 — ✅ LULUS

**Pertanyaan:** Penerbit apa yang tidak diperhitungkan dalam IKU 6?

**Jawaban chatbot:**

```text
Berdasarkan ketentuan IKU 6, penerbit yang tidak diperhitungkan meliputi penerbit seperti **MDPI**, **Frontiers**, dan **Hindawi Publisher** [1].
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

### D12 — ✅ LULUS

**Pertanyaan:** Berapa besaran UKT di Universitas Gadjah Mada tahun 2026?

**Jawaban chatbot:**

```text
Informasi mengenai besaran UKT di Universitas Gadjah Mada tahun 2026 tidak ditemukan di dalam dokumen IKU.
```

**Jawaban yang diharapkan:**

- Halaman kunci: -

Informasi ini **tidak ada** di Buku IKU. Chatbot harus menyatakan tidak menemukan jawabannya di dokumen, bukan mengarang angka.

*Catatan soal:* Soal di luar cakupan: chatbot harus menolak, bukan mengarang angka UKT.

**Pemeriksaan otomatis:**

- ✅ fakta: tidak ditemukan / tidak terdapat / tidak tersedia / tidak ada informasi / tidak dijelaskan / tidak memuat
- ✅ tidak mengarang sitasi

### H07 — ✅ LULUS

**Pertanyaan:** Sebuah PT memiliki 1.000 mahasiswa S1/Diploma. Rinciannya: - 100 mahasiswa magang 20 SKS - 150 mahasiswa pertukaran 8 SKS - 50 mahasiswa riset 4 SKS - 5 mahasiswa juara 1 lomba nasional - 10 mahasiswa finalis lomba internasional Berapa capaian IKU 3?

**Jawaban chatbot:**

```text
Berdasarkan formula dan ketentuan bobot pada IKU 3 [1], capaian IKU 3 dihitung sebagai berikut:

**Langkah Perhitungan:**
1. **Kegiatan 20 SKS** (bobot $\ge 10$ SKS = 1):  
   $100 \times 1 = 100$ [1]
2. **Kegiatan 8 SKS** (bobot 6–10 SKS = 0,6):  
   $150 \times 0,6 = 90$ [1]
3. **Kegiatan 4 SKS** (bobot $\le 5$ SKS = 0,4):  
   $50 \times 0,4 = 20$ [1]
4. **Prestasi Juara 1 Nasional** (bobot = 0,6):  
   $5 \times 0,6 = 3$ [1]
5. **Prestasi Finalis Internasional** (bobot = 0,2):  
   $10 \times 0,2 = 2$ [1]

**Total Pembilang ($\sum n_i k_i$):**  
$100 + 90 + 20 + 3 + 2 = 215$ [1]

**Perhitungan Capaian:**  
$$\text{Capaian IKU 3} = \frac{215}{1.000} \times 100\% = 21,5\% \text{ [1]}$$

Dengan demikian, capaian IKU 3 perguruan tinggi tersebut adalah **21,5%** [1].
```

**Sitasi chatbot:**

- [1] Buku IKU Diktisaintek Berdampak V1, hlm. 53–54 (IKU 3, Formula); juga di Buku (Lampiran Kepmen 358/M/KEP/2025) hlm. 107–108; PPT hlm. 50

**Sumber rumus (kalkulator):**

- Buku IKU Diktisaintek Berdampak V1, IKU 3 – Formula & Ketentuan Bobot, hlm. 53–54

**Panggilan kalkulator:**

- argumen `{"argumen_json":"{\"kegiatan\":[{\"jumlah\":100,\"sks\":20},{\"jumlah\":150,\"sks\":8},{\"jumlah\":50,\"sks\":4}],\"prestasi\":[{\"jumlah\":5,\"peringkat\":\"juara1\",\"tingkat\":\"nasional\"},{\"jumlah\":10,\"peringkat\":\"finalis\",\"tingkat\":\"internasional\"}],\"total_mahasiswa\":1000}","fungsi":"iku3"}` → 21,50

**Jawaban yang diharapkan:**

- Angka kunci: **21,50**
- Halaman kunci: 53, 54

**21,5%**.

**Pemeriksaan otomatis:**

- ✅ kalkulator dipanggil
- ✅ hasil kalkulator = kunci
- ✅ angka kunci ada di jawaban
- ✅ halaman sitasi benar
