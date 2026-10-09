"""
eval_retrieval.py
Evaluasi tahap RETRIEVAL terhadap test set (data/evaluation/test_set_buku_iku.md).

Untuk tiap pertanyaan, "chunk bukti" = chunk yang memuat SEMUA "Kata kunci bukti"
soal tersebut. Metrik yang dihitung:
- Hit@1/3/5 : ada chunk bukti di k hasil teratas Retriever.search()
- MRR       : rata-rata 1/rank chunk bukti pertama
- Halaman   : apakah halaman chunk bukti dari dokumen utama (Buku) cocok dengan
              halaman di test set -> mengukur akurasi sitasi
- Rank@20   : posisi chunk bukti pada 20 hasil mentah (diagnosis "nyaris kena")
- Corpus    : apakah chunk bukti ada di corpus sama sekali; jika tidak, masalahnya
              di parsing/chunking, bukan di retrieval
Soal di luar cakupan (tanpa kata kunci) lolos jika distance hasil #1 >= --oos-threshold.

Output: reports/evaluation/retrieval_eval_<timestamp>.json dan .md

Jalankan dari root project:
    python src/evaluation/eval_retrieval.py                     # preset v2, koleksi pmpt_qa_v2
    python src/evaluation/eval_retrieval.py --rerank            # + reranker bge-reranker-v2-m3
    python src/evaluation/eval_retrieval.py --preset lama --collection pmpt_qa         --metadata data/legacy/v1/embeddings/metadata.jsonl --oos-threshold 0.9   # baseline v1
"""

import argparse
import json
import re
import statistics
import sys
import time
from datetime import datetime
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(PROJECT_ROOT / "src" / "retrieval"))
from retriever import Retriever, MODEL_NAME, COLLECTION_NAME_V2  # noqa: E402

TEST_SET_FILE = PROJECT_ROOT / "data" / "evaluation" / "test_set_buku_iku.md"
METADATA_FILE = PROJECT_ROOT / "data" / "embeddings" / "metadata.jsonl"
RESULTS_DIR = PROJECT_ROOT / "reports" / "evaluation"

PRIMARY_SOURCE = "Buku_IKU_Diktisaintek_Berdampak_V1.md"
DIAG_DEPTH = 20
SNIPPET_LEN = 300

SECTION_RE = re.compile(r"^### ([DH]\d{2})\b(.*)$", re.M)
SUMMARY_ROW_RE = re.compile(
    r"^\| ([DH]\d{2}) \| ([^|]+?) \| ([^|]+?) \| ([^|]+?) \| ([^|]+?) \|$", re.M
)


# ---------------------------------------------------------------------------
# Parsing test set
# ---------------------------------------------------------------------------

def get_field(block: str, name: str) -> str:
    """Isi dari '**name:**' sampai field bold berikutnya ('**Xxx:**') atau akhir blok."""
    m = re.search(
        rf"\*\*{re.escape(name)}:\*\*(.*?)(?=\n\*\*[A-Z][^*\n]*:\*\*|\Z)", block, re.S
    )
    return m.group(1).strip() if m else ""


def parse_pages(sumber: str) -> list[int]:
    """'hlm. 49–50' -> [49, 50]; 'hlm. 49; ... hlm. 51' -> [49, 51]."""
    pages = set()
    for group in re.findall(r"hlm\.\s*([\d\s,–-]+)", sumber):
        for part in group.split(","):
            nums = [int(x) for x in re.findall(r"\d+", part)]
            if len(nums) == 2 and re.search(r"[–-]", part):
                pages.update(range(nums[0], nums[1] + 1))
            else:
                pages.update(nums)
    return sorted(pages)


