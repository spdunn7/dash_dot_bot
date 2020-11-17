"""'Dash Dot Bot'
Morse Code Translator Program.
This program coverts a text string to Morse code.

Created: 2020-10-10
Author: Sean P. Dunn
"""
import time


# TODO: write master loop for the interface
# TODO: add dictionary w/ English - Morse translations
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

# for x in key:
#     print(key[x])
#     time.sleep(1)

