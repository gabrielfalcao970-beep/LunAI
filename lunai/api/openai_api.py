#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
LunAI OpenAI API Integration
Integration with OpenAI GPT
"""

import openai

class OpenAIAPI:
    """
    OpenAI API integration for LunAI.
    """
    
    def __init__(self, api_key: str):
        """Initialize OpenAI API"""
        openai.api_key = api_key
        self.model = "gpt-3.5-turbo"
    
    def generate_response(self, prompt: str, conversation_history: list = None) -> str:
        """
        Generate response using OpenAI API.
        """
        try:
            messages = [
                {"role": "system", "content": "Você é LunAI, um assistente pessoal de IA amigável e empático. Responda sempre em português."},
            ]
            
            if conversation_history:
                for msg in conversation_history[-5:]:
                    messages.append({
                        "role": msg.get("author", "user"),
                        "content": msg.get("content", "")
                    })
            
            messages.append({"role": "user", "content": prompt})
            
            response = openai.ChatCompletion.create(
                model=self.model,
                messages=messages,
                temperature=0.7,
                max_tokens=150
            )
            
            return response.choices[0].message.content
        except Exception as e:
            return f"Desculpe, ocorreu um erro: {str(e)}"
