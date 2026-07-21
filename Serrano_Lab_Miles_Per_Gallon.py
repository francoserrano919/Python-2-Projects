# Calculate your miles per gallon!
def calculate_mpg():    # Function to calculate miles per gallon
    # Originally had parameters for total_miles and total_gallons, but
    # they are not needed as they are initialized within the function.
    print("Welcome to the Miles Per Gallon Calculator!")
    print("------------")
    total_miles = 0.0
    total_gallons = 0.0 # Values initialized to zero for accumulation when 
    # user eventually ends the program.

    while True: # Simple boolean loop to keep program running until user ends it.
        try:    # Try-except block to catch non-numeric inputs, including
            # empty inputs.
            gallons_filled = float(input("Enter the gallons used (-1 to end): "))
            print("------------")
            if gallons_filled == -1:
                break
            if gallons_filled <= 0:
                print("Gallons must be greater than 0.")
                continue
# Spaces for readability.
            miles_driven = float(input("Enter the miles driven on current tank: "))
            print("------------")   # Added these lines for readability of output.
            if miles_driven < 0:
                print("Miles driven must be greater than or equal to 0.")
                continue

            mpg_this_tank = miles_driven / gallons_filled # Calculation of mpg for current tank.
            print(f"The miles/gallon for this tank was {mpg_this_tank:.6f}.\n")
            
            total_miles += miles_driven # Here is where the totals are accumulated.
            total_gallons += gallons_filled

        except ValueError:
            print("Invalid input, please enter numeric values.")
    if total_gallons > 0:   # To avoid division by zero error.
        overall_mpg = total_miles / total_gallons # Calculation of overall mpg.
        print(f"The overall average miles/gallon was {overall_mpg:.6f}.") # Originally had
        # round() function, but formatted string literals are more closer to the
        # example output you gave. 
    
    print("Thank you for using the Miles Per Gallon Calculator. Goodbye!")
calculate_mpg() # Call the function to run the program.



