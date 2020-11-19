"""'Dash Dot Bot'
Morse Code Translator Program.
This program coverts a text string to Morse code.

Created: 2020-10-10
Author: Sean P. Dunn
"""

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
    '0': '- - - - -',
    ' ': '  ',
    ',': ',',
    '.': '.'
}


def translate(user_input):
    temp_list = ""

    for x in user_input:
        temp_list += key[x.upper()]

    print(temp_list)


intro = """
Hi, I'm Dash Dot Bot.
I translate what you say into Morse code!
Type something in and I'll say it back to you in Morse code!
"""

print(intro)

while True:
    user_input = input("""
Type 'H' for HELP & more info.
Type 'Q' to Quit.
Otherwise, type anything else, and I'll repeat it back in Morse code!
""")
    if user_input.upper() == "H":
        print()
        print("CONVERSION CHART:")
        print(key)
        print(intro)
        # Do i need a 'continue' statement here?
    elif user_input.upper() == "Q":
        break
    else:
        translate(user_input)

