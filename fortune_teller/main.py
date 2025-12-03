#!/usr/bin/env python3
"""
Madame Zelda's Winter Fortune Teller CLI

A CLI application that generates winter-themed fortunes with different
mystical personalities.

Usage:
    python fortune_teller/main.py [options]

Options:
    -h, --help            Show this help message
    -p, --personality     Specify personality type
    -n, --number          Number of fortunes to generate (default: 1)
    -l, --list            List available personalities
    --version             Show version information
"""

import argparse
import json
import os
import random
import sys
from typing import Dict, List, Optional

# Get the directory of this script
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# Add the project root to sys.path so we can import modules
sys.path.insert(0, os.path.join(SCRIPT_DIR, '..'))

from fortune_teller.fortune_generator import FortuneGenerator
from fortune_teller.display import DisplayFormatter


def load_fortunes() -> Dict:
    """Load fortunes from JSON file."""
    data_path = os.path.join(SCRIPT_DIR, 'data', 'fortunes.json')
    try:
        with open(data_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: Could not find fortunes data file at {data_path}")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Error: Could not parse fortunes data file: {e}")
        sys.exit(1)


def list_personalities(fortune_data: Dict) -> None:
    """List all available personalities."""
    formatter = DisplayFormatter()
    formatter.print_header("Available Fortune Teller Personalities")
    
    personalities = fortune_data.get('personalities', {})
    for key, personality in personalities.items():
        print(f"  {personality.get('emoji', '')} {key.capitalize()}: {personality.get('description', '')}")
    
    print()


def main():
    """Main application entry point."""
    # Load fortune data
    fortune_data = load_fortunes()
    
    # Set up argument parser
    parser = argparse.ArgumentParser(
        description="Madame Zelda's Winter Fortune Teller - CLI Edition",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python fortune_teller/main.py                           # Generate 1 random fortune
  python fortune_teller/main.py --personality mysterious  # Generate mysterious fortune
  python fortune_teller/main.py --number 3                # Generate 3 random fortunes
  python fortune_teller/main.py --list                    # List all personalities
        """
    )
    
    parser.add_argument(
        '-p', '--personality',
        choices=['mysterious', 'festive', 'grumpy', 'poetic', 'sarcastic'],
        help='Specify the fortune teller personality'
    )
    
    parser.add_argument(
        '-n', '--number',
        type=int,
        default=1,
        help='Number of fortunes to generate (default: 1)'
    )
    
    parser.add_argument(
        '-l', '--list',
        action='store_true',
        help='List available personalities'
    )
    
    parser.add_argument(
        '--version',
        action='version',
        version='Madame Zelda\'s Winter Fortune Teller 1.0'
    )
    
    # Parse arguments
    args = parser.parse_args()
    
    # Handle list option
    if args.list:
        list_personalities(fortune_data)
        return
    
    # Validate number argument
    if args.number < 1:
        print("Error: Number of fortunes must be at least 1")
        sys.exit(1)
    
    if args.number > 10:
        print("Error: Cannot generate more than 10 fortunes at once")
        sys.exit(1)
    
    # Initialize components
    generator = FortuneGenerator(fortune_data)
    formatter = DisplayFormatter()
    
    # Print welcome message for first fortune
    if args.number >= 1:
        formatter.print_welcome()
    
    # Generate and display fortunes
    for i in range(args.number):
        # Add separator between fortunes (except for the first one)
        if i > 0:
            print()
            formatter.print_divider()
            print()
        
        # Generate fortune
        try:
            if args.personality:
                fortune = generator.generate_fortune(args.personality)
            else:
                fortune = generator.generate_random_fortune()
        except ValueError as e:
            print(f"Error: {e}")
            sys.exit(1)
        
        # Display fortune
        formatter.print_fortune(fortune)
    
    # Print footer after last fortune
    if args.number >= 1:
        formatter.print_footer()


if __name__ == '__main__':
    main()
