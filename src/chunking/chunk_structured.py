"""
chunk_structured.py
Tahap CHUNKING (versi 2): structure-aware chunking untuk embedding BAAI/bge-m3.

Input : data/processed/*_processed.json  (hasil process_markdown.py)
Output: data/chunks/chunks.jsonl

Prinsip (lihat docs/02-desain/panduan_chunking.md):
1. Ikuti struktur dokumen, bukan potongan ukuran tetap: satu chunk = satu bagian
   (heading + isinya). Heading tidak pernah menjadi chunk sendiri.
2. Tabel definisi IKU ("DEFINISI, KRITERIA, KETENTUAN, DAN FORMULA") yang terpotong
   antarhalaman digabung dulu, lalu dipecah per bagian: Definisi / Kriteria /
   Ketentuan / Formula (+Satuan). Baris lanjutan dengan label kosong mewarisi
   label baris di atasnya.
3. Ukuran diukur dengan tokenizer bge-m3: chunk yang melewati --max-tokens dipecah
   di batas baris tabel / kalimat (header tabel diulang); chunk yang terlalu kecil
   digabung ke chunk sebelumnya pada bagian yang sama.
4. Setiap chunk diberi header konteks (dokumen, jalur bagian, halaman) yang IKUT
   di-embed, agar chunk tetap bermakna walau dibaca terpisah (contextual chunk header).
5. Metadata dibawa lengkap: source_priority, doc_part, iku_id, bagian, rentang
   halaman, dan source_notes (catatan cacat sumber).

Jalankan dari root project:
    python src/chunking/chunk_structured.py
    python src/chunking/chunk_structured.py --max-tokens 512 --min-tokens 64
"""

import argparse
import json
import re
import sys
from pathlib import Path

from transformers import AutoTokenizer

PROJECT_ROOT = Path(__file__).resolve().parents[2]
INPUT_DIR = PROJECT_ROOT / "data" / "processed"
OUTPUT_FILE = PROJECT_ROOT / "data" / "chunks" / "chunks.jsonl"

TOKENIZER_NAME = "BAAI/bge-m3"

DOC_LABELS = {
    "Buku_IKU_Diktisaintek_Berdampak_V1.md": ("BUKU", "Buku IKU Diktisaintek Berdampak V1"),
    "PPT_IKU_Diktisaintek_Berdampak_PTS_V2.md": ("PPT", "PPT IKU Diktisaintek Berdampak PTS V2"),
}

DEFINITION_TABLE_RE = re.compile(r"DEFINISI,\s*KRITERIA", re.I)
FIELD_GROUPS = {          # label baris tabel definisi -> nama bagian chunk
    "definisi": "Definisi",
    "kriteria": "Kriteria",
    "ketentuan": "Ketentuan",
    "kriteria dan ketentuan": "Kriteria dan Ketentuan",
    "formula": "Formula",
    "satuan": "Formula",      # satuan digabung dengan formula
}
IKU_ID_RE = re.compile(r"IKU\s*(\d{1,2})\s*[:(]?\s*\(?([a-d])?\)?", re.I)
SENTENCE_SPLIT_RE = re.compile(r"(?<=[.;:])\s+(?=(?:[a-z]\)|[a-h]\.|\d+\)|\d+\.|[A-Z•▪]))")


class TokenCounter:
    def __init__(self):
        try:
            self.tok = AutoTokenizer.from_pretrained(TOKENIZER_NAME, local_files_only=True)
        except OSError:
            self.tok = AutoTokenizer.from_pretrained(TOKENIZER_NAME)

    def __call__(self, text: str) -> int:
        return len(self.tok.encode(text, add_special_tokens=False))


# ---------------------------------------------------------------------------
# Tabel
# ---------------------------------------------------------------------------

def table_rows(content: str) -> tuple[list[str], list[str], list[str]]:
    """Pisahkan tabel markdown menjadi (baris pembuka non-tabel, [header, separator], baris isi)."""
    pre, head, body = [], [], []
    for line in content.split("\n"):
        s = line.strip()
        if not s.startswith("|"):
            pre.append(s)
        elif len(head) < 2:
            head.append(s)
        else:
            body.append(s)
    return pre, head, body


