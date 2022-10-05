#!/usr/bin/env python3
# Created by: Nathan Araujo
# Created on: Oct 4 2022
# This program calculates the tax and total when given the subtotal
import constants


def main():

    # Get the input for the subtotal
    subtotal = float(input("Enter the subtotal: "))

    # Calculate the tax and total
    tax = subtotal * constants.HST
    total = tax + subtotal

    # Display the tax and total
    print("")
    print("The tax is ${:.8}".format(tax))
    print("The total is ${:.8}".format(total))


if __name__ == "__main__":
    main()
