# -*- coding: utf-8 -*-
"""CLI entry point for LunAI"""

import sys
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from lunai.utils.logger import setup_logging
from lunai.gui.window import MainWindow
from lunai.utils.config import Config
from PyQt5.QtWidgets import QApplication


def main():
    """Main CLI entry point."""
    # Setup logging
    setup_logging()
    logger = setup_logging()
    
    # Create directories
    dirs = [
        "data/chat_history",
        "data/logs",
        "assets/avatars",
    ]
    for directory in dirs:
        Path(directory).mkdir(parents=True, exist_ok=True)
    
    # Load configuration
    config = Config()
    logger.info("LunAI starting via CLI...")
    
    # Create Qt Application
    app = QApplication(sys.argv)
    app.setApplicationName("LunAI")
    app.setApplicationVersion("1.0.0")
    
    # Create and show main window
    window = MainWindow(config)
    window.show()
    
    logger.info("GUI initialized successfully")
    
    # Start event loop
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
