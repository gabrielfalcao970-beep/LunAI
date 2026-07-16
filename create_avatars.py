#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Generate placeholder avatar images for LunAI
Creates simple emoji-based avatars if PIL avatars are not available
"""

from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
import colorsys

def create_avatar(emotion: str, filename: str):
    """
    Create a simple avatar image with emoji and emotion.
    """
    # Create image
    size = (200, 200)
    img = Image.new('RGB', size, color=(45, 45, 45))
    draw = ImageDraw.Draw(img)
    
    # Emotion emojis
    emojis = {
        'happy': '😊',
        'calm': '😌',
        'neutral': '😐',
        'sad': '😢',
        'worried': '😟',
        'angry': '😠',
        'confused': '😕',
        'thinking': '🤔',
        'surprised': '😮',
        'serene': '🧘'
    }
    
    emoji = emojis.get(emotion, '🤖')
    
    # Add text
    try:
        # Try to use a larger font
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 120)
    except:
        font = ImageFont.load_default()
    
    # Draw emoji (using text approximation)
    text = emoji
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    x = (size[0] - text_width) // 2
    y = (size[1] - text_height) // 2
    draw.text((x, y), text, fill=(255, 255, 255), font=font)
    
    # Save
    img.save(filename)
    print(f"✓ Created {filename}")

def main():
    """
    Create all avatar images.
    """
    avatar_dir = Path("assets/avatars")
    avatar_dir.mkdir(parents=True, exist_ok=True)
    
    emotions = [
        'happy',
        'calm',
        'neutral',
        'sad',
        'worried',
        'angry',
        'confused',
        'thinking',
        'surprised',
        'serene'
    ]
    
    print("Creating avatar images...")
    for emotion in emotions:
        filename = avatar_dir / f"{emotion}.png"
        create_avatar(emotion, str(filename))
    
    print("\n✓ All avatars created successfully!")

if __name__ == "__main__":
    main()
