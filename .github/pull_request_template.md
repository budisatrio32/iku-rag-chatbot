## Ringkasan

<!-- Apa yang diubah dan mengapa. Tautkan issue: "Closes #12" -->

## Jenis perubahan

- [ ] Fitur baru (`feat`)
- [ ] Perbaikan bug (`fix`)
- [ ] Eksperimen retrieval/chunking/prompt (`exp`)
- [ ] Data / artefak pipeline (`data`)
- [ ] Dokumentasi (`docs`)
- [ ] Lainnya:

## Tahap pipeline yang terdampak

- [ ] Parsing  - [ ] Processing  - [ ] Chunking  - [ ] Embedding
- [ ] Vector DB  - [ ] Retrieval  - [ ] Kalkulator  - [ ] Generation (LLM)
- [ ] Evaluasi  - [ ] UI

## Bukti pengujian

- [ ] `pytest` lulus
- [ ] Validasi lulus (`validate_processed.py` / `validate_chunks.py`) bila processing/chunking berubah
- [ ] `eval_retrieval.py --preset v2` dijalankan bila retrieval/chunking/embedding berubah
- [ ] `run_calc_tests.py` dijalankan bila kalkulator atau retrieval berubah
- [ ] Chatbot dicoba dengan `chat_cli.py --detail` bila generation/prompt/alat berubah

| Metrik | Sebelum | Sesudah |
|---|---|---|
| Hit@1 | | |
| Hit@5 | | |
| MRR@5 | | |
| Halaman sitasi benar | | |
| Soal hitungan benar (kalkulator) | | |
| Jawaban LLM: angka benar / sitasi valid / soal jebakan lolos | | |

Laporan: `reports/evaluation/...`

## Bila tahap Generation (LLM) berubah

- Penyedia & model yang dipakai saat uji: <!-- LLM_BASE_URL dan LLM_MODEL -->
- Perubahan prompt atau deskripsi alat: <!-- ringkas apa yang diubah dan alasannya -->
- Contoh pertanyaan uji dan jawabannya (sebelum/sesudah):

## Checklist

- [ ] Tidak ada `.env` / API key (`LLAMA_CLOUD_API_KEY`, `LLM_API_KEY`) yang ikut ter-commit
- [ ] Variabel baru di `.env` juga ditambahkan ke `.env.example` (tanpa nilai rahasia)
- [ ] Dependensi baru ditambahkan ke `requirements.txt`
- [ ] Artefak data yang berubah ikut di-commit bersama kode yang menghasilkannya
- [ ] README / docs / CHANGELOG diperbarui bila perlu
