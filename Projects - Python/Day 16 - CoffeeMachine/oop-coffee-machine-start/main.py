from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

m = Menu()
cm = CoffeeMaker()
mm = MoneyMachine()

pore_coffee = True
while pore_coffee:
    print("☕ Coffee Machine ☕")
    user_choice = input(f"What would you like? ({m.get_items()}): ").lower()

    if user_choice == "off":
        pore_coffee = False
    elif user_choice == "report":
        cm.report()
        mm.report()
    else:
        ingredients_list = m.find_drink(user_choice)
        if cm.is_resource_sufficient(ingredients_list) and mm.make_payment(ingredients_list.cost):
            cm.make_coffee(ingredients_list)