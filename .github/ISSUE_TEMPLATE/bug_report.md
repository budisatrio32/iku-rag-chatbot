---
name: Laporan bug
about: Script error atau crash di salah satu tahap pipeline
labels: bug
---

<!-- Jawaban chatbot yang keliru (angka, sitasi, isi) dilaporkan lewat template "Jawaban chatbot salah". -->

## Yang terjadi

<!-- Pesan error lengkap (traceback). JANGAN menempel isi .env atau API key apa pun. -->

## Langkah reproduksi

```powershell
python src/...
```

## Yang diharapkan

## Tahap pipeline

<!-- Parsing / Processing / Chunking / Embedding / Vector DB / Retrieval / Kalkulator / Generation (LLM) / Evaluasi -->

## Lingkungan

- OS:
- Python: <!-- python --version, pastikan venv aktif -->
- GPU / CPU:
- Commit: <!-- git rev-parse --short HEAD -->
- Koleksi Chroma: <!-- mis. pmpt_qa_v2 -->
- Penyedia & model LLM (bila tahap Generation): <!-- isi LLM_BASE_URL dan LLM_MODEL, tanpa LLM_API_KEY -->
