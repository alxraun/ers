if (Get-Command uv -ErrorAction SilentlyContinue) {
    uv run python -m src @args
    exit $LASTEXITCODE
}

$VENV_PYTHON = ".\.venv\Scripts\python.exe"
if (Test-Path $VENV_PYTHON) {
    & $VENV_PYTHON -m src @args
    exit $LASTEXITCODE
}

Write-Host "❌ Error: 'uv' not found and no virtual environment detected in .\.venv" -ForegroundColor Red
Write-Host "💡 To fix this, please:"
Write-Host "   - Install 'uv' (recommended): https://github.com/astral-sh/uv"
Write-Host "   - OR create venv manually: python -m venv .venv; .\.venv\Scripts\activate; pip install -r requirements.txt"
exit 1
