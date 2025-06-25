from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()


def handle_request(item):
    if item == "report":
        coffee_maker.report()
        money_machine.report()
        return
    menu_item = menu.find_drink(item)
    if coffee_maker.is_resource_sufficient(menu_item) and money_machine.make_payment(menu_item.cost):
        coffee_maker.make_coffee(menu_item)


request = input(f"What would you like to order? ({menu.get_items()}): ")
while request != 'off':
    handle_request(request)
    request = input(f"What would you like to order? ({menu.get_items()}): ")

