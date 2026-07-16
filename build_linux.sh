#!/bin/bash
# Build standalone executable for Linux

echo "Building LunAI executable..."

# Activate virtual environment
source venv/bin/activate

# Install PyInstaller if not present
pip install -q PyInstaller

# Create hidden imports file
cat > hidden_imports.txt << 'EOF'
hiddenimports=[
    'lunai.utils.logger',
    'lunai.utils.config',
    'lunai.core.chatbot',
    'lunai.core.sentiment',
    'lunai.core.memory',
    'lunai.gui.window',
    'lunai.gui.styles',
    'lunai.api.openai_api',
    'lunai.api.gemini_api',
]
EOF

# Build executable
pyinstaller --onefile \
    --windowed \
    --name LunAI \
    --icon=assets/lunai.ico 2>/dev/null || pyinstaller --onefile --windowed --name LunAI main.py

echo "✓ Build complete! Executable created in dist/LunAI"
