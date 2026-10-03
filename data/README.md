# Data

| Folder | Isi | Dihasilkan oleh | Di-commit? |
|---|---|---|---|
| `raw/` | PDF sumber (Buku IKU V1, PPT IKU PTS V2) | manual | ✅ |
| `parsed/` | Markdown + `.pages.json` + `_jobs.json` | `src/parsing/parse_pdf.py` | ✅ (parsing berbayar) |
| `processed/` | JSON terstruktur per dokumen (blok, halaman, tabel) | `src/processing/process_markdown.py` | ✅ |
| `chunks/` | `chunks.jsonl` (605 chunk) | `src/chunking/chunk_structured.py` | ✅ |
| `embeddings/` | `embeddings.npy` (605 × 1024) + `metadata.jsonl` | `src/embedding/embed_chunks.py` | ✅ (lama tanpa GPU) |
| `vectorstore/` | ChromaDB persisten | `src/vectordb/build_chroma.py` | ❌ biner, bangun ulang dalam beberapa detik |
| `metadata/` | `known_source_issues.json`: cacat/salah ketik di dokumen sumber | manual | ✅ |
| `evaluation/` | `test_set_buku_iku.md` (30 soal + kunci), `test_inputs_hitung.json` | manual | ✅ |
| `legacy/v1/` | Artefak pipeline v1 (baseline pembanding) | `src/legacy/chunk_json.py` dkk. | ✅ |

Nomor halaman di semua artefak = **nomor halaman file PDF** (bukan nomor tercetak).

Bila menambah dokumen sumber: letakkan PDF di `raw/`, daftarkan di `DOCUMENTS` dalam `src/parsing/parse_pdf.py`, lalu jalankan pipeline dari tahap 1 (lihat README).
