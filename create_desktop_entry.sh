#!/bin/bash
# Create desktop entry for LunAI

echo "Creating desktop entry for LunAI..."

DESKTOP_DIR="$HOME/.local/share/applications"
mkdir -p "$DESKTOP_DIR"

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

cat > "$DESKTOP_DIR/lunai.desktop" << EOF
[Desktop Entry]
Version=1.0
Type=Application
Name=LunAI
Comment=Personal AI Assistant
Exec=bash -c 'cd "$SCRIPT_DIR" && bash start.sh'
Icon=application-brain
Terminal=false
Categories=Utility;Development;
EOF

chmod +x "$DESKTOP_DIR/lunai.desktop"

echo "✓ Desktop entry created at $DESKTOP_DIR/lunai.desktop"
