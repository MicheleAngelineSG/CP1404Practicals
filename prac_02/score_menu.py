"""
FUNCTION get_valid_score()
    WHILE True:
        TRY:
            PROMPT user to enter a score
            READ score from user
            IF score < 0 OR score > 100 THEN
                DISPLAY "Invalid score. Please enter a score between 0 and 100."
            ELSE
                RETURN score
        EXCEPT ValueError:
            DISPLAY "Invalid input. Please enter a valid integer."

FUNCTION print_result(score)
    CALL determine_grade function from score module with score as parameter
    DISPLAY result

FUNCTION show_stars(score)
    DISPLAY '*' repeated for the length of score

FUNCTION main_menu()
    DISPLAY "MAIN MENU"
    DISPLAY "(G)et a valid score"
    DISPLAY "(P)rint result"
    DISPLAY "(S)how stars"
    DISPLAY "(Q)uit"

FUNCTION main()
    SET user_score to None
    WHILE True:
        CALL main_menu()
        PROMPT user to enter choice
        READ choice from user
        IF choice EQUALS 'G' THEN
            SET user_score to get_valid_score()
        ELSE IF choice EQUALS 'P' THEN
            IF user_score is not None THEN
                CALL print_result function with user_score as parameter
            ELSE
                DISPLAY "Please enter a valid score first."
        ELSE IF choice EQUALS 'S' THEN
            IF user_score is not None THEN
                CALL show_stars function with user_score as parameter
            ELSE
                DISPLAY "Please enter a valid score first."
        ELSE IF choice EQUALS 'Q' THEN
            DISPLAY "Goodbye!"
            BREAK
        ELSE
            DISPLAY "Invalid choice. Please choose from the menu."

IF __name__ EQUALS "__main__" THEN
    CALL main()
"""
import score

def get_valid_score():
    while True:
        try:
            score = int(input("Enter a score (0-100): "))
            if score < 0 or score > 100:
                print("Invalid score. Please enter a score between 0 and 100.")
            else:
                return score
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def print_result(score):
    result = score.determine_grade(score)
    print("Result:", result)

def show_stars(score):
    print("*" * score)

def main_menu():
    print("\nMAIN MENU")
    print("(G)et a valid score")
    print("(P)rint result")
    print("(S)how stars")
    print("(Q)uit")

def main():
    user_score = None
    while True:
        main_menu()
        choice = input("Enter your choice: ").upper()
        if choice == 'G':
            user_score = get_valid_score()
        elif choice == 'P':
            if user_score is not None:
                print_result(user_score)
            else:
                print("Please enter a valid score first.")
        elif choice == 'S':
            if user_score is not None:
                show_stars(user_score)
            else:
                print("Please enter a valid score first.")
        elif choice == 'Q':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose from the menu.")

if __name__ == "__main__":
    main()
