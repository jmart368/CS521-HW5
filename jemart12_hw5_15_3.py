"""
Name: Jose Martinez
Class: CS 521 - 2020 Spring 1
Date: February 22, 2020
Homework Problem # 15.3
Description: Computing the GCD in recursion mode
"""


def gcd(m, n):
    """
    Function to determine the GCD for m and n
    """
    # avoid the zerodvision error by equating the n to 0 in abs form
    if n == 0:
        return abs(m)
    elif m % n == 0:
        return abs(n)
    else:
        # if both numbers are not zero, then return the GCD using the modulo
        return gcd(n, (m % n))


while True:
    # prompts the user to enter for two integers
    try:
        user_ints = [int(value) for value in input(
            'Enter two integers, separated by a space: ').split()]

        # ensure that user enters 2 integers only using len
        if len(user_ints) != 2:
            print('Incorrect number of integers. Please try again.')
            # loop until entered correctly
            continue
        break

    # if any input is not an int, user prompted again.
    except ValueError:
        print('Input is not an integer. Please try again.')
        # loop until entered correctly
        continue

# display the GCD
print(gcd(user_ints[0], user_ints[1]))
