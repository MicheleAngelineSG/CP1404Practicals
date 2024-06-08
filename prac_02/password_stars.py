"""
FUNCTION get_password(min_length)
    WHILE True:
        PROMPT user to enter a password
        READ password from user
        IF length of password < min_length THEN
            DISPLAY "Password must be at least min_length characters long."
        ELSE
            RETURN password

FUNCTION print_asterisks(password)
    DISPLAY '*' repeated for the length of password

FUNCTION main()
    SET min_length to 8
    CALL get_password(min_length)
    CALL print_asterisks(password)

IF __name__ EQUALS "__main__" THEN
    CALL main()

"""
def get_password(min_length):
    while True:
        password = input("Enter a password: ")
        if len(password) < min_length:
            print(f"Password must be at least {min_length} characters long.")
        else:
            return password

def print_asterisks(password):
    print('*' * len(password))

def main():
    min_length = 8  # Minimum length for the password
    password = get_password(min_length)
    print_asterisks(password)

if __name__ == "__main__":
    main()
