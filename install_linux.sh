#!/bin/bash
# Installer script for LunAI on Linux Mint
# Run with: bash install_linux.sh

echo "========================================"
echo "LunAI - Installer for Linux Mint"
echo "========================================"
echo ""

# Check if running as root (optional, for system-wide installation)
if [ "$EUID" -ne 0 ]; then 
    echo "Installing to user home directory (~/.local/bin)"
    INSTALL_DIR="$HOME/.local/bin"
    ICON_DIR="$HOME/.local/share/icons"
    DESKTOP_DIR="$HOME/.local/share/applications"
else
    echo "Installing system-wide to /opt"
    INSTALL_DIR="/opt/LunAI"
    ICON_DIR="/usr/share/icons"
    DESKTOP_DIR="/usr/share/applications"
fi

echo ""
echo "Installation directory: $INSTALL_DIR"
echo ""

# Check if executable exists
if [ ! -f "dist/LunAI" ]; then
    echo "Error: dist/LunAI not found"
    echo "Please run build_linux.sh first"
    exit 1
fi

echo "Installing LunAI..."

# Create installation directory
mkdir -p "$INSTALL_DIR"

# Copy executable
cp dist/LunAI "$INSTALL_DIR/LunAI"
chmod +x "$INSTALL_DIR/LunAI"
echo "✓ Executable installed"

# Copy assets if not included
if [ -d "assets" ]; then
    mkdir -p "$INSTALL_DIR/assets"
    cp -r assets/* "$INSTALL_DIR/assets/" 2>/dev/null || true
    echo "✓ Assets installed"
fi

# Create desktop entry for application menu
echo ""
echo "Creating desktop entry..."

mkdir -p "$DESKTOP_DIR"

cat > "$DESKTOP_DIR/lunai.desktop" << EOF
[Desktop Entry]
Version=1.0
Type=Application
Name=LunAI
Comment=Personal AI Assistant
Exec=$INSTALL_DIR/LunAI
Icon=lunai
Terminal=false
Categories=Utility;Application;
Keywords=ai;assistant;chatbot;
EOF

echo "✓ Desktop entry created"

# Create launcher script for easy access
echo ""
echo "Creating launcher script..."

cat > "$INSTALL_DIR/lunai" << 'EOF'
#!/bin/bash
cd "$(dirname "$0")"
./LunAI "$@"
EOF

chmod +x "$INSTALL_DIR/lunai"
echo "✓ Launcher created"

# Add to PATH if user installation
if [ "$EUID" -ne 0 ]; then
    if [ -w "$HOME/.bashrc" ]; then
        if ! grep -q "$INSTALL_DIR" "$HOME/.bashrc"; then
            echo "" >> "$HOME/.bashrc"
            echo "# LunAI" >> "$HOME/.bashrc"
            echo "export PATH=\"$INSTALL_DIR:\$PATH\"" >> "$HOME/.bashrc"
            echo "✓ Added LunAI to PATH"
        fi
    fi
fi

echo ""
echo "========================================"
echo "Installation Complete!"
echo "========================================"
echo ""
echo "You can now run LunAI with:"
echo "  lunai"
echo ""
echo "Or find it in your application menu as 'LunAI'"
echo ""
echo "To update your PATH, run:"
echo "  source ~/.bashrc"
echo ""
