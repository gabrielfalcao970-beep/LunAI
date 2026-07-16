# -*- coding: utf-8 -*-
"""OpenAI API integration"""

import logging
from typing import Optional


class OpenAIAPI:
    """OpenAI API handler."""
    
    def __init__(self, api_key: str, config):
        """Initialize OpenAI API.
        
        Args:
            api_key: OpenAI API key
            config: Configuration object
        """
        self.api_key = api_key
        self.config = config
        self.logger = logging.getLogger("LunAI.OpenAI")
        
        try:
            import openai
            openai.api_key = api_key
            self.openai = openai
            self.logger.info("OpenAI API initialized")
        except ImportError:
            self.logger.warning("OpenAI library not installed")
            self.openai = None
    
    def get_response(self, message: str, context: list = None) -> Optional[str]:
        """Get response from OpenAI.
        
        Args:
            message: User message
            context: Previous messages context
            
        Returns:
            AI response or None if failed
        """
        if not self.openai or not self.api_key:
            return None
        
        try:
            # Prepare messages
            messages = []
            if context:
                messages.extend(context)
            messages.append({"role": "user", "content": message})
            
            # Call API
            response = self.openai.ChatCompletion.create(
                model=self.config.OPENAI_MODEL,
                messages=messages,
                temperature=self.config.TEMPERATURE,
                max_tokens=self.config.MAX_TOKENS
            )
            
            return response.choices[0].message.content
            
        except Exception as e:
            self.logger.error(f"OpenAI API error: {e}")
            return None
