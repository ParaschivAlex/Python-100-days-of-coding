# ☕
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def check_resources_for_drink(drink):
    match drink:
        case 'espresso':
            if resources['water'] < MENU['espresso']['ingredients']['water']:
                print("Sorry there is not enough water.")
                return 0
            if resources['coffee'] < MENU['espresso']['ingredients']['coffee']:
                print("Sorry there is not enough coffee.")
                return 0
        case 'latte':
            if resources['water'] < MENU['latte']['ingredients']['water']:
                print("Sorry there is not enough water.")
                return 0
            if resources['milk'] < MENU['latte']['ingredients']['milk']:
                print("Sorry there is not enough milk.")
                return 0
            if resources['coffee'] < MENU['latte']['ingredients']['coffee']:
                print("Sorry there is not enough coffee.")
                return 0
        case 'cappuccino':
            if resources['water'] < MENU['cappuccino']['ingredients']['water']:
                print("Sorry there is not enough water.")
                return 0
            if resources['milk'] < MENU['cappuccino']['ingredients']['milk']:
                print("Sorry there is not enough milk.")
                return 0
            if resources['coffee'] < MENU['cappuccino']['ingredients']['coffee']:
                print("Sorry there is not enough coffee.")
                return 0
    return 1


def greetings(drink):
    print(f"Here is your {drink}. ENJOY!")


still_serving = True
money = 0
while still_serving:
    quarters, dimes, nickles, pennies, total_paid = 0, 0, 0, 0, 0
    option = input("What would you like? (espresso/latte/cappuccino): ")
    if option == 'off':
        still_serving = False
        continue
    elif option == 'report':
        print(
            f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${money}")
        continue
    enough_resources = check_resources_for_drink(option)
    if enough_resources == 1:
        print(f"This costs ${MENU[option]['cost']}")
        quarters = int(input("How many quarters? ($0.25): "))
        dimes = int(input("How many dimes? ($0.10): "))
        nickles = int(input("How many nickles? ($0.05): "))
        pennies = int(input("How many pennies? ($0.01): "))
        total_paid += quarters*0.25 + dimes*0.10 + nickles*0.05 + pennies*0.01
        if total_paid < MENU[option]['cost']:
            print("Sorry that's not enough money. Money refunded.")
            continue
        elif total_paid >= MENU[option]['cost']:
            print("Your order is ready")
            if total_paid > MENU[option]['cost']:
                print(f"Here is ${(total_paid - MENU[option]['cost']):.2f} dollars in change.")
            money += MENU[option]['cost']
            resources['water'] -= MENU[option]['ingredients']['water']
            if option != 'espresso':
                resources['milk'] -= MENU[option]['ingredients']['milk']
            resources['coffee'] -= MENU[option]['ingredients']['coffee']

