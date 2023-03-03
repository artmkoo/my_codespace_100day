from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu =  Menu()
coffee_machine = CoffeeMaker()
money_machine = MoneyMachine()

is_working = True

while is_working:
    order = input(f"What would you like? {menu.get_items()}: ")
    if order == "turnoff":
        is_working = False
    elif order == "report":
        coffee_machine.report()
        money_machine.report()
    else:
        drink = menu.find_drink(order)
        if drink and coffee_machine.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_machine.make_coffee(drink)
                coffee_machine.report()
                money_machine.report()
