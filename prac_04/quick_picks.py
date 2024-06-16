import random

# Constants
MIN_NUMBER = 1
MAX_NUMBER = 45
NUMBERS_PER_PICK = 6


def main():
    number_of_picks = int(input("How many quick picks? "))

    for _ in range(number_of_picks):
        quick_pick = generate_quick_pick()
        quick_pick.sort()
        print_formatted_quick_pick(quick_pick)


def generate_quick_pick():
    """Generate a single quick pick with unique random numbers."""
    quick_pick = []
    while len(quick_pick) < NUMBERS_PER_PICK:
        number = random.randint(MIN_NUMBER, MAX_NUMBER)
        if number not in quick_pick:
            quick_pick.append(number)
    return quick_pick


def print_formatted_quick_pick(quick_pick):
    """Print the quick pick numbers in a formatted way."""
    print(" ".join(f"{number:2}" for number in quick_pick))


if __name__ == "__main__":
    main()
