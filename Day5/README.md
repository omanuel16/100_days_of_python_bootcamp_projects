# Password Generator

A simple command-line Password Generator built with Python as part of the 100 Days of Python Bootcamp.

## Description

This is an interactive password generator that creates secure passwords based on your specifications. The program generates two versions of passwords:
- **Easy version**: Characters are in a predictable order (letters, then numbers, then symbols)
- **Hard version**: All characters are randomly shuffled for maximum security

The generator uses a combination of lowercase letters, numbers, and symbols to create strong passwords.

## Features

- Customizable password length (letters, numbers, and symbols)
- Two password generation modes (easy and hard)
- Random character selection
- Uses 26 lowercase letters, 10 numbers, and 6 symbols
- Hard version shuffles all characters for enhanced security

## How to Play

1. Run the script: `python Password_Creator.py`
2. Enter how many letters you want in your password
3. Enter how many symbols you want in your password
4. Enter how many numbers you want in your password
5. The program will generate both an easy and hard version of the password

## Requirements

- Python 3.x
- No external dependencies (uses only built-in `random` module)

## Example Output

```
How many letters woould you like in your passwords?
8
How many symbols woudl you like? 
2
How many numbers would you like?
4
This password was created with the Easy version code 
abcdefgh1234!$
This password was created with the hard version code 
 a4$b2c!d1e3fgh
```

