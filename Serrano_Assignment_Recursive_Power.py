"""
script: Serrano_Assignment_Recursive_Power.py
action: 
    a. Implements a recursive function to compute powers of a base integer
    b. Prompts user for base and exponent, ensuring exponent >= 1
    c. Prints powers from base^exponent down to base^1j
Author: Franco Xavier Serrano
Date: 10/21/2025
"""
def power(base: int, exponent: int) -> int:
    """
    Return base ** exponent using recursion. Assumes exponent >= 1.
    input: base (int), exponent (int >= 1)
    output: base raised to exponent (int)
    return: int
    """
    if exponent == 1:
        return base
    return base * power(base, exponent - 1)


def main() -> None:
    """
    Prompt for base and exponent, then print each power in descending order.
    input: none
    output: prints base^exponent down to base^1
    return: none
    """

    # Try-except block to handle invalid input
    try:
        base = int(input("Enter the base (integer): "))
        exponent = int(input("Enter the exponent (integer >= 1): "))
        if exponent < 1:
            raise ValueError("Exponent must be >= 1.")
    except ValueError as e:
        print(f"Invalid input: {e}")
        return
    
    # Print powers from base^exponent down to base^1
    print(f"Powers of {base} in descending order:")
    for exp in range(exponent, 0, -1):
        print(f"{base}^{exp} = {power(base, exp)}")

# Run the main function
if __name__ == "__main__":
    main()