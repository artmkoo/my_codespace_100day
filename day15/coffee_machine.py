''' menu for coffee machine - basic concept'''
from menu import MENU

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def report():
    '''generate report for user resource availability and cash in coffee machine'''
    for key, value in resources.items():
        print (f"{key}: {value}")
#report()

def check_resources_for_order(coffee, available_resources):
    '''checking available resources to make a coffee'''
    for ingredient in MENU[coffee]["ingredients"]:
        if (MENU[coffee]["ingredients"].get(ingredient)) < (available_resources.get(ingredient)):
            pass
        else:
            print(f"NOK - not enough {ingredient}")
            return False
    print(f"insert coins:$ {MENU[coffee]['cost']}")
    return True

def process_coins():
    '''count coins for coffee'''
    coins = {
        "quarters": 0.25,
        "dimes" : 0.10,
        "nickles" : 0.05,
        "pennies": 0.01
        }
    order_cash = 0
    for key, value in coins.items():
        order_cash += (value * (int(input(f"how many {key} ({value}$)?: "))))
        print (f"{order_cash}$")
    return order_cash
#process_coins()

#money = 0
user_choice = input("What would you like? (1-espresso/ 2-latte/ 3-cappucicino):")
if user_choice == "1":
    check_resources_for_order("espresso", resources)
    if process_coins() >= MENU["espresso"]["cost"]:
        print("making coffe")
    else:
        print("not enought many")
elif user_choice == "2":
    check_resources_for_order("latte", resources)
elif user_choice == "3":
    check_resources_for_order("cappuccino", resources)
#elif user_choice == "off":
    #service mode
else:
    print("please select correct product form list")
