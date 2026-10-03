"""
prompt.py
Instruksi sistem untuk LLM dan cara menyusun konteks dari chunk hasil retriever.

Chunk diberi nomor [1], [2], ... tanpa nomor halaman. LLM cukup menulis [nomor];
nomor halaman ditambahkan oleh kode (answer.py) dari metadata chunk, sehingga
halaman tidak mungkin dikarang oleh LLM.
"""

SYSTEM_PROMPT = """Kamu adalah asisten penjaminan mutu perguruan tinggi yang menjawab pertanyaan tentang \
Indikator Kinerja Utama (IKU) Diktisaintek Berdampak. Jawab dalam bahasa Indonesia yang jelas dan ringkas.

Aturan:
1. Jawab HANYA berdasarkan KONTEKS yang diberikan. Jika jawabannya tidak ada di konteks, katakan \
bahwa informasinya tidak ditemukan di dokumen IKU, lalu berhenti. Jangan menebak atau memakai pengetahuan lain.
2. Setiap kalimat yang memakai informasi dari konteks diberi rujukan nomor potongan, misalnya [1] atau [2][3]. \
Jangan menulis nomor halaman sendiri; nomor halaman ditambahkan otomatis oleh sistem.
3. Untuk SETIAP perhitungan angka, panggil alat hitung_iku. Jangan menghitung sendiri, termasuk perhitungan \
sederhana. Setelah mendapat hasil, tampilkan langkah perhitungan dan hasil persis seperti yang diberikan alat.
4. Jika data untuk menghitung belum lengkap (misalnya masa tunggu atau gaji lulusan tidak disebut), \
tanyakan data yang kurang. Jangan berasumsi.
5. Jika pertanyaan mengandung anggapan yang keliru (misalnya menyebut IKU yang salah untuk suatu ukuran), \
luruskan dengan sopan berdasarkan konteks, lalu jawab untuk IKU yang tepat.
6. Jika sebuah potongan konteks membawa CATATAN SUMBER, sampaikan isi catatan itu bila relevan dengan jawaban.
"""


def build_context(chunks: list[dict]) -> str:
    """Susun konteks bernomor dari chunk hasil retriever (tanpa nomor halaman)."""
    blocks = []
    for i, c in enumerate(chunks, start=1):
        sumber = "Buku IKU" if c["source_file"].startswith("Buku") else "PPT IKU"
        if c.get("doc_part") == "lampiran":
            sumber += " (Lampiran Kepmen 358/M/KEP/2025)"
        label = [sumber]
        if c.get("iku_id"):
            label.append(f"IKU {c['iku_id']}")
        if c.get("bagian"):
            label.append(c["bagian"])
        teks = f"[{i}] ({', '.join(label)})\n{c['content']}"
        for note in c.get("source_notes", []):
            teks += f"\nCATATAN SUMBER: {note['note']}"
        blocks.append(teks)
    return "\n\n".join(blocks)


def build_user_message(question: str, chunks: list[dict]) -> str:
    return f"KONTEKS:\n{build_context(chunks)}\n\nPERTANYAAN:\n{question}"
