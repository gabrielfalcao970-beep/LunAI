# -*- coding: utf-8 -*-
"""Conversational memory module"""

import logging
from typing import List, Dict
from collections import deque


class ConversationMemory:
    """Manages conversation history and context."""
    
    def __init__(self, config):
        """Initialize memory.
        
        Args:
            config: Configuration object
        """
        self.config = config
        self.logger = logging.getLogger("LunAI.Memory")
        self.memory = deque(maxlen=config.CONVERSATION_MEMORY)
    
    def add_message(self, role: str, content: str, emotion: str = None):
        """Add message to memory.
        
        Args:
            role: 'user' or 'assistant'
            content: Message content
            emotion: Detected emotion (optional)
        """
        message = {
            "role": role,
            "content": content,
            "emotion": emotion
        }
        self.memory.append(message)
        self.logger.debug(f"Added to memory: {role} - {content[:50]}...")
    
    def get_context(self) -> List[Dict]:
        """Get current memory context.
        
        Returns:
            List of recent messages
        """
        return list(self.memory)
    
    def clear(self):
        """Clear memory."""
        self.memory.clear()
        self.logger.info("Memory cleared")
    
    def get_last_emotion(self) -> str:
        """Get last detected emotion.
        
        Returns:
            Last emotion or 'neutral'
        """
        for message in reversed(self.memory):
            if message.get("emotion"):
                return message["emotion"]
        return "neutral"
