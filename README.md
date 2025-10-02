# Octopus Automation Script

An automated feeding and gathering script for MapleStory octopus training.

## Overview

This script automatically detects and interacts with:
- NPCs for gathering resources
- Feed buttons for octopus feeding
- Level 7 detection to stop the automation

## Installation

### Prerequisites

1. **Python 3.7 or higher**
   - Download from [python.org](https://www.python.org/downloads/)
   - During installation, make sure to check "Add Python to PATH"
   - Verify installation by opening Command Prompt and typing: `python --version`

### Setup Instructions

1. **Download the project**
   ```bash
   git clone https://github.com/Puiguqu/octopus.git
   cd octopus
   ```
   
   Or download as ZIP and extract to your desired folder.

2. **Prepare template images**
   - Take screenshots of the following game elements:
     - `npc_gather.png` - The NPC gathering interface/button
     - `feed.png` - The octopus feed button
     - `level7.png` - The level 7 indicator/text
   - Save these images in the same folder as the script
   - Use PNG format for best results
   - Ensure images are clear and cropped tightly around the target

3. **Run the automation**
   - Double-click `run_octopus.bat`
   - The batch file will automatically:
     - Create a virtual environment
     - Install all required packages
     - Start the automation script

### Manual Installation (Advanced)

If you prefer to set up manually:

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install requirements
pip install -r requirements.txt

# Run the script
python octopus.py
```

## Quick Start

1. **Run the automation**: Double-click `run_octopus.bat`
   - Creates virtual environment automatically
   - Installs required packages
   - Runs the script in a continuous loop

2. **Stop the script**: Close the command window or press Ctrl+C

## Requirements

- Python 3.7+
- Template images in the same folder:
  - `npc_gather.png` - NPC gathering interface
  - `feed.png` - Feed button
  - `level7.png` - Level 7 indicator

## Features

- **Auto-restart**: Script automatically restarts if it stops
- **Template matching**: Uses OpenCV for reliable image detection
- **Safe operation**: Moves cursor away after actions to prevent interference
- **Level detection**: Stops at level 7 to avoid interfering with bot behavior

## ⚠️ IMPORTANT DISCLAIMER

**This script does NOT account for level skips!**

If your octopus level jumps from 6 directly to 8 (skipping level 7), the automation will **continue running indefinitely** until one of the following occurs:

- All feeding resources are completely exhausted
- The octopus runs away naturally
- You manually stop the script

**The script only stops when it detects level 7 specifically.** If level 7 is skipped, the safety mechanism will not trigger.

## ⚠️ KEY BINDING WARNING

**DO NOT bind consumables to the 'R' key!**

This script uses the 'R' key for NPC chat interactions. If you have consumables (potions, buffs, etc.) bound to 'R', they will be automatically consumed whenever the script detects an NPC chat window.

**Recommended setup:**
- Keep 'R' key free for NPC chat only
- Bind consumables to other keys (Q, W, E, etc.)
- Verify your key bindings before running the script

### Recommended Usage

- Monitor the script during use
- Manually stop if you notice unexpected level progression
- Keep track of your feeding resources
- Be prepared to intervene if the octopus behavior changes

## Script Behavior

1. **Gathering**: Holds 'R' key for 5 seconds when NPC detected
2. **Feeding**: Clicks and holds feed button for 5 seconds
3. **Level Check**: Continuously monitors for level 7 to auto-stop
4. **Cursor Management**: Moves cursor left after each action

## Troubleshooting

- Ensure template images are clear and match your game resolution
- Run the game in windowed mode for better detection
- Adjust threshold values in the script if detection is unreliable
- Check that Python is properly installed and in your system PATH

## Files

- `octopus.py` - Main automation script
- `run_octopus.bat` - Setup and execution batch file
- `requirements.txt` - Python dependencies
- Template images (`.png` files)

---

**Use at your own discretion. Monitor the script's behavior and be prepared to intervene manually.**