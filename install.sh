#!/bin/bash
# LunAI - The easy 2-click installer for Linux Mint

set -e

echo ""
echo "╔════════════════════════════════════╗"
echo "║  🌙 LunAI - AI Assistant Setup    ║"
echo "║     For Linux Mint & Ubuntu        ║"
echo "╚════════════════════════════════════╝"
echo ""

# Colors for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
RED='\033[0;31m'
NC='\033[0m'

echo -e "${BLUE}Step 1:${NC} Checking system requirements..."

# Check Python
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}✗ Python 3 not found!${NC}"
    echo "Please install: sudo apt install python3 python3-pip python3-venv"
    exit 1
fi

echo -e "${GREEN}✓ Python 3 found${NC}"

echo ""
echo -e "${BLUE}Step 2:${NC} Setting up project..."

# Make scripts executable
chmod +x *.sh 2>/dev/null || true

echo -e "${GREEN}✓ Scripts prepared${NC}"

echo ""
echo -e "${BLUE}Step 3:${NC} Creating Python environment..."

# Create venv
if [ ! -d "venv" ]; then
    python3 -m venv venv
    echo -e "${GREEN}✓ Virtual environment created${NC}"
else
    echo -e "${GREEN}✓ Virtual environment already exists${NC}"
fi

# Activate venv
source venv/bin/activate

echo ""
echo -e "${BLUE}Step 4:${NC} Installing dependencies..."

pip install -q --upgrade pip setuptools wheel
pip install -q -r requirements.txt

echo -e "${GREEN}✓ Dependencies installed${NC}"

echo ""
echo -e "${BLUE}Step 5:${NC} Creating configuration..."

if [ ! -f "config.py" ]; then
    cp config.example.py config.py
    echo -e "${GREEN}✓ Configuration file created${NC}"
else
    echo -e "${GREEN}✓ Configuration already exists${NC}"
fi

echo ""
echo -e "${BLUE}Step 6:${NC} Generating avatars..."

if [ ! -d "assets/avatars" ] || [ -z "$(ls -A assets/avatars 2>/dev/null)" ]; then
    python3 create_avatars.py
else
    echo -e "${GREEN}✓ Avatars already exist${NC}"
fi

echo ""
echo -e "${BLUE}Step 7:${NC} Creating desktop shortcut..."

# Get absolute path of script directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Create .local/share/applications directory
DESKTOP_DIR="$HOME/.local/share/applications"
mkdir -p "$DESKTOP_DIR"

# Create .desktop file
cat > "$DESKTOP_DIR/lunai.desktop" << EOF
[Desktop Entry]
Version=1.0
Type=Application
Name=LunAI
Comment=🌙 Personal AI Assistant
Exec=bash -c 'cd "$SCRIPT_DIR" && bash start.sh'
Icon=application-brain
Terminal=false
Categories=Utility;Development;Application;
Keywords=AI;Assistant;Chat;Chatbot;LunAI;
X-GNOME-Autostart-enabled=false
EOF

chmod +x "$DESKTOP_DIR/lunai.desktop"

echo -e "${GREEN}✓ Desktop shortcut created${NC}"

echo ""
echo "╔════════════════════════════════════╗"
echo -e "║${GREEN}  ✅ Setup Complete!              ${NC}║"
echo "╚════════════════════════════════════╝"
echo ""
echo "🚀 How to launch LunAI:"
echo ""
echo -e "${YELLOW}Option 1:${NC} Click the ${BLUE}LunAI${NC} icon in your application menu"
echo -e "${YELLOW}Option 2:${NC} Run from terminal:"
echo -e "          ${BLUE}bash start.sh${NC}"
echo ""
echo "📝 Configuration: Edit ${BLUE}config.py${NC} to customize"
echo ""
echo "💡 Tips:"
echo "  • Set USE_OFFLINE_MODE = True (default) for no API needed"
echo "  • Add OPENAI_API_KEY or GEMINI_API_KEY for better responses"
echo "  • Change THEME to 'light' for light mode"
echo ""
echo "🌙 Enjoy your new AI Assistant!"
echo ""
