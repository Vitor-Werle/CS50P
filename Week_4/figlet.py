import sys
from pyfiglet import Figlet
import random

# Create an instance of Figlet
figlet = Figlet()

# Check the number of command-line arguments
if len(sys.argv) not in [1, 3]:
    sys.exit("Usage: python figlet.py [-f FONT]")

# If no arguments are provided, choose a random font
if len(sys.argv) == 1:
    # Get a random font
    random_font = random.choice(figlet.getFonts())
    figlet.setFont(font=random_font)
    
    # Prompt the user for text
    text = input("Text: ")
    
    # Render and print the text
    print(figlet.renderText(text))

# If two arguments are provided
elif len(sys.argv) == 3:
    # Check if the first argument is valid
    if sys.argv[1] not in ["-f", "--font"]:
        sys.exit("Invalid argument. Use -f or --font.")
    
    # Check if the second argument is a valid font
    font = sys.argv[2]
    if font not in figlet.getFonts():
        sys.exit("Invalid font name.")
    
    # Set the specified font
    figlet.setFont(font=font)
    
    # Prompt the user for text
    text = input("Text: ")
    
    # Render and print the text
    print(figlet.renderText(text))
