#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
LunAI Conversation Memory
Manages chat history and persistence
"""

import json
from pathlib import Path
from datetime import datetime

class Memory:
    """
    Manages conversation history and memory.
    Saves and loads chat history from disk.
    """
    
    def __init__(self):
        """Initialize memory manager"""
        self.history_dir = Path("data/chat_history")
        self.history_dir.mkdir(parents=True, exist_ok=True)
        self.current_session = []
    
    def add_message(self, author: str, content: str, sentiment: str = "neutral"):
        """
        Add message to current session.
        """
        message = {
            "timestamp": datetime.now().isoformat(),
            "author": author,
            "content": content,
            "sentiment": sentiment
        }
        self.current_session.append(message)
    
    def save_session(self, name: str = None) -> str:
        """
        Save current session to file.
        Returns: filename of saved session
        """
        if not self.current_session:
            return None
        
        if name is None:
            name = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        
        filename = self.history_dir / f"{name}.json"
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(self.current_session, f, ensure_ascii=False, indent=2)
        
        return str(filename)
    
    def load_session(self, filename: str) -> list:
        """
        Load session from file.
        """
        filepath = self.history_dir / f"{filename}.json"
        
        if not filepath.exists():
            return []
        
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    
    def get_history(self) -> list:
        """
        Get current session history.
        """
        return self.current_session
    
    def clear_session(self):
        """
        Clear current session.
        """
        self.current_session = []
    
    def get_last_sessions(self, limit: int = 10) -> list:
        """
        Get list of recent sessions.
        """
        files = sorted(self.history_dir.glob("*.json"), reverse=True)[:limit]
        return [f.stem for f in files]
