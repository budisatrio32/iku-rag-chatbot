"""
process_markdown.py
Tahap PROCESSING pada pipeline RAG Penjaminan Mutu Perguruan Tinggi.
(pdf parsing -> [processing] -> chunking -> embedding -> vector db -> retrieval -> LLM)

Input : file markdown hasil parse_pdf.py (data/parsed/*.md), berisi penanda
        halaman <!-- page: N --> serta blok <!-- header --> / <!-- footer -->
Output: file JSON terstruktur per dokumen (data/processed/*_processed.json)
        berisi list of "blocks" (heading / paragraph / table / image_note)
        lengkap dengan metadata (source_file, source_priority, doc_part, page,
        section_path, source_notes)

Tugas tahap ini (BUKAN chunking, chunking dilakukan di tahap berikutnya):
1. Nomor halaman diambil langsung dari penanda <!-- page: N --> (dasar sitasi)
2. Header/footer halaman: buang isi berulang (label BAB, logo, judul dokumen,
   nomor halaman), simpan sisanya (judul slide, keterangan sumber, "LAMPIRAN")
3. Buang gambar dekoratif (logo/icon), KECUALI labelnya memuat data
   (mis. "Prodi S2 = 98", "2.370 Dosen") -> disimpan sebagai teks
4. Menormalkan semua <table> HTML -> Markdown table, termasuk caption dan
   rowspan (nilai sel diisi ke semua baris yang dicakupnya)
5. Melacak hierarki heading (BAB / sub-bab) sbg section_path -> penting utk sitasi
6. Menandai blok yang terkena cacat/kesalahan yang diketahui di dokumen sumber
   (data/metadata/known_source_issues.json) dengan field source_notes
"""

import re
import json
from pathlib import Path
from bs4 import BeautifulSoup

PROJECT_ROOT = Path(__file__).resolve().parents[2]
INPUT_DIR = PROJECT_ROOT / "data" / "parsed"
OUTPUT_DIR = PROJECT_ROOT / "data" / "processed"
KNOWN_ISSUES_FILE = PROJECT_ROOT / "data" / "metadata" / "known_source_issues.json"

# Buku = sumber utama, PPT = sumber sekunder
SOURCE_PRIORITY = {
    "Buku_IKU_Diktisaintek_Berdampak_V1.md": 1,
    "PPT_IKU_Diktisaintek_Berdampak_PTS_V2.md": 2,
}

# ---------------------------------------------------------------------------
# Konfigurasi noise & filter — sesuaikan bila menemukan pola lain di dokumen
# ---------------------------------------------------------------------------

NOISE_LINE_PATTERNS = [
    # footer berulang, polos/bold, dgn/tanpa nomor halaman menyatu di baris yg sama
    r"^\*{0,2}Indikator Kinerja Utama \(IKU\) Diktisaintek Berdampak\*{0,2}\s*\*{0,2}\d{0,3}\s*\|?\s*\*{0,2}$",
    r"^\*{0,2}\d{1,3}\s*\|?\*{0,2}$",   # nomor halaman berdiri sendiri: "14", "**14**", "**2 |**"
    # label bab berulang di pojok halaman: "**BAB II**", "# BAB V" (tanpa tanda hubung).
    # Judul bab yang sah selalu bertanda hubung ("# BAB - II") dan tidak terkena pola ini.
    r"^#{0,4}\s*\*{0,2}\s*BAB\s+[IVX]+\s*\*{0,2}$",
]

# Baris yang dibuang HANYA bila berada di dalam blok header/footer halaman
RUNNING_HEADER_PATTERNS = [
    r"^#{0,4}\s*\*{0,2}\s*BAB\s*-?\s*[IVX]+\s*\*{0,2}$",                 # label bab: "**BAB IV**", "# BAB V"
    r"^-{3,}\s*$",                                                     # garis pemisah
    r"^-\s*\d+\s*-$",                                                  # penomoran lokal Lampiran: "- 2 -"
    r"^\*{0,2}INDIKATOR KINERJA UTAMA \(IKU\) DIKTISAINTEK BERDAMPAK\*{0,2}$",
    r"^\*{0,2}KEMENTERIAN PENDIDIKAN TINGGI,? SAINS,? DAN TEKNOLOGI( REPUBLIK INDONESIA)?\*{0,2}$",
]

INLINE_IMAGE_RE = re.compile(r"!\[(.*?)\]\((.*?)\)")

