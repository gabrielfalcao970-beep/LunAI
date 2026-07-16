# -*- coding: utf-8 -*-
"""Sentiment analysis module"""

import logging
from typing import Optional


class SentimentAnalyzer:
    """Sentiment analysis using TextBlob."""
    
    def __init__(self, config):
        """Initialize sentiment analyzer.
        
        Args:
            config: Configuration object
        """
        self.config = config
        self.logger = logging.getLogger("LunAI.Sentiment")
        
        try:
            from textblob import TextBlob
            self.textblob = TextBlob
            self.logger.info("TextBlob sentiment analyzer initialized")
        except ImportError:
            self.logger.warning("TextBlob not available, using fallback")
            self.textblob = None
    
    def analyze(self, text: str) -> str:
        """Analyze sentiment of text.
        
        Args:
            text: Text to analyze
            
        Returns:
            Emotion label: 'happy', 'sad', 'angry', 'neutral', 'worried', 'surprised', 'confused'
        """
        if not self.config.ENABLE_SENTIMENT_ANALYSIS:
            return "neutral"
        
        if self.textblob:
            return self._analyze_with_textblob(text)
        else:
            return self._analyze_with_keywords(text)
    
    def _analyze_with_textblob(self, text: str) -> str:
        """Analyze using TextBlob.
        
        Args:
            text: Text to analyze
            
        Returns:
            Emotion label
        """
        try:
            blob = self.textblob(text)
            polarity = blob.sentiment.polarity
            subjectivity = blob.sentiment.subjectivity
            
            # Determine emotion based on polarity and subjectivity
            if polarity > 0.5:
                return "happy"
            elif polarity < -0.5:
                if subjectivity > 0.5:
                    return "angry"
                else:
                    return "sad"
            elif -0.3 <= polarity <= 0.3 and subjectivity > 0.6:
                return "confused"
            else:
                return "neutral"
        except Exception as e:
            self.logger.error(f"TextBlob analysis error: {e}")
            return "neutral"
    
    def _analyze_with_keywords(self, text: str) -> str:
        """Fallback keyword-based sentiment analysis.
        
        Args:
            text: Text to analyze
            
        Returns:
            Emotion label
        """
        text_lower = text.lower()
        
        happy_words = ['feliz', 'alegre', 'ótimo', 'maravilhoso', 'excelente', 'adorei', 'amei', 'legal', 'incrível']
        sad_words = ['triste', 'infeliz', 'chato', 'ruim', 'horrível', 'péssimo', 'terrível', 'desisti']
        angry_words = ['raiva', 'irritado', 'furioso', 'enfurecido', 'brava', 'não aguento', 'estou bravo', 'enojado']
        worried_words = ['preocupado', 'ansioso', 'tenso', 'nervoso', 'assustado', 'medo', 'receio', 'apreensivo']
        surprised_words = ['surpreendido', 'espantado', 'chocado', 'wow', 'caramba', 'nossa', 'impressionado']
        confused_words = ['confuso', 'confundido', 'perdido', 'não entendo', 'não sei', 'como assim', 'eh?']
        
        if any(word in text_lower for word in happy_words):
            return "happy"
        elif any(word in text_lower for word in sad_words):
            return "sad"
        elif any(word in text_lower for word in angry_words):
            return "angry"
        elif any(word in text_lower for word in worried_words):
            return "worried"
        elif any(word in text_lower for word in surprised_words):
            return "surprised"
        elif any(word in text_lower for word in confused_words):
            return "confused"
        
        return "neutral"
