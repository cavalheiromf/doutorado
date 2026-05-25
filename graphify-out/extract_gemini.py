import json
import sys
import time
from pathlib import Path
import graphify.llm
from graphify.llm import _pack_chunks_by_tokens, _extract_with_adaptive_retry, _merge_into

# 1. Monkeypatch _call_openai_compat to add 15s delay
original_call = graphify.llm._call_openai_compat

def rate_limited_call(*args, **kwargs):
    print(f"[rate-limiter] Sleeping 15 seconds to respect Gemini Free Tier rate limits...", flush=True)
    time.sleep(15)
    print(f"[rate-limiter] Calling LLM model={kwargs.get('model')} (input len={len(kwargs.get('user_message', ''))})...", flush=True)
    return original_call(*args, **kwargs)

graphify.llm._call_openai_compat = rate_limited_call

# 2. Load files
print("Loading files from graphify-out/.graphify_uncached.txt...", flush=True)
uncached = [Path(line) for line in Path("graphify-out/.graphify_uncached.txt").read_text(encoding="utf-8").splitlines()]
print(f"Loaded {len(uncached)} files.", flush=True)

# 3. Pack chunks (deterministic sorting and grouping)
chunks = _pack_chunks_by_tokens(uncached, token_budget=60000)
total_chunks = len(chunks)
print(f"Packed into {total_chunks} chunks.", flush=True)

# 4. Try loading existing semantic new file to support resume!
semantic_file = Path("graphify-out/.graphify_semantic_new.json")
if semantic_file.exists():
    try:
        merged = json.loads(semantic_file.read_text(encoding="utf-8"))
        print(f"Loaded existing partial result with {len(merged.get('nodes', []))} nodes and {len(merged.get('edges', []))} edges.", flush=True)
    except Exception:
        merged = {
            "nodes": [], "edges": [], "hyperedges": [],
            "input_tokens": 0, "output_tokens": 0,
            "failed_chunks": 0,
        }
else:
    merged = {
        "nodes": [], "edges": [], "hyperedges": [],
        "input_tokens": 0, "output_tokens": 0,
        "failed_chunks": 0,
    }

# Track which files have already been processed to avoid re-extracting if we resume
processed_files = set()
for node in merged.get("nodes", []):
    if node.get("source_file"):
        processed_files.add(node["source_file"])

# 5. Extract chunks sequentially
for idx, chunk in enumerate(chunks):
    # Check if this chunk is already fully processed by looking at its files
    # A file is processed if its relative path matches one of the files in processed_files
    chunk_paths_str = []
    for p in chunk:
        try:
            rel = str(p.relative_to(Path(".").resolve()))
        except ValueError:
            rel = str(p)
        chunk_paths_str.append(rel)

    if all(rel in processed_files for rel in chunk_paths_str) and len(processed_files) > 0:
        print(f"Chunk {idx + 1}/{total_chunks} already processed. Skipping.", flush=True)
        continue

    print(f"\n--- Extracting chunk {idx + 1}/{total_chunks} ({len(chunk)} files) ---", flush=True)
    for p in chunk:
        print(f"  - {p}", flush=True)

    t0 = time.time()
    try:
        result = _extract_with_adaptive_retry(
            chunk,
            backend="gemini",
            api_key=None,
            model=None,
            root=Path("."),
            max_depth=3,
        )
        elapsed = round(time.time() - t0, 2)
        print(f"Chunk {idx + 1}/{total_chunks} done in {elapsed}s: {len(result.get('nodes', []))} nodes, {len(result.get('edges', []))} edges.", flush=True)
        _merge_into(merged, result)
        
        # Save intermediate results incrementally!
        semantic_file.write_text(
            json.dumps(merged, indent=2, ensure_ascii=False), encoding="utf-8"
        )
    except Exception as exc:
        print(f"Chunk {idx + 1}/{total_chunks} failed: {exc}", file=sys.stderr, flush=True)
        merged["failed_chunks"] = merged.get("failed_chunks", 0) + 1

print("\nAll chunks processed!", flush=True)
print(f"Total merged semantic nodes: {len(merged.get('nodes', []))}", flush=True)
print(f"Total merged semantic edges: {len(merged.get('edges', []))}", flush=True)
print(f"Failed chunks count: {merged.get('failed_chunks', 0)}", flush=True)

# Final save
semantic_file.write_text(
    json.dumps(merged, indent=2, ensure_ascii=False), encoding="utf-8"
)
print("Done!", flush=True)