def first_cell(row: str) -> str:
    cells = row.strip().strip("|").split("|")
    return re.sub(r"\*+", "", cells[0]).strip() if cells else ""


def is_definition_table(block: dict) -> bool:
    return block["block_type"] == "table" and bool(DEFINITION_TABLE_RE.search(block["content"].split("\n")[0]))


def cells(row: str) -> list[str]:
    return [re.sub(r"\*+", "", c).strip() for c in row.strip().strip("|").split("|")]


def split_definition_table(blocks: list[dict]) -> list[dict]:
    """Gabungkan potongan tabel definisi (bisa lintas halaman) lalu pecah per IKU & bagian.

    Dua format di dokumen:
    - Bab V   : | IKU 3 | DEFINISI, KRITERIA... |  -> 1 IKU per tabel, label bagian di kolom 1
    - Lampiran: | NO. | IKU | DEFINISI... | |     -> banyak IKU per tabel; kolom 1-2 = nomor &
                nama IKU, label bagian di kolom 3
    Baris lanjutan dengan label/IKU kosong mewarisi nilai baris di atasnya.
    """
    head = None
    rows = []                         # (nama_iku, label_bagian, baris, blok_asal)
    current_group, current_iku = None, None
    for b in blocks:
        _, h, body = table_rows(b["content"])
        head = head or h
        multi_iku = bool(head) and cells(head[0])[0].upper().startswith("NO")
        for row in body:
            cs = cells(row)
            group = next((FIELD_GROUPS[c.lower()] for c in cs[:3] if c.lower() in FIELD_GROUPS), None)
            if multi_iku and len(cs) >= 2 and re.match(r"^\d+\.?$", cs[0]) and cs[1]:
                iku = f"IKU {cs[0].rstrip('.')}. {cs[1]}"
                if iku != current_iku:            # IKU baru -> bagian dimulai ulang
                    current_iku, current_group = iku, None
            if group:
                current_group = group
            rows.append((current_iku, current_group or "Isi", row, b))

    units, order = {}, []
    for iku, group, row, b in rows:
        key = (iku, group)
        if key not in units:
            units[key] = {"rows": [], "blocks": []}
            order.append(key)
        units[key]["rows"].append(row)
        if b not in units[key]["blocks"]:
            units[key]["blocks"].append(b)

    # format Bab V: label IKU ada di sel pertama kepala tabel ("| IKU 1 | DEFINISI ... |").
    # Dipakai bila judul IKU tidak ikut terbaca parser (mis. IKU 1 di Buku hlm. 49).
    table_iku = None
    if head and not cells(head[0])[0].upper().startswith("NO"):
        m = re.match(r"^IKU\s*\d+(?:\.\d+)?(?:\s*[a-d]\b)?", cells(head[0])[0], re.I)
        table_iku = m.group(0) if m else None

    return [{
        "bagian": group,
        "iku_name": iku,
        "table_iku": table_iku,
        "content": "\n".join(head + units[(iku, group)]["rows"]),
        "blocks": units[(iku, group)]["blocks"],
        "table_head": head,
        "kind": "table",
    } for iku, group in order]


# ---------------------------------------------------------------------------
# Pemecahan unit yang terlalu besar
# ---------------------------------------------------------------------------

def split_text(text: str, max_tokens: int, count) -> list[str]:
    """Pecah teks panjang di batas kalimat / butir daftar."""
    pieces = [p for p in SENTENCE_SPLIT_RE.split(text) if p.strip()]
    out, cur = [], ""
    for p in pieces:
        candidate = f"{cur} {p}".strip() if cur else p
        if cur and count(candidate) > max_tokens:
            out.append(cur)
            cur = p
        else:
            cur = candidate
    if cur:
        out.append(cur)
    return out


