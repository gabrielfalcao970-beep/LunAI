#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
LunAI Chatbot Core
Handles AI responses and conversations
"""

import random
from typing import Tuple

class Chatbot:
    """
    Simple chatbot with basic NLP responses.
    Can be extended with API integrations.
    """
    
    def __init__(self, config, sentiment_analyzer=None):
        """Initialize chatbot"""
        self.config = config
        self.sentiment_analyzer = sentiment_analyzer
        self.conversation_history = []
        
        # Response templates
        self.greetings = [
            "Olá! Como você está?",
            "Oi! Bem vindo! Como posso ajudar?",
            "E aí! Tudo certo com você?",
        ]
        
        self.happy_responses = [
            "Que legal! Fico feliz em ouvir isso! 😊",
            "Que bom! Sua felicidade é contagiante! 🌟",
            "Eba! Vejo que você está de bom humor! ✨",
        ]
        
        self.sad_responses = [
            "Entendo... Quer conversar sobre isso? Estou aqui para ouvir. 💙",
            "Lamento ouvir que você está triste. Como posso ajudar?",
            "Não fique triste! Posso tentar melhorar seu dia. 🌙",
        ]
        
        self.confused_responses = [
            "Hmm, deixe-me pensar sobre isso...",
            "Ótima pergunta! Deixa eu considerar isso.",
            "Entendi, vou analisar melhor.",
        ]
        
        self.default_responses = [
            "Isso é interessante! Fale mais sobre isso.",
            "Entendo! Como você se sente a respeito disso?",
            "Legal! E o que mais você gostaria de saber?",
            "Que interessante! Me conte mais.",
        ]
    
    def process_message(self, user_input: str) -> Tuple[str, str]:
        """
        Process user message and generate response.
        Returns: (response, sentiment)
        """
        # Add to history
        self.conversation_history.append(user_input)
        
        # Get sentiment if analyzer available
        sentiment = "neutral"
        if self.sentiment_analyzer:
            sentiment = self.sentiment_analyzer.analyze(user_input)
        
        # Generate response
        response = self._generate_response(user_input, sentiment)
        
        return response, sentiment
    
    def _generate_response(self, user_input: str, sentiment: str) -> str:
        """
        Generate response based on user input and sentiment.
        """
        user_input_lower = user_input.lower()
        
        # Check for greetings
        if any(word in user_input_lower for word in ["olá", "oi", "opa", "e aí", "hello", "hi"]):
            return random.choice(self.greetings)
        
        # Check sentiment
        if sentiment == "happy":
            return random.choice(self.happy_responses)
        elif sentiment == "sad":
            return random.choice(self.sad_responses)
        elif sentiment == "confused":
            return random.choice(self.confused_responses)
        
        # Default response
        return random.choice(self.default_responses)
    
    def get_history(self) -> list:
        """Get conversation history"""
        return self.conversation_history
    
    def clear_history(self):
        """Clear conversation history"""
        self.conversation_history = []
