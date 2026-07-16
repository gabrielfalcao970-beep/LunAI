#!/bin/bash
# Quick start script for LunAI on Linux
# Run with: bash start.sh

echo "LunAI - Starting..."
echo ""

# Check if venv exists
if [ ! -d "venv" ]; then
    echo "Virtual environment not found. Creating..."
    python3 -m venv venv
    source venv/bin/activate
    echo "Installing dependencies..."
    pip install -q -r requirements.txt
    echo "✓ Setup complete!"
else
    source venv/bin/activate
fi

echo "Launching LunAI..."
python3 main.py
