from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffeeMaker = CoffeeMaker()
menu = Menu()
moneyMachine = MoneyMachine()

is_on = True
while is_on == True:

    command = input(f"What would you like? ({menu.get_items()}): ").lower()

    if command == "off":
        is_on = False
    elif command == "report":
        coffeeMaker.report()
    elif command == "profit":
        moneyMachine.report()
    else:
        order = menu.find_drink(command)
        if order is not None:
            if not coffeeMaker.is_resource_sufficient(order):
                pass
            elif moneyMachine.make_payment(order.cost):
                coffeeMaker.make_coffee(order)


