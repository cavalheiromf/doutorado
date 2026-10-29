#!/usr/bin/env bash
# ==============================================================================
# Master Pipeline Orchestrator: OSCA Mechanosensitive Ion Channels (Vellozia)
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
  -s, --step STEP       Etapa a executar: 'all', 'sequences', 'rates', 'promoters', 'expression', 'verify' (padrão: all)
  -t, --threads N       Número de threads para processamento paralelo (padrão: 8)
  -m, --mode MODE       Modo de execução: 'local' ou 'slurm' (padrão: local)
  -h, --help            Exibe esta mensagem de ajuda

Exemplos:
  $0 --step all --mode local
  $0 --step rates --threads 4
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
echo "    PIPELINE CANAIS MECANOSSENSÍVEIS OSCA (VELLOZIA)"
echo "=============================================================================="
echo "Modo: ${MODE} | Threads: ${THREADS} | Etapa: ${STEP}"
echo "Diretório base: ${SCRIPT_DIR}"
echo "Data: $(date)"
echo "------------------------------------------------------------------------------"

run_sequences() {
    echo -e "\n>>> [1/5] Extração de Sequências e Validação de IDs OSCA <<<"
    if [[ -f "${SCRIPT_DIR}/01_gene_identification/results/oscasIDs.txt" ]]; then
        echo "[LOCAL] Mapeando pares ortólogos e extraindo CDS/Proteínas..."
        "$PYTHON" "${WORKFLOW_DIR}/04_extract_sequences.py" || true
    else
        echo "[AVISO] Tabela de mapeamento oscasIDs.txt não encontrada. Pulando etapa de extração."
    fi
}

run_rates() {
    echo -e "\n>>> [2/5] Taxas Evolutivas Ka/Ks e Estimativa PAML (codeml/yn00) <<<"
    echo "[LOCAL] Executando re-estimativas de taxas de divergência..."
    "$PYTHON" "${WORKFLOW_DIR}/04_rerun_pal2nal_yn00.py" || true
    "$PYTHON" "${WORKFLOW_DIR}/04_rerun_codeml_pairwise.py" || true
}

run_promoters() {
    echo -e "\n>>> [3/5] Análise de Motivos Promotores (PlantCARE) <<<"
    echo "[LOCAL] Extraindo e mapeando coordenadas regulatórias 2000 bp upstream..."
    "$PYTHON" "${WORKFLOW_DIR}/04_extract_promoters.py" || true
    "$PYTHON" "${WORKFLOW_DIR}/04_rename_promoters.py" || true
}

run_expression() {
    echo -e "\n>>> [4/5] Análise Transcriptômica e Expressão Diferencial (DESeq2) <<<"
    if command -v Rscript &> /dev/null; then
        echo "[LOCAL] Executando modelo DESeq2 em R..."
        Rscript "${WORKFLOW_DIR}/06_run_deseq2.R" || true
        Rscript "${WORKFLOW_DIR}/06_run_lfcshrink_rankings.R" || true
    else
        echo "[AVISO] Rscript não encontrado no ambiente ativo. Para rodar a etapa de expressão, instale as dependências R listadas no environment.yml."
    fi
}

run_verify() {
    echo -e "\n>>> [5/5] Testes de Verificação Empírica e Consistência <<<"
    echo "[LOCAL] Executando challenger empírico do manuscrito..."
    "$PYTHON" "${WORKFLOW_DIR}/root_test_empirical_challenger.py" || true
}

case "$STEP" in
    sequences)
        run_sequences ;;
    rates)
        run_rates ;;
    promoters)
        run_promoters ;;
    expression)
        run_expression ;;
    verify)
        run_verify ;;
    all)
        run_sequences
        run_rates
        run_promoters
        run_expression
        run_verify
        ;;
    *)
        echo "[ERRO] Etapa desconhecida: $STEP" >&2
        exit 1
        ;;
esac

echo -e "\n=============================================================================="
echo "    PIPELINE OSCA EXECUTADO COM SUCESSO!"
echo "=============================================================================="

