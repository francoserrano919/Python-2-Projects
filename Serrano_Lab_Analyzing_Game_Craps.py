"""
script:   Serrano_Lab_Analyzing_Game_Craps.py
action:   Modify the book script from Fig 4.2 to simulate 1,000,000 games of craps. Track wins/losses by
          the number of rolls when each game is resolved, then print overall and
          per-roll percentages with a cumulative column.
author:   Franco Xavier Serrano
date:     09/16/2025
"""

# Simulating the dice game Craps

import random

# Variables for simulation parameters
games_to_play = 1_000_000
last_bucket = 25

# Kept unchanged from Fig 4.2
def roll_dice():
    # Roll two dice and return their face values as a tuple
    die1 = random.randrange(1, 7)
    die2 = random.randrange(1, 7)
    return (die1, die2)  # pack die face values into a tuple

# Everything below here is code modified from original Fig 4.2
def play_one_game():
    """
    action: Function to play one game of craps with no print statements.

    input:  None
    output: None
    return: True if player wins, False if player loses, and number of rolls taken.
    """
    # First roll of the game
    rolls = 1
    die_values = roll_dice()
    sum_of_dice = sum(die_values)

    # Immediate resolution on the come-out roll
    if sum_of_dice in (7, 11):      # win immediately
        return True, rolls
    elif sum_of_dice in (2, 3, 12): # lose immediately
        return False, rolls

    # Otherwise, establish point and keep rolling until point (win) or 7 (loss)
    my_point = sum_of_dice

    # Keep rolling until the game resolves
    while True:
        rolls += 1
        die_values = roll_dice()
        sum_of_dice = sum(die_values)

        if sum_of_dice == my_point:  # win by making point
            return True, rolls
        elif sum_of_dice == 7:       # lose by rolling 7 before the point
            return False, rolls

def percent(count: int, total: int) -> float:
    """
    action: Convert a count to a percentage of a total

    input:  count (int) - the portion you're measuring (wins on a roll)
            total (int) - the overall quantity (total games)
    output: None
    return: Percentage as a float 0.0 to 100.0
    """
    return (count / total * 100.0) if total else 0.0
# Will prevent division by zero


def main():
    """
    action: Run one million games of craps, tallying wins/losses by roll count.

    input:  None
    output: Prints overall win/loss percentages and a per-roll resolution table.
    return: None
    """
    
    wins = {}    # Empty dictionaries to hold counts of wins/losses by roll count
    losses = {}

    # Loop to play the one million games
    for _ in range(games_to_play):
        won, rolls = play_one_game()

       # Use last_bucket for any roll count exceeding it like in example output
        key = rolls if rolls < last_bucket else last_bucket
        # Update the appropriate dictionary based on win/loss
        if won:
            wins[key] = wins.get(key, 0) + 1
        else:
            losses[key] = losses.get(key, 0) + 1

    # Compute and print overall win/loss percentages

    total_wins = sum(wins.values())
    total_losses = sum(losses.values())
    total_games = total_wins + total_losses

    print(f"Percentage of wins: {percent(total_wins, total_games):.1f}%\n")
    print(f"Percentage of losses: {percent(total_losses, total_games):.1f}%\n")

    # Build and print the per-roll resolution table
    print("Percentage of wins/losses based on total number of rolls\n")
    print("% Resolved        Cumulative %")
    print("Rolls   on this roll   of games resolved")

    cumulative = 0.0 # Variable to track cumulative percentage

    # Print rows 1..(last_bucket-1), then a final 'last_bucket' row
    for roll in list(range(1, last_bucket)) + [last_bucket]:
        resolved_this_roll = wins.get(roll, 0) + losses.get(roll, 0)
        pct_this = percent(resolved_this_roll, total_games)
        cumulative += pct_this

        label = f"{roll}" 
        # Rolls >= last_bucket are grouped into the last row.
        # Format columns with alignment like example output
        print(f"{label:<6}   {pct_this:8.2f}%          {cumulative:8.2f}%")

# Main script entry point
if __name__ == "__main__":
    main()


