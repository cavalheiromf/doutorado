import json
from pathlib import Path
import sys
import networkx as nx

# Import graphify helpers
from graphify.build import build
from graphify.cluster import cluster, score_all
from graphify.analyze import god_nodes, surprising_connections, suggest_questions
from graphify.report import generate
from graphify.export import to_json, to_html, _git_head as _gh

# 1. Load AST result
ast_path = Path("graphify-out/.graphify_ast.json")
ast_result = json.loads(ast_path.read_text(encoding="utf-8"))

# 2. Load Semantic result
semantic_path = Path("graphify-out/.graphify_semantic_new.json")
sem_result = json.loads(semantic_path.read_text(encoding="utf-8"))

# 3. Combine in order: AST first, then Semantic
merged = {
    "nodes": list(ast_result.get("nodes", [])) + list(sem_result.get("nodes", [])),
    "edges": list(ast_result.get("edges", [])) + list(sem_result.get("edges", [])),
    "hyperedges": list(sem_result.get("hyperedges", [])),
    "input_tokens": ast_result.get("input_tokens", 0) + sem_result.get("input_tokens", 0),
    "output_tokens": ast_result.get("output_tokens", 0) + sem_result.get("output_tokens", 0),
}

# 4. Build NetworkX graph
print("Building graph...")
G = build([merged], dedup=True, root=Path("."))
print(f"Graph constructed: {G.number_of_nodes()} nodes, {G.number_of_edges()} edges")

# 5. Community detection
print("Running community clustering...")
communities = cluster(G, resolution=1.0)
cohesion = score_all(G, communities)
print(f"Detected {len(communities)} communities.")

# Print some community sizes and top nodes to help us label them
for cid, nodes in sorted(communities.items(), key=lambda kv: len(kv[1]), reverse=True)[:10]:
    print(f"Community {cid} (size {len(nodes)}):")
    # print top 10 nodes by degree in this community
    subg = G.subgraph(nodes)
    degrees = sorted(subg.degree(), key=lambda x: x[1], reverse=True)
    top_deg = [f"{G.nodes[n].get('label', n)} (deg={subg.degree(n)})" for n, d in degrees[:8]]
    print(f"  Top nodes: {', '.join(top_deg)}")

# 6. Analyze God nodes & Surprising connections
print("Analyzing god nodes and surprising connections...")
try:
    gods = god_nodes(G)
except Exception as e:
    print(f"Warning: god nodes analysis failed: {e}")
    gods = []

try:
    surprises = surprising_connections(G, communities)
except Exception as e:
    print(f"Warning: surprising connections analysis failed: {e}")
    surprises = []

# Load/create labels
labels_path = Path("graphify-out/.graphify_labels.json")
if labels_path.exists():
    try:
        labels = {int(k): v for k, v in json.loads(labels_path.read_text(encoding="utf-8")).items()}
    except Exception:
        labels = {cid: f"Community {cid}" for cid in communities}
else:
    labels = {cid: f"Community {cid}" for cid in communities}

# Ensure all communities have a label
for cid in communities:
    labels.setdefault(cid, f"Community {cid}")

questions = suggest_questions(G, communities, labels)

# 7. Generate report
print("Generating GRAPH_REPORT.md...")
tokens = {"input": merged["input_tokens"], "output": merged["output_tokens"]}
_commit = _gh()

# Get some stats
stats = {
    "total_files": 139,
    "total_words": 150000,
}

report = generate(
    G, communities, cohesion, labels, gods, surprises,
    stats, tokens, ".", suggested_questions=questions,
    min_community_size=3, built_at_commit=_commit
)
(Path("graphify-out") / "GRAPH_REPORT.md").write_text(report, encoding="utf-8")

# 8. Export to graph.json
print("Saving graph.json...")
to_json(G, communities, "graphify-out/graph.json")

# Save labels
labels_json = {str(k): v for k, v in labels.items()}
labels_path.write_text(json.dumps(labels_json, ensure_ascii=False), encoding="utf-8")

# Save HTML visualization
print("Saving graph.html...")
try:
    to_html(G, communities, "graphify-out/graph.html", community_labels=labels)
    print("Graph visualization saved successfully!")
except Exception as e:
    print(f"Warning: could not export html: {e}")

print("All done!")
