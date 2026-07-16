#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
LunAI Main Window
PyQt5 GUI for LunAI Assistant
"""

from PyQt5.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QTextEdit, QPushButton, QLabel, QScrollArea
)
from PyQt5.QtCore import Qt, QSize, QTimer
from PyQt5.QtGui import QPixmap, QIcon, QFont
from pathlib import Path
import sys

from lunai.core.chatbot import Chatbot
from lunai.core.sentiment import SentimentAnalyzer
from lunai.core.memory import Memory
from lunai.gui.styles import get_style

class MainWindow(QMainWindow):
    """
    Main application window for LunAI.
    """
    
    def __init__(self, config):
        """Initialize main window"""
        super().__init__()
        
        self.config = config
        self.sentiment_analyzer = SentimentAnalyzer()
        self.chatbot = Chatbot(config, self.sentiment_analyzer)
        self.memory = Memory()
        
        # Setup window
        self.setWindowTitle("LunAI - Personal AI Assistant")
        self.setGeometry(100, 100, config.WINDOW_WIDTH, config.WINDOW_HEIGHT)
        self.setWindowOpacity(config.WINDOW_OPACITY)
        
        # Apply stylesheet
        self.setStyleSheet(get_style(config.THEME))
        
        # Create central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Create layout
        layout = QVBoxLayout()
        central_widget.setLayout(layout)
        
        # Avatar label
        self.avatar_label = QLabel()
        self.avatar_label.setAlignment(Qt.AlignCenter)
        self.avatar_label.setFixedSize(150, 150)
        self._load_avatar("neutral.png")
        layout.addWidget(self.avatar_label, alignment=Qt.AlignCenter)
        
        # Title
        title = QLabel(config.AI_NAME)
        title.setAlignment(Qt.AlignCenter)
        title_font = QFont()
        title_font.setPointSize(14)
        title_font.setBold(True)
        title.setFont(title_font)
        layout.addWidget(title)
        
        # Chat display
        self.chat_display = QTextEdit()
        self.chat_display.setReadOnly(True)
        self.chat_display.setMinimumHeight(250)
        layout.addWidget(self.chat_display)
        
        # Input area
        input_layout = QHBoxLayout()
        
        self.input_field = QTextEdit()
        self.input_field.setMinimumHeight(60)
        self.input_field.setMaximumHeight(80)
        self.input_field.setPlaceholderText("Digite sua mensagem...")
        input_layout.addWidget(self.input_field)
        
        # Send button
        self.send_button = QPushButton("Enviar")
        self.send_button.setFixedSize(80, 60)
        self.send_button.clicked.connect(self.send_message)
        input_layout.addWidget(self.send_button)
        
        layout.addLayout(input_layout)
        
        # Status bar
        self.statusBar().showMessage("Pronto para conversar...")
        
        # Show initial greeting
        self._show_greeting()
    
    def send_message(self):
        """
        Send message and get response.
        """
        user_input = self.input_field.toPlainText().strip()
        
        if not user_input:
            return
        
        # Display user message
        self._add_to_chat(f"Você: {user_input}", "user")
        self.input_field.clear()
        
        # Get response
        response, sentiment = self.chatbot.process_message(user_input)
        
        # Save to memory
        self.memory.add_message("user", user_input, sentiment)
        self.memory.add_message("assistant", response, "neutral")
        
        # Display response
        self._add_to_chat(f"LunAI: {response}", "assistant")
        
        # Update avatar
        if self.config.ENABLE_AVATAR:
            avatar_file = self.sentiment_analyzer.get_avatar_from_sentiment(sentiment)
            self._load_avatar(avatar_file)
        
        # Update status
        self.statusBar().showMessage(f"Sentimento detectado: {sentiment}")
    
    def _add_to_chat(self, message: str, author: str = "system"):
        """
        Add message to chat display.
        """
        current_text = self.chat_display.toPlainText()
        self.chat_display.setText(current_text + "\n" + message if current_text else message)
        
        # Scroll to bottom
        self.chat_display.verticalScrollBar().setValue(
            self.chat_display.verticalScrollBar().maximum()
        )
    
    def _load_avatar(self, filename: str):
        """
        Load and display avatar.
        """
        avatar_path = Path("assets/avatars") / filename
        
        if avatar_path.exists():
            pixmap = QPixmap(str(avatar_path))
            scaled_pixmap = pixmap.scaledToWidth(150)
            self.avatar_label.setPixmap(scaled_pixmap)
        else:
            # Show placeholder if avatar not found
            self.avatar_label.setText("🤖")
    
    def _show_greeting(self):
        """
        Show initial greeting message.
        """
        self._add_to_chat(f"LunAI: {self.config.AI_GREETING}")
        self.memory.add_message("assistant", self.config.AI_GREETING)
    
    def closeEvent(self, event):
        """
        Handle window close event.
        """
        # Save session
        if self.memory.get_history():
            self.memory.save_session()
        event.accept()
