#!/usr/bin/env python
# Copyright(c) 2022 Ioana Marinescu All rights reserved.
# Created By: Ioana Marinescu

# Date: No thank you Nov. 10, 2022
# tells user if a letter is a vowel or a consonant


# checks if letter is capital
def to_capital(letter):
    # turns it back to a capital letter
    if is_capital:
        letter = letter.upper()
        return letter

    # if it was lowercase to begin with
    else:
        return letter

# checks is user put in a valid input
def is_letter(user_input):
    # checks string length not 1 char long
    if len(user_input) != 1:
        print("please enter a single character.\n")
        main()
    else:
        valid_input = True
        # if not a letter
        if not user_input.isalpha():
            print(f"{user_input} is not a letter.\n")
            main()


# main function
def main():
    # global variables
    global is_capital
    global is_not_finished

    # lets user know what the program does
    print("\nThis program will check weather or not a letter is a vowel or a consonant.")
    print("*takes capital and lowercase letters*\n")

    # variables
    user_letter = input("Enter a letter: ")
    vowels = ["a", "e", "i", "o", "u"]
    is_not_finished = True

    # checks if letter is actually a letter
    is_letter(user_letter)

# if statements for upper or lowercase
    # checks if letter is uppercase
    if user_letter.isupper():
        # makes the user's letter lowercase
        is_capital = True
        user_letter = user_letter.lower()

    # if user's letter is lowercase
    else:
        is_capital = False

# displays weather or not the letter is a vowel or a consonant
    if is_not_finished:
        # checks if letter is "y"
        if user_letter == "y":
            user_letter = to_capital(user_letter)
            print(f"{user_letter} is both a vowel and a consonant")
        
        # checks if letter is a vowel
        elif user_letter in vowels:
            user_letter = to_capital(user_letter)
            print(f"{user_letter} is a vowel")
            is_not_finished = True

        # vowel is a consonant
        else:
            user_letter = to_capital(user_letter)
            print(f"{user_letter} is a consonant")


if __name__ == "__main__":
    main()
