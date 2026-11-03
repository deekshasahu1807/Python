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
    "money": 0
}

def calculate_resources(coffee):
    if resources['coffee'] < MENU[coffee]['ingredients']['coffee']:
        return "Coffee"

    if resources['water'] < MENU[coffee]['ingredients']['water']:
        return "Water"

    if (coffee != "espresso") and (resources['milk'] < MENU[coffee]['ingredients']['milk']):
        return "Milk"

    return True

def calculate_cost(coffee):
    print("Please insert coins.")
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickles = int(input("How many nickles? "))
    pennies = int(input("How many pennies? "))
    # Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
    total = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
    if total < MENU[coffee]['cost']:
        return False

    resources['money'] += MENU[coffee]['cost']

    if coffee != "espresso":
        resources["milk"] -= MENU[coffee]['ingredients']["milk"]

    resources["water"] -= MENU[coffee]['ingredients']['water']
    resources["coffee"] -= MENU[coffee]['ingredients']['coffee']

    return total - MENU[coffee]['cost']

pore_coffee = True
while pore_coffee:
    print("☕ Coffee Machine ☕")
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if user_choice == "off":
        pore_coffee = False
    elif user_choice == "report":
        print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${resources['money']:.2f}")
    elif user_choice in ["latte", "cappuccino", "espresso"]:
        is_resource_available = calculate_resources(user_choice)
        if is_resource_available == True:
            change = calculate_cost(user_choice)
            if not change:
                print("Sorry that's not enough money. Money refunded.")
            else:
                print(f"Here is ${change:.2f} in change.")
                print(f"Here is your ${user_choice} ☕ Enjoy!")
        else:
            print(f"Sorry there is not enough {is_resource_available}.")
    else:
        print("Please choose correct option.")
