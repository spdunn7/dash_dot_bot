# Dash Dot Bot

> Morse code translator bot
>
> Created: 2020-10-10  
> Author: Sean P. Dunn

***

## Description

- This bot takes a text string and converts it to Morse code.

## Features

### Implement Master Loop

- master loop serves as the console app
- provides options to:
  - display HELP
  - QUIT program
  - type text to be translated

### Create Dictionary

- 'key' dictionary holds the conversion key/values for translating from English to Morse code

### Create & Call At Least 3 Functions

- 4 total functions:

  - translate()
    - line 67
    - converts user input to Morse code
  - print_intro()
    - line 77
    - prints intro text
  - display_key()
    - line 82
    - prints conversion key dictionary
  - play()
    - line 91
    - enters the master loop that acts as application interface

### Build Conversion Tool

- 'translate()' function receives user input in the form of a text string, iterates through that input, and, using the 'key' conversion dictionary, prints the associated Morse code stored in the dict
  - converts English to Morse code

## Special Instructions

- use 'python3' to run the program
  - run program with 'python3 dash_dot_bot.py' command
- follow the on-screen prompts
  - 'H' for HELP
    - displays the conversion chart
    - re-displays the intro summary
  - 'Q' to QUIT the program
  - Any other text will be translated to Morse code and printed to the screen
