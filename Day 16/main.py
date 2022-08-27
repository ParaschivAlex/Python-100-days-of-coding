from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

still_serving = True

while still_serving:
    options = menu.get_items()
    option = input(f"What would you like? ({options}): ")
    if option == 'off':
        still_serving = False
        continue
    elif option == 'report':
        coffee_maker.report()
        #CoffeeMaker().report()
        continue
    else:
        drink = menu.find_drink(option)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
