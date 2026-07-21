'''
script: Serrano_Assignment_Class_Average_P1.py
action: a. Reads input grades from the user.
        b. Appends each grade to a list.
        c. Writes the list of grades to a text file named output_grades.txt.
author: Franco Xavier Serrano
date: 09/23/2025
'''
"""Class average program with sentinel-controlled iteration."""

# initialization phase with variables to run the script
total = 0  # sum of grades
grade_counter = 0  # number of grades entered
grades_list = []  # list to store each grade

# processing phase, gets input from the user
grade = int(input('Enter grade, -1 to end: '))  # get one grade

# Loop to continue getting grades until sentinel value (-1) is entered
while grade != -1:
    total += grade
    grade_counter += 1
    grades_list.append(grade)  # 'Save' each grade
    grade = int(input('Enter grade, -1 to end: '))

# Save each grade into output_grades.txt
file_path = "output_grades.txt"

# Try-except block to handle potential file operation errors
try:

    # Open the file in append mode
    with open(file=file_path, mode="a") as file:
        # For loop to write each grade from the list to the file
        for grade in grades_list:
            file.write(f"{grade}\n")  # Write each grade on a new line
        print(f"txt file '{file_path}' was created.")
# Ran into a TypeError when trying to add user input as an integer.
# I created the above for loop to ensure each grade is written as a string.
# I also added a newline character to ensure each grade is on its own line.
except TypeError:
    print("You need a string, not an integer argument")

## Use this code for the part 2 of the assingnment
# termination phase
if grade_counter != 0:
    average = total / grade_counter
    print(f'Class average is {average:.2f}')
else:
    print('No grades were entered') 