DECORATIVE_IMAGE_ALT_PREFIXES = ("logo:", "icon:")          # dibuang, kecuali memuat data
# label gambar dekoratif tetap disimpan bila memuat data: tanda "=", angka >=2 digit,
# persentase, atau "angka + kata" (mis. "Prodi S2 = 98", "2.370 Dosen", "7 PTN-BH")
DATA_IN_ALT_RE = re.compile(r"=|\d[\d.,]*\d|\d+\s*%|\b\d+(?:[.,]\d+)?\s+[A-Za-z]")

PAGE_MARKER_RE = re.compile(r"^<!-- page: (\d+)(?: \|.*)? -->$")
REGION_OPEN_RE = re.compile(r"^<!-- (header|footer) -->$")
REGION_CLOSE_RE = re.compile(r"^<!-- /(header|footer) -->$")
IMAGE_LINE_RE = re.compile(r"^!\[(.*?)\]\((.*?)\)$")
HEADING_RE = re.compile(r"^(#{1,4})\s*(.+)$")
MD_TABLE_ROW_RE = re.compile(r"^\|.*\|$")
MD_TABLE_SEP_RE = re.compile(r"^\|[\s:\-|]+\|$")
# huruf besar saja: "**Lampiran**" di daftar isi (Buku hlm. 3) tidak boleh memicu
LAMPIRAN_START_RE = re.compile(r"^\*{0,2}(SALINAN\s+)?LAMPIRAN\b")


def image_alt_text(alt: str) -> str | None:
    """Teks yang disimpan dari sebuah gambar, atau None bila gambar dibuang."""
    alt = alt.strip()
    if not alt:
        return None
    if alt.lower().startswith(DECORATIVE_IMAGE_ALT_PREFIXES):
        label = alt.split(":", 1)[1].strip()
        return label if DATA_IN_ALT_RE.search(label) else None
    return alt


def replace_inline_images(line: str) -> str:
    """Gambar di tengah baris: ganti sintaks gambar dengan labelnya bila informatif,
    hapus bila dekoratif."""
    def repl(m):
        kept = image_alt_text(m.group(1))
        return f" {kept} " if kept else " "
    return re.sub(r"[ \t]{2,}", " ", INLINE_IMAGE_RE.sub(repl, line)).strip()


def is_running_header_line(stripped: str) -> bool:
    if any(re.match(p, stripped, re.I) for p in RUNNING_HEADER_PATTERNS):
        return True
    if any(re.match(p, stripped) for p in NOISE_LINE_PATTERNS):
        return True
    # baris yang isinya hanya gambar dekoratif / nomor halaman setelah gambar dibuang
    return replace_inline_images(stripped).strip(" *#|") == ""


# ---------------------------------------------------------------------------
# Rumus di dalam sel tabel HTML
# LlamaParse menulis pecahan secara "visual": pembilang bergaris bawah <u> lalu
# penyebut di baris berikutnya, garis <hr> sebagai garis pecahan, atau MathML
# <math><mfrac>. Jika tag dibuang begitu saja, tanda bagi hilang. Fungsi di bawah
# menulis ulang rumus menjadi teks eksplisit: (pembilang) / (penyebut) × 100%,
# subskrip/superskrip menjadi _{..} dan ^{..}.
# ---------------------------------------------------------------------------

FORMAT_TAG_RE = re.compile(r"</?(?:i|em|b|strong|span)\b[^>]*>", re.I)
TIMES_100_RE = re.compile(r"\s*[x×]\s*100\s*%\s*$", re.I)
# pembilang bergaris bawah, lalu (opsional) operator/hasil singkat, lalu penyebut di baris berikutnya:
#   <u>Jumlah luaran</u> x 100%<br/>Total kerja sama      <u>30%</u> = 90,91%<br/>33%
FRACTION_U_RE = re.compile(
    r"<u>\s*(?P<num>[^<]*?(?:<(?:sub|sup)>[^<]*</(?:sub|sup)>[^<]*?)*)\s*</u>"
    r"(?P<op>[^<]{0,40}?)\s*<br\s*/?>\s*(?P<den>[^<]*?)\s*(?=<br|<hr|$)",
    re.S | re.I)
# baris yang berfungsi sebagai garis pecahan: <hr>, "______", "————", "—" (+ opsional "x 100%")
HR_MARK = "@@GARIS_PECAHAN@@"
BAR_LINE_RE = re.compile(r"^(?:_{3,}|-{3,}|[—–]+)\s*(?P<op>[x×]\s*100\s*%)?$")
BORDER_BOTTOM_RE = re.compile(r"border-bottom", re.I)


