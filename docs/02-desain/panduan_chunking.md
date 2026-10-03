# Panduan Chunking v2 untuk bge-m3

Panduan ini menjelaskan cara chunking yang dipakai di proyek, alasannya (best practice beserta sumbernya), dan langkah-langkah menjalankannya sampai evaluasi.

## 1. Best practice yang dipakai

### a. Ikuti struktur dokumen, bukan "semantic chunking" berbasis embedding

Ada teknik *semantic chunking*: dokumen dipotong di titik ketika kemiripan embedding antarkalimat turun. Penelitian Vectara (2024) membandingkannya dengan potongan biasa di tiga tugas retrieval dan menyimpulkan **biaya komputasinya tidak sebanding dengan hasilnya**, karena keuntungannya tidak konsisten ([Vectara](https://vectara.com/blog/is-semantic-chunking-worth-the-computational-cost), [arXiv 2410.13070](https://arxiv.org/abs/2410.13070v1)).

Dokumen IKU sudah punya struktur yang jelas: bab, subbab, dan tabel IKU dengan baris Definisi / Kriteria / Ketentuan / Formula. Jadi chunking **mengikuti struktur itu**. Satu chunk = satu bagian yang utuh maknanya, misalnya "IKU 3 – Formula beserta tabel bobotnya". Ini juga yang membuat chunk tidak memotong rumus di tengah.

bge-m3 tetap dipakai, tapi di dua tempat:
- **tokenizer bge-m3** untuk mengukur panjang chunk dalam token yang benar-benar dilihat model;
- **model bge-m3** untuk embedding.

### b. Ukuran chunk: maksimal 512 token

bge-m3 sanggup membaca sampai 8.192 token ([model card](https://huggingface.co/BAAI/bge-m3)). Tapi satu vektor yang mewakili teks sangat panjang menjadi "rata-rata" dari banyak topik, sehingga kurang tajam untuk pertanyaan spesifik. Karena itu:
- batas atas **512 token** (median hasil sekarang ±256 token);
- chunk di bawah **64 token** digabung ke chunk sebelumnya di bagian yang sama, atau ke saudara bagiannya;
- chunk yang terlalu besar dipecah di batas **baris tabel** atau **kalimat/butir**, dengan header tabel diulang.

Angka 512/64 adalah titik awal, bukan angka keramat. Coba variasi (misalnya 384 atau 768) lalu bandingkan dengan `eval_retrieval.py`.

### c. Header konteks di setiap chunk (contextual chunk header)

Setiap chunk diawali header yang **ikut di-embed**:

```
[Buku IKU Diktisaintek Berdampak V1 | 3 IKU 3: Persentase Mahasiswa ... | Bagian: Formula | hlm. 53–54]
```

Tujuannya agar chunk tetap bermakna walau dibaca terpisah dari dokumennya. Anthropic melaporkan bahwa menambahkan konteks ke setiap chunk sebelum embedding menurunkan kegagalan retrieval top-20 sebesar 35%, menjadi 49% bila digabung BM25, dan 67% bila ditambah reranker ([Anthropic, Contextual Retrieval](https://www.anthropic.com/news/contextual-retrieval)). Proyek ini memakai versi sederhananya (header dari struktur dokumen, tanpa LLM), yang gratis dan deterministik.

### d. Aturan pakai bge-m3

- **Query tidak perlu instruksi/prefix** apa pun ([model card](https://huggingface.co/BAAI/bge-m3)).
- Embedding dinormalisasi, dan koleksi Chroma memakai jarak **cosine** (`hnsw:space = cosine`).
- Langkah lanjutan yang disarankan model card: **hybrid retrieval** (dense + sparse/BM25) dan **reranker** `bge-reranker-v2-m3`. Belum diterapkan di sini; kerjakan setelah chunking dievaluasi.

### e. Tidak ada informasi yang hilang, dan dibuktikan

`validate_chunks.py` mengecek:
- setiap blok processing masuk ke chunk;
- cakupan kata per blok ≥ 99%;
- **0 angka hilang**;
- `source_notes` (catatan cacat sumber) ikut terbawa;
- tidak ada chunk yang melewati batas token.

## 2. Apa yang dilakukan `chunk_structured.py`

1. **Section** = heading + blok-blok di bawahnya. Heading tidak pernah menjadi chunk sendiri; judulnya masuk header konteks.
2. **Tabel definisi IKU** yang terpotong antarhalaman digabung, lalu dipecah per bagian (Definisi, Kriteria, Ketentuan, Formula + Satuan). Baris lanjutan dengan label kosong mewarisi label di atasnya. Contoh: tabel bobot prestasi IKU 3 di hlm. 54 ikut ke chunk Formula hlm. 53.
3. **Tabel Lampiran** (format `No. | IKU | Bagian | Isi`, banyak IKU dalam satu tabel) dipecah per IKU dan per bagian, dan nama IKU masuk ke header.
4. **Metadata** setiap chunk: `source_priority` (Buku = 1, PPT = 2), `doc_part` (utama/lampiran), `iku_id` (IKU LLDIKTI diberi awalan `LLDIKTI-`), `bagian`, `page_start`/`page_end`, `source_notes`.
5. Field **`text`** (header + isi) adalah yang di-embed dan disimpan di Chroma; field **`content`** adalah isi tanpa header.

## 3. Langkah eksekusi

Jalankan dari root repo dengan venv aktif (lihat bagian *Setup* di [README](../../README.md)):

```powershell
.venv\Scripts\Activate.ps1
```

| # | Perintah | Hasil yang diharapkan |
|---|---|---|
| 1 | `python src/processing/process_markdown.py` | `data/processed/` diperbarui (Buku ±815 blok, PPT ±601 blok) |
| 2 | `python src/processing/validate_processed.py` | `number_coverage_pct: 100.0`, `table_row_mismatches: 0` untuk kedua dokumen |
| 3 | `python src/chunking/chunk_structured.py` | ±611 chunk, `> max_tokens: 0` → `data/chunks/chunks.jsonl` |
| 4 | `python src/chunking/validate_chunks.py` | `HASIL AKHIR: SEMUA OK - tidak ada informasi yang hilang` |
| 5 | `python src/embedding/embed_chunks.py --input data/chunks/chunks.jsonl --output-dir data/embeddings` | `Shape: (611, 1024)` → `data/embeddings/` |
| 6 | `python src/vectordb/build_chroma.py --embeddings-dir data/embeddings --collection pmpt_qa_v2 --reset` | `Distance: cosine`, `Jumlah data: 611` |
| 7 | `python src/evaluation/eval_retrieval.py --collection pmpt_qa_v2 --metadata data/embeddings/metadata.jsonl --oos-threshold 0.45` | Laporan di `reports/evaluation/retrieval_eval_pmpt_qa_v2_*.md` |

**Jangan lanjut ke langkah berikutnya bila validasi (langkah 2 atau 4) tidak OK.**

Catatan langkah 5: bila GPU kehabisan memori (`CUDA out of memory`), tambahkan `--batch-size 4`.

Catatan langkah 6: koleksi lama `pmpt_qa` tidak disentuh, jadi tetap bisa dipakai sebagai pembanding.

Catatan langkah 7, soal `--oos-threshold`: koleksi baru memakai jarak **cosine** (0 = identik), sedangkan koleksi lama memakai L2 kuadrat. Untuk vektor ternormalisasi, L2² = 2 × cosine, jadi ambang lama 0,9 setara dengan **0,45** di koleksi baru. Angka *distance* antara laporan lama dan baru tidak bisa dibandingkan langsung, tapi Hit@k, MRR, dan halaman sitasi bisa.

## 4. Membaca hasil evaluasi

Bandingkan dengan baseline (koleksi lama `pmpt_qa`, laporan `retrieval_eval_20261003_140456.md`):

| Metrik | Baseline |
|---|---|
| Hit@1 | 15/29 (51,7%) |
| Hit@3 | 22/29 (75,9%) |
| Hit@5 | 25/29 (86,2%) |
| MRR@5 | 0,649 |
| Halaman sitasi benar | 15/23 (65%) |
| Hasil #1 dari PPT | 12/29 |

Bila ada soal yang masih MISS, buka bagian "Detail per soal" di laporan:
- **"bukti tidak ada di corpus":** kata kunci bukti soal itu tidak ada di satu chunk pun. Cek apakah chunknya memang terpecah, atau kata kuncinya perlu disesuaikan dengan format chunk baru.
- **"bukti di rank mentah N":** chunknya ada tapi kalah peringkat. Ini yang diperbaiki di langkah berikutnya (dedup PPT, dahulukan Buku, hybrid/BM25, reranker).

## 5. Keterbatasan yang diketahui

- Jalur bagian (`section_path`) masih mengikuti level heading dari LlamaParse yang kadang tidak konsisten, misalnya "Langkah Strategis > 4.11. ALOKASI ...". Ini memengaruhi tampilan header, bukan kelengkapan isi.
- Sisa 8 chunk pendek (< 12 kata) adalah bagian yang memang berdiri sendiri dan tidak punya saudara untuk digabung.
- Retriever masih membuang dokumen < 80 karakter dan belum mendahulukan Buku atau membuang duplikat PPT. Itu langkah perbaikan retriever berikutnya.
