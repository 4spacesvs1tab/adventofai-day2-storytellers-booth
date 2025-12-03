# Fortune Teller CLI

This is a CLI-based fortune teller application that generates winter-themed fortunes with different mystical personalities.

## Usage

Run the application from the project root directory:

```bash
# Generate a random fortune
python3 fortune_teller/main.py

# Generate a fortune with specific personality
python3 fortune_teller/main.py --personality mysterious

# Generate multiple fortunes
python3 fortune_teller/main.py --number 3

# List available personalities
python3 fortune_teller/main.py --list

# Show help
python3 fortune_teller/main.py --help
```

## Personalities

- **Mysterious Morgan** (🧙‍♀️): Speaks in riddles and rhymes
- **Festive Felicia** (🎄): Joyful and celebratory
- **Grumpy Gus** (🐻): Cranky but honest
- **Poetic Penelope** (🖋️): Eloquent and artistic
- **Sarcastic Sam** (😏): Witty with a sharp tongue

## Features

- Visually appealing ASCII art borders
- Colorful output with personality-specific colors
- Emoji support for each personality
- Magic level indicators for each fortune
- Support for generating multiple fortunes
- Cross-platform compatibility
