# Target Heart Rate Calculator
# This program calculates the target heart rate range for a user based on their age.
heart_rate = 220
age = int(input("Please enter your age: "))
max_heart_rate = 220 - age
upper_limit = round(max_heart_rate * 0.85) # Thought of truncating but rounding seems more appropriate
lower_limit = round(max_heart_rate * 0.5)
print(
    f"Your maximum heart rate for being {age} should be {max_heart_rate}.\n"
    f"Your target heart rate is between {lower_limit} and {upper_limit} bpm."
)   # Instead of printing with two print statements, I used one with a newline character.