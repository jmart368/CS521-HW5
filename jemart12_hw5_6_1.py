"""
Name: Jose Martinez
Class: CS 521 - 2020 Spring 1
Date: February 22, 2020
Homework Problem # 6.1
Description: Math - Pentagonal Numbers
"""


def get_pentagonal_number(n):
    """
    Returns a pentagonal number using the formula (n * (3 * n - 1)) / 2
    """
    pentagonal_number = (n * (3 * n - 1)) / 2
    return int(pentagonal_number)


def print_pentagonal_numbers(n):
    """
    Iterates through the numbers to display 10 numbers per line retrieving
    the 'n' value from the previous function whilke aligning the output in a
    10 * 10 grid
    """
    # displays 10 integers per line
    pentagonal_numbers_per_line = 10
    # count the number of pentagonal numbers
    count = 0
    # begin the count at 1
    number = 1

    # fine the pentagonal numbers
    while count < n:
        # print the numbers using a comma and aligning format
        print('{:>7,}\t' .format(get_pentagonal_number(number)), end="")
        # increase the count
        count += 1
        # increase the number
        number += 1
        if count % pentagonal_numbers_per_line == 0:
            # print the numbers to continue on the next line
            print()


if __name__ == "__main__":
    print('The first 100 integers of pentagonal numbers are: ')
    # retreive from the print_pentagonal_numbers(n) where n = 100
    print_pentagonal_numbers(100)
