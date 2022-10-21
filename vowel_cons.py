#!/usr/bin/env python
# Copyright(c) 2022 Ioana Marinescu All rights reserved.
# Created By: Ioana Marinescu

# Date: No thank you Nov. 10, 2022


# tells user if a letter is a vowel or a consonant
def string_length(user_string):
    return len(user_string) # change later

# main function
def main():

    # variables
    user_letter = input("Enter a letter: ")
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

    # checks if letter is actually a letter
    # is_letter(user_letter)

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
