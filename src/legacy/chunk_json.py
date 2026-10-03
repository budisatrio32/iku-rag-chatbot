import json
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[2]

INPUT_DIR = PROJECT_ROOT / "data" / "legacy" / "v1" / "processed"
OUTPUT_DIR = PROJECT_ROOT / "data" / "legacy" / "v1" / "chunks"
OUTPUT_FILE = OUTPUT_DIR / "chunks.jsonl"


def is_decorative_image(block):
    if block.get("block_type") != "image_note":
        return False

    content = block.get("content", "").lower()

    decorative_words = [
        "decorative",
        "decoration",
        "ornament",
        "background",
        "separator",
    ]

    return any(word in content for word in decorative_words)


def create_chunk(blocks, chunk_number):
    if not blocks:
        return None

    first = blocks[0]

    contents = []

    for block in blocks:
        content = block.get("content", "").strip()

        if content:
            contents.append(content)

    if not contents:
        return None

    return {
        "chunk_id": f"chunk_{chunk_number:05d}",
        "source_file": first.get("source_file"),
        "page": first.get("page"),
        "section_path": first.get("section_path"),
        "content": "\n\n".join(contents),
    }


def process_file(input_file, chunks, start_number):
    with input_file.open("r", encoding="utf-8") as f:
        blocks = json.load(f)

    current_blocks = []
    current_section = None
    chunk_number = start_number

    for block in blocks:
        block_type = block.get("block_type")
        section_path = block.get("section_path")

        # Abaikan image yang jelas dekoratif
        if is_decorative_image(block):
            continue

        # Heading = awal section baru
        if block_type == "heading":
            if current_blocks:
                chunk = create_chunk(current_blocks, chunk_number)

                if chunk:
                    chunks.append(chunk)
                    chunk_number += 1

            current_blocks = [block]
            current_section = section_path
            continue

        # Kalau section berubah, tutup chunk sebelumnya
        if current_section != section_path and current_blocks:
            chunk = create_chunk(current_blocks, chunk_number)

            if chunk:
                chunks.append(chunk)
                chunk_number += 1

            current_blocks = []
            current_section = section_path

        # Table tetap sebagai satu kesatuan
        if block_type == "table":
            if current_blocks:
                chunk = create_chunk(current_blocks, chunk_number)

                if chunk:
                    chunks.append(chunk)
                    chunk_number += 1

            table_chunk = create_chunk([block], chunk_number)

            if table_chunk:
                chunks.append(table_chunk)
                chunk_number += 1

            current_blocks = []
            continue

        # Paragraph dan block lain masuk ke chunk section
        current_blocks.append(block)

    # Simpan sisa block
    if current_blocks:
        chunk = create_chunk(current_blocks, chunk_number)

        if chunk:
            chunks.append(chunk)
            chunk_number += 1

    return chunk_number


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    input_files = sorted(INPUT_DIR.glob("*_processed.json"))

    if not input_files:
        print("Tidak ditemukan file processed JSON.")
        return

    chunks = []
    chunk_number = 1

    for input_file in input_files:
        print(f"Processing: {input_file.name}")

        chunk_number = process_file(
            input_file,
            chunks,
            chunk_number,
        )

    with OUTPUT_FILE.open("w", encoding="utf-8") as f:
        for chunk in chunks:
            f.write(
                json.dumps(
                    chunk,
                    ensure_ascii=False,
                )
                + "\n"
            )

    print()
    print("Chunking selesai.")
    print(f"Total chunks : {len(chunks)}")
    print(f"Output       : {OUTPUT_FILE}")


if __name__ == "__main__":
    main()