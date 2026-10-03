# Panduan Kontribusi

## Strategi branch

```text
main      ← selalu stabil; hanya menerima merge dari develop (rilis)
develop   ← integrasi; semua PR fitur masuk ke sini
  ├── feat/<nama>   fitur baru            mis. feat/llm-generation
  ├── fix/<nama>    perbaikan bug          mis. fix/sitasi-lampiran
  ├── exp/<nama>    eksperimen retrieval   mis. exp/chunk-384-token
  └── docs/<nama>   dokumentasi
```

1. Mulai dari `develop` terbaru:
   ```powershell
   git switch develop
   git pull
   git switch -c feat/nama-fitur
   ```
2. Commit kecil dan sering, lalu `git push -u origin feat/nama-fitur`.
3. Buka Pull Request ke `develop` dan isi template PR, termasuk tabel metrik bila retrieval terdampak.
4. Setelah review dan CI hijau, lakukan *squash and merge*, lalu hapus branch.
5. Rilis: PR `develop` → `main`, perbarui `CHANGELOG.md`, beri tag `vX.Y.Z`.

## Format pesan commit

Memakai [Conventional Commits](https://www.conventionalcommits.org/):

```text
<tipe>(<tahap>): <ringkasan singkat>
```

| Tipe | Untuk |
|---|---|
| `feat` | fitur baru |
| `fix` | perbaikan bug |
| `exp` | eksperimen (chunking, retriever, model) beserta hasil evaluasinya |
| `data` | artefak data yang dibangun ulang (chunks, embeddings, parsed) |
| `test` | menambah atau memperbaiki test |
| `docs` | dokumentasi |
| `refactor` | merapikan kode tanpa mengubah perilaku |
| `chore` | konfigurasi, dependency, CI |

Contoh:

```text
feat(retrieval): tambah reranker bge-reranker-v2-m3
exp(chunking): max-tokens 384 -> Hit@1 22/29 menjadi 23/29
data(embeddings): bangun ulang setelah perbaikan header konteks
```

## Aturan kerja

- **Ubah satu hal setiap kali.** Jalankan `eval_retrieval.py` dan cantumkan metrik sebelum/sesudah di PR. Kalau beberapa hal diubah sekaligus, tidak jelas mana yang berdampak.
- **Validasi harus OK** (`validate_processed.py`, `validate_chunks.py`) sebelum melanjutkan ke tahap berikutnya.
- **Artefak data di-commit bersama kode yang menghasilkannya.** Misalnya, bila `chunk_structured.py` berubah, commit juga `data/chunks/`, `data/embeddings/`, dan laporan evaluasinya dalam PR yang sama.
- **Jangan commit** `.env`, API key, `.venv/`, atau `data/vectorstore/`.
- **Laporan evaluasi** (`reports/evaluation/`) cukup di-commit untuk run yang dirujuk di PR atau CHANGELOG.
- Script dijalankan dari **root repo**: `python src/<tahap>/<script>.py`.
- Gunakan Bahasa Indonesia untuk komentar, docstring, dan dokumentasi, mengikuti kode yang sudah ada.
