"""
# Constants
START = 0
END = 100
STEP = 10

function count_in_tens():
    for i in range(START, END + 1, STEP):
        print i, end=' '
    print()

function count_down():
    start = 20
    end = 0
    step = -1
    for i in range(start, end, step):
        print i, end=' '
    print()

function print_stars():
    n = input("Number of stars: ")
    for _ in range(n):
        print '*', end=''
    print()

function print_increasing_stars():
    n = input("Number of stars: ")
    for i in range(1, n + 1):
        print '*' * i

function main():
    display "a. Count in 10s from 0 to 100:"
    call count_in_tens

    display "b. Count down from 20 to 1:"
    call count_down

    display "c. Print n stars:"
    call print_stars

    display "d. Print n lines of increasing stars:"
    call print_increasing_stars

call main
"""
# Constants
START = 0
END = 100
STEP = 10


def count_in_tens():
    for i in range(START, END + 1, STEP):
        print(i, end=' ')
    print()


def count_down():
    start = 20
    end = 0
    step = -1
    for i in range(start, end, step):
        print(i, end=' ')
    print()


def print_stars():
    n = int(input("Number of stars: "))
    for _ in range(n):
        print('*', end='')
    print()


def print_increasing_stars():
    n = int(input("Number of stars: "))
    for i in range(1, n + 1):
        print('*' * i)


def main():
    print("a. Count in 10s from 0 to 100:")
    count_in_tens()

    print("b. Count down from 20 to 1:")
    count_down()

    print("c. Print n stars:")
    print_stars()

    print("d. Print n lines of increasing stars:")
    print_increasing_stars()


main()
