#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
LunAI Configuration
Personalize your LunAI assistant here
"""

# ============================================
# AI MODE CONFIGURATION
# ============================================
# Set to True for offline mode (no API needed)
# Set to False to use online APIs (GPT, Gemini)
USE_OFFLINE_MODE = True

# API Keys (only needed if USE_OFFLINE_MODE = False)
OPENAI_API_KEY = ""
GEMINI_API_KEY = ""

# ============================================
# INTERFACE CONFIGURATION
# ============================================
THEME = "dark"  # or "light"
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 600
WINDOW_OPACITY = 0.95  # 0.0 to 1.0

# ============================================
# AI PERSONALITY
# ============================================
AI_NAME = "LunAI"
AI_GREETING = "Olá! Como você está?"
AI_DESCRIPTION = "Seu assistente pessoal de IA 🌙"

# ============================================
# FEATURES
# ============================================
ENABLE_SENTIMENT_ANALYSIS = True
ENABLE_CHAT_HISTORY = True
ENABLE_AVATAR = True
ENABLE_TYPING_INDICATOR = True

# ============================================
# LOGGING
# ============================================
LOG_LEVEL = "INFO"  # DEBUG, INFO, WARNING, ERROR, CRITICAL
SAVE_LOGS = True
MAX_LOG_SIZE_MB = 10

# ============================================
# CHAT HISTORY
# ============================================
MAX_HISTORY_MESSAGES = 100
AUTO_SAVE_INTERVAL = 10  # seconds
