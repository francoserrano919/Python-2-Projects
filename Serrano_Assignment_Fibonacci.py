"""
script: Serrano_Assignment_Recursive_Fibonacci.py
action: 
    a. Implements a recursive function to compute Fibonacci numbers
    b. Tracks and displays the number of function calls made during computation
    c. Demonstrates the function for Fibonacci(10), Fibonacci(20), and Fibonacci(30)
Author: Franco Xavier Serrano
Date: 10/21/2025
"""

# Global variable to count function calls
call_count = 0

def fibonacci(n: int):
    '''
    Return the nth Fibonacci number using recursion.
    Also increments global call_count for each call.
    action: compute Fibonacci number and count calls
    input: n (int)
    output: nth Fibonacci number (int)
    return: int
    '''
    # Use the global call_count variable
    global call_count
    call_count += 1
    # If loop reaches base case, return n
    if n in (0, 1):
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def show_fib_and_calls(n: int):
    '''
    Show Fibonacci number and call count for a given n.
    action: print Fibonacci(n) and number of calls made
    input: n (int)
    output: printed Fibonacci number and call count
    return: none
    '''
    # Reset call count before computation
    global call_count
    call_count = 0
    result = fibonacci(n)
    print(f"Fibonacci({n}) = {result} (calls: {call_count})\n")


def main():
    """
    Main function to demonstrate Fibonacci with call tracking.
    action: demonstrate Fibonacci function and call counting
    input: none
    output: printed Fibonacci numbers and call counts
    return: none
    """

    # For loop to show Fibonacci and call counts for 10, 20, 30
    for n in [10, 20, 30]:
        show_fib_and_calls(n)


if __name__ == "__main__":
    main()
