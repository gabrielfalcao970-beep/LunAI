# -*- coding: utf-8 -*-
"""Main GUI window for LunAI"""

import logging
from pathlib import Path
from PyQt5.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QTextEdit, QPushButton, QLabel, QScrollArea
)
from PyQt5.QtGui import QPixmap, QIcon, QFont
from PyQt5.QtCore import Qt, QTimer

from lunai.core.chatbot import Chatbot
from lunai.core.sentiment import SentimentAnalyzer
from lunai.gui.styles import get_stylesheet


class MainWindow(QMainWindow):
    """Main application window."""
    
    def __init__(self, config):
        """Initialize main window.
        
        Args:
            config: Configuration object
        """
        super().__init__()
        self.config = config
        self.logger = logging.getLogger("LunAI.GUI")
        
        # Initialize AI components
        self.sentiment_analyzer = SentimentAnalyzer(config)
        self.chatbot = Chatbot(config, self.sentiment_analyzer)
        
        # Setup UI
        self.setup_ui()
        self.apply_styles()
        
        self.logger.info("Main window initialized")
    
    def setup_ui(self):
        """Setup user interface."""
        self.setWindowTitle("LunAI - Personal AI Assistant")
        self.setGeometry(100, 100, self.config.WINDOW_WIDTH, self.config.WINDOW_HEIGHT)
        self.setWindowFlags(Qt.WindowStaysOnTopHint if self.config.ALWAYS_ON_TOP else Qt.Window)
        
        # Central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        main_layout.setContentsMargins(10, 10, 10, 10)
        main_layout.setSpacing(10)
        
        # Header with avatar
        header_layout = QHBoxLayout()
        
        # Avatar label
        self.avatar_label = QLabel()
        self.avatar_label.setMaximumWidth(70)
        self.avatar_label.setMaximumHeight(70)
        self.update_avatar("neutral")
        header_layout.addWidget(self.avatar_label)
        
        # Title
        title_label = QLabel(f"{self.config.AI_NAME}")
        title_font = QFont()
        title_font.setPointSize(14)
        title_font.setBold(True)
        title_label.setFont(title_font)
        header_layout.addWidget(title_label)
        header_layout.addStretch()
        
        main_layout.addLayout(header_layout)
        
        # Chat display area
        self.chat_display = QTextEdit()
        self.chat_display.setReadOnly(True)
        self.chat_display.setPlaceholderText("Conversation will appear here...\n\nTry saying: Olá, Como você está? ou Estou triste")
        main_layout.addWidget(self.chat_display)
        
        # Input area
        input_layout = QHBoxLayout()
        
        self.input_field = QTextEdit()
        self.input_field.setPlaceholderText("Type your message here...")
        self.input_field.setMaximumHeight(60)
        input_layout.addWidget(self.input_field)
        
        # Send button
        self.send_button = QPushButton("Send")
        self.send_button.clicked.connect(self.send_message)
        self.send_button.setMaximumWidth(80)
        input_layout.addWidget(self.send_button)
        
        main_layout.addLayout(input_layout)
        
        # Status bar
        self.statusBar().showMessage("Ready")
        
        # Connect keyboard shortcut (Enter to send)
        self.input_field.setFocus()
    
    def apply_styles(self):
        """Apply stylesheet to the application."""
        stylesheet = get_stylesheet(self.config.THEME)
        self.setStyleSheet(stylesheet)
    
    def update_avatar(self, emotion: str):
        """Update avatar based on emotion.
        
        Args:
            emotion: Emotion string
        """
        avatar_map = {
            "calm": "calm.png",
            "neutral": "neutral.png",
            "surprised": "surprised.png",
            "worried": "worried.png",
            "sad": "sad.png",
            "confused": "confused.png",
            "thinking": "thinking.png",
            "happy": "happy.png",
            "serene": "serene.png",
            "angry": "angry.png",
        }
        
        avatar_file = avatar_map.get(emotion, "neutral.png")
        avatar_path = Path("assets/avatars") / avatar_file
        
        if avatar_path.exists():
            pixmap = QPixmap(str(avatar_path))
            scaled_pixmap = pixmap.scaledToHeight(70, Qt.SmoothTransformation)
            self.avatar_label.setPixmap(scaled_pixmap)
        else:
            # Create placeholder if avatar doesn't exist
            placeholder = QPixmap(70, 70)
            placeholder.fill(Qt.gray)
            self.avatar_label.setPixmap(placeholder)
    
    def send_message(self):
        """Send user message and get AI response."""
        user_message = self.input_field.toPlainText().strip()
        
        if not user_message:
            return
        
        # Display user message
        self.chat_display.append(f"<b>You:</b> {user_message}")
        self.input_field.clear()
        
        # Get AI response
        response, emotion = self.chatbot.get_response(user_message)
        
        # Update avatar
        self.update_avatar(emotion)
        
        # Display AI response
        self.chat_display.append(f"<b>{self.config.AI_NAME}:</b> {response}")
        
        # Scroll to bottom
        self.chat_display.verticalScrollBar().setValue(
            self.chat_display.verticalScrollBar().maximum()
        )
        
        self.statusBar().showMessage(f"Emotion: {emotion.capitalize()}")
