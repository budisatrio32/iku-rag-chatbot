"""
build_chroma.py
Tahap VECTOR DB: simpan embedding + metadata ke ChromaDB.

Jalankan dari root project:
    python src/vectordb/build_chroma.py --reset             # koleksi v2 (pmpt_qa_v2) dari data/embeddings
    python src/vectordb/build_chroma.py --embeddings-dir data/legacy/v1/embeddings --collection pmpt_qa --reset

--reset menghapus koleksi dengan nama itu lebih dulu, agar tidak ada chunk usang
yang tertinggal (upsert saja tidak menghapus id lama yang sudah tidak ada).
Koleksi baru memakai jarak cosine (cocok untuk embedding bge-m3 yang dinormalisasi).
"""

from pathlib import Path
import argparse
import json
import numpy as np
import chromadb


PROJECT_ROOT = Path(__file__).resolve().parents[2]

EMBEDDINGS_DIR = PROJECT_ROOT / "data" / "embeddings"
CHROMA_DIR = PROJECT_ROOT / "data" / "vectorstore"

COLLECTION_NAME = "pmpt_qa_v2"


def load_metadata(path: Path):
    metadata = []

    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                metadata.append(json.loads(line))

    return metadata


def to_chroma_metadata(item: dict) -> dict:
    """Chroma hanya menerima nilai skalar (str/int/float/bool) dan tidak menerima None."""
    keys = ["source_file", "source_priority", "doc_part", "page", "page_start", "page_end",
            "section_path", "iku_id", "iku_name", "jenis", "bagian", "n_tokens"]
    meta = {}
    for key in keys:
        value = item.get(key)
        if value is not None:
            meta[key] = value
    if "page" not in meta and "page_start" in meta:
        meta["page"] = meta["page_start"]
    if item.get("source_notes"):
        meta["source_notes"] = json.dumps(item["source_notes"], ensure_ascii=False)
    if item.get("block_ids"):
        meta["block_ids"] = json.dumps(item["block_ids"])
    return meta


def main():
    parser = argparse.ArgumentParser(description="Bangun koleksi ChromaDB")
    parser.add_argument("--embeddings-dir", type=Path, default=EMBEDDINGS_DIR)
    parser.add_argument("--collection", default=COLLECTION_NAME)
    parser.add_argument("--reset", action="store_true",
                        help="hapus koleksi dengan nama ini sebelum membangun ulang")
    args = parser.parse_args()

    print("Load embeddings...")

    embeddings = np.load(args.embeddings_dir / "embeddings.npy")

    print("Embedding shape:", embeddings.shape)

    print("Load metadata...")

    metadata = load_metadata(args.embeddings_dir / "metadata.jsonl")

    print("Jumlah metadata:", len(metadata))

    if len(embeddings) != len(metadata):
        raise ValueError(
            f"Jumlah embedding ({len(embeddings)}) "
            f"tidak sama dengan metadata ({len(metadata)})"
        )

    print("Membuka ChromaDB...")

    client = chromadb.PersistentClient(
        path=str(CHROMA_DIR)
    )

    if args.reset and args.collection in [c.name for c in client.list_collections()]:
        print(f"Menghapus koleksi lama: {args.collection}")
        client.delete_collection(args.collection)

    collection = client.get_or_create_collection(
        name=args.collection,
        metadata={"hnsw:space": "cosine"},
    )

    ids = [item["chunk_id"] for item in metadata]

    # chunk v2: simpan teks lengkap (header konteks + isi) agar LLM ikut melihat konteksnya
    documents = [item.get("text") or item["content"] for item in metadata]

    metadatas = [to_chroma_metadata(item) for item in metadata]

    print("Memasukkan data ke ChromaDB...")

    collection.upsert(
        ids=ids,
        embeddings=embeddings.tolist(),
        documents=documents,
        metadatas=metadatas,
    )

    print()
    print("Indexing selesai.")
    print("Collection :", args.collection)
    print("Distance   :", collection.metadata.get("hnsw:space", "l2") if collection.metadata else "l2")
    print("Jumlah data:", collection.count())
    print("Database   :", CHROMA_DIR)


if __name__ == "__main__":
    main()
