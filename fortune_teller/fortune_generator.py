"""
Fortune Generator Module

Handles the generation of fortunes with different personalities.
"""

import random
from typing import Dict, Any, Optional


class FortuneGenerator:
    """Generates fortunes with different mystical personalities."""
    
    def __init__(self, fortune_data: Dict):
        """Initialize the fortune generator with fortune data.
        
        Args:
            fortune_data: Dictionary containing personality and fortune data
        """
        self.fortune_data = fortune_data
        self.personalities = fortune_data.get('personalities', {})
    
    def generate_fortune(self, personality: str) -> Dict[str, Any]:
        """Generate a fortune for a specific personality.
        
        Args:
            personality: The personality type to generate a fortune for
            
        Returns:
            Dictionary containing fortune data
            
        Raises:
            ValueError: If personality is not found
        """
        if personality not in self.personalities:
            available = ', '.join(self.personalities.keys())
            raise ValueError(f"Personality '{personality}' not found. Available personalities: {available}")
        
        personality_data = self.personalities[personality]
        fortunes = personality_data.get('fortunes', [])
        
        if not fortunes:
            raise ValueError(f"No fortunes available for personality '{personality}'")
        
        # Select a random fortune
        selected_fortune = random.choice(fortunes)
        
        # Return fortune with personality metadata
        return {
            'personality': personality,
            'name': personality_data.get('name', personality.capitalize()),
            'emoji': personality_data.get('emoji', ''),
            'fortune': selected_fortune
        }
    
    def generate_random_fortune(self) -> Dict[str, Any]:
        """Generate a fortune with a randomly selected personality.
        
        Returns:
            Dictionary containing fortune data with random personality
        """
        if not self.personalities:
            raise ValueError("No personalities available")
        
        # Select a random personality
        personality = random.choice(list(self.personalities.keys()))
        return self.generate_fortune(personality)
    
    def get_personality_names(self) -> list:
        """Get a list of available personality names.
        
        Returns:
            List of personality names
        """
        return list(self.personalities.keys())
    
    def get_personality_info(self, personality: str) -> Optional[Dict]:
        """Get information about a specific personality.
        
        Args:
            personality: The personality to get information for
            
        Returns:
            Dictionary with personality information or None if not found
        """
        return self.personalities.get(personality)
