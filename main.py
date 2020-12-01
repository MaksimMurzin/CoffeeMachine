from CoffeeUtilities import *
from art import *
from functions import *

art_1 = text2art("coffee") # return art as str in normal mode
print(art_1)


coffeeChoice = input("Enter what kind of coffee would you like today? (espresso/latte/cappuccino): ")

if coffeeChoice == "off":
    print("Powering down")
elif coffeeChoice == "report":
    report()
elif coffeeChoice not in MENU :
    print(f"We don't have {coffeeChoice}, sorry")

else:
    print(f"You chose {coffeeChoice}, the price of this coffee is £{MENU.get(coffeeChoice).get('cost') }")
    money_entered = input("enter your money: ")
    count_money_entered(money_entered)









def report():
    print(resources)