"""
Name: Jose Martinez
Class: CS 521 - 2020 Spring 1
Date: February 22, 2020
Homework Problem # 6.5
Description: Sort three numbers
"""


try:
    def sort_numbers(num1, num2, num3):
        """
        Ask & Display the sorted numbers in increasing order
        """

        new_list = (num1, num2, num3)
        sort_list = sorted(new_list)

        print('The sorted numbers are {}, {}, {}'.format(
            sort_list[0], sort_list[1], sort_list[2]))

    user_input = input('Enter three numbers seperated by a comma: ')
    number_list = user_input.split(',')
    num1 = float(number_list[0])
    num2 = float(number_list[1])
    num3 = float(number_list[2])

    sort_numbers(num1, num2, num3)

except ValueError:
    print('You did not enter 3 valid numbers separated by a comma')
