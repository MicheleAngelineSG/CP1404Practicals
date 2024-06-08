"""
BEGIN
    # Question 1: Write user's name to a file
    INPUT "Enter your name" and assign it to name
    OPEN 'name.txt' in write mode as file
    WRITE name to the file
    CLOSE the file

    # Question 2: Read user's name from the file and print it
    OPEN 'name.txt' in read mode as file
    READ the name from the file
    PRINT "Hi" followed by the name

    # Question 3: Read and sum the first two numbers from numbers.txt
    OPEN 'numbers.txt' in read mode as file
    READ the first number from the file and assign it to number1
    READ the second number from the file and assign it to number2
    CALCULATE the total by adding number1 and number2
    PRINT the total

    # Question 4: Print the total for all lines in numbers.txt
    SET total to 0
    OPEN 'numbers.txt' in read mode as file
    FOR EACH line IN file
        CONVERT the line to an integer and add it to total
    END FOR
    PRINT the total
END
"""
# Write user's name to a file
name = input("Enter your name: ")
with open('name.txt', 'w') as file:
    file.write(name)

# Read user's name from the file and print it
with open('name.txt', 'r') as file:
    name = file.read()
print(f"Hi {name}!")

# Read and sum the first two numbers from numbers.txt
with open('numbers.txt', 'r') as file:
    number1 = int(file.readline())
    number2 = int(file.readline())
total = number1 + number2
print(f"The sum of the first two numbers is: {total}")

# Print the total for all lines in numbers.txt
total = 0
with open('numbers.txt', 'r') as file:
    for line in file:
        total += int(line)
print(f"The total for all numbers in numbers.txt is: {total}")
