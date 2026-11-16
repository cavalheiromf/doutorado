#!/usr/bin/env bash

# run_analysis.sh
# Wrapper script to execute the R downstream differential expression analysis.

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(cd "$SCRIPT_DIR/../../.." && pwd)"

LOG_DIR="$PROJECT_DIR/logs"
mkdir -p "$LOG_DIR"

LOG_FILE="$LOG_DIR/06_expression.log"

echo "=================================================="
echo "Starting OSCA RNA-Seq Expression & DE Analysis"
echo "Date: $(date)"
echo "Log file: $LOG_FILE"
echo "=================================================="

# Run the Rscript and redirect stdout and stderr to both the log file and terminal
Rscript "$SCRIPT_DIR/run_deseq2.R" 2>&1 | tee "$LOG_FILE"

EXIT_STATUS=${PIPESTATUS[0]}

echo "=================================================="
if [ $EXIT_STATUS -eq 0 ]; then
  echo "Analysis completed successfully!"
else
  echo "Error: Analysis failed with exit code $EXIT_STATUS. Please check the log file: $LOG_FILE"
fi
echo "Date: $(date)"
echo "=================================================="

exit $EXIT_STATUS