def mathml_to_text(node) -> str:
    """MathML -> teks linear: mfrac -> (a) / (b), msub -> a_{b}, msup -> a^{b}."""
    if getattr(node, "name", None) is None:
        return " ".join(str(node).split())
    kids = [k for k in node.children if getattr(k, "name", None) or str(k).strip()]
    parts = [mathml_to_text(k) for k in kids]
    name = node.name.lower()
    if name == "mfrac" and len(parts) == 2:
        return f"({parts[0]}) / ({parts[1]})"
    if name == "msub" and len(parts) == 2:
        return f"{parts[0]}_{{{parts[1]}}}"
    if name == "msup" and len(parts) == 2:
        return f"{parts[0]}^{{{parts[1]}}}"
    if name == "msubsup" and len(parts) == 3:
        return f"{parts[0]}_{{{parts[1]}}}^{{{parts[2]}}}"
    if name == "msqrt":
        return f"sqrt({' '.join(parts)})"
    return " ".join(p for p in parts if p)


def _fraction(num: str, den: str, op: str | None) -> str:
    num = " ".join(num.split())
    den = " ".join(den.split())
    op = " ".join((op or "").split())
    if TIMES_100_RE.search(den):              # "× 100%" yang tertulis di baris penyebut
        den = TIMES_100_RE.sub("", den)
        op = op or "× 100%"
    text = f"({num}) / ({den})"
    return f"{text} {op}" if op else text


def _plain(fragment: str) -> str:
    return " ".join(BeautifulSoup(fragment, "html.parser").get_text(" ").split())


def _bar_fractions(html: str) -> str:
    """Pecahan yang garisnya berupa baris tersendiri (<hr>, '____', '———').
    Pembilang = baris-baris tidak kosong tepat di atas garis; penyebut = baris pertama di bawahnya."""
    html = re.sub(r"<hr\s*/?>", f"<br/>{HR_MARK}<br/>", html, flags=re.I)
    lines = re.split(r"<br\s*/?>", html, flags=re.I)
    out: list[str] = []
    i = 0
    while i < len(lines):
        text = _plain(lines[i])
        bar = text == HR_MARK or BAR_LINE_RE.match(text)
        if bar:
            op = bar.group("op") if bar is not True and hasattr(bar, "group") else None
            while out and not _plain(out[-1]):
                out.pop()
            num: list[str] = []
            while out and _plain(out[-1]):
                num.insert(0, _plain(out.pop()))
            j = i + 1
            while j < len(lines) and not _plain(lines[j]):
                j += 1
            if num and j < len(lines):
                out.append(_fraction(" ".join(num), _plain(lines[j]), op))
                i = j + 1
                continue
            out.extend(num)                   # bukan pecahan yang lengkap: kembalikan apa adanya
        out.append(lines[i] if text != HR_MARK else "")
        i += 1
    return "<br/>".join(out)


def cell_to_text(cell, formula_row: bool) -> str:
    """Teks sel tabel; rumus dipertahankan strukturnya."""
    for math in cell.find_all("math"):
        math.replace_with(f" {mathml_to_text(math)} ")

    # subskrip/superskrip yang menempel pada simbol (n<sub>i</sub>, ∑<sup>n</sup>)
    for tag in cell.find_all(["sub", "sup"]):
        prev = tag.previous_sibling
        prev_text = prev if isinstance(prev, str) else (prev.get_text() if prev is not None else "")
        attached = getattr(prev, "name", None) in ("sub", "sup") or (
            prev_text and (prev_text[-1].isalnum() or prev_text[-1] in "∑Σ)]}"))
        if attached:
            mark = "_" if tag.name == "sub" else "^"
            tag.replace_with(f"{mark}{{{tag.get_text(' ', strip=True)}}}")

    html = FORMAT_TAG_RE.sub("", cell.decode_contents())
    if formula_row or re.search(r"=\s*<u>", html):
        html = FRACTION_U_RE.sub(lambda m: _fraction(_plain(m.group("num")), m.group("den"), m.group("op")), html)
        html = _bar_fractions(html)
    return " ".join(BeautifulSoup(html, "html.parser").get_text(" ", strip=True).split())


