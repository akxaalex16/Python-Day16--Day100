from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_on = True

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

coffee_maker.report()
money_machine.report()

while is_on:
    options = menu.get_items()
    coffee_choice = input(f"What would you like? {options}:")
    if coffee_choice == 'off':
        is_on = False
    elif coffee_choice == 'report':
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(coffee_choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
