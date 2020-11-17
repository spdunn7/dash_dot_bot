"""'Dash Dot Bot'
Morse Code Translator Program.
This program coverts a text string to Morse code.

Created: 2020-10-10
Author: Sean P. Dunn
"""

# TODO: write master loop for the interface
# TODO: add dictionary w/ English - Morse translations
# TODO: log transcript of the translation session to a .txt file
# TODO: use the 'time' module and an equation to print the answers in the correct tempo & rhythm

# I've added a space after each letter to add the space between letters when spelling a word
key = {
    'a': '. - ',
    'b': '- . . . ',
    'c': '- . - . ',
    'd': '- . . '
}
print(key)
print(key[1])
