"""
embed_chunks.py
Tahap EMBEDDING: chunk -> vektor dengan BAAI/bge-m3 (dense, dinormalisasi).

Yang di-embed adalah field "text" bila ada (header konteks + isi, chunk v2),
atau "content" (chunk lama).

Jalankan dari root project:
    python src/embedding/embed_chunks.py                     # data/chunks -> data/embeddings
    python src/embedding/embed_chunks.py --batch-size 4      # bila GPU kehabisan memori
"""

from pathlib import Path
import argparse
import json

import numpy as np
import torch
from sentence_transformers import SentenceTransformer


PROJECT_ROOT = Path(__file__).resolve().parents[2]

INPUT_FILE = PROJECT_ROOT / "data" / "chunks" / "chunks.jsonl"
OUTPUT_DIR = PROJECT_ROOT / "data" / "embeddings"

MODEL_NAME = "BAAI/bge-m3"
# chunk v2 dibatasi 512 token; 1024 memberi ruang aman tanpa memboroskan memori GPU
MAX_SEQ_LENGTH = 1024


def load_chunks(path: Path, limit=None):
    chunks = []

    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            if not line.strip():
                continue

            chunks.append(json.loads(line))

            if limit and len(chunks) >= limit:
                break

    return chunks


def main():
    parser = argparse.ArgumentParser(description="Embedding chunk dengan bge-m3")
    parser.add_argument("--input", type=Path, default=INPUT_FILE)
    parser.add_argument("--output-dir", type=Path, default=OUTPUT_DIR)
    parser.add_argument("--batch-size", type=int, default=8)
    args = parser.parse_args()

    chunks = load_chunks(args.input)

    print(f"Jumlah chunk: {len(chunks)}")

    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"Load model ({device})...")
    model = SentenceTransformer(MODEL_NAME, device=device)
    model.max_seq_length = MAX_SEQ_LENGTH

    print("Model device:", model.device)

    texts = [chunk.get("text") or chunk["content"] for chunk in chunks]

    print("Mulai embedding...")

    embeddings = model.encode(
        texts,
        batch_size=args.batch_size,
        show_progress_bar=True,
        normalize_embeddings=True,
    )

    embeddings = np.asarray(embeddings, dtype=np.float32)

    args.output_dir.mkdir(parents=True, exist_ok=True)

    np.save(
        args.output_dir / "embeddings.npy",
        embeddings
    )

    with open(
        args.output_dir / "metadata.jsonl",
        "w",
        encoding="utf-8"
    ) as f:
        for chunk in chunks:
            f.write(json.dumps(chunk, ensure_ascii=False) + "\n")

    print()
    print("Embedding selesai.")
    print("Shape:", embeddings.shape)
    print("Output:", args.output_dir)


if __name__ == "__main__":
    main()
