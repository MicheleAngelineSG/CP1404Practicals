numbers = [3, 1, 4, 1, 5, 9, 2]
# 1. What is the value of numbers[0]?
# Answer: 3
# 2. What is the value of numbers[-1]?
# Answer: 2
# 3. What is the value of numbers[3]?
# Answer: 1
# 4. What is the value of numbers[:-1]?
# Answer: [3, 1, 4, 1, 5, 9]
# 5. What is the value of numbers[3:4]?
# Answer: [1]
# 6. What is the value of 5 in numbers?
# Answer: True
# 7. What is the value of 7 in numbers?
# Answer: False
# 8. What is the value of "3" in numbers?
# Answer: False
# 9. What is the value of numbers + [6, 5, 3]?
# Answer: [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]


# 1. Change the first element of numbers to "ten" (the string, not the number 10)
numbers[0] = "ten"

# 2. Change the last element of numbers to 1
numbers[-1] = 1

# 3. Print all the elements from numbers except the first two (slice)
print(numbers[2:])

# 4. Print whether 9 is an element of numbers
print(9 in numbers)