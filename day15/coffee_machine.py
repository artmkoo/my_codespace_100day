''' menu for coffee machine - basic concept'''
from menu import MENU

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def report():
    '''generate report for user'''
    for key, value in resources.items():
        print (f"{key}: {value}")
report()

user_choice = input("What would you like? (espresso/latte/cappucicino):")
