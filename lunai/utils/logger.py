# -*- coding: utf-8 -*-
"""Logger configuration for LunAI"""

import logging
import os
from pathlib import Path
from datetime import datetime


def setup_logging(log_level=logging.INFO):
    """Setup logging configuration."""
    
    # Create logs directory if it doesn't exist
    log_dir = Path("data/logs")
    log_dir.mkdir(parents=True, exist_ok=True)
    
    # Create log filename with timestamp
    log_filename = log_dir / f"lunai_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
    
    # Configure logging
    logging.basicConfig(
        level=log_level,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_filename),
            logging.StreamHandler()
        ]
    )
    
    logger = logging.getLogger("LunAI")
    logger.info("Logging initialized")
    
    return logger
