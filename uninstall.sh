#!/bin/bash
# Uninstall script for LunAI

echo "LunAI - Uninstall Script"
echo ""

INSTALL_DIR="$HOME/.local/bin"
DESKTOP_DIR="$HOME/.local/share/applications"

if [ -f "$INSTALL_DIR/LunAI" ]; then
    echo "Removing LunAI from $INSTALL_DIR..."
    rm -f "$INSTALL_DIR/LunAI"
    rm -f "$INSTALL_DIR/lunai"
    echo "✓ Executable removed"
fi

if [ -f "$DESKTOP_DIR/lunai.desktop" ]; then
    echo "Removing desktop entry..."
    rm -f "$DESKTOP_DIR/lunai.desktop"
    echo "✓ Desktop entry removed"
fi

echo ""
echo "LunAI has been uninstalled."
