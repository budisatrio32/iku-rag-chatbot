# Artefak pipeline v1 (legacy)

Hasil pipeline pertama (sebelum 2026-10-03), disimpan sebagai **baseline pembanding** evaluasi. Tidak dipakai lagi oleh pipeline utama.

| Folder | Isi |
|---|---|
| `v1/parsed/` | Markdown hasil parsing v1 |
| `v1/processed/` | JSON hasil processing v1 |
| `v1/chunks/` | Chunk v1 (`src/legacy/chunk_json.py`) |
| `v1/embeddings/` | Embedding v1 (+ subset uji `*_test`) |

Laporan baseline: `reports/evaluation/retrieval_eval_20261003_140456.md`.

Membangun ulang koleksi v1 untuk dibandingkan:

```powershell
python src/vectordb/build_chroma.py --embeddings-dir data/legacy/v1/embeddings --collection pmpt_qa --reset
python src/evaluation/eval_retrieval.py --preset lama --collection pmpt_qa --metadata data/legacy/v1/embeddings/metadata.jsonl
```

Catatan: koleksi asli v1 memakai jarak L2. `build_chroma.py` sekarang selalu memakai cosine, sehingga angka *distance* (dan ambang `--oos-threshold`) berbeda dari laporan lama. Hit@k dan MRR tetap sebanding.
