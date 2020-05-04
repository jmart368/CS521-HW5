"""
Name: Jose Martinez
Class: CS 521 - 2020 Spring 1
Date: February 22, 2020
Homework Problem # 6.3
Description: Palindrome integers
"""


def reverse(integer):
    """
    Takes and creates the reversal form of an integer ie 123 would convert
    to 321
    """
    # extract the elements in the list and convert the stirng as int
    number_list = [char for char in str(integer)]
    # reverse the given number list
    number_list.reverse()
    # reverse the string
    reverse_string = ''
    # loop through the reversal of elements
    for x in number_list:
        reverse_string += x
    # returtn the integer in reverse form
    return int(reverse_string)


def is_palindrome(number):
    """
    Determines if the reversal of a number is palidrome
    """
    # if the number is less than 0
    if number < 0:
        return False
    # if the number is a palidrome, return true
    elif number == reverse(number):
        return True
    # if the number is not a palidrome, return false
    else:
        return False


while True:
    # prompt the user input
    try:
        user_int = int(input('Please enter an integer as whole number.'
                             ' Do not use spaces or commas: '))
        # use break to capture invalid inputs that are not int value form
        break
    except ValueError:
        print('Invalid format. You did not enter an integer.')
        # use continue to allow the user to loop until input is valid
        continue

if is_palindrome(user_int) is True:
    print(user_int, 'is a palindrome.')
else:
    print(user_int, 'is not a palindrome.')
