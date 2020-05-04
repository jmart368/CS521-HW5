"""
Name: Jose Martinez
Class: CS 521 - 2020 Spring 1
Date: February 22, 2020
Homework Problem # 15.1
Description: Sum the digits of an integer using recursion
"""


def sum_digits(n):
    """
    Function where the elements of the digits are added
    """
    # create a list for the elements within the integer
    number_list = [digit for digit in str(n)]
    # begin the index at 0
    index = 0
    # return the elements of the list in recrusive from as an integer
    return int(number_list[index]) + recursive_output(n, index)


def recursive_output(n, index):
    """
    Function to determine the recursive output
    """
    index += 1
    number_list = [digit for digit in str(n)]
    # loop the index to determine which elements will be summed up
    if index == len(number_list) - 1:
        return int(number_list[index])
    else:
        return int(number_list[index]) + recursive_output(n, index)


while True:
    try:
        # Prompts user for integer using the absolute value to check negatives
        user_input = abs(int(input('Enter an integer as a whole number: ')
                             .strip()))
        break

    # Capture user excpetions
    except ValueError:
        print('Not a valid input. Please enter an integer as 12345 etc.')
        continue

print(sum_digits(user_input))
