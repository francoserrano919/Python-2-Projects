"""
script: Serrano_Assingment_DATETIME.pyy
action: a. Get the current date and time and store it in variable x. 
        b. Repeat Part (a) and store the result in variable y. 
        c. Display each datetime object. 
        d. Display each datetime object’s data attributes individually. 
        e. Use the comparison operators to compare the two datetime objects. 
        f. Calculate the difference between y and x.
author: Franco Xavier Serrano
date: 10/07/2025
"""
from datetime import datetime

def main():
    '''
    Demonstrates datetime capabilities in 5 different ways
    action: output to user demonstrations of how datetime works
    input: none
    output: demonstration of datetime capabilities
    return: none
    '''    
    # Get current date and time, store in x and y
    x = datetime.now()
    y = datetime.now()
    
    # Separation line
    print("\n" + "=" * 60)

    # Print x and y respectively
    print("x =", x)
    print("y =", y)

    print("\n" + "=" * 60)

    # Print individual attributes of x and y
    print("x:", x.year, x.month, x.day, x.hour, x.minute, x.second)
    print("y:", y.year, y.month, y.day, y.hour, y.minute, y.second)

    print("\n" + "=" * 60)

    # Compare x and y using comparison operators
    print("x == y:", x == y)
    print("x < y:", x < y) # Will always be true as x is created before y.
    print("x > y:", x > y) # Will always be false as x is created before y.

    print("\n" + "=" * 60)

    # Calculate and display the difference between y and x
    difference = y - x
    print("Difference:", difference) 

    print("\n" + "=" * 60)

# Allows the script to be run standalone
if __name__ == '__main__':
    main()
