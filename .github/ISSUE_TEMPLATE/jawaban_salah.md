---
name: Jawaban chatbot salah
about: Hitungan keliru, sitasi/halaman salah, jawaban mengarang, atau premis keliru tidak dikoreksi
labels: jawaban, generation
---

## Pertanyaan yang diajukan

<!-- Tulis persis seperti yang diketik ke chatbot -->

## Jawaban chatbot

<!-- Tempel output lengkap dari: python src/generation/chat_cli.py --detail
     termasuk bagian "Sumber", "Sumber rumus (kalkulator)", "PERINGATAN",
     baris [kalkulator] dan [chunk]. -->

```text

```

## Jenis kesalahan

- [ ] Angka hasil hitungan salah
- [ ] Kalkulator tidak dipanggil untuk soal hitungan
- [ ] Argumen kalkulator salah (angka dari soal salah dipindahkan)
- [ ] Sitasi / nomor halaman salah, atau rujukan [n] tidak valid
- [ ] Jawaban memuat informasi yang tidak ada di dokumen (mengarang)
- [ ] Pertanyaan di luar dokumen tidak ditolak
- [ ] Premis keliru tidak diluruskan (mis. IKU yang disebut salah)
- [ ] Tidak bertanya balik padahal data kurang
- [ ] Catatan cacat sumber (source_notes) tidak disampaikan
- [ ] Lainnya:

## Jawaban yang benar

<!-- Jawaban yang seharusnya, beserta halaman di Buku IKU (nomor halaman file PDF) -->

## Dugaan penyebab

<!-- Pilih bila tahu: chunk yang benar tidak terambil (retrieval) / chunk benar tapi LLM salah membaca (prompt) /
     rumus atau bobot di kalkulator salah / data sumber cacat. Lihat baris [chunk] di output --detail. -->

## Lingkungan

- Penyedia & model LLM: <!-- LLM_BASE_URL dan LLM_MODEL, tanpa LLM_API_KEY -->
- Koleksi Chroma: <!-- mis. pmpt_qa_v2 -->
- Commit: <!-- git rev-parse --short HEAD -->

## Masuk test set?

- [ ] Pertanyaan ini sebaiknya ditambahkan ke `data/evaluation/test_set_buku_iku.md`
