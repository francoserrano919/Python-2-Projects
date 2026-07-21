"""
script:   Serrano_Lab_Telephone_Number_Word_Generator.py
action:   Generate all possible letter combinations (words) for a 7-digit 
          phone number using a digit-to-letter mapping similar to old phone keypads.
author:   Franco Xavier Serrano
date:     09/16/2025
"""

# Digit-to-letter mapping

# I took advantage of the liberty you gave us in this class to use concepts from other
# classes I'm taking. I felt recursion and generator expressions would be a good fit,
# as well as other cool formatting ideas that you'll see below.

# Dictionary mapping digits to letters
def phone_keypad_mapping():
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
def valid_number(phone_number: str) -> bool:
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
def generate_words(num_str: str, word: str = ""):
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
# Printing helper
# -----------------------------
def print_in_blocks(words, per_line: int = 20, pause_every: int = 200):
    """
    action:   Print generated words in neat blocks for readability.

    input:    words (iterable[str]) - words to display.
              per_line (int) - number of words per printed line.
              pause_every (int) - pause after printing this many words.
    output:   Prints words in a formatted block style.
    return:   None
    """
    count = 0

    # Iterate through generated words and format nicely.
    # Took inspiration from one of my C coding problems where I had to print "mario" blocks
    # into blocks like shown below. I didn't like how the output was just a wall of text.
    # Had to go online to help refine the pausing logic as I knew what i wanted to do, but couldn't
    # figure out the right syntax.
    for word in words:
        print(word, end=' ')
        count += 1

        # Break line after per_line words
        if count % per_line == 0:
            print()

        # Pause after pause_every words
        if count % pause_every == 0:
            input("Press Enter to continue...")


# -----------------------------
# Script entry point
# -----------------------------
if __name__ == "__main__":
    # Prompt user once for input
    phone_number = input('Enter a 7-digit phone number (digits 2-9 only): ')

    # Validate, then generate and print combinations
    if valid_number(phone_number):
        combos = generate_words(phone_number)
        print_in_blocks(combos)
