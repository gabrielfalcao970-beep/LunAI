#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
LunAI - Personal AI Assistant
Main entry point for the application
"""

import sys
import os
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

# Import Qt
try:
    from PyQt5.QtWidgets import QApplication
except ImportError:
    print("Error: PyQt5 is not installed.")
    print("Please install it with: pip install -r requirements.txt")
    sys.exit(1)

from lunai.utils.logger import setup_logging
from lunai.gui.window import MainWindow
from lunai.utils.config import Config


def setup_directories():
    """Create necessary directories if they don't exist."""
    dirs = [
        "data/chat_history",
        "data/logs",
        "assets/avatars",
    ]
    for directory in dirs:
        Path(directory).mkdir(parents=True, exist_ok=True)


def main():
    """Main application entry point."""
    # Setup logging
    logger = setup_logging()
    
    # Create directories
    setup_directories()
    
    # Load configuration
    config = Config()
    logger.info("LunAI starting...")
    logger.info(f"Configuration loaded from config.py")
    logger.info(f"Mode: {'Offline' if config.USE_OFFLINE_MODE else 'Online with API'}")
    
    # Create Qt Application
    app = QApplication(sys.argv)
    app.setApplicationName("LunAI")
    app.setApplicationVersion("1.0.0")
    
    # Create and show main window
    window = MainWindow(config)
    window.show()
    
    logger.info("GUI initialized successfully")
    logger.info("LunAI is ready!")
    
    # Start event loop
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
