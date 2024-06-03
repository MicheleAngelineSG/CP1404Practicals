"""
function calculate_total_price(num_items, prices)
    total_price = sum(prices)
    if total_price > 100 then
        total_price *= 0.9  // Apply 10% discount
    return total_price

function main()
    num_items = -1  // Initialize num_items to an invalid value
    while num_items < 0 do
        try
            num_items = input("Number of items: ")
            if num_items < 0 then
                print("Invalid number of items!")
        except ValueError
            print("Invalid input! Please enter a valid number.")

    prices = []
    for i = 1 to num_items do
        repeat
            try
                price = input("Price of item {}: ".format(i))
                if price <= 0 then
                    print("Price must be greater than zero.")
                else
                    prices.append(price)
                    exit repeat
            except ValueError
                print("Invalid input! Please enter a valid price.")

    total_price = calculate_total_price(num_items, prices)
    print("Total price for {} items is ${:.2f}".format(num_items, total_price))

if __name__ == "__main__" then
    main()
"""
def calculate_total_price(num_items, prices):
    total_price = sum(prices)
    if total_price > 100:
        total_price *= 0.9  # Apply 10% discount
    return total_price

def main():
    num_items = -1  # Initialize num_items to an invalid value
    while num_items < 0:
        try:
            num_items = int(input("Number of items: "))
            if num_items < 0:
                print("Invalid number of items!")
        except ValueError:
            print("Invalid input! Please enter a valid number.")

    prices = []
    for i in range(num_items):
        while True:
            try:
                price = float(input("Price of item {}: ".format(i+1)))
                if price <= 0:
                    print("Price must be greater than zero.")
                else:
                    prices.append(price)
                    break
            except ValueError:
                print("Invalid input! Please enter a valid price.")

    total_price = calculate_total_price(num_items, prices)
    print("Total price for {} items is ${:.2f}".format(num_items, total_price))

if __name__ == "__main__":
    main()
