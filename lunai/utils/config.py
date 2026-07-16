# -*- coding: utf-8 -*-
"""Configuration manager for LunAI"""

import os
from pathlib import Path
import logging


class Config:
    """Configuration handler."""
    
    def __init__(self):
        """Initialize configuration from config.py"""
        self._load_config()
    
    def _load_config(self):
        """Load configuration from config.py file."""
        config_file = Path("config.py")
        
        if not config_file.exists():
            # Use defaults if config.py doesn't exist
            self._set_defaults()
        else:
            try:
                import importlib.util
                spec = importlib.util.spec_from_file_location("config", config_file)
                config_module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(config_module)
                
                # Load all uppercase attributes as config
                for key in dir(config_module):
                    if key.isupper():
                        setattr(self, key, getattr(config_module, key))
                        
            except Exception as e:
                print(f"Error loading config.py: {e}")
                self._set_defaults()
    
    def _set_defaults(self):
        """Set default configuration values."""
        # API Configuration
        self.OPENAI_API_KEY = ""
        self.GEMINI_API_KEY = ""
        self.USE_OFFLINE_MODE = True
        self.PREFERRED_API = "offline"
        self.TEMPERATURE = 0.7
        self.MAX_TOKENS = 500
        
        # GUI Configuration
        self.THEME = "dark"
        self.WINDOW_WIDTH = 500
        self.WINDOW_HEIGHT = 600
        self.ALWAYS_ON_TOP = True
        self.START_MINIMIZED = False
        
        # Personalization
        self.AI_NAME = "LunAI"
        self.PERSONALITY = "helpful"
        
        # Data & Storage
        self.CHAT_HISTORY_PATH = "data/chat_history/"
        self.LOGS_PATH = "data/logs/"
        self.AUTO_SAVE_HISTORY = True
        self.HISTORY_SIZE_LIMIT = 100
        
        # Sentiment Analysis
        self.ENABLE_SENTIMENT_ANALYSIS = True
        self.SENTIMENT_THRESHOLD = 0.5
        
        # Logging
        self.LOG_LEVEL = "INFO"
        self.SAVE_LOGS_TO_FILE = True
        self.MAX_CONSOLE_LINES = 100
        
        # Memory
        self.CONVERSATION_MEMORY = 10
        self.CONTINUOUS_LEARNING = False
        
        # Advanced
        self.DEBUG = False
        self.CHECK_FOR_UPDATES = True
