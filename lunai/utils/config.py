#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
LunAI Configuration Manager
"""

import sys
from pathlib import Path

class Config:
    """
    Configuration manager for LunAI.
    Loads settings from config.py
    """
    
    def __init__(self):
        """Initialize configuration from config.py"""
        try:
            # Try to import config
            import config as config_module
            
            # Load all config attributes
            for attr in dir(config_module):
                if attr.isupper():
                    setattr(self, attr, getattr(config_module, attr))
        except ImportError:
            print("Error: config.py not found!")
            print("Please copy config.example.py to config.py")
            sys.exit(1)
        except Exception as e:
            print(f"Error loading config: {e}")
            sys.exit(1)
    
    def __repr__(self):
        """String representation of config"""
        attrs = []
        for attr in dir(self):
            if attr.isupper():
                attrs.append(f"{attr}={getattr(self, attr)}")
        return f"Config({', '.join(attrs)})"
