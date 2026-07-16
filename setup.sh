#!/bin/bash
# Setup script - Make scripts executable and prepare project

echo "========================================"
echo "LunAI - Setup Script"
echo "========================================"
echo ""

echo "Setting up LunAI..."
echo ""

# Make scripts executable
chmod +x build_linux.sh 2>/dev/null
chmod +x install_linux.sh 2>/dev/null
chmod +x start.sh 2>/dev/null
chmod +x create_desktop_entry.sh 2>/dev/null
chmod +x uninstall.sh 2>/dev/null
chmod +x setup.sh 2>/dev/null

echo "✓ Scripts are now executable"
echo ""
echo "========================================"
echo "LunAI Setup Complete!"
echo "========================================"
echo ""
echo "Quick Start Options:"
echo ""
echo "1. Run directly (fastest):"
echo "   bash start.sh"
echo ""
echo "2. Build standalone executable:"
echo "   bash build_linux.sh"
echo ""
echo "3. Install after building:"
echo "   bash install_linux.sh"
echo ""
echo "4. Create desktop entry:"
echo "   bash create_desktop_entry.sh"
echo ""
echo "5. Uninstall:"
echo "   bash uninstall.sh"
echo ""
echo "========================================"
echo ""
echo "Recommended first run: bash start.sh"
echo ""