def merge_split_row_fractions(grid: list[list[str]], bottom_border: list[list[bool]]) -> tuple[list[list[str]], int]:
    """Pecahan yang disusun memakai dua baris tabel (pembilang di baris atas, penyebut di baris
    bawah, kolom lain sama karena rowspan) -> satu baris dengan '(atas) / (bawah)'.
    Hanya pada baris berlabel 'Formula', dan hanya bila sel atas bergaris bawah (border-bottom)
    atau kedua sel sangat pendek (mis. 'n' dan 't'). Mengembalikan (grid baru, jumlah baris digabung)."""
    out, merged, r = [], 0, 0
    while r < len(grid):
        row = grid[r]
        if r + 1 < len(grid) and any(c.strip("* ").lower() == "formula" for c in row):
            nxt = grid[r + 1]
            diff = [k for k in range(min(len(row), len(nxt))) if row[k] != nxt[k]]
            if len(diff) == 1:
                k = diff[0]
                top, bottom = row[k], nxt[k]
                if top and bottom and (bottom_border[r][k] or (len(top) <= 3 and len(bottom) <= 3)):
                    out.append(row[:k] + [f"({top}) / ({bottom})"] + row[k + 1:])
                    merged += 1
                    r += 2
                    continue
        out.append(row)
        r += 1
    return out, merged


def html_table_to_markdown(html: str) -> tuple[str, int]:
    """Konversi 1 blok <table>...</table> HTML menjadi Markdown table.
    - caption disimpan sebagai baris "Tabel: ..." di atas tabel
    - colspan: isi sel di kolom pertama, kolom sisanya kosong
    - rowspan: isi sel diulang di setiap baris yang dicakupnya
    - rumus di sel (baris berlabel "Formula") ditulis ulang dengan tanda bagi eksplisit
    Mengembalikan (markdown, jumlah baris yang digabung karena pecahan dua-baris).
    """
    soup = BeautifulSoup(html, "html.parser")
    table = soup.find("table")
    if table is None:
        return "", 0

    caption = table.find("caption")
    caption_text = caption.get_text(" ", strip=True) if caption else ""

    grid: list[list[str]] = []
    borders: list[list[bool]] = []             # sel bergaris bawah (dipakai sbg garis pecahan)
    pending: dict[int, tuple[str, int]] = {}   # kolom -> (teks, sisa baris rowspan)
    for tr in table.find_all("tr"):
        row: list[str] = []
        row_border: list[bool] = []
        col = 0

        def fill_pending():
            nonlocal col
            while col in pending:
                text, left = pending[col]
                row.append(text)
                row_border.append(False)
                if left <= 1:
                    del pending[col]
                else:
                    pending[col] = (text, left - 1)
                col += 1

        tr_cells = tr.find_all(["th", "td"])
        formula_row = any(c.get_text(" ", strip=True).strip("* ").lower() == "formula" for c in tr_cells)
        for cell in tr_cells:
            fill_pending()
            text = cell_to_text(cell, formula_row)
            colspan = int(cell.get("colspan", 1) or 1)
            rowspan = int(cell.get("rowspan", 1) or 1)
            has_border = bool(BORDER_BOTTOM_RE.search(cell.get("style", "") or ""))
            for k in range(colspan):
                value = text if k == 0 else ""
                row.append(value)
                row_border.append(has_border)
                if rowspan > 1:
                    pending[col] = (value, rowspan - 1)
                col += 1
        fill_pending()
        grid.append(row)
        borders.append(row_border)

    if not grid:
        return "", 0

    width = max(len(r) for r in grid)
    grid = [r + [""] * (width - len(r)) for r in grid]
    borders = [b + [False] * (width - len(b)) for b in borders]
    grid, merged = merge_split_row_fractions(grid, borders)

    header, *body = grid
    lines = []
    if caption_text:
        lines.append(f"Tabel: {caption_text}")
    lines += ["| " + " | ".join(header) + " |",
              "| " + " | ".join(["---"] * width) + " |"]
    for r in body:
        lines.append("| " + " | ".join(c.replace("|", "/") for c in r) + " |")
    return "\n".join(lines), merged


# ---------------------------------------------------------------------------
# Tingkat heading
# Jumlah '#' dari LlamaParse tidak konsisten (mis. "IKU 11 (d)" bertanda '#', sedangkan
# "5.4. Sub Indikator" bertanda '##', sehingga Sub Indikator salah menjadi anak IKU 11 d).
# Tingkat ditentukan dari penomoran dokumen:
#   BAB - V -> 1 | 5.3 -> 2 | 5.3.1 -> 3 | 5.4.1.1 -> 4 | IKU N: -> 4
#   heading tanpa nomor -> satu tingkat di bawah heading bernomor terakhir (antar-heading
#   tanpa nomor menjadi saudara, bukan anak-beranak)
# ---------------------------------------------------------------------------

