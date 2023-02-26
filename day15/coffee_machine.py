''' menu for coffee machine - basic concept'''
from menu import MENU

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = 0

def report(resources, money):
    '''generate report for user resource availability and cash in coffee machine'''
    for key, value in resources.items():
        print (f"{key}: {value}")
    print(f"you earn: {money}")
#report()

def check_resources_for_order(coffee, available_resources):
    '''checking available resources to make a coffee return True if is sufficient
    and return cooffe price '''
    #coffe_cost = MENU[coffee]['cost']
    for ingredient in MENU[coffee]["ingredients"]:
        if (MENU[coffee]["ingredients"].get(ingredient)) <= (available_resources.get(ingredient)):
            pass
        else:
            print(f"NOK - not enough {ingredient}")
            return False
    print(f"insert coins:$ {coffe_cost}")
    return True

def process_coins(coffe_price):
    '''count coins for coffee !!do foget round pricess!!'''
    coins = {
        "quarters": 0.25,
        "dimes" : 0.10,
        "nickles" : 0.05,
        "pennies": 0.01
        }
    order_cash = 0
    money_refund = 0
    while order_cash < coffe_price:
        for key, value in coins.items():
            order_cash += (value * (int(input(f"how many {key} ({value}$)?: "))))
            print (f"{order_cash}$")
        if order_cash >= coffe_price:
            money_refund = order_cash - coffe_price
            print(f"money_refund: {money_refund}")
        else:
            print(f"not enough cash, coffee price is: {coffe_price}")
    return

#process_coins()  for test

def make_a_coffee(available_resources, coffe_type):
    ''' checkig that all conditions are ok to make a coffee'''
    #print(available_resources, coffe_type)   for test
    available_resources = {key: available_resources[key] - coffe_type[key] for key in coffe_type}
    #print (f"nowy dictionary: {available_resources}") for test
    return available_resources

#make_a_coffee(resources, MENU["espresso"]["ingredients"] )  for test

def coffe_machine(resources, money):
    '''main coffe maichione program'''
    user_choice = input("What would you like? (1-espresso/ 2-latte/ 3-cappucicino):")
    if user_choice == "1" and (check_resources_for_order("espresso", resources)):
        process_coins(MENU["espresso"]["cost"])
        resources = make_a_coffee(resources, MENU["espresso"]["ingredients"])
        money += MENU["espresso"]["cost"]
        print("Your coffe is ready")
        coffe_machine(resources, money)
    elif user_choice == "2" and check_resources_for_order("latte", resources):
        process_coins(MENU["latte"]["cost"])
        resources = make_a_coffee(resources, MENU["latte"]["ingredients"])
        money += MENU["latte"]["cost"]
        print("Your coffe is ready")
        coffe_machine(resources, money)
    elif user_choice == "3" and check_resources_for_order("cappuccino", resources):
        process_coins(MENU["cappuccino"]["cost"])
        resources = make_a_coffee(resources, MENU["cappuccino"]["ingredients"])
        money += MENU["cappuccino"]["cost"]
        print("Your coffe is ready")
        coffe_machine(resources, money)
    elif user_choice == "report":
        report(resources, money)
        coffe_machine(resources, money)
    else:
        print("please select other product form list")
        coffe_machine(resources, money)

coffe_machine(resources, money)
#print (f"money: {money}, resources: {resources}")