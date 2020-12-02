from CoffeeUtilities import *
from decimal import Decimal


def report():
    print(resources)


def count_money_entered():
    dimes = Decimal(input("enter the number of dimes (£0.10): ")) * 0.1
    quarters = Decimal(input("Enter number of quarters (£0.25): "))*0.25
    nickles = Decimal(input("Enter number of nickles (£0.05): "))*0.05
    total = dimes + quarters + nickles
    print(f"total value entered: {total}")
    return total




