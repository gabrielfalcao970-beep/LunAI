#!/bin/bash
# Start LunAI - Quick launch script

echo "🌙 LunAI - Starting..."
echo ""

# Get script directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

# Activate virtual environment if it exists
if [ -d "venv" ]; then
    source venv/bin/activate
else
    echo "⚠️  Virtual environment not found."
    echo "Please run: bash install.sh"
    exit 1
fi

# Launch application
python3 main.py
