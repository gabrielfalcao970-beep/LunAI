#!/bin/bash
# LunAI Quick Installer for Linux Mint
# One-click installation and setup

set -e

echo "================================="
echo "🌙 LunAI Quick Installer"
echo "================================="
echo ""

# Colors
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Step 1: Check dependencies
echo -e "${YELLOW}[1/5]${NC} Checking dependencies..."

if ! command -v python3 &> /dev/null; then
    echo -e "${RED}Error: Python 3 is not installed${NC}"
    exit 1
fi

echo -e "${GREEN}✓ Python 3 found${NC}"

# Step 2: Setup directory
echo -e "${YELLOW}[2/5]${NC} Setting up directories..."

LUNAI_DIR="$HOME/.local/opt/LunAI"
DESKTOP_DIR="$HOME/.local/share/applications"

mkdir -p "$LUNAI_DIR"
mkdir -p "$DESKTOP_DIR"
mkdir -p "$LUNAI_DIR/data/chat_history"
mkdir -p "$LUNAI_DIR/data/logs"

echo -e "${GREEN}✓ Directories created${NC}"

# Step 3: Setup virtual environment
echo -e "${YELLOW}[3/5]${NC} Setting up Python environment..."

cd "$(dirname "$0")"

if [ ! -d "venv" ]; then
    python3 -m venv venv
    echo -e "${GREEN}✓ Virtual environment created${NC}"
else
    echo -e "${GREEN}✓ Virtual environment already exists${NC}"
fi

source venv/bin/activate

echo -e "${YELLOW}[4/5]${NC} Installing dependencies..."
pip install -q --upgrade pip
pip install -q -r requirements.txt

echo -e "${GREEN}✓ Dependencies installed${NC}"

# Step 4: Copy config
echo -e "${YELLOW}[5/5]${NC} Creating configuration..."

if [ ! -f "config.py" ]; then
    cp config.example.py config.py 2>/dev/null || true
    echo -e "${GREEN}✓ Configuration created${NC}"
else
    echo -e "${GREEN}✓ Configuration already exists${NC}"
fi

# Step 5: Create desktop entry
echo ""
echo "Creating desktop shortcut..."

# Get full path of start.sh
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

cat > "$DESKTOP_DIR/lunai.desktop" << EOF
[Desktop Entry]
Version=1.0
Type=Application
Name=LunAI
Comment=Personal AI Assistant
Exec=/bin/bash -c 'cd "$SCRIPT_DIR" && source venv/bin/activate && python3 main.py'
Icon=application-brain
Terminal=false
Categories=Utility;Development;
Keywords=AI;Assistant;Chat;
EOF

chmod +x "$DESKTOP_DIR/lunai.desktop"

echo -e "${GREEN}✓ Desktop entry created${NC}"

# Completion message
echo ""
echo "================================="
echo -e "${GREEN}✅ Installation Complete!${NC}"
echo "================================="
echo ""
echo "You can now launch LunAI by:"
echo -e "${GREEN}1. Click the LunAI icon in your Application Menu${NC}"
echo -e "${GREEN}2. Or run: bash start.sh${NC}"
echo ""
echo "Enjoy your AI Assistant! 🌙"
echo ""
