"""
Name: Jose Martinez
Class: CS 521 - 2020 Spring 1
Date: February 22, 2020
Homework Problem # 6.9
Description: Conversion between feet and meters
"""


def foot_to_meter(foot):
    """
    Converts from feet to meters
    """
    foot_calculation = foot * 0.305
    # return the foot calculation from above
    return foot_calculation


def meter_to_foot(meter):
    """
    Converts from meters to feet
    """
    meter_calculation = meter / 0.305
    # return the meter calcultation from above
    return meter_calculation


if __name__ == "__main__":
    """
    Display a table of the conversions from feet to meters and meters to feet
    """
    meter = 20
    # print out the caluclations using using the feet to meter/meter to feet
    # use \t for tab
    print('Feet \t Meters  |\tMeters \tFeet')
    # take the elements and print range 1 to 11 including header
    for feet in range(1, 11):
        # format the print to display a table and recal the two functions
        print('{:.1f} \t {:.3f} \t | \t{:.1f} \t{:.3f}'.format
              (feet, foot_to_meter(feet), meter, meter_to_foot(meter)))
        meter += 5
