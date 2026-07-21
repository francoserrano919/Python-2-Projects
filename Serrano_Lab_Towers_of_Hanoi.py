"""
script: Serrano_Lab_Towers_of_Hanoi.py
action:
    a. Solves the Towers of Hanoi problem recursively
    b. Prints each move from source peg to destination peg
    c. Uses four parameters: number of disks, source peg, destination peg, temporary peg
author: Franco Xavier Serrano
date: 10/28/2025
"""

# Recursive function to solve Towers of Hanoi
def hanoi(num_disks: int, source: int, destination: int, temporary: int) -> None:
    """
    Recursively solve the Towers of Hanoi problem.

    action: Print each move from source to destination
    input: num_disks (int), source (int), destination (int), temporary (int)
    output: Prints each disk move in the format "source → destination"
    return: None
    """
    # Base case: move one disk directly
    if num_disks == 1:
        print(f"{source} → {destination}")
        return

    # Step 1: move n-1 disks from source to temporary using destination as helper
    hanoi(num_disks - 1, source, temporary, destination)

    # Step 2: move the largest disk from source to destination
    print(f"{source} → {destination}")

    # Step 3: move n-1 disks from temporary to destination using source as helper
    hanoi(num_disks - 1, temporary, destination, source)

# Main function
def main() -> None:
    """
    Prompt user for number of disks and solve the Towers of Hanoi puzzle.

    action: Prompt user and display solution
    input: User enters number of disks (int)
    output: Prints the sequence of moves
    return: None
    """
    print("Franco Xavier Serrano\n")
    print("Towers of Hanoi Recursive Solution\n")

    # Prompt user for number of disks
    try:
        num_disks = int(input("Enter the number of disks: "))
        if num_disks < 1:
            print("Number of disks must be at least 1.")
            return

        # Display moves
        print("\nSequence of moves:\n")
        hanoi(num_disks, 1, 3, 2)

        # Display total number of moves after completion
        total_moves = 2 ** num_disks - 1
        print(f"\nTotal moves: {total_moves}")

    except ValueError:
        print("Invalid input. Please enter an integer.")


# Run program
if __name__ == "__main__":
    main()