def split_unit(unit: dict, max_tokens: int, count) -> list[dict]:
    if count(unit["content"]) <= max_tokens:
        return [unit]

    if unit["kind"] == "table":
        pre, head, body = table_rows(unit["content"])
        head = unit.get("table_head") or head
        prefix = [p for p in pre if p] + head
        budget = max_tokens - count("\n".join(prefix))
        parts, cur = [], []
        for row in body:
            if count(row) > budget:                 # satu baris (sel panjang) terlalu besar
                if cur:
                    parts.append(cur)
                    cur = []
                label = first_cell(row)
                cell_text = row.strip().strip("|").split("|", 1)[-1].strip().rstrip("|").strip()
                for piece in split_text(cell_text, budget - count(f"| {label} | |"), count):
                    parts.append([f"| {label} | {piece} |"])
                continue
            if cur and count("\n".join(cur + [row])) > budget:
                parts.append(cur)
                cur = []
            cur.append(row)
        if cur:
            parts.append(cur)
        return [{**unit, "content": "\n".join(prefix + p)} for p in parts]

    return [{**unit, "content": piece} for piece in split_text(unit["content"], max_tokens, count)]


# ---------------------------------------------------------------------------
# Section -> unit -> chunk
# ---------------------------------------------------------------------------

def group_sections(blocks: list[dict]) -> list[dict]:
    """Section = blok heading + blok-blok sesudahnya sampai heading berikutnya."""
    sections, cur = [], None
    for b in blocks:
        if b["block_type"] == "heading":
            cur = {"heading": b, "path": b["section_path"], "blocks": []}
            sections.append(cur)
        else:
            if cur is None:
                cur = {"heading": None, "path": b["section_path"], "blocks": []}
                sections.append(cur)
            cur["blocks"].append(b)
    return sections


def section_units(section: dict) -> list[dict]:
    units, pending_def = [], []

    def flush_def():
        nonlocal pending_def
        if pending_def:
            units.extend(split_definition_table(pending_def))
            pending_def = []

    for b in section["blocks"]:
        if is_definition_table(b):
            pending_def.append(b)
            continue
        flush_def()
        units.append({
            "bagian": None,
            "content": b["content"],
            "blocks": [b],
            "kind": "table" if b["block_type"] == "table" else "text",
        })
    flush_def()
    return units


def full_path(path: str, iku_name: str | None, table_iku: str | None = None) -> str:
    """Jalur bagian + nama IKU (Lampiran) atau label IKU dari kepala tabel bila jalur
    belum menyebut IKU tersebut."""
    if iku_name:
        return f"{path} > {iku_name}"
    if table_iku:
        same = lambda s: (iku_id(s) or "").replace("LLDIKTI-", "")
        if same(path or "") != same(table_iku):          # jalur belum menyebut IKU ini
            return f"{path} > {table_iku}" if path else table_iku
    return path


def indicator_kind(path: str, ident: str | None) -> str | None:
    if not ident:
        return None
    if ident.startswith("LLDIKTI-"):
        return "iku_lldikti"
    if re.search(r"Sub Indikator", path or "", re.I):
        return "sub_indikator"
    return "iku"


def iku_id(path: str) -> str | None:
    """'... > IKU 3: Persentase ...' -> '3'; 'IKU 11: (b) ...' -> '11b'.
    IKU milik LLDIKTI diberi awalan agar tidak tertukar dengan IKU perguruan tinggi."""
    matches = IKU_ID_RE.findall(path or "")
    if not matches:
        return None
    num, sub = matches[-1]
    ident = f"{int(num)}{sub.lower()}" if sub else str(int(num))
    if re.search(r"LLDIKTI|LEMBAGA LAYANAN", path, re.I):
        ident = f"LLDIKTI-{ident}"
    return ident


def context_header(doc_label: str, doc_part: str, path: str, bagian: str | None, pages: list[int]) -> str:
    parts = [doc_label + (" (Lampiran Kepmen 358/M/KEP/2025)" if doc_part == "lampiran" else "")]
    if path:
        parts.append(path)
    if bagian:
        parts.append(f"Bagian: {bagian}")
    lo, hi = min(pages), max(pages)
    parts.append(f"hlm. {lo}" if lo == hi else f"hlm. {lo}–{hi}")
    return "[" + " | ".join(parts) + "]"


