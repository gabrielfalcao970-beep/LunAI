"""LunAI - Personal AI Assistant"""

__version__ = "1.0.0"
__author__ = "Gabriel Falcão"
__email__ = "gabrielfalcao970@example.com"

from .core.chatbot import Chatbot
from .core.sentiment import SentimentAnalyzer

__all__ = ["Chatbot", "SentimentAnalyzer"]
