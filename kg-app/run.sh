#!/usr/bin/env bash
# Launch the IEC 60617 KG app (backend serves the API + the frontend).
set -e
cd "$(dirname "$0")/backend"
python3 build_kg.py                      # rebuild derived data from ../../wiki (the source of truth)
exec python3 -m uvicorn main:app --port "${PORT:-8077}" --reload
