#!/usr/bin/env bash
# Sync vital-ontology-curator into curatedhealth/vital-expert-marketplace (rsync -aL, no symlinks).
set -euo pipefail
SRC="$(cd "$(dirname "$0")/.." && pwd)"
DEST="${MARKETPLACE_DIR:-$HOME/src/vital-expert-marketplace}/plugins/vital-ontology-curator"
mkdir -p "$DEST"
rsync -aL --delete \
  --exclude '.git' \
  --exclude '__pycache__' \
  --exclude '*.pyc' \
  --exclude '.DS_Store' \
  "$SRC/" "$DEST/"
echo "Synced to $DEST"
if command -v claude >/dev/null 2>&1; then
  (cd "$DEST" && claude plugin validate .) || true
fi
