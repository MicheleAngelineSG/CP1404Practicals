"""
while True:
    # Get sales amount from the user
    prompt user for sales amount
    get sales from user input

    # Check if the sales amount is negative, if so, exit the loop
    if sales < 0:
        break

    # Calculate the bonus based on the sales amount
    if sales < 1000:
        bonus = sales * 0.10  # 10% bonus for sales under $1,000
    else:
        bonus = sales * 0.15  # 15% bonus for sales $1,000 or over

    # Print the bonus amount
    print bonus

# Print a message to thank the user for using the program
print "Thank you."
"""
while True:
    sales = float(input("Enter sales: $"))
    if sales < 0:
        break
    elif sales < 1000:
        bonus = sales * 0.10
    else:
        bonus = sales * 0.15
    print(f"Bonus: ${bonus:.2f}")

print("Thank you.")
