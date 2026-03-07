#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
OUT_DIR="${1:-$ROOT_DIR/public_release}"
TEMPLATE_DIR="$ROOT_DIR/templates/public_release"

rm -rf "$OUT_DIR"
mkdir -p "$OUT_DIR"

rsync -a "$ROOT_DIR/" "$OUT_DIR/" \
  --exclude ".git/" \
  --exclude ".venv/" \
  --exclude ".DS_Store" \
  --exclude "__pycache__/" \
  --exclude "*.pyc" \
  --exclude ".env" \
  --exclude "config/.encryption_key" \
  --exclude "database/db/*.db" \
  --exclude "README.md" \
  --exclude "core/pipeline.py" \
  --exclude "workflows/builder.py" \
  --exclude "workflows/routers.py" \
  --exclude "agenticai_private/" \
  --exclude "private/" \
  --exclude "templates/" \
  --exclude "public_release/" \
  --exclude "templates/public_release/"

# Replace sensitive core implementation with portfolio-safe templates
cp "$TEMPLATE_DIR/README.en_ja.md" "$OUT_DIR/README.md"
cp "$TEMPLATE_DIR/core/pipeline.py" "$OUT_DIR/core/pipeline.py"
cp "$TEMPLATE_DIR/workflows/builder.py" "$OUT_DIR/workflows/builder.py"
cp "$TEMPLATE_DIR/workflows/routers.py" "$OUT_DIR/workflows/routers.py"

echo "Public release prepared at: $OUT_DIR"
