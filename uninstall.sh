#!/bin/bash
# Uninstall LunAI

echo "Removing LunAI..."

# Remove desktop entry
rm -f ~/.local/share/applications/lunai.desktop

# Remove virtual environment
rm -rf venv

# Optional: remove data
read -p "Remove chat history and logs? (y/n) " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    rm -rf data
fi

echo "✓ LunAI uninstalled"
