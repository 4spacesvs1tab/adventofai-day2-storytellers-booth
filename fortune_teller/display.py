"""
Display Formatter Module

Handles the visual presentation of fortunes in the terminal with post-apocalyptic theme.
"""

import sys
from typing import Dict, Any


class DisplayFormatter:
    """Formats and displays fortunes with visual appeal."""
    
    def __init__(self):
        """Initialize the display formatter."""
        # Check if terminal supports colors
        self.colors_supported = self._check_color_support()
    
    def _check_color_support(self) -> bool:
        """Check if the terminal supports colors.
        
        Returns:
            True if colors are supported, False otherwise
        """
        # Simple check - most modern terminals support colors
        return hasattr(sys.stdout, 'isatty') and sys.stdout.isatty()
    
    def _get_personality_color(self, personality: str) -> str:
        """Get ANSI color code for a personality.
        
        Args:
            personality: The personality type
            
        Returns:
            ANSI color code string
        """
        colors = {
            'mysterious': '\033[35m',  # Purple
            'festive': '\033[33m',     # Yellow
            'grumpy': '\033[31m',      # Red
            'poetic': '\033[34m',      # Blue
            'sarcastic': '\033[37m'    # White
        }
        return colors.get(personality, '\033[0m')  # Default reset color
    
    def _reset_color(self) -> str:
        """Get ANSI reset color code.
        
        Returns:
            ANSI reset color code string
        """
        return '\033[0m'
    
    def print_welcome(self) -> None:
        """Print the welcome message with decorative border."""
        print("┌─────────────────────────────────────────────────────────────────┐")
        print("│ ☢️  Welcome to the Fortune Teller's Booth - Nuclear Winter  ☢️  │")
        print("└─────────────────────────────────────────────────────────────────┘")
        print()
    
    def print_divider(self) -> None:
        """Print a decorative divider."""
        print("☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁")
    
    def print_header(self, text: str) -> None:
        """Print a header with decorative border.
        
        Args:
            text: The header text to display
        """
        # Pad text to fit nicely in the box
        padded_text = f" {text} "
        text_length = len(padded_text)
        box_width = max(text_length + 4, 50)
        
        # Top border
        print("┌" + "─" * (box_width - 2) + "┐")
        
        # Text line
        left_padding = (box_width - 2 - len(padded_text)) // 2
        right_padding = box_width - 2 - len(padded_text) - left_padding
        print("│" + " " * left_padding + padded_text + " " * right_padding + "│")
        
        # Bottom border
        print("└" + "─" * (box_width - 2) + "┘")
    
    def print_fortune(self, fortune_data: Dict[str, Any]) -> None:
        """Print a formatted fortune.
        
        Args:
            fortune_data: Dictionary containing fortune information
        """
        personality = fortune_data['personality']
        name = fortune_data['name']
        emoji = fortune_data['emoji']
        fortune_text = fortune_data['fortune']['text']
        radiation_level = fortune_data['fortune'].get('magic_level', 50)
        
        # Apply color if supported
        color_prefix = self._get_personality_color(personality) if self.colors_supported else ""
        color_suffix = self._reset_color() if self.colors_supported else ""
        
        # Print personality introduction
        print(f"  {color_prefix}{emoji}  {name} whispers:{color_suffix}")
        print()
        
        # Print fortune text with indentation
        for line in fortune_text.split('\n'):
            print(f"  {line}")
        
        print()
        
        # Print radiation level indicator
        radiation_bars = "█" * (radiation_level // 10) + "░" * (10 - (radiation_level // 10))
        print(f"  🌟  Radiation Levels: {radiation_bars} {radiation_level}%")
    
    def print_footer(self) -> None:
        """Print the footer message."""
        print()
        print("┌─────────────────────────────────────────────────────────────────┐")
        print("│ May your journey through the wasteland be guided by wisdom! ☢️ │")
        print("└─────────────────────────────────────────────────────────────────┘")
