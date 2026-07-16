#!/bin/bash
# Desktop entry creator for LunAI
# Creates a .desktop file for easy application menu integration

DESKTOP_FILE="$HOME/.local/share/applications/lunai.desktop"

echo "Creating desktop entry for LunAI..."
mkdir -p "$HOME/.local/share/applications"

cat > "$DESKTOP_FILE" << 'EOF'
[Desktop Entry]
Version=1.0
Type=Application
Name=LunAI
Comment=Personal AI Assistant
Exec=python3 -m lunai.cli
Icon=lunai
Terminal=false
Categories=Utility;Application;
StartupNotify=true
X-KDE-RunInTerminal=false
EOF

echo "✓ Desktop entry created at: $DESKTOP_FILE"
echo ""
echo "You can now find LunAI in your application menu!"
