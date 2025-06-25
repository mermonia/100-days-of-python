from menu import MENU, resources
COINS = {
    "quarters": 0.25,
    "dimes": 0.10,
    "nickels": 0.05,
    "pennies": 0.01,
}


def print_report():
    for item in resources:
        print(f"{item.title()}: {resources[item]}")


def check_resources(item):
    for ingredient in MENU[item]["ingredients"]:
        if resources[ingredient] < MENU[item]["ingredients"][ingredient]:
            print(f"Sorry, there's not enough {ingredient}")
            return False
    return True


def ask_for_coins():
    total_value = 0
    for coin_type in COINS:
        quantity = int(input(f"How many {coin_type} would you like to put in?: "))
        total_value += quantity * COINS[coin_type]
    return total_value


def consume_resources(item):
    for resource in MENU[item]["ingredients"]:
        resources[resource] -= MENU[item]["ingredients"][resource]


def handle_payment(customer_input, cost):
    if customer_input > cost:
        resources["money"] += cost
        print(f"Here's your {request}! ☕")
        print(f"Here's ${format(customer_input - cost, '.2f')} in change.")
        consume_resources(request)
    elif customer_input == cost:
        resources["money"] += cost
        print(f"Here's your {request}!")
        consume_resources(request)
    else:
        print("Sorry, that's not enough money!")


request = input("What would you like? (espresso/latte/cappuccino): ")
while request != "off":
    if request == "report":
        print_report()
    elif check_resources(request):
        total_input = ask_for_coins()
        handle_payment(total_input, MENU[request]["cost"])
    request = input("What would you like? (espresso/latte/cappuccino): ")
