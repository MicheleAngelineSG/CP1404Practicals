"""
CP1404/CP5632 - Practical
Fixed program to determine score status
"""

# Get score from user input
score = float(input("Enter score: "))

# Check if the score is valid (between 0 and 100 inclusive)
if 0 <= score <= 100:
    # Determine the score status based on the score range
    if score >= 90:
        print("Excellent")
    elif score >= 50:
        print("Passable")
    else:
        print("Bad")
else:
    # If the score is invalid, print an error message
    print("Invalid score")
