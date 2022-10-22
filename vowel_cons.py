#!/usr/bin/env python
# Copyright(c) 2022 Ioana Marinescu All rights reserved.
# Created By: Ioana Marinescu

# Date: No thank you Nov. 10, 2022
# Tells user weather a letter is a vowel or a consonant


# tells user if their input is valid
def is_valid(user_input):
    # variables
    invalid = True

    while invalid:
        # if user imputed multiple letters or symbols
        if len(user_input) > 1:
            print("Please input ONE character.")
            user_input = input("Enter a letter: ")

        # if user doesn't input anything
        elif len(user_input) == 0:
            print("Please type in your input.")
            user_input = input("Enter a letter: ")

        else:
            character = ord(user_input)

            # checks if character is not a letter
            if character < 65 or (character > 90 and character < 97) or character > 122:
                print(f"{user_input} is not a letter. Please try again")
                user_input = input("Enter a letter: ")

            # checks if character is an accented letter
            elif character >= 192 and character <= 383:
                print("Letters can't be accented. Please try again.")
                user_input = input("Enter a letter: ")

            else:
                invalid = False


# main function
def main():
    # variables
    user_letter = input("Enter a letter: ")
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

    # checks if letter is actually a letter
    # is_letter(user_letter)
    is_valid(user_letter)

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
