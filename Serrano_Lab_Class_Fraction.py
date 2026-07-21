'''
Demonstrates the use of the Fraction class from the fractions module 
and basic operations with complex numbers.
action: a. Adding two fractions
        b. Subtracting two fractions
        c. Multiplying two fractions
        d. Dividing two fractions
        e. Displaying numerator and denominator of each fraction
        f. Converting fractions to float
        Part 2: Complex numbers
        a. Adding two complex numbers
        b. Subtracting two complex numbers
        c. Printing complex numbers
        d. Displaying real and imaginary parts of complex numbers
author: Franco Xavier Serrano
date: 10/07/2025
'''
from fractions import Fraction

# Function to print a separator line
def sep(width: int = 60) -> None:
    print("=" * width)

def demo_fraction():
    '''
    Demonstrates the use of the Fraction class from the fractions module
    and basic operations with complex numbers.
    action: output to user demonstrations of Fraction class and complex numbers
    input: none
    output: demonstration of Fraction class and complex numbers
    return: none
    '''

    # Variables for fractions section
    fraction_1 = Fraction(1, 3)
    fraction_2 = Fraction(3, 5)

    # Fractions section
    sep()
    addition = fraction_1 + fraction_2
    print("Sum =", addition)
    sep()
    subtraction = fraction_2 - fraction_1
    print("Subtraction =", subtraction)
    sep()
    print("Product =", fraction_1 * fraction_2)
    sep()
    print("Quotient =", fraction_1 / fraction_2)
    sep()
    print(f"Fraction 1: {fraction_1.numerator}/{fraction_1.denominator}")
    print(f"Fraction 2: {fraction_2.numerator}/{fraction_2.denominator}")
    sep()
    print("Float value of Fraction 1:", float(fraction_1))
    print("Float value of Fraction 2:", float(fraction_2))
    sep()


def demo_complex_numbers():
    '''
    Demonstrates basic operations with complex numbers.
    action: output to user demonstrations of how complex numbers work
    input: none
    output: demonstration of complex number capabilities
    return: none
    '''
    comp_1 = complex(2, 3)
    comp_2 = complex(1, 4)

    print("Difference:", comp_1 - comp_2)
    sep()
    print("Complex numbers 1 =", comp_1)
    print("Complex numbers 2 =", comp_2)
    sep()
    # Display real and imaginary parts of complex numbers
    print(f"Real part of complex numbers 1 and 2 = {comp_1.real}, {comp_2.real}")
    print(f"Imaginary part of complex numbers 1 and 2 = {comp_1.imag}, {comp_2.imag}")
    sep()

# Allows the script to be run standalone
if __name__ == "__main__":
    demo_fraction()
    demo_complex_numbers()