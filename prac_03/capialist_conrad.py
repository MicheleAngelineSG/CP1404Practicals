"""
BEGIN
    IMPORT random module

    # Define constants for the simulation
    SET MAX_INCREASE to 0.175  # 17.5%
    SET MAX_DECREASE to 0.05   # 5%
    SET MIN_PRICE to 1.0
    SET MAX_PRICE to 100.0
    SET INITIAL_PRICE to 10.0
    SET FILENAME to "capitalist_conrad_output.txt"

    # Initialize variables
    SET price to INITIAL_PRICE
    SET number_of_days to 0

    # Open the output file for writing
    OPEN file FILENAME for writing as out_file

    # Write the starting price to the file
    WRITE "Starting price: $price" to out_file

    # Start simulation loop
    WHILE price is greater than or equal to MIN_PRICE AND price is less than or equal to MAX_PRICE DO
        SET price_change to 0

        # Determine if the price increases or decreases
        SET random_choice to random.randint(1, 2)
        IF random_choice is equal to 1 THEN
            # Generate a random increase
            SET price_change to random.uniform(0, MAX_INCREASE)
            SET price to price * (1 + price_change)
        ELSE
            # Generate a random decrease
            SET price_change to random.uniform(0, MAX_DECREASE)
            SET price to price * (1 - price_change)
        END IF

        # Increment the number of days
        INCREMENT number_of_days by 1

        # Write the price for the current day to the file
        WRITE "On day number_of_days price is: $price" to out_file
    END WHILE

    # Close the output file
    CLOSE out_file
END
"""


import random

# Constants for the simulation
MAX_INCREASE = 0.175  # 17.5%
MAX_DECREASE = 0.05   # 5%
MIN_PRICE = 1.0
MAX_PRICE = 100.0
INITIAL_PRICE = 10.0
FILENAME = "capitalist_conrad_output.txt"

# Initialize variables
price = INITIAL_PRICE
number_of_days = 0

# Open the file for writing
out_file = open(FILENAME, 'w')

# Write the starting price to the file
print(f"Starting price: ${price:,.2f}", file=out_file)

# Simulation loop
while MIN_PRICE <= price <= MAX_PRICE:
    price_change = 0

    # Determine if the price increases or decreases
    if random.randint(1, 2) == 1:
        # Generate a random increase
        price_change = random.uniform(0, MAX_INCREASE)
        price *= (1 + price_change)
    else:
        # Generate a random decrease
        price_change = random.uniform(0, MAX_DECREASE)
        price *= (1 - price_change)

    number_of_days += 1
    # Write the price for the current day to the file
    print(f"On day {number_of_days} price is: ${price:,.2f}", file=out_file)

# Close the file at the end
out_file.close()
