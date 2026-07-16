#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
LunAI CLI
Command-line interface for LunAI
"""

import argparse
import sys
from pathlib import Path

def main():
    """
    Main CLI entry point.
    """
    parser = argparse.ArgumentParser(
        description="LunAI - Personal AI Assistant"
    )
    
    parser.add_argument(
        '--version',
        action='version',
        version='LunAI 1.0.0'
    )
    
    parser.add_argument(
        '--gui',
        action='store_true',
        help='Launch GUI (default)'
    )
    
    parser.add_argument(
        '--chat',
        action='store_true',
        help='Launch interactive chat'
    )
    
    args = parser.parse_args()
    
    if args.chat:
        run_cli_chat()
    else:
        # Default: launch GUI
        from PyQt5.QtWidgets import QApplication
        from lunai.gui.window import MainWindow
        from lunai.utils.config import Config
        
        config = Config()
        app = QApplication(sys.argv)
        window = MainWindow(config)
        window.show()
        sys.exit(app.exec_())

def run_cli_chat():
    """
    Run interactive CLI chat.
    """
    from lunai.utils.config import Config
    from lunai.core.chatbot import Chatbot
    from lunai.core.sentiment import SentimentAnalyzer
    
    config = Config()
    sentiment_analyzer = SentimentAnalyzer()
    chatbot = Chatbot(config, sentiment_analyzer)
    
    print("\n🌙 LunAI - Personal AI Assistant")
    print("Type 'quit' to exit\n")
    
    while True:
        try:
            user_input = input("You: ").strip()
            if user_input.lower() in ['quit', 'exit', 'q']:
                print("\nGoodbye! 🌙")
                break
            if not user_input:
                continue
            
            response, sentiment = chatbot.process_message(user_input)
            print(f"LunAI: {response}\n")
        except KeyboardInterrupt:
            print("\n\nGoodbye! 🌙")
            break
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