def parent_path(path: str) -> str:
    return path.rsplit(" > ", 1)[0] if " > " in path else ""


def merge_small_siblings(chunks: list[dict], doc_label: str, max_tokens: int, min_tokens: int,
                         count) -> list[dict]:
    """Chunk teks yang sangat kecil (mis. satu butir 'Dana riset: Rp150.000.000/tahun' yang punya
    heading sendiri) digabung ke chunk sebelumnya bila keduanya bersaudara di bawah induk yang sama.
    Judul bagian chunk kecil ditulis di depan isinya agar tidak hilang."""
    out: list[dict] = []
    for c in chunks:
        prev = out[-1] if out else None
        title = c["section_path"].rsplit(" > ", 1)[-1]
        siblings = prev is not None and parent_path(c["section_path"]) != "" and (
            parent_path(c["section_path"]) in (parent_path(prev["section_path"]), prev["section_path"]))
        if (siblings and count(c["content"]) < min_tokens
                and c["bagian"] is None and prev["bagian"] is None
                and c["doc_part"] == prev["doc_part"] and not c.get("iku_name") and not prev.get("iku_name")):
            addition = f"{title}\n{c['content']}" if title and title not in prev["content"] else c["content"]
            candidate = prev["content"] + "\n\n" + addition
            pages = [prev["page_start"], prev["page_end"], c["page_start"], c["page_end"]]
            header = context_header(doc_label, prev["doc_part"], prev["section_path"], None, pages)
            if count(header + "\n" + candidate) <= max_tokens:
                prev["content"] = candidate
                prev["page_start"], prev["page_end"] = min(pages), max(pages)
                prev["header"] = header
                prev["block_ids"] += c["block_ids"]
                seen = {n["id"] for n in prev["source_notes"]}
                prev["source_notes"] += [n for n in c["source_notes"] if n["id"] not in seen]
                continue
        out.append(c)
    return out


