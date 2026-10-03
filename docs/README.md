# Dokumentasi

Dokumentasi disusun mengikuti fase SDLC. Folder fase baru dibuat ketika sudah ada isinya.

| Fase | Lokasi | Isi |
|---|---|---|
| 1. Perencanaan & analisis kebutuhan | [01-analisis/](01-analisis/) | [Inventaris formula](01-analisis/inventaris_formula.md): 41 rumus IKU yang harus bisa dijawab chatbot |
| 2. Desain | [02-desain/](02-desain/) | [Panduan chunking](02-desain/panduan_chunking.md), [Skema embedding & retrieval](02-desain/skema_embedding.md) |
| 3. Implementasi | [`src/`](../src/) | Satu folder per tahap pipeline; cara menjalankan ada di [README](../README.md) |
| 4. Pengujian | [`tests/`](../tests/), [`data/evaluation/`](../data/evaluation/), [`reports/`](../reports/) | Unit test, test set 30 soal, laporan validasi & evaluasi |
| 5. Deployment | `04-deployment/` (belum ada) | Untuk tahap API/UI chatbot |
| 6. Pemeliharaan | [CHANGELOG](../CHANGELOG.md), [CONTRIBUTING](../CONTRIBUTING.md) | Riwayat versi, aturan kontribusi |

Usulan isi berikutnya:

- `01-analisis/kebutuhan.md`: pengguna sasaran, jenis pertanyaan, batasan (mis. menolak pertanyaan di luar IKU)
- `02-desain/desain_generation.md`: prompt LLM, format sitasi, alur *tool calling* ke kalkulator
- `03-pengujian/strategi_pengujian.md`: metrik target per tahap dan cara menambah soal ke test set
