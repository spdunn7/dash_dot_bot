"""'Dash Dot Bot'
Morse Code Translator Program.
This program coverts a text string to Morse code.

Created: 2020-10-10
Author: Sean P. Dunn
"""

# Store English to Morse code conversion key
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

intro = """
Hi, I'm Dash Dot Bot.
I translate what you say into Morse code!
Type something in and I'll say it back to you in Morse code!
"""

instructions = """
Type 'H' for HELP & more info.
Type 'Q' to Quit.
Otherwise, type anything else, and I'll repeat it back in Morse code!

"""


# Function to convert user input to Morse code
def translate(user_input):
    temp_str = ""

    for x in user_input:
        temp_str += key[x.upper()]

    return temp_str


# Print intro function
def print_intro():
    print(intro)


# Display Key Function
def display_key():
    for x, y in key.items():
        print(x, " ", y)


print_intro()


# Master loop that serves as the console app
def play():
    while True:
        user_input = input(instructions)
        if user_input.upper() == "H":
            print()
            print("CONVERSION CHART:")
            display_key()
            print_intro()
        elif user_input.upper() == "Q":
            break
        else:
            print(translate(user_input))


play()
