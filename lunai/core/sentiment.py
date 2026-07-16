#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
LunAI Sentiment Analysis
Analyzes user emotions from text
"""

from textblob import TextBlob

class SentimentAnalyzer:
    """
    Analyzes sentiment of user messages.
    Uses TextBlob for Portuguese language support.
    """
    
    def __init__(self):
        """Initialize sentiment analyzer"""
        self.sentiment_map = {}
    
    def analyze(self, text: str) -> str:
        """
        Analyze sentiment of text.
        Returns: 'happy', 'sad', 'angry', 'confused', or 'neutral'
        """
        try:
            blob = TextBlob(text)
            polarity = blob.sentiment.polarity
            
            # Map polarity to sentiment
            if polarity > 0.5:
                return "happy"
            elif polarity > 0.1:
                return "content"
            elif polarity < -0.5:
                return "sad"
            elif polarity < -0.1:
                return "worried"
            else:
                # Check for confusion indicators
                if any(word in text.lower() for word in ["que", "como", "por quê", "o que", "qual"]):
                    return "confused"
                return "neutral"
        except Exception as e:
            print(f"Sentiment analysis error: {e}")
            return "neutral"
    
    def get_avatar_from_sentiment(self, sentiment: str) -> str:
        """
        Get avatar filename based on sentiment.
        """
        sentiment_to_avatar = {
            "happy": "happy.png",
            "content": "calm.png",
            "sad": "sad.png",
            "worried": "worried.png",
            "angry": "angry.png",
            "confused": "confused.png",
            "neutral": "neutral.png",
        }
        return sentiment_to_avatar.get(sentiment, "neutral.png")
