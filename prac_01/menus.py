"""
function display_menu()
    print("(H)ello")
    print("(G)oodbye")
    print("(Q)uit")

function get_choice()
    choice = input(">>> ").upper()
    return choice

function say_hello(name)
    print("Hello", name)

function say_goodbye(name)
    print("Goodbye", name)

function main()
    name = input("Enter name: ")
    choice = ""

    while choice != "Q" do
        display_menu()
        choice = get_choice()

        if choice == "H" then
            say_hello(name)
        else if choice == "G" then
            say_goodbye(name)
        else
            print("Invalid choice")

    print("Finished.")

if __name__ == "__main__" then
    main()
"""
def display_menu():
    print("(H)ello")
    print("(G)oodbye")
    print("(Q)uit")

def get_choice():
    choice = input(">>> ").upper()
    return choice

def say_hello(name):
    print("Hello", name)

def say_goodbye(name):
    print("Goodbye", name)

def main():
    name = input("Enter name: ")
    choice = ""

    while choice != "Q":
        display_menu()
        choice = get_choice()

        if choice == "H":
            say_hello(name)
        elif choice == "G":
            say_goodbye(name)
        else:
            print("Invalid choice")

    print("Finished.")

if __name__ == "__main__":
    main()