def load_test_set(path: Path) -> list[dict]:
    text = path.read_text(encoding="utf-8")

    summary = {
        m.group(1): {"tipe": m.group(2).strip(), "iku": m.group(3).strip(),
                     "topik": m.group(4).strip()}
        for m in SUMMARY_ROW_RE.finditer(text)
    }

    matches = list(SECTION_RE.finditer(text))
    questions = []
    for idx, m in enumerate(matches):
        qid = m.group(1)
        end = matches[idx + 1].start() if idx + 1 < len(matches) else len(text)
        block = text[m.end():end].split("\n---", 1)[0]

        question = get_field(block, "Pertanyaan")
        if not question:
            # soal definisi: pertanyaan ada di judul, setelah tanda '—'
            title = m.group(2).split("—", 1)[-1]
            question = title.replace("⚠️", "").strip().strip('"').strip()

        questions.append({
            "id": qid,
            **summary.get(qid, {"tipe": "?", "iku": "?", "topik": "?"}),
            "question": " ".join(question.split()),
            "expected_answer": get_field(block, "Jawaban benar"),
            "expected_pages": parse_pages(get_field(block, "Sumber")),
            "keywords": re.findall(r"`([^`]+)`", get_field(block, "Kata kunci bukti")),
        })
    return questions


# ---------------------------------------------------------------------------
# Pencocokan bukti
# ---------------------------------------------------------------------------

