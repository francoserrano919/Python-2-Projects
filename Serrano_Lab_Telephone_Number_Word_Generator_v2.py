"""
script:   Serrano_Lab_Telephone_Number_Word_Generator_v2.py
action:   1. Generate all possible letter combinations (words) for a 7-digit 
          phone number using a digit-to-letter mapping similar to old phone keypads.
          2. Save all generated words to a text file named output_words.txt.
          3. Only output to console when there is an error or when the file is created.
author:   Franco Xavier Serrano
date:     09/23/2025
"""

# Digit-to-letter mapping

# I removed the entire printing block as it was no longer needed. I simply output
# to the console when the file is created or if there is an error. All words are
# saved to the text file.
# New code is at the bottom of the script at "script entry point".
# Added type hints to functions for better clarity and error checking.
from typing import Generator

# Dictionary mapping digits to letters
def phone_keypad_mapping() -> dict[str, str]: # Added type hint
    """
    action:   Provide a dictionary mapping digits (2-9) to their corresponding letters.

    input:    None
    output:   None
    return:   A mapping of digits to letters accoridng to typical phone keypads.
    """
    return {
        '2': 'ABC',
        '3': 'DEF',
        '4': 'GHI',
        '5': 'JKL',
        '6': 'MNO',
        '7': 'PRS',
        '8': 'TUV',
        '9': 'WXY'
    }

# -----------------------------
# Validation function
# -----------------------------
def valid_number(phone_number: str) -> bool: # Added type hint
    """
    action:   Validate a user-supplied phone number string.

    input:    phone_number (str) - the phone number entered by the user.
    output:   Prints an error message if the number is invalid.
    return:   bool - True if valid, False otherwise.
    """
    mapping = phone_keypad_mapping()

    # Check length and make sure all digits are within 2–9
    if len(phone_number) == 7 and all(d in mapping for d in phone_number):
        return True
    else:
        print("Please enter exactly 7 digits, using only 2-9.")
        return False

# -----------------------------
# Recursive generator
# -----------------------------
def generate_words(num_str: str, word: str = "") -> Generator[str, None, None]: # Added type hint
    """
    action:   Recursively generate all possible words from a digit string.

    input:    num_str (str) - digits still to convert.
              word (str) - partial word built so far.
    output:   None
    return:   generator[str] - yield completes words one by one.
    """
    mapping = phone_keypad_mapping() 

    # If no more digits, yield the completed word
    # I saw generator expressions from the book would apply nicely to problems that
    # output a large number of results, so I used one here. I've been using recursion
    # in my Intro to Programming class from Online Harvard, and felt it would be beneficial to
    # combine both concepts to make the solution efficient. 
    if not num_str:
        yield word
    else:
        # Recursive step to yield all combinations by appending each possible letter for current digit.
        for letter in mapping[num_str[0]]:
            yield from generate_words(num_str[1:], word + letter)

# -----------------------------
# Script entry point
# -----------------------------
if __name__ == "__main__":
    phone_number = input('Enter a 7-digit phone number (digits 2-9 only): ')
    if valid_number(phone_number):
        combos = list(generate_words(phone_number))
        # Above code is unchanged from original assignment.
        
        # In original assignment that I turned it for Module 4, I had file_path 
        # defined at the very top of the script, tried it here and it worked fine, 
        # looks more uniform and not out of place.
        file_path = "output_words.txt"  # Defined output file path

        # Try block to perform file writing by appending to the file
        try:
            
            # I choose to append to the .txt file instead of overwriting it, as I felt
            # it would be more useful to keep previous results to see script works.
            with open(file=file_path, mode="a") as file:
                
                # Write a header for the new batch of results
                file.write(f"Results for {phone_number}:\n")
                
                # For loop to write each generated word to the file
                for word in combos:
                    file.write(f"{word}\n")
            print(f"All words written to '{file_path}'.")
            # Exception used instead of just TypeError to catch any file 
            # operation errors I couldn't think of.
        except Exception as e:
            print(f"Error writing to file: {e}")
