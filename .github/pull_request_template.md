## Ringkasan

<!-- Apa yang diubah dan mengapa. Tautkan issue: "Closes #12" -->

## Jenis perubahan

- [ ] Fitur baru (`feat`)
- [ ] Perbaikan bug (`fix`)
- [ ] Eksperimen retrieval/chunking (`exp`)
- [ ] Data / artefak pipeline (`data`)
- [ ] Dokumentasi (`docs`)
- [ ] Lainnya:

## Tahap pipeline yang terdampak

- [ ] Parsing  - [ ] Processing  - [ ] Chunking  - [ ] Embedding
- [ ] Vector DB  - [ ] Retrieval  - [ ] Kalkulator  - [ ] Evaluasi

## Bukti pengujian

- [ ] `pytest` lulus
- [ ] Validasi lulus (`validate_processed.py` / `validate_chunks.py`) bila processing/chunking berubah
- [ ] `eval_retrieval.py` dijalankan bila retrieval/chunking/embedding berubah

| Metrik | Sebelum | Sesudah |
|---|---|---|
| Hit@1 | | |
| Hit@5 | | |
| MRR@5 | | |
| Halaman sitasi benar | | |

Laporan: `reports/evaluation/...`

## Checklist

- [ ] Tidak ada `.env` / API key yang ikut ter-commit
- [ ] Artefak data yang berubah ikut di-commit bersama kode yang menghasilkannya
- [ ] README / docs / CHANGELOG diperbarui bila perlu
