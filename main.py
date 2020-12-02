from CoffeeUtilities import *
from art import *
from functions import *

isOn = True
art_1 = text2art("coffee") # return art as str in normal mode
print(art_1)

profit = 0
while isOn :

    coffeeChoice = input("Enter what kind of coffee would you like today? (espresso/latte/cappuccino): ")

    if coffeeChoice == "off":
        print("Powering down")
        isOn = False
        break
    if coffeeChoice == "report":
        print(profit)
    if coffeeChoice not in MENU:
        print(f"We don't have {coffeeChoice}, sorry")
        continue

    # resource check
    remaining_ingredients = resources
    ingredients = MENU.get(coffeeChoice).get("ingredients")
    for ingredient in ingredients:
        if resources.get(ingredient) < ingredients.get(ingredient) :
            print(f"Can't make this, not enough {ingredient}")

        remaining_ingredients[ingredient] = remaining_ingredients.get(ingredient) \
                                              - ingredients.get(ingredient)
    print(f"after the {remaining_ingredients}")

    # Money check
    money_needed = MENU.get(coffeeChoice).get("cost")
    print(f"You chose {coffeeChoice}, the price of this coffee is £{money_needed}")
    money_entered = count_money_entered()
    balance = money_entered - money_needed


    if balance > 0:
        print(f"you have £{balance} left")
    elif balance < 0:
        print(f"sorry not enough money, you need £{abs(money_entered - money_needed)} more")
        profit = MENU.get(coffeeChoice).get("cost")
    else:
        print("You have no balance left")












