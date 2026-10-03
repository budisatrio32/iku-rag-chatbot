# Chatbot RAG IKU Diktisaintek Berdampak

Chatbot *Retrieval-Augmented Generation* (RAG) untuk penjaminan mutu perguruan tinggi. Chatbot menjawab pertanyaan tentang **Indikator Kinerja Utama (IKU) Diktisaintek Berdampak**: definisi, kriteria, ketentuan, dan perhitungan rumus. Setiap jawaban disertai **sitasi halaman** dari dokumen resmi.

Sumber pengetahuan:

- `Buku IKU Diktisaintek Berdampak_V1.pdf` (143 halaman, sumber utama)
- `PPT IKU Diktisaintek Berdampak_PTS V2.pdf` (sumber pendukung)

## Daftar isi

1. [Status proyek](#status-proyek)
2. [Arsitektur pipeline](#arsitektur-pipeline)
3. [Struktur repositori](#struktur-repositori)
4. [Prasyarat](#prasyarat)
5. [Setup (langkah demi langkah)](#setup-langkah-demi-langkah)
6. [Menjalankan pipeline dari awal](#menjalankan-pipeline-dari-awal)
7. [Pengujian & evaluasi](#pengujian--evaluasi)
8. [Alur kerja pengembangan](#alur-kerja-pengembangan)
9. [Troubleshooting](#troubleshooting)
10. [Dokumentasi lanjutan](#dokumentasi-lanjutan)

## Status proyek

| Tahap | Status | Script utama |
|---|---|---|
| 1. Parsing PDF → Markdown (+ penanda halaman) | ✅ Selesai | `src/parsing/parse_pdf.py` |
| 2. Processing → JSON terstruktur + validasi | ✅ Selesai | `src/processing/` |
| 3. Chunking berbasis struktur (bge-m3, ≤ 512 token) | ✅ Selesai | `src/chunking/chunk_structured.py` |
| 4. Embedding `BAAI/bge-m3` | ✅ Selesai | `src/embedding/embed_chunks.py` |
| 5. Vector DB ChromaDB (cosine) | ✅ Selesai | `src/vectordb/build_chroma.py` |
| 6. Retrieval hybrid (dense + BM25 + RRF, IKU boost, dedupe) | ✅ Selesai | `src/retrieval/retriever.py` |
| 6b. Kalkulator rumus IKU (*formula registry*) | ✅ Selesai | `src/calculator/iku_formulas.py` |
| 7. LLM + sitasi (generation) | ⬜ Berikutnya | – |
| 8. Antarmuka (API / UI chat) | ⬜ Belum | – |

**Hasil evaluasi terakhir** (test set 30 soal, koleksi `pmpt_qa_v2`, 605 chunk). Laporan lengkap ada di [reports/evaluation/](reports/evaluation/).

| Metrik | Baseline v1 | Sekarang (v2) |
|---|---|---|
| Hit@1 | 15/29 (51,7%) | **22/29 (75,9%)** |
| Hit@5 | 25/29 (86,2%) | **26/29 (89,7%)** |
| MRR@5 | 0,649 | **0,822** |
| Halaman sitasi benar | 15/23 (65%) | **25/26 (96,2%)** |
| Soal hitungan: hasil benar | – | **18/18** |
| Soal hitungan: halaman sitasi benar | – | **17/18** |

## Arsitektur pipeline

```text
data/raw/*.pdf
   │  [1] parse_pdf.py          LlamaParse (butuh API key, berbayar kredit)
   ▼
data/parsed/*.md (+ .pages.json)
   │  [2] process_markdown.py   → validate_processed.py, validate_cross_source.py
   ▼
data/processed/*_processed.json
   │  [3] chunk_structured.py   → validate_chunks.py
   ▼
data/chunks/chunks.jsonl
   │  [4] embed_chunks.py       bge-m3, GPU disarankan
   ▼
data/embeddings/embeddings.npy + metadata.jsonl
   │  [5] build_chroma.py
   ▼
data/vectorstore/  (ChromaDB, koleksi pmpt_qa_v2)
   │  [6] retriever.py          dense + BM25 + RRF → IKU boost → dedupe → (rerank)
   ▼
top-k chunk + sitasi halaman ──► [7] LLM (berikutnya)
                                  ▲
       [6b] iku_formulas.py ──────┘  rumus dihitung deterministik, bukan oleh LLM
```

Semua artefak tahap 1–4 **sudah di-commit**, jadi anggota tim tidak perlu mengulang parsing (berbayar) atau embedding (lama tanpa GPU). Hanya `data/vectorstore/` yang perlu dibangun sendiri karena berupa database biner (beberapa detik).

## Struktur repositori

```text
iku-rag-chatbot/
├── .github/
│   ├── workflows/ci.yml          # CI: cek sintaks + unit test di setiap push/PR
│   ├── ISSUE_TEMPLATE/           # template laporan bug & usulan fitur
│   └── pull_request_template.md
├── data/                         # lihat data/README.md
│   ├── raw/                      # PDF sumber (input)
│   ├── parsed/                   # [1] Markdown hasil LlamaParse
│   ├── processed/                # [2] JSON terstruktur per dokumen
│   ├── chunks/                   # [3] chunks.jsonl
│   ├── embeddings/               # [4] vektor bge-m3 + metadata
│   ├── vectorstore/              # [5] ChromaDB (di-generate, tidak di-commit)
│   ├── metadata/                 # catatan cacat dokumen sumber (known_source_issues.json)
│   ├── evaluation/               # test set: 30 soal + input soal hitungan
│   └── legacy/v1/                # artefak pipeline v1 (baseline pembanding)
├── docs/                         # dokumentasi per fase SDLC, lihat docs/README.md
│   ├── 01-analisis/
│   └── 02-desain/
├── reports/
│   ├── validation/               # output script validasi
│   └── evaluation/               # laporan eval retrieval & uji hitungan (bertanggal)
├── src/                          # satu folder = satu tahap pipeline
│   ├── parsing/  processing/  chunking/  embedding/
│   ├── vectordb/ retrieval/   calculator/ evaluation/
│   └── legacy/                   # script v1 yang sudah tidak dipakai
├── tests/                        # unit test (pytest), tanpa GPU
├── .env.example
├── requirements.txt              # dependency runtime
├── requirements-dev.txt          # dependency pengujian
├── CHANGELOG.md
├── CONTRIBUTING.md               # aturan branch, commit, PR
└── README.md
```

## Prasyarat

| Kebutuhan | Keterangan |
|---|---|
| **Python 3.13** | Versi yang sudah diuji: 3.13.5. Cek dengan `python --version` |
| **Git** | Untuk clone & kolaborasi |
| **GPU NVIDIA** (opsional, disarankan) | Diuji di RTX 4050 6 GB dengan CUDA 12.6. Tanpa GPU semua tetap jalan di CPU, hanya lebih lambat |
| **Ruang disk ±8 GB** | PyTorch CUDA ±3 GB, model `bge-m3` ±2,3 GB, reranker opsional ±2,3 GB (cache HuggingFace) |
| **Internet** | Saat pertama kali: unduh dependency & model dari HuggingFace |
| **LlamaCloud API key** (opsional) | Hanya untuk parsing ulang PDF. Hasil parsing sudah ada di repo |

## Setup (langkah demi langkah)

Perintah di bawah memakai **PowerShell (Windows)**. Padanan Linux/macOS diberikan di bagian yang berbeda.

### 1. Clone repositori

```powershell
git clone https://github.com/<username>/iku-rag-chatbot.git
cd iku-rag-chatbot
```

### 2. Buat & aktifkan virtual environment

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

Linux/macOS: `python3 -m venv .venv && source .venv/bin/activate`

Jika muncul error *"running scripts is disabled on this system"*, jalankan sekali:

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

Pastikan prompt diawali `(.venv)` sebelum lanjut.

### 3. Pasang PyTorch (pilih salah satu)

PyTorch dipasang **sebelum** `requirements.txt` agar yang terpasang versi yang sesuai hardware.

```powershell
# GPU NVIDIA (CUDA 12.6)
pip install torch --index-url https://download.pytorch.org/whl/cu126

# CPU saja (tanpa GPU NVIDIA)
pip install torch --index-url https://download.pytorch.org/whl/cpu
```

Cek GPU terdeteksi (harus `True` jika memakai versi CUDA):

```powershell
python -c "import torch; print(torch.__version__, torch.cuda.is_available())"
```

### 4. Pasang dependency proyek

```powershell
pip install -r requirements.txt
pip install -r requirements-dev.txt   # untuk menjalankan unit test
```

### 5. Konfigurasi environment

```powershell
Copy-Item .env.example .env
```

Isi `LLAMA_CLOUD_API_KEY` di `.env` **hanya jika** akan parsing ulang PDF. File `.env` sudah di-`.gitignore`, jadi jangan pernah di-commit.

### 6. Bangun vector database

```powershell
python src/vectordb/build_chroma.py --reset
```

Hasil yang diharapkan: `Collection : pmpt_qa_v2`, `Distance : cosine`, `Jumlah data: 605`.

### 7. Verifikasi instalasi

```powershell
# a. Unit test kalkulator (cepat, tanpa GPU)
pytest

# b. Coba retriever secara interaktif (pertama kali mengunduh bge-m3 ±2,3 GB)
python src/retrieval/test_retrieval.py
#    Pertanyaan: Bagaimana rumus IKU 3?

# c. Evaluasi retrieval lengkap → angkanya harus sama dengan tabel di "Status proyek"
python src/evaluation/eval_retrieval.py
```

Setup selesai bila `pytest` lulus dan `eval_retrieval.py` menghasilkan Hit@1 22/29 serta MRR@5 0,822.

## Menjalankan pipeline dari awal

Pipeline penuh hanya perlu dijalankan bila **dokumen sumber atau logika suatu tahap berubah**. Jalankan dari root repo, berurutan. Cukup mulai dari tahap yang berubah.

| # | Perintah | Output | Hasil yang diharapkan |
|---|---|---|---|
| 1 | `python src/parsing/parse_pdf.py` | `data/parsed/` | Dokumen yang sudah punya hasil di-SKIP (tidak memakai kredit) |
| 2 | `python src/processing/process_markdown.py` | `data/processed/` | Buku ±815 blok, PPT ±601 blok |
| 2a | `python src/processing/validate_processed.py` | `reports/validation/` | `number_coverage_pct: 100.0`, `table_row_mismatches: 0` |
| 2b | `python src/processing/validate_cross_source.py` | `reports/validation/` | Selisih angka Buku vs PPT; yang sudah dikenal ditandai |
| 3 | `python src/chunking/chunk_structured.py` | `data/chunks/chunks.jsonl` | 605 chunk, `> max_tokens: 0` |
| 3a | `python src/chunking/validate_chunks.py` | `reports/validation/` | `HASIL AKHIR: SEMUA OK` |
| 4 | `python src/embedding/embed_chunks.py` | `data/embeddings/` | `Shape: (605, 1024)` |
| 5 | `python src/vectordb/build_chroma.py --reset` | `data/vectorstore/` | `Jumlah data: 605` |
| 6 | `python src/evaluation/eval_retrieval.py` | `reports/evaluation/` | Bandingkan dengan laporan sebelumnya |

> **Jangan lanjut ke tahap berikutnya bila validasi (2a atau 3a) tidak OK.**

Opsi penting:

```powershell
# Parsing
python src/parsing/parse_pdf.py --rebuild   # susun ulang .md dari .pages.json (gratis, tanpa API)
python src/parsing/parse_pdf.py --force     # parsing ulang semua PDF (memakai kredit LlamaCloud)

# Chunking: ukuran chunk
python src/chunking/chunk_structured.py --max-tokens 384 --min-tokens 64

# Embedding: GPU kehabisan memori
python src/embedding/embed_chunks.py --batch-size 4

# Inspeksi chunk
python src/chunking/show_chunks.py --iku 3 --bagian Formula
python src/chunking/show_chunks.py --cari "NUPTK" --maks 3
```

## Pengujian & evaluasi

| Jenis | Perintah | Butuh GPU/model? | Kapan dijalankan |
|---|---|---|---|
| Unit test kalkulator | `pytest` | Tidak | Setiap perubahan; otomatis di CI |
| Validasi data | `validate_processed.py`, `validate_chunks.py` | Tidak | Setelah processing / chunking |
| Evaluasi retrieval | `python src/evaluation/eval_retrieval.py` | bge-m3 | Setelah chunking / embedding / retriever berubah |
| Uji soal hitungan + sitasi | `python src/evaluation/run_calc_tests.py` | bge-m3 | Setelah kalkulator / retriever berubah |

Variasi evaluasi:

```powershell
python src/evaluation/eval_retrieval.py --rerank            # + reranker (unduh ±2,3 GB sekali)
python src/evaluation/run_calc_tests.py --id H07            # satu soal saja

# Baseline v1, untuk perbandingan (bangun koleksinya dulu)
python src/vectordb/build_chroma.py --embeddings-dir data/legacy/v1/embeddings --collection pmpt_qa --reset
python src/evaluation/eval_retrieval.py --preset lama --collection pmpt_qa --metadata data/legacy/v1/embeddings/metadata.jsonl --oos-threshold 0.9
```

Test set ada di [data/evaluation/test_set_buku_iku.md](data/evaluation/test_set_buku_iku.md): 10 soal definisi, 18 soal hitungan, dan soal jebakan/di luar cakupan. Setiap run menulis laporan bertanggal ke `reports/evaluation/`. Bandingkan metrik Hit@k, MRR, dan halaman sitasi. Jangan membandingkan angka *distance* antar-koleksi, karena koleksi v1 memakai L2 sedangkan v2 memakai cosine.

## Alur kerja pengembangan

Ringkasnya (detail di [CONTRIBUTING.md](CONTRIBUTING.md)):

1. **Rencanakan**: buat issue (template *Usulan fitur / eksperimen*) dengan target metrik.
2. **Branch**: `git switch develop && git switch -c feat/nama-fitur`.
3. **Implementasi**: ubah **satu hal** per eksperimen.
4. **Uji**: `pytest` + validasi + `eval_retrieval.py`.
5. **Pull request** ke `develop`, isi tabel metrik sebelum/sesudah di template PR.
6. **Rilis**: merge `develop` → `main`, perbarui [CHANGELOG.md](CHANGELOG.md), beri tag versi (`v0.3.0`).

## Troubleshooting

| Gejala | Penyebab & solusi |
|---|---|
| `Collection [pmpt_qa_v2] does not exist` | Vector DB belum dibangun. Jalankan `python src/vectordb/build_chroma.py --reset` |
| `torch.cuda.is_available()` = `False` padahal ada GPU | Terpasang torch versi CPU. `pip uninstall torch`, lalu pasang ulang dengan `--index-url .../cu126`. Pastikan driver NVIDIA terbaru |
| `CUDA out of memory` saat embedding / rerank | Tambahkan `--batch-size 4` (embedding), atau tutup aplikasi lain yang memakai GPU |
| `LLAMA_CLOUD_API_KEY belum ditemukan` | Hanya muncul saat parsing. Isi `.env`, atau pakai `--rebuild` bila hanya ingin menyusun ulang `.md` |
| Unduhan model HuggingFace lambat / terputus | Jalankan ulang; unduhan dilanjutkan dari cache `%USERPROFILE%\.cache\huggingface` |
| `Activate.ps1 cannot be loaded` | `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` |
| Hasil eval berbeda dari tabel di atas | Pastikan `data/chunks` dan `data/embeddings` tidak berubah (`git status`) dan vector DB dibangun ulang dengan `--reset` |

## Dokumentasi lanjutan

- [docs/README.md](docs/README.md): indeks dokumentasi per fase SDLC
- [docs/01-analisis/inventaris_formula.md](docs/01-analisis/inventaris_formula.md): inventaris 41 rumus IKU di Buku
- [docs/02-desain/panduan_chunking.md](docs/02-desain/panduan_chunking.md): desain chunking v2 dan alasannya
- [docs/02-desain/skema_embedding.md](docs/02-desain/skema_embedding.md): best practice embedding & retrieval, beserta status penerapannya
- [data/README.md](data/README.md): penjelasan setiap folder data
