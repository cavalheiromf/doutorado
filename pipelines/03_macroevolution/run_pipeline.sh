#!/usr/bin/env bash
# ==============================================================================
# Master Pipeline Orchestrator: Macroevolution & Gene Family Dynamics (6 Taxa)
# Author: Mariana Feitosa Cavalheiro
# Supports: Local execution (--local) and Cluster submission (--slurm)
# ==============================================================================

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "${SCRIPT_DIR}/../.." && pwd)"
WORKFLOW_DIR="${SCRIPT_DIR}/workflow/scripts"
THREADS="${THREADS:-8}"
STEP="all"
MODE="local"

usage() {
    cat << EOF
Uso: $0 [opções]

Opções:
  -s, --step STEP       Etapa a executar: 'all', 'cafe5', 'duplications', 'enrichment', 'manuscript' (padrão: all)
  -t, --threads N       Número de threads/CPUs para execução paralela (padrão: 8)
  -m, --mode MODE       Modo de execução: 'local' ou 'slurm' (padrão: local)
  -h, --help            Exibe esta mensagem de ajuda

Exemplos:
  $0 --step all --mode local
  $0 --step manuscript --threads 4
EOF
    exit 0
}

while [[ $# -gt 0 ]]; do
    case "$1" in
        -s|--step) STEP="$2"; shift 2 ;;
        -t|--threads) THREADS="$2"; shift 2 ;;
        -m|--mode) MODE="$2"; shift 2 ;;
        -h|--help) usage ;;
        *) echo "[ERRO] Opção desconhecida: $1" >&2; usage ;;
    esac
done

export THREADS
export PROJECT_ROOT
export BASE_DIR="${SCRIPT_DIR}"
PYTHON="${PYTHON:-python3}"

echo "=============================================================================="
echo "    PIPELINE MACROEVOLUÇÃO VELLOZIACEAE (6 MONOCOTILEDÔNEAS)"
echo "=============================================================================="
echo "Modo: ${MODE} | Threads: ${THREADS} | Etapa: ${STEP}"
echo "Diretório base: ${SCRIPT_DIR}"
echo "Data: $(date)"
echo "------------------------------------------------------------------------------"

run_cafe5() {
    echo -e "\n>>> [1/4] Modelagem CAFE5 de Ganho e Perda Gênica <<<"
    if [[ "${MODE}" == "slurm" ]]; then
        echo "[SLURM] Submetendo jobs encadeados via SLURM..."
        bash "${WORKFLOW_DIR}/01_cafe5/submit_all_pipeline.sh"
    else
        echo "[LOCAL] Avaliando réplicas e modelos convergidos M1-M5 (Gamma k=3)..."
        "$PYTHON" "${WORKFLOW_DIR}/01_cafe5/05_evaluate_cafe5_models.py"
    fi
}

run_duplications() {
    echo -e "\n>>> [2/4] Modos de Duplicação e Sintenia (MCScanX / JCVI) <<<"
    echo "[LOCAL] Classificando modos de duplicação e associando a expansões CAFE5..."
    "$PYTHON" "${WORKFLOW_DIR}/02_duplications_synteny/03_classify_gene_duplications.py" || true
    "$PYTHON" "${WORKFLOW_DIR}/02_duplications_synteny/04_extract_expansions_and_duplications.py"
}

run_enrichment() {
    echo -e "\n>>> [3/4] Enriquecimento Funcional e Permutações Estratificadas <<<"
    if [[ "${MODE}" == "slurm" ]]; then
        echo "[SLURM] Submetendo pipeline de enriquecimento ao SLURM..."
        sbatch "${WORKFLOW_DIR}/03_functional_enrichment/09_run_enrichment_pipeline.sh"
    else
        echo "[LOCAL] Validando controles metodológicos de anotação e covariáveis..."
        "$PYTHON" "${WORKFLOW_DIR}/03_functional_enrichment/07_validate_outputs.py" || true
    fi
}

run_manuscript() {
    echo -e "\n>>> [4/4] Exportação das Tabelas e Figuras de Publicação <<<"
    echo "[LOCAL] Exportando tabelas suplementares e mestras em TSV..."
    "$PYTHON" "${WORKFLOW_DIR}/04_manuscript/01_export_manuscript_tables.py"
    "$PYTHON" "${WORKFLOW_DIR}/04_manuscript/06_format_publication_tables.py"
    
    echo "[LOCAL] Gerando figuras vetoriais (PDF/SVG) e rasterizadas (PNG 300 DPI)..."
    "$PYTHON" "${WORKFLOW_DIR}/04_manuscript/02_plot_manuscript_figures.py" || true
    "$PYTHON" "${WORKFLOW_DIR}/04_manuscript/03_plot_divergent_expansion_matrix.py" || true
    "$PYTHON" "${WORKFLOW_DIR}/04_manuscript/05_plot_supplementary_figures.py" || true
}

case "$STEP" in
    cafe5)
        run_cafe5 ;;
    duplications)
        run_duplications ;;
    enrichment)
        run_enrichment ;;
    manuscript)
        run_manuscript ;;
    all)
        run_cafe5
        run_duplications
        run_enrichment
        run_manuscript
        ;;
    *)
        echo "[ERRO] Etapa desconhecida: $STEP" >&2
        exit 1
        ;;
esac

echo -e "\n=============================================================================="
echo "    PIPELINE DE MACROEVOLUÇÃO EXECUTADO COM SUCESSO!"
echo "=============================================================================="
