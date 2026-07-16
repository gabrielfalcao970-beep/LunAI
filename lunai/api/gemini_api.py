# -*- coding: utf-8 -*-
"""Google Gemini API integration"""

import logging
from typing import Optional


class GeminiAPI:
    """Google Gemini API handler."""
    
    def __init__(self, api_key: str, config):
        """Initialize Gemini API.
        
        Args:
            api_key: Gemini API key
            config: Configuration object
        """
        self.api_key = api_key
        self.config = config
        self.logger = logging.getLogger("LunAI.Gemini")
        
        try:
            import google.generativeai as genai
            genai.configure(api_key=api_key)
            self.genai = genai
            self.model = genai.GenerativeModel('gemini-pro')
            self.logger.info("Gemini API initialized")
        except ImportError:
            self.logger.warning("Google Generative AI library not installed")
            self.genai = None
    
    def get_response(self, message: str, context: list = None) -> Optional[str]:
        """Get response from Gemini.
        
        Args:
            message: User message
            context: Previous messages context
            
        Returns:
            AI response or None if failed
        """
        if not self.genai or not self.api_key:
            return None
        
        try:
            # Start chat session
            chat = self.model.start_chat(
                history=context or []
            )
            
            # Send message
            response = chat.send_message(
                message,
                generation_config={
                    "temperature": self.config.TEMPERATURE,
                    "max_output_tokens": self.config.MAX_TOKENS
                }
            )
            
            return response.text
            
        except Exception as e:
            self.logger.error(f"Gemini API error: {e}")
            return None
