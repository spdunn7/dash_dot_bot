"""'Dash Dot Bot'
Morse Code Translator Program.
This program coverts a text string to Morse code.

Created: 2020-10-10
Author: Sean P. Dunn
"""
import time


# TODO: write master loop for the interface
# TODO: write function to perform the translation
# TODO: log transcript of the translation session to a .txt file
# TODO: use the 'time' module and an equation to print the answers in the correct tempo & rhythm

key = {
    'A': '. -',
    'B': '- . . .',
    'C': '- . - .',
    'D': '- . .',
    'E': '.',
    'F': '. . - .',
    'G': '- - .',
    'H': '. . . .',
    'I': '. .',
    'J': '. - - -',
    'K': '- . -',
    'L': '. - . .',
    'M': '- -',
    'N': '- .',
    'O': '- - -',
    'P': '. - - .',
    'Q': '- - . -',
    'R': '. - .',
    'S': '. . .',
    'T': '-',
    'U': '. . -',
    'V': '. . . -',
    'W': '. - -',
    'X': '- . . -',
    'Y': '- . - -',
    'Z': '- - . .',
    '1': '. - - - -',
    '2': '. . - - -',
    '3': '. . . - -',
    '4': '. . . . -',
    '5': '. . . . .',
    '6': '- . . . .',
    '7': '- - . . .',
    '8': '- - - . .',
    '9': '- - - - .',
    '0': '- - - - -'
}


# TODO: add a count to make intro statement only appear upon first opening app
while True:
    print("""Hi, I'm Dash Dot Bot.
    I translate what you say into Morse code!
    Type something in and I'll say it back to you in Morse code!""")
    user_input = input("""To view the conversion chart, type 'view chart'.
    Or, type 'Q' to Quit """)
    if user_input.upper() == "VIEW CHART":
        print(key)
        # Do i need a 'continue' statement here?
    if user_input.upper() == "Q":
        break
