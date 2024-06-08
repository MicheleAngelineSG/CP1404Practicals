"""
BEGIN
    IMPORT the random module

    PRINT "Random integer between 5 and 20:"
    SET random_integer TO random.randint(5, 20)
    PRINT random_integer

    PRINT "Random number between 3 and 9 with a step of 2:"
    SET random_step_number TO random.randrange(3, 10, 2)
    PRINT random_step_number

    PRINT "Random floating-point number between 2.5 and 5.5:"
    SET random_float TO random.uniform(2.5, 5.5)
    PRINT random_float

    PRINT "Random integer between 1 and 100:"
    SET random_number TO random.randint(1, 100)
    PRINT random_number
END
"""
import random
# Generate and print a random integer between 5 and 20 (inclusive)
print(random.randint(5, 20))  # Example output: 12
# Explanation for line 1:
# - The smallest possible number is 5.
# - The largest possible number is 20.

# Generate and print a random number from the range 3 to 9 with increments of 2
print(random.randrange(3, 10, 2))  # Example output: 7
# Explanation for line 2:
# - The smallest possible number is 3.
# - The largest possible number is 9.
# - Possible outcomes are 3, 5, 7, and 9.
# - The number 4 cannot appear since the step is 2.

# Generate and print a random floating-point number between 2.5 and 5.5
print(random.uniform(2.5, 5.5))  # Example output: 3.789
# Explanation for line 3:
# - The smallest possible number is 2.5.
# - The largest possible number is 5.5.

# Generate and print a random integer between 1 and 100 (inclusive)
print(random.randint(1, 100))  # Example output: 56
