# Project Design: The Fortune Teller's Booth

## Design Vision
Create a CLI-based fortune teller application that generates post-apocalyptic themed fortunes with different mystical personalities. The application will provide visually appealing output in the terminal using ASCII art, decorative borders, and emojis while maintaining the mysterious atmosphere of a carnival booth in a nuclear winter wasteland.

## CLI Interface Design

### Command Structure
```
fortune-teller [options]

Options:
  -h, --help            Show help message
  -p, --personality     Specify personality type (grumpy, poetic, festive, sarcastic, mysterious)
  -n, --number          Number of fortunes to generate (default: 1)
  -l, --list            List available personalities
  --version             Show version information
```

### Output Structure
```
┌─────────────────────────────────────────────────────────────────┐
│ ☢️  Welcome to the Fortune Teller's Booth - Nuclear Winter  ☢️  │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  🔮  Mysterious Morgan whispers:                                │
│                                                                 │
│  "In the ruins where the old gods dwelt,                        │
│   New spirits in the shadows belt.                              │
│   The Geiger counters' clicking song                            │
│   Foretells where you belong."                                  │
│                                                                 │
│  🌟  Radiation Levels: ████████░░ 80%                           │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

## Data Structure

### Fortune Data Format
Fortunes will be stored in JSON format for easy maintenance:

```json
{
  "personalities": {
    "mysterious": {
      "name": "Mysterious Morgan",
      "emoji": "🔮",
      "description": "Speaks in riddles about the old world and new mysteries",
      "fortunes": [
        {
          "text": "In the ruins where the old gods dwelt,\nNew spirits in the shadows belt.\nThe Geiger counters' clicking song\nForetells where you belong.",
          "magic_level": 80
        }
      ]
    },
    "festive": {
      "name": "Festive Felicia",
      "emoji": "🎉",
      "description": "Celebrates the absurd joy of surviving the apocalypse",
      "fortunes": []
    }
  }
}
```

## Visual Design Elements

### Border Styles
- **Main Border**: Heavy box drawing characters (═, ║, ╒, ╕, ╘, ╛)
- **Section Separators**: Medium weight characters (─, │, ├, ┤, ┬, ┴)
- **Decorative Elements**: Radioactive symbols ☢️, skulls 💀, fallout clouds ☁️

### Color Scheme
- **Primary**: Dark grays and blacks for post-apocalyptic atmosphere
- **Accents**: Glowing greens and oranges for radioactive elements
- **Personality Colors**: 
  - Grumpy: Dark reds and browns
  - Poetic: Deep purples and blues
  - Festive: Bright yellows and oranges (contrast to surroundings)
  - Sarcastic: Grays and silvers
  - Mysterious: Dark purples and greens

### ASCII Art Elements
```
☢️  Fallout cloud divider:
☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁

🔮  Crystal ball:
    _____
   /     \
  | () () |
   \  ^  /
    |||||
    |||||

💀  Skull decoration:
   .-'''''-.
  /         \
  | ()  ()  |
  |    ^    |
   \  ===  /
    |||||||
```

## Technical Architecture

### Module Structure
```
fortune_teller/
├── main.py              # Entry point and CLI argument parsing
├── fortune_generator.py # Core fortune generation logic
├── display.py           # Visual presentation and formatting
├── data/
│   └── fortunes.json    # Fortune data storage
└── README.md            # Module-specific documentation
```

### Core Classes

#### FortuneGenerator
- Manages fortune selection and randomization
- Handles personality-specific logic
- Ensures variety in fortune selection
- Loads fortune data from JSON file

#### DisplayFormatter
- Creates visually appealing output
- Manages ASCII art and decorative elements
- Handles color output when supported
- Formats fortunes with personality-specific styling

## User Experience Flow

### 1. Application Startup
1. Parse command line arguments
2. Load fortune data
3. Validate inputs
4. Display welcome message with post-apocalyptic theme

### 2. Fortune Generation
1. Select personality (based on user input or random)
2. Choose random fortune from selected personality
3. Format fortune with appropriate visual elements
4. Display formatted output with wasteland-themed decorations

### 3. Error Handling
1. Invalid personality selection
2. Missing data files
3. Unsupported terminal features
4. General exceptions with friendly messages

## Performance Considerations

### Memory Usage
- Load fortune data once at startup
- Cache formatted elements
- Use generators for large datasets

### Execution Speed
- Minimal startup overhead
- Efficient random selection algorithms
- Pre-format static elements

## Cross-Platform Compatibility

### Terminal Support
- Handle different terminal sizes
- Gracefully degrade visual elements for basic terminals
- Support both color and monochrome output

### Character Encoding
- UTF-8 for emoji support
- Fallbacks for terminals without Unicode support
- ASCII-only alternatives for compatibility

## Extensibility Features

### Adding New Personalities
1. Add personality definition to data file
2. No code changes required
3. Automatic inclusion in help/list commands

### Adding New Fortunes
1. Edit JSON data file
2. Follow existing structure
3. Immediate availability after save

### Customizing Visuals
1. Modify border styles in display module
2. Update ASCII art elements
3. Adjust color schemes
