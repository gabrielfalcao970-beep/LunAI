#!/bin/bash
# Build script for LunAI on Linux
# This script creates a standalone executable for Linux Mint

echo "========================================"
echo "LunAI - Build Script for Linux"
echo "========================================"

# Check Python version
PYTHON_CMD="python3"
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is not installed"
    echo "Please install Python 3.8 or higher"
    exit 1
fi

echo "✓ Python 3 found"

# Create virtual environment
echo ""
echo "Creating virtual environment..."
$PYTHON_CMD -m venv venv
source venv/bin/activate

echo "✓ Virtual environment created"

# Upgrade pip
echo ""
echo "Upgrading pip..."
pip install --upgrade pip setuptools wheel -q

echo "✓ Pip upgraded"

# Install requirements
echo ""
echo "Installing requirements..."
pip install -r requirements.txt -q

echo "✓ Requirements installed"

# Build executable with PyInstaller
echo ""
echo "Building executable with PyInstaller..."
pyinstaller --onefile \
    --windowed \
    --name LunAI \
    --add-data "assets:assets" \
    --add-data "lunai:lunai" \
    --add-data "data:data" \
    --hidden-import=PyQt5 \
    --hidden-import=textblob \
    main.py

if [ $? -eq 0 ]; then
    echo "✓ Executable built successfully!"
    echo ""
    echo "Your executable is located at: dist/LunAI"
    echo ""
    echo "To run LunAI:"
    echo "  ./dist/LunAI"
    echo ""
    echo "To install system-wide:"
    echo "  bash install_linux.sh"
    echo ""
else
    echo "✗ Build failed"
    exit 1
fi
