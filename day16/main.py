from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_menu =  Menu()
coffee_machine = CoffeeMaker()

order = input(f"What would you like? {coffee_menu.get_items()}: ")
drink = coffee_menu.find_drink(order)
#coffee_machine.is_resource_sufficient(drink)


#check_resources = coffee_machine.is_resource_sufficient(drink)

#print(f"{drink}")
