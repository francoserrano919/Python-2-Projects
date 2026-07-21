"""
This was relatively easy to do, the lab mimicks a code review we had over the summer.
script: Serrano_Lab_Guess_The_Number.py
action: a. Reads input from the user
         b. Compares input to a randomly generated number
         c. Provides feedback to the user
         d. Loops until the user guesses the number or exceeds max attempts
         e. Offers to play again after the game ends
author: Franco Serrano
date: 09/09/2025
"""
# Much of this code was taken from a code review we had over the summer.
import random

def play_game():
    """
    Main game loop for the guessing game.
    action: a. Reads input from the user
    input: integer guesses from the user
    output: feedback on guesses, number of attempts, and option to play again
    return: guess result and attempts
    """
    attempts = 0
    secret_number = random.randint(1, 1000) # Random number between 1 and 1000
    print("Guess my number between 1 and 1000 with the fewest guesses:")

    while True: # Chose a boolean loop to continue until the user guesses correctly or exceeds attempts
        try:
            guess = int(input("Your guess: "))
            attempts += 1

            if guess < secret_number:
                print("Too low. Try again.") 
            elif guess > secret_number:
                print("Too high. Try again.")
            else: # Was about to say elif guess == secret_number, but else is sufficient here
                print("Congratulations. You guessed the number!")
                if attempts <= 10: # 10 attempts to match lab instructions.
                    print("Either you know the secret or you got lucky!")
                else:
                    print("You should be able to do better!")
                print(f"You guessed {attempts} times.")
                break
        except ValueError: # Handles non-integer inputs
            print("Invalid input, please enter a numeric number.")
# Added two functions, main and play_game, to modularize the code.
def main():
    """
    Main function to start the guessing game.

    Action: Starts the game loop and handles replay logic.
    input: User's choice to play again or not
    output: Starts a new game or exits
    return: This returns None
    """
    while True: # Used another boolean loop to allow replaying the game
        play_game()
        again = input("Play again? (y/n): ").strip().lower() # Normalize input.
        if again != 'y':
            print("Thanks for playing!")
            break

main()