UNNUMBERED_OFFSET = 1
NUMBERED_LEVELS_RE = re.compile(r"^(\d+(?:\.\d+)+)\.?\s")


def numbered_level(title: str) -> int | None:
    t = re.sub(r"^\d+\s+(?=IKU\b)", "", title)            # "3 IKU 3: ..." -> "IKU 3: ..."
    if re.match(r"^BAB\s*-?\s*[IVX]+\b", t, re.I):
        return 1
    m = NUMBERED_LEVELS_RE.match(t)
    if m:
        return 1 + m.group(1).count(".")
    if re.match(r"^IKU\s*\d+\s*:", t, re.I):
        return 4
    return None


def heading_level(title: str, stack: list[tuple[int, str]]) -> int:
    level = numbered_level(title)
    if level is not None:
        return level
    anchors = [lvl for lvl, t in stack if numbered_level(t) is not None or lvl == 0]
    return (max(anchors) if anchors else 0) + UNNUMBERED_OFFSET


def load_known_issues() -> list[dict]:
    if not KNOWN_ISSUES_FILE.exists():
        return []
    return json.loads(KNOWN_ISSUES_FILE.read_text(encoding="utf-8"))["issues"]


def attach_source_notes(blocks: list[dict], issues: list[dict]):
    """Tandai blok yang memuat cacat/kesalahan yang diketahui di dokumen sumber."""
    for issue in issues:
        for b in blocks:
            if issue.get("source_files") and b["source_file"] not in issue["source_files"]:
                continue
            content = b["content"].lower()
            if all(term.lower() in content for term in issue["match_all"]):
                b.setdefault("source_notes", []).append({"id": issue["id"], "note": issue["note"]})


