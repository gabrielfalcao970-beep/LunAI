#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
LunAI Google Gemini API Integration
Integration with Google Generative AI
"""

import google.generativeai as genai

class GeminiAPI:
    """
    Google Gemini API integration for LunAI.
    """
    
    def __init__(self, api_key: str):
        """Initialize Gemini API"""
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-pro')
    
    def generate_response(self, prompt: str, conversation_history: list = None) -> str:
        """
        Generate response using Gemini API.
        """
        try:
            system_prompt = "Você é LunAI, um assistente pessoal de IA amigável e empático. Responda sempre em português de forma concisa."
            
            full_prompt = f"{system_prompt}\n\nUsuário: {prompt}\n\nLunAI:"
            
            response = self.model.generate_content(full_prompt)
            return response.text
        except Exception as e:
            return f"Desculpe, ocorreu um erro: {str(e)}"