def normalize(text: str) -> str:
    text = text.lower().replace("\\ ", " ")
    text = re.sub(r"[*_`|$]", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def is_evidence(content: str, keywords: list[str]) -> bool:
    if not keywords:
        return False
    norm_content = normalize(content)
    return all(normalize(k) in norm_content for k in keywords)


def load_corpus(path: Path = METADATA_FILE) -> list[dict]:
    with open(path, encoding="utf-8") as f:
        return [json.loads(line) for line in f if line.strip()]


def page_range(item: dict) -> tuple[int, int]:
    """Chunk lama punya 'page'; chunk v2 punya 'page_start'/'page_end'."""
    start = item.get("page_start", item.get("page"))
    end = item.get("page_end", start)
    return start, end


def page_label(start: int, end: int) -> str:
    return str(start) if start == end else f"{start}–{end}"


def pages_overlap(start: int, end: int, expected: list[int]) -> bool:
    return any(start <= p <= end for p in expected)


# ---------------------------------------------------------------------------
# Evaluasi
# ---------------------------------------------------------------------------

def evaluate_question(q: dict, retriever: Retriever, corpus: list[dict], top_k: int,
                      oos_threshold: float) -> dict:
    keywords = q["keywords"]
    in_scope = bool(keywords)

    t0 = time.perf_counter()
    results = retriever.search(q["question"])
    latency = time.perf_counter() - t0

    # hasil mentah (tanpa filter panjang chunk) untuk diagnosis "nyaris kena"
    query_emb = retriever.model.encode([q["question"]], normalize_embeddings=True)[0]
    raw = retriever.collection.query(query_embeddings=[query_emb.tolist()],
                                     n_results=DIAG_DEPTH)

    retrieved = []
    for rank, r in enumerate(results, start=1):
        start, end = page_range(r)
        retrieved.append({
            "rank": rank,
            "source_file": r["source_file"],
            "page": page_label(start, end),
            "section_path": r["section_path"],
            "distance": round(r["distance"], 4),
            "is_evidence": is_evidence(r["content"], keywords),
            "page_match": pages_overlap(start, end, q["expected_pages"]),
            "doc_part": r.get("doc_part"),
            "also_in": r.get("also_in", []),
            "snippet": " ".join(r["content"].split())[:SNIPPET_LEN],
        })

    first_hit = next((r for r in retrieved if r["is_evidence"]), None)
    # bukti gabungan: semua kata kunci tercakup oleh GABUNGAN chunk top-k (untuk isi yang
    # memang terpecah ke beberapa chunk, mis. tabel panjang)
    union_text = normalize("\n".join(r["content"] for r in results))
    union_hit = bool(keywords) and all(normalize(k) in union_text for k in keywords)
    first_hit_rank = first_hit["rank"] if first_hit else None

    primary_hit = next(
        (r for r in retrieved if r["is_evidence"] and r["source_file"] == PRIMARY_SOURCE), None
    )

    raw_rank = None
    for rank, doc in enumerate(raw["documents"][0], start=1):
        if is_evidence(doc, keywords):
            raw_rank = rank
            break

    corpus_evidence = [
        {"chunk_id": c["chunk_id"], "source_file": c["source_file"], "page": page_label(*page_range(c))}
        for c in corpus if is_evidence(c.get("text") or c["content"], keywords)
    ]

    top1 = retrieved[0] if retrieved else None

    if not in_scope:
        passed = top1 is None or top1["distance"] >= oos_threshold
        status = "LOLOS (di luar cakupan)" if passed else "GAGAL (di luar cakupan)"
    elif first_hit_rank:
        status = f"HIT @{first_hit_rank}"
    elif not corpus_evidence:
        status = "MISS - bukti tidak ada di corpus"
    elif raw_rank:
        status = f"MISS - bukti di rank mentah {raw_rank}"
    else:
        status = f"MISS - bukti tidak masuk top-{DIAG_DEPTH}"

    return {
        **q,
        "in_scope": in_scope,
        "status": status,
        "n_returned": len(retrieved),
        "first_hit_rank": first_hit_rank,
        "union_hit": union_hit,
        "reciprocal_rank": (1 / first_hit_rank) if first_hit_rank else 0.0,
        "hit_source": first_hit["source_file"] if first_hit else None,
        "primary_hit_page": primary_hit["page"] if primary_hit else None,
        "page_correct": primary_hit["page_match"] if primary_hit else None,
        "primary_hit_lampiran": (primary_hit.get("doc_part") == "lampiran") if primary_hit else None,
        "raw_rank_top20": raw_rank,
        "corpus_evidence_count": len(corpus_evidence),
        "corpus_evidence": corpus_evidence,
        "top1_source": top1["source_file"] if top1 else None,
        "top1_distance": top1["distance"] if top1 else None,
        "oos_pass": (status.startswith("LOLOS")) if not in_scope else None,
        "latency_s": round(latency, 3),
        "retrieved": retrieved,
    }


def pct(num: int, den: int) -> str:
    return f"{num / den * 100:.1f}%" if den else "-"


def hit_at(rows: list[dict], k: int) -> int:
    return sum(1 for r in rows if r["first_hit_rank"] and r["first_hit_rank"] <= k)


def summarize(rows: list[dict], top_k: int) -> dict:
    scoped = [r for r in rows if r["in_scope"]]
    oos = [r for r in rows if not r["in_scope"]]
    n = len(scoped)

    def group_stats(group: list[dict]) -> dict:
        return {
            "n": len(group),
            "hit@1": hit_at(group, 1),
            "hit@3": hit_at(group, 3),
            f"hit@{top_k}": hit_at(group, top_k),
            "mrr": round(statistics.mean(r["reciprocal_rank"] for r in group), 3) if group else 0,
        }

    by_type = {}
    for r in scoped:
        by_type.setdefault(r["tipe"], []).append(r)
    by_iku = {}
    for r in scoped:
        by_iku.setdefault(r["iku"], []).append(r)

    with_primary = [r for r in scoped if r["page_correct"] is not None]
    hits = [r for r in scoped if r["first_hit_rank"]]
    misses = [r for r in scoped if not r["first_hit_rank"]]

    return {
        "overall": group_stats(scoped),
        "hit_union": sum(1 for r in scoped if r.get("union_hit")),
        "by_type": {k: group_stats(v) for k, v in by_type.items()},
        "by_iku": {k: group_stats(v) for k, v in sorted(by_iku.items(), key=lambda x: x[0])},
        "page_citation": {
            "n_with_primary_evidence": len(with_primary),
            "page_correct": sum(1 for r in with_primary if r["page_correct"]),
            "from_lampiran": sum(1 for r in with_primary if r.get("primary_hit_lampiran")),
        },
        "top1_from_secondary": sum(
            1 for r in scoped if r["top1_source"] and r["top1_source"] != PRIMARY_SOURCE
        ),
        "hit_from_secondary": sum(
            1 for r in hits if r["hit_source"] != PRIMARY_SOURCE
        ),
        "evidence_not_in_corpus": [r["id"] for r in scoped if r["corpus_evidence_count"] == 0],
        "near_miss": [r["id"] for r in misses if r["raw_rank_top20"]],
        "out_of_scope": {
            "n": len(oos),
            "passed": sum(1 for r in oos if r["oos_pass"]),
            "top1_distances": {r["id"]: r["top1_distance"] for r in oos},
        },
        "distance": {
            "mean_top1_hit": round(statistics.mean(r["top1_distance"] for r in hits), 4) if hits else None,
            "mean_top1_miss": round(statistics.mean(r["top1_distance"] for r in misses), 4) if misses else None,
            "max_top1_in_scope": max((r["top1_distance"] for r in scoped if r["top1_distance"] is not None), default=None),
        },
        "latency_mean_s": round(statistics.mean(r["latency_s"] for r in rows), 3),
    }


# ---------------------------------------------------------------------------
# Laporan
# ---------------------------------------------------------------------------

def short_source(name: str | None) -> str:
    if not name:
        return "-"
    return "Buku" if name == PRIMARY_SOURCE else "PPT" if name.startswith("PPT") else name


def build_report(rows: list[dict], summary: dict, config: dict) -> str:
    k = config["top_k"]
    ov = summary["overall"]
    n = ov["n"]
    pc = summary["page_citation"]
    oos = summary["out_of_scope"]
    lines = []
    add = lines.append

    add("# Laporan Evaluasi Retrieval")
    add("")
    add(f"- Waktu: {config['timestamp']}")
    add(f"- Test set: `{config['test_set']}` ({len(rows)} soal, {n} dalam cakupan, {oos['n']} di luar cakupan)")
    add(f"- Model embedding: `{config['model']}` | Koleksi: `{config['collection']}` ({config['n_chunks']} chunk)")
    add(f"- top_k: {k} | ambang di luar cakupan: distance ≥ {config['oos_threshold']}")
    add(f"- Retriever: `{config.get('retriever')}`")
    add(f"- Sitasi Buku yang berasal dari Lampiran: {pc.get('from_lampiran', 0)}")
    add("")
    add("Definisi: sebuah soal **HIT** jika ada chunk yang memuat semua *kata kunci bukti* soal "
        f"tersebut di {k} hasil teratas `Retriever.search()`.")
    add("")

    add("## Ringkasan")
    add("")
    add("| Metrik | Nilai |")
    add("|---|---|")
    add(f"| Hit@1 | {ov['hit@1']}/{n} ({pct(ov['hit@1'], n)}) |")
    add(f"| Hit@3 | {ov['hit@3']}/{n} ({pct(ov['hit@3'], n)}) |")
    add(f"| Hit@{k} | {ov[f'hit@{k}']}/{n} ({pct(ov[f'hit@{k}'], n)}) |")
    add(f"| MRR@{k} | {ov['mrr']} |")
    add(f"| Hit@{k} gabungan (semua kata kunci ada di gabungan top-{k}) | {summary['hit_union']}/{n} "
        f"({pct(summary['hit_union'], n)}) |")
    add(f"| Halaman sitasi benar (chunk bukti dari Buku) | {pc['page_correct']}/{pc['n_with_primary_evidence']} "
        f"({pct(pc['page_correct'], pc['n_with_primary_evidence'])}) |")
    add(f"| Hasil #1 berasal dari PPT (bukan Buku) | {summary['top1_from_secondary']}/{n} |")
    add(f"| Chunk bukti pertama berasal dari PPT | {summary['hit_from_secondary']} soal |")
    add(f"| Bukti tidak ada di corpus (masalah chunking) | {len(summary['evidence_not_in_corpus'])} "
        f"{summary['evidence_not_in_corpus'] or ''} |")
    add(f"| Nyaris kena (bukti di top-{DIAG_DEPTH} tapi tidak di top-{k}) | {len(summary['near_miss'])} "
        f"{summary['near_miss'] or ''} |")
    add(f"| Soal di luar cakupan lolos | {oos['passed']}/{oos['n']} |")
    d = summary["distance"]
    add(f"| Rata-rata distance #1 (soal HIT / MISS) | {d['mean_top1_hit']} / {d['mean_top1_miss']} |")
    add(f"| Distance #1 tertinggi soal dalam cakupan | {d['max_top1_in_scope']} |")
    add(f"| Distance #1 soal di luar cakupan | {oos['top1_distances']} |")
    add(f"| Rata-rata waktu per query | {summary['latency_mean_s']} s |")
    add("")

    add("### Per tipe soal")
    add("")
    add(f"| Tipe | n | Hit@1 | Hit@3 | Hit@{k} | MRR |")
    add("|---|---|---|---|---|---|")
    for tipe, s in summary["by_type"].items():
        add(f"| {tipe} | {s['n']} | {pct(s['hit@1'], s['n'])} | {pct(s['hit@3'], s['n'])} | "
            f"{pct(s[f'hit@{k}'], s['n'])} | {s['mrr']} |")
    add("")

    add("### Per IKU")
    add("")
    add(f"| IKU | n | Hit@1 | Hit@{k} | MRR |")
    add("|---|---|---|---|---|")
    for iku, s in summary["by_iku"].items():
        add(f"| {iku} | {s['n']} | {s['hit@1']}/{s['n']} | {s[f'hit@{k}']}/{s['n']} | {s['mrr']} |")
    add("")

    add("## Hasil per soal")
    add("")
    add("| ID | IKU | Status | Sumber bukti | Hlm. bukti (Buku) | Hlm. benar | Rank mentah | Distance #1 | Sumber #1 |")
    add("|---|---|---|---|---|---|---|---|---|")
    for r in rows:
        page_cell = "-"
        if r["primary_hit_page"] is not None:
            page_cell = f"{r['primary_hit_page']} {'✅' if r['page_correct'] else '❌'}"
        add(f"| {r['id']} | {r['iku']} | {r['status']} | {short_source(r['hit_source'])} | {page_cell} | "
            f"{', '.join(map(str, r['expected_pages'])) or '-'} | {r['raw_rank_top20'] or '-'} | "
            f"{r['top1_distance']} | {short_source(r['top1_source'])} |")
    add("")

    add("## Detail per soal")
    add("")
    for r in rows:
        mark = "✅" if (r["first_hit_rank"] or r["oos_pass"]) else "❌"
        add(f"<details><summary>{mark} <b>{r['id']}</b> — {r['status']} — {r['question'][:90]}</summary>")
        add("")
        add(f"**Pertanyaan:** {r['question']}")
        add("")
        add(f"**Kata kunci bukti:** {', '.join(f'`{k}`' for k in r['keywords']) or '— (di luar cakupan)'}")
        add("")
        add(f"**Halaman benar:** {', '.join(map(str, r['expected_pages'])) or '-'} | "
            f"**Chunk bukti di corpus:** {r['corpus_evidence_count']} "
            + (f"({', '.join(f'{short_source(c['source_file'])} hlm.{c['page']}' for c in r['corpus_evidence'][:6])})"
               if r["corpus_evidence"] else ""))
        add("")
        add("| # | Bukti | Sumber | Hlm. | Distance | Section | Cuplikan |")
        add("|---|---|---|---|---|---|---|")
        for it in r["retrieved"]:
            snippet = it["snippet"][:160].replace("|", "/")
            section = (it["section_path"] or "")[-70:].replace("|", "/")
            add(f"| {it['rank']} | {'✅' if it['is_evidence'] else ''} | {short_source(it['source_file'])} | "
                f"{it['page']} | {it['distance']} | …{section} | {snippet} |")
        add("")
        add("</details>")
        add("")

    return "\n".join(lines)


def print_console(rows: list[dict], summary: dict, top_k: int):
    ov = summary["overall"]
    n = ov["n"]
    print()
    print("=" * 78)
    print("HASIL EVALUASI RETRIEVAL")
    print("=" * 78)
    for r in rows:
        print(f"{r['id']:<4} IKU {r['iku']:<5} {r['status']:<42} d#1={r['top1_distance']}")
    print("-" * 78)
    print(f"Hit@1   : {ov['hit@1']}/{n} ({pct(ov['hit@1'], n)})")
    print(f"Hit@3   : {ov['hit@3']}/{n} ({pct(ov['hit@3'], n)})")
    print(f"Hit@{top_k}   : {ov[f'hit@{top_k}']}/{n} ({pct(ov[f'hit@{top_k}'], n)})")
    print(f"MRR@{top_k}   : {ov['mrr']}")
    print(f"Hit@{top_k} gabungan: {summary['hit_union']}/{n} ({pct(summary['hit_union'], n)})")
    pc = summary["page_citation"]
    print(f"Halaman sitasi benar : {pc['page_correct']}/{pc['n_with_primary_evidence']} "
          f"(sitasi dari Lampiran: {pc.get('from_lampiran', 0)})")
    print(f"Hasil #1 dari PPT    : {summary['top1_from_secondary']}/{n}")
    oos = summary["out_of_scope"]
    print(f"Di luar cakupan lolos: {oos['passed']}/{oos['n']}")


def main():
    parser = argparse.ArgumentParser(description="Evaluasi retrieval terhadap test set IKU")
    parser.add_argument("--top-k", type=int, default=5)
    parser.add_argument("--oos-threshold", type=float, default=0.45,
                        help="soal di luar cakupan lolos jika distance hasil #1 >= nilai ini "
                             "(cosine v2: 0.45; L2 koleksi lama: 0.9)")
    parser.add_argument("--test-set", type=Path, default=TEST_SET_FILE)
    parser.add_argument("--collection", default=COLLECTION_NAME_V2,
                        help="koleksi Chroma yang diuji, mis. pmpt_qa_v2")
    parser.add_argument("--metadata", type=Path, default=METADATA_FILE,
                        help="metadata.jsonl dari tahap embedding yang sesuai dengan koleksi")
    parser.add_argument("--preset", choices=["lama", "v2"], default="v2",
                        help="lama = dense saja; v2 = kandidat 30 + hybrid + IKU boost + dedupe (tanpa rerank)")
    parser.add_argument("--candidates", type=int, help="jumlah kandidat sebelum dipilih top-k")
    parser.add_argument("--hybrid", action="store_true", help="tambahkan BM25 (kata persis) + RRF")
    parser.add_argument("--iku-boost", action="store_true", help="dahulukan IKU yang disebut di pertanyaan")
    parser.add_argument("--dedupe", action="store_true", help="dahulukan Bab V, buang kembaran Lampiran/PPT")
    parser.add_argument("--rerank", action="store_true", help="reranker bge-reranker-v2-m3 (unduh ±2 GB sekali)")
    parser.add_argument("--min-chars", type=int, help="buang dokumen lebih pendek dari ini (lama: 80)")
    parser.add_argument("--sambung-tabel", action=argparse.BooleanOptionalAction, default=None,
                        help="sambung potongan lanjutan tabel dengan potongan sebelumnya (v2: aktif; "
                             "--no-sambung-tabel untuk pembanding)")
    args = parser.parse_args()
    if args.preset == "v2":
        args.candidates = args.candidates or 30
        args.hybrid = args.iku_boost = args.dedupe = True
        args.min_chars = 0 if args.min_chars is None else args.min_chars
        args.sambung_tabel = True if args.sambung_tabel is None else args.sambung_tabel
    retriever_options = {
        "candidates": args.candidates, "hybrid": args.hybrid, "iku_boost": args.iku_boost,
        "dedupe": args.dedupe, "rerank": args.rerank,
        "min_chars": 80 if args.min_chars is None else args.min_chars,
        "sambung_tabel": bool(args.sambung_tabel),
    }

    sys.stdout.reconfigure(encoding="utf-8")

    questions = load_test_set(args.test_set)
    missing_kw = [q["id"] for q in questions if not q["keywords"] and not q["tipe"].startswith("Jebakan")]
    print(f"Soal dimuat: {len(questions)}")
    if missing_kw:
        print(f"[PERINGATAN] Soal tanpa 'Kata kunci bukti' (dianggap di luar cakupan): {missing_kw}")

    corpus = load_corpus(args.metadata)
    print(f"Chunk corpus: {len(corpus)}")

    print("Load retriever...")
    retriever = Retriever(top_k=args.top_k, collection_name=args.collection, **retriever_options)
    print(f"Konfigurasi retriever: {retriever_options}")

    rows = []
    for q in questions:
        rows.append(evaluate_question(q, retriever, corpus, args.top_k, args.oos_threshold))

    summary = summarize(rows, args.top_k)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    config = {
        "timestamp": timestamp,
        "test_set": str(args.test_set.relative_to(PROJECT_ROOT)),
        "model": MODEL_NAME,
        "collection": args.collection,
        "n_chunks": retriever.collection.count(),
        "top_k": args.top_k,
        "oos_threshold": args.oos_threshold,
        "retriever": retriever_options,
    }

    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    stem = f"retrieval_eval_{args.collection}_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    json_path = RESULTS_DIR / f"{stem}.json"
    md_path = RESULTS_DIR / f"{stem}.md"

    json_path.write_text(
        json.dumps({"config": config, "summary": summary, "results": rows},
                   ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    md_path.write_text(build_report(rows, summary, config), encoding="utf-8")

    print_console(rows, summary, args.top_k)
    print()
    print(f"Laporan : {md_path}")
    print(f"Detail  : {json_path}")


if __name__ == "__main__":
    main()
