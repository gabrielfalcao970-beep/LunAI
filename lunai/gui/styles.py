# -*- coding: utf-8 -*-
"""GUI Stylesheet definitions"""


def get_stylesheet(theme: str = "dark") -> str:
    """Get stylesheet for the application.
    
    Args:
        theme: "dark" or "light"
        
    Returns:
        Stylesheet string
    """
    if theme == "light":
        return LIGHT_STYLESHEET
    else:
        return DARK_STYLESHEET


DARK_STYLESHEET = """
    QMainWindow {
        background-color: #1a1a2e;
        color: #eaeaea;
    }
    
    QWidget {
        background-color: #1a1a2e;
        color: #eaeaea;
    }
    
    QTextEdit {
        background-color: #16213e;
        color: #eaeaea;
        border: 2px solid #0f3460;
        border-radius: 8px;
        padding: 8px;
        font-family: 'Segoe UI', Arial, sans-serif;
        font-size: 10pt;
        selection-background-color: #00d4ff;
    }
    
    QPushButton {
        background-color: #00d4ff;
        color: #1a1a2e;
        border: none;
        border-radius: 6px;
        padding: 10px 20px;
        font-weight: bold;
        font-size: 10pt;
        font-family: 'Segoe UI', Arial, sans-serif;
    }
    
    QPushButton:hover {
        background-color: #00e6ff;
    }
    
    QPushButton:pressed {
        background-color: #00a8cc;
    }
    
    QLabel {
        color: #eaeaea;
    }
    
    QStatusBar {
        background-color: #16213e;
        color: #eaeaea;
        border-top: 1px solid #0f3460;
    }
"""

LIGHT_STYLESHEET = """
    QMainWindow {
        background-color: #f5f5f5;
        color: #333333;
    }
    
    QWidget {
        background-color: #f5f5f5;
        color: #333333;
    }
    
    QTextEdit {
        background-color: #ffffff;
        color: #333333;
        border: 2px solid #ddd;
        border-radius: 8px;
        padding: 8px;
        font-family: 'Segoe UI', Arial, sans-serif;
        font-size: 10pt;
        selection-background-color: #4CAF50;
    }
    
    QPushButton {
        background-color: #4CAF50;
        color: #ffffff;
        border: none;
        border-radius: 6px;
        padding: 10px 20px;
        font-weight: bold;
        font-size: 10pt;
        font-family: 'Segoe UI', Arial, sans-serif;
    }
    
    QPushButton:hover {
        background-color: #45a049;
    }
    
    QPushButton:pressed {
        background-color: #3d8b40;
    }
    
    QLabel {
        color: #333333;
    }
    
    QStatusBar {
        background-color: #f0f0f0;
        color: #333333;
        border-top: 1px solid #ddd;
    }
"""
