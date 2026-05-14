#!/bin/bash

if command -v uv &> /dev/null
then
    uv run python -m src "$@"
    exit $?
fi

if [ -d ".venv" ]; then
    VENV_PYTHON="./.venv/bin/python"
    if [ -f "$VENV_PYTHON" ]; then
        "$VENV_PYTHON" -m src "$@"
        exit $?
    fi
fi

echo "❌ Error: 'uv' not found and no virtual environment detected in ./.venv"
echo "💡 To fix this, please:"
echo "   - Install 'uv' (recommended): https://github.com/astral-sh/uv"
echo "   - OR create venv manually: python3 -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt"
exit 1
