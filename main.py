from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


cofe_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()




is_on = True
while is_on:
    options = menu.get_items()
    choice = input(f"What would you like {options}: ").lower()
    if choice == 'off':
        is_on = False
    elif choice == 'report':
        cofe_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if cofe_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                cofe_maker.make_coffee(drink)