def process_file(path: Path) -> list[dict]:
    text = path.read_text(encoding="utf-8")
    lines = text.split("\n")

    blocks: list[dict] = []
    current_page = None
    region = None                # None | "header" | "footer"
    doc_part = "utama"           # berubah menjadi "lampiran" sejak penanda LAMPIRAN pertama
    section_stack: list[tuple[int, str]] = []
    buffer: list[str] = []
    block_id = 0

    def section_path() -> str:
        return " > ".join(t for _, t in section_stack)

    def add_block(block_type: str, content: str, **extra):
        nonlocal block_id
        block_id += 1
        blocks.append({
            "id": f"{path.stem}_{block_id}",
            "source_file": path.name,
            "source_priority": SOURCE_PRIORITY.get(path.name, 9),
            "doc_part": doc_part,
            "page": current_page,
            "section_path": section_path(),
            "block_type": block_type,
            "content": content,
            **extra,
        })

    def flush_paragraph():
        nonlocal buffer
        content = "\n".join(buffer).strip()
        buffer = []
        if content:
            add_block("paragraph", content)

    in_table = False
    table_buffer: list[str] = []

    i = 0
    n = len(lines)
    while i < n:
        line = lines[i].rstrip()
        stripped = line.strip()

        # 1) penanda halaman & batas blok header/footer
        m = PAGE_MARKER_RE.match(stripped)
        if m:
            flush_paragraph()
            current_page = int(m.group(1))
            region = None
            i += 1
            continue
        m = REGION_OPEN_RE.match(stripped)
        if m:
            flush_paragraph()
            region = m.group(1)
            i += 1
            continue
        if REGION_CLOSE_RE.match(stripped):
            flush_paragraph()
            region = None
            i += 1
            continue

        # 2) header/footer: buang isi berulang, sisanya diproses seperti isi biasa
        if region and is_running_header_line(stripped):
            i += 1
            continue

        # 2b) penanda awal Lampiran (SK Menteri) -> blok berikutnya diberi doc_part "lampiran",
        #     dan jalur bagian dimulai ulang agar tidak menempel ke bab sebelumnya (Daftar Pustaka)
        if LAMPIRAN_START_RE.match(stripped.lstrip("# ")):
            doc_part = "lampiran"
            flush_paragraph()
            section_stack = [(0, "LAMPIRAN Kepmen 358/M/KEP/2025")]

        # 3) buang baris noise (footer berulang, nomor halaman berdiri sendiri)
        if any(re.match(p, stripped) for p in NOISE_LINE_PATTERNS):
            i += 1
            continue

        # 4) tabel HTML
        if stripped.startswith("<table"):
            flush_paragraph()
            in_table = True
            table_buffer = []
        if in_table:
            table_buffer.append(line)
            if "</table>" in line:
                in_table = False
                md_table, merged = html_table_to_markdown("\n".join(table_buffer))
                if md_table:
                    extra = {"merged_formula_rows": merged} if merged else {}
                    add_block("table", replace_inline_images(md_table), table_source="html", **extra)
            i += 1
            continue

        # 4b) tabel Markdown pipe -> baris "| ... |" diikuti separator "| --- |"
        if (MD_TABLE_ROW_RE.match(stripped) and i + 1 < n
                and MD_TABLE_SEP_RE.match(lines[i + 1].strip())):
            flush_paragraph()
            md_rows = [stripped, lines[i + 1].strip()]
            j = i + 2
            while j < n and MD_TABLE_ROW_RE.match(lines[j].strip()):
                md_rows.append(lines[j].strip())
                j += 1
            content = "\n".join(replace_inline_images(r) for r in md_rows)
            add_block("table", content, table_source="markdown_pipe")
            i = j
            continue

        # 5) gambar satu baris penuh: dekoratif dibuang, informatif jadi image_note
        img_match = IMAGE_LINE_RE.match(stripped)
        if img_match:
            kept = image_alt_text(img_match.group(1))
            if kept:
                flush_paragraph()
                add_block("image_note", kept)
            i += 1
            continue

        # gambar di tengah baris: ganti dengan labelnya (bila informatif) lalu proses biasa
        if INLINE_IMAGE_RE.search(stripped):
            line = replace_inline_images(line)
            stripped = line.strip()
            if not stripped or stripped.strip("#* ") == "":
                i += 1
                continue

        # 6) heading -> update section_stack
        h_match = HEADING_RE.match(stripped)
        if h_match:
            flush_paragraph()
            title = re.sub(r"\*+", "", h_match.group(2)).strip()
            # bersihkan sisa kurung kosong akibat penanda footnote "(*)" yg asteriknya terbuang,
            # lalu rapikan spasi ganda yg mungkin tertinggal
            title = re.sub(r"\(\s*\)", "", title)
            title = re.sub(r"\s{2,}", " ", title).strip()
            if title:
                level = heading_level(title, section_stack)
                section_stack = [s for s in section_stack if s[0] < level]
                section_stack.append((level, title))
                add_block("heading", title)
            i += 1
            continue

        # 7) baris kosong -> pemisah paragraf, selain itu masuk buffer
        if stripped == "":
            flush_paragraph()
        else:
            buffer.append(line)
        i += 1

    flush_paragraph()
    return blocks


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    issues = load_known_issues()

    total = 0
    for md_file in sorted(INPUT_DIR.glob("*.md")):
        blocks = process_file(md_file)
        attach_source_notes(blocks, issues)
        total += len(blocks)
        out_path = OUTPUT_DIR / f"{md_file.stem}_processed.json"
        out_path.write_text(json.dumps(blocks, ensure_ascii=False, indent=2), encoding="utf-8")

        counts: dict[str, int] = {}
        for b in blocks:
            counts[b["block_type"]] = counts.get(b["block_type"], 0) + 1
        noted = sum(1 for b in blocks if b.get("source_notes"))
        no_page = sum(1 for b in blocks if b["page"] is None)
        lampiran = sum(1 for b in blocks if b["doc_part"] == "lampiran")
        print(f"{md_file.name}: {len(blocks)} blocks {counts} | lampiran {lampiran} | "
              f"tanpa halaman {no_page} | bercatatan sumber {noted} -> {out_path}")

    print(f"Total blocks (semua dokumen): {total}")

    # setiap catatan cacat sumber harus menempel di setiap dokumen yang disebutkannya
    attached: dict[str, set[str]] = {}
    for out_path in OUTPUT_DIR.glob("*_processed.json"):
        for b in json.loads(out_path.read_text(encoding="utf-8")):
            for n in b.get("source_notes", []):
                attached.setdefault(n["id"], set()).add(b["source_file"])
    for issue in issues:
        missing = set(issue.get("source_files", [])) - attached.get(issue["id"], set())
        if missing:
            print(f"[PERINGATAN] catatan '{issue['id']}' tidak menempel di: {sorted(missing)} "
                  f"(periksa match_all di {KNOWN_ISSUES_FILE.name})")


if __name__ == "__main__":
    main()
