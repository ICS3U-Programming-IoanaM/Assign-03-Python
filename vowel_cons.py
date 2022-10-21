#!/usr/bin/env python
# Copyright(c) 2022 Ioana Marinescu All rights reserved.
# Created By: Ioana Marinescu

# Date: No thank you Nov. 10, 2022
# tells user if a letter is a vowel or a consonant


# checks is user put in a valid input
def is_letter(user_input):
    # checks string length not 1 char long
    if len(user_input) != 1:
        print("please enter a single character.\n")
        main()

    # if string is one char long
    else:
        # letter is a lowercase 
        if chr(user_input) >= 97 and chr(user_input) <= 122:
            print("lowercase") # get rid of this later
        elif chr(user_input) >= 65 and chr(user_input) <= 90:
            print("Uppercase")
        else:
            ("invalid")


# main function
def main():
    # global variables
    global is_capital

    # variables
    user_letter = input("Enter a letter: ")
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

    # checks if letter is actually a letter
    is_letter(user_letter)

    # checks if letter is "y"
    if user_letter == "y" or user_letter == "Y":
        print(f"{user_letter} is both a vowel and a consonant")

    # checks if letter is a vowel
    elif user_letter in vowels:
        print(f"{user_letter} is a vowel")

    # vowel is a consonant
    else:
        print(f"{user_letter} is a consonant")


if __name__ == "__main__":
    main()
