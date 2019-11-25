#!/usr/bin/env python3

# Created by: Joseph Palermo
# Created on: November 2019
# This program uses calculates the volume of a cylinder

import math


def calculate_volume(radius, height):
    # this function calculates and returns volume

    # process
    volume = math.pi*radius**2*height

    return volume


def main():
    # this function gets radius and height and outputs volume of a cylinder

    try:
        # input
        radius_from_user = float(input("Enter the radius (cm): "))
        height_from_user = float(input("Enter the height (cm): "))
        print("")

        radius = radius_from_user
        height = height_from_user

        # call functions
        volume = calculate_volume(radius_from_user, height_from_user)

        # output
        print("The volume is {:,.2f} cm³".format(volume))

    except ValueError:
        print("Please enter a valid number.")


if __name__ == "__main__":
    main()