def make_chunks(blocks: list[dict], source_file: str, max_tokens: int, min_tokens: int, count) -> list[dict]:
    prefix, doc_label = DOC_LABELS.get(source_file, (Path(source_file).stem[:6].upper(), source_file))
    chunks = []
    carry_headings: list[dict] = []          # heading tanpa isi -> ikut ke chunk berikutnya

    def emit(section_heading, path, unit):
        bagian, content, src_blocks = unit["bagian"], unit["content"], unit["blocks"]
        iku_name = unit.get("iku_name")
        path_full = full_path(path, iku_name, unit.get("table_iku"))
        ident = iku_id(path_full)
        all_blocks = carry_headings + ([section_heading] if section_heading else []) + src_blocks
        pages = [b["page"] for b in all_blocks]
        notes, seen = [], set()
        for b in src_blocks:
            for n in b.get("source_notes", []):
                if n["id"] not in seen:
                    seen.add(n["id"])
                    notes.append(n)
        doc_part = "lampiran" if any(b["doc_part"] == "lampiran" for b in src_blocks) else "utama"
        orphan_titles = [h["content"] for h in carry_headings if h["content"] not in path]
        body = "\n".join(orphan_titles + [content]) if orphan_titles else content
        chunks.append({
            "source_file": source_file,
            "source_priority": src_blocks[0].get("source_priority", 9),
            "doc_part": doc_part,
            "page_start": min(pages),
            "page_end": max(pages),
            "section_path": path,
            "iku_name": iku_name,
            "iku_id": ident,
            "jenis": indicator_kind(path_full, ident),
            "bagian": bagian,
            "block_ids": [b["id"] for b in all_blocks],
            "source_notes": notes,
            "content": body,
            "header": context_header(doc_label, doc_part, path_full, bagian, pages),
        })

    for section in group_sections(blocks):
        units = section_units(section)
        if not units:
            if section["heading"]:
                carry_headings.append(section["heading"])
            continue

        # header konteks ikut di-embed -> anggaran token isi = max_tokens - panjang header
        budget = max_tokens - count(context_header(doc_label + " (Lampiran Kepmen 358/M/KEP/2025)", "utama",
                                                    section["path"], "Kriteria dan Ketentuan", [100, 100]))
        budget = max(budget, max_tokens // 2)     # jaga-jaga bila jalur bagian sangat panjang

        # pecah unit besar, lalu kemas unit kecil berurutan (bagian sama) sampai anggaran
        packed: list[dict] = []
        for unit in units:
            unit_budget = budget - (count(" > " + unit["iku_name"]) if unit.get("iku_name") else 0)
            for piece in split_unit(unit, unit_budget, count):
                last = packed[-1] if packed else None
                can_pack = (last is not None and last["bagian"] is None and piece["bagian"] is None
                            and last.get("iku_name") == piece.get("iku_name")
                            and count(last["content"] + "\n\n" + piece["content"]) <= budget)
                if can_pack:
                    last["content"] += "\n\n" + piece["content"]
                    last["blocks"] += [b for b in piece["blocks"] if b not in last["blocks"]]
                else:
                    packed.append({**piece, "blocks": list(piece["blocks"])})

        # chunk kecil (< min_tokens) digabung ke chunk sebelumnya di section yang sama
        merged: list[dict] = []
        for unit in packed:
            if (merged and count(unit["content"]) < min_tokens
                    and count(merged[-1]["content"] + "\n\n" + unit["content"]) <= budget):
                merged[-1]["content"] += "\n\n" + unit["content"]
                merged[-1]["blocks"] += [b for b in unit["blocks"] if b not in merged[-1]["blocks"]]
            else:
                merged.append(unit)

        for k, unit in enumerate(merged):
            emit(section["heading"] if k == 0 else None, section["path"], unit)
            carry_headings = []

    if carry_headings and chunks:             # heading terakhir tanpa isi -> tempel ke chunk terakhir
        last = chunks[-1]
        last["content"] += "\n" + "\n".join(h["content"] for h in carry_headings)
        last["block_ids"] += [h["id"] for h in carry_headings]

    chunks = merge_small_siblings(chunks, doc_label, max_tokens, min_tokens, count)

    for i, c in enumerate(chunks, start=1):
        c["chunk_id"] = f"{prefix}_{i:04d}"
        c["text"] = c["header"] + "\n" + c["content"]   # teks yang di-embed
        c["n_tokens"] = count(c["text"])
    return chunks


def main():
    parser = argparse.ArgumentParser(description="Structure-aware chunking untuk bge-m3")
    parser.add_argument("--max-tokens", type=int, default=512)
    parser.add_argument("--min-tokens", type=int, default=64)
    parser.add_argument("--input-dir", type=Path, default=INPUT_DIR)
    parser.add_argument("--output", type=Path, default=OUTPUT_FILE)
    args = parser.parse_args()

    sys.stdout.reconfigure(encoding="utf-8")
    print("Load tokenizer bge-m3...")
    count = TokenCounter()

    all_chunks = []
    for path in sorted(args.input_dir.glob("*_processed.json")):
        blocks = json.loads(path.read_text(encoding="utf-8"))
        source_file = blocks[0]["source_file"] if blocks else path.name
        chunks = make_chunks(blocks, source_file, args.max_tokens, args.min_tokens, count)
        all_chunks += chunks
        sizes = sorted(c["n_tokens"] for c in chunks)
        print(f"{source_file}: {len(blocks)} blok -> {len(chunks)} chunk | token min {sizes[0]} "
              f"median {sizes[len(sizes) // 2]} maks {sizes[-1]} | "
              f"> max_tokens: {sum(1 for s in sizes if s > args.max_tokens)}")

    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", encoding="utf-8") as f:
        for c in all_chunks:
            f.write(json.dumps(c, ensure_ascii=False) + "\n")

    print(f"\nTotal chunk : {len(all_chunks)}")
    print(f"Output      : {args.output}")


if __name__ == "__main__":
    main()
