"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
   A ValueError will occur when the user inputs something that cannot be converted to an integer, such as a string or a float that is not formatted as an integer.
2. When will a ZeroDivisionError occur?
   A ZeroDivisionError will occur when the user inputs 0 as the denominator, since division by zero is undefined.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
   Yes, we can add a check to ensure the denominator is not zero before performing the division.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))

    # Check if the denominator is zero and handle it appropriately
    if denominator == 0:
        print("Cannot divide by zero!")
    else:
        fraction = numerator / denominator
        print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")
