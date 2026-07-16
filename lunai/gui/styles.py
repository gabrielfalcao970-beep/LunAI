#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
LunAI GUI Styles
CSS-like styling for PyQt5
"""

DARK_THEME = """
    QMainWindow {
        background-color: #1e1e1e;
    }
    
    QWidget {
        background-color: #2d2d2d;
        color: #ffffff;
        font-family: 'Segoe UI', Arial, sans-serif;
        font-size: 10pt;
    }
    
    QTextEdit {
        background-color: #3d3d3d;
        color: #ffffff;
        border: 1px solid #555555;
        border-radius: 5px;
        padding: 5px;
    }
    
    QPushButton {
        background-color: #4CAF50;
        color: white;
        border: none;
        border-radius: 5px;
        padding: 8px 16px;
        font-weight: bold;
    }
    
    QPushButton:hover {
        background-color: #45a049;
    }
    
    QPushButton:pressed {
        background-color: #3d8b40;
    }
    
    QLabel {
        color: #ffffff;
    }
    
    QScrollBar:vertical {
        background-color: #3d3d3d;
        width: 10px;
        border: none;
    }
    
    QScrollBar::handle:vertical {
        background-color: #555555;
        border-radius: 5px;
    }
    
    QScrollBar::handle:vertical:hover {
        background-color: #666666;
    }
"""

LIGHT_THEME = """
    QMainWindow {
        background-color: #ffffff;
    }
    
    QWidget {
        background-color: #f5f5f5;
        color: #333333;
        font-family: 'Segoe UI', Arial, sans-serif;
        font-size: 10pt;
    }
    
    QTextEdit {
        background-color: #ffffff;
        color: #333333;
        border: 1px solid #dddddd;
        border-radius: 5px;
        padding: 5px;
    }
    
    QPushButton {
        background-color: #4CAF50;
        color: white;
        border: none;
        border-radius: 5px;
        padding: 8px 16px;
        font-weight: bold;
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
"""

def get_style(theme: str = "dark") -> str:
    """
    Get stylesheet for given theme.
    """
    if theme.lower() == "light":
        return LIGHT_THEME
    return DARK_THEME
