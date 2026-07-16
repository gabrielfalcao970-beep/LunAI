# -*- coding: utf-8 -*-
"""Chatbot core module"""

import logging
from typing import Optional, Dict, List, Tuple
from datetime import datetime
import json
from pathlib import Path


class Chatbot:
    """Main chatbot class."""
    
    def __init__(self, config, sentiment_analyzer=None):
        """Initialize chatbot.
        
        Args:
            config: Configuration object
            sentiment_analyzer: Sentiment analyzer instance
        """
        self.config = config
        self.sentiment_analyzer = sentiment_analyzer
        self.logger = logging.getLogger("LunAI.Chatbot")
        self.conversation_history: List[Dict] = []
        self.current_emotion = "neutral"
        
        # Load responses database
        self.responses = self._load_responses()
        
        self.logger.info("Chatbot initialized")
    
    def _load_responses(self) -> Dict:
        """Load response templates."""
        return {
            "greeting": [
                "Oi! Como você está hoje?",
                "Olá! Bem-vindo! Como posso ajudar?",
                "Oi! Tudo bem? Em que posso ajudar?",
            ],
            "happy": [
                "Que alegria! Me conta mais sobre isso! 😊",
                "Adorei saber que você está feliz! O que aconteceu?",
                "Que legal! Estou feliz por você!",
            ],
            "sad": [
                "Entendo que você está triste. Quer conversar sobre isso? Estou aqui para ouvir.",
                "Sinto muito que esteja se sentindo assim. Qual é o problema?",
                "Estou aqui para você. Quer me contar o que aconteceu?",
            ],
            "angry": [
                "Vejo que você está irritado. Respira fundo, podemos resolver isso juntos.",
                "Parece que algo te deixou brava. Quer falar sobre isso?",
                "Entendo sua frustração. Como posso ajudar?",
            ],
            "worried": [
                "Percebi que você está preocupada. Qual é a preocupação?",
                "Parece que algo a está perturbando. Quer conversar?",
                "Estou aqui se você quiser desabafar.",
            ],
            "confused": [
                "Parece que você está confusa. Posso clarificar algo?",
                "Não entendi bem. Pode repetir ou explicar melhor?",
                "Deixe-me ajudar a esclarecer isso.",
            ],
            "neutral": [
                "Interessante! O que mais você quer saber?",
                "Como posso te ajudar?",
                "Entendi. E então?",
            ],
            "help": [
                "Claro! Estou aqui para ajudar com qualquer coisa.",
                "Adoraria ajudar! O que você precisa?",
                "Deixe comigo! Em que posso ser útil?",
            ],
            "motivation": [
                "Você é mais forte do que pensa! Cada dia é uma nova oportunidade para crescer.",
                "Lembre-se: você já conseguiu superar desafios antes. Você consegue novamente!",
                "Acredite em si mesmo! Você tem potencial para tudo que deseja.",
            ],
        }
    
    def get_response(self, user_message: str) -> Tuple[str, str]:
        """Get AI response to user message.
        
        Args:
            user_message: User's input message
            
        Returns:
            Tuple of (response_text, emotion_detected)
        """
        # Analyze sentiment
        emotion = "neutral"
        if self.sentiment_analyzer:
            emotion = self.sentiment_analyzer.analyze(user_message)
            self.current_emotion = emotion
        
        # Store in history
        self.conversation_history.append({
            "timestamp": datetime.now().isoformat(),
            "user": user_message,
            "emotion": emotion
        })
        
        # Generate response
        response = self._generate_response(user_message, emotion)
        
        # Store response
        self.conversation_history[-1]["ai_response"] = response
        
        # Save history if enabled
        if self.config.AUTO_SAVE_HISTORY:
            self._save_history()
        
        self.logger.debug(f"User: {user_message}")
        self.logger.debug(f"Emotion: {emotion}")
        self.logger.debug(f"AI: {response}")
        
        return response, emotion
    
    def _generate_response(self, user_message: str, emotion: str) -> str:
        """Generate AI response.
        
        Args:
            user_message: User's message
            emotion: Detected emotion
            
        Returns:
            AI response text
        """
        user_lower = user_message.lower()
        
        # Check for specific keywords
        if any(word in user_lower for word in ["oi", "olá", "e aí", "opa"]):
            return self._random_response("greeting")
        
        if any(word in user_lower for word in ["ajuda", "pode", "consigo", "posso"]):
            return self._random_response("help")
        
        if any(word in user_lower for word in ["motiva", "força", "anima", "consigo"]):
            return self._random_response("motivation")
        
        # Use emotion-based responses
        if emotion in self.responses:
            return self._random_response(emotion)
        
        return "Como posso te ajudar? 😊"
    
    def _random_response(self, category: str) -> str:
        """Get random response from category."""
        import random
        if category in self.responses:
            return random.choice(self.responses[category])
        return "Como posso te ajudar?"
    
    def _save_history(self):
        """Save conversation history to file."""
        try:
            history_dir = Path(self.config.CHAT_HISTORY_PATH)
            history_dir.mkdir(parents=True, exist_ok=True)
            
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            history_file = history_dir / f"chat_{timestamp}.json"
            
            with open(history_file, 'w', encoding='utf-8') as f:
                json.dump(self.conversation_history, f, ensure_ascii=False, indent=2)
            
            self.logger.debug(f"History saved to {history_file}")
        except Exception as e:
            self.logger.error(f"Error saving history: {e}")
    
    def get_history(self) -> List[Dict]:
        """Get conversation history.
        
        Returns:
            List of conversation messages
        """
        return self.conversation_history
    
    def clear_history(self):
        """Clear conversation history."""
        self.conversation_history = []
        self.logger.info("Conversation history cleared")
    
    def get_current_emotion(self) -> str:
        """Get current detected emotion.
        
        Returns:
            Current emotion string
        """
        return self.current_emotion
