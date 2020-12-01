from CoffeeUtilities import *


def report():
    print(resources)


def count_money_entered():
    dimes = int(input("enter the number of dimes: ")) * 0.1
    quarters = int(input("\nEnter number of quarters: "))*0.25
    nickles = int(input("\nEnter number of nickles: "))*0.05
    return dimes + quarters + nickles

def 