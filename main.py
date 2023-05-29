from data import MENU, resources

is_machine_running = True


def report(user_input):
    """print the report of all the resources"""
    if user_input == 'report':
        for name, quantity in resources.items():
            if name == "coffee":
                print(f"{name}: {quantity}g")
            elif name == "money":
                print(f"{name}: ${quantity}")
            else:
                print(f"{name}: {quantity}ml")


def check_resources(coffee):
    """Check the available resources for the coffee if sufficient"""
    coffee_recipe = MENU[coffee]["ingredients"].items()
    for resource, quantity in coffee_recipe:
        if quantity > resources[resource]:
            return f"Sorry there is not enough {resource}."
    return None


def insert_coin():
    """"Return the sum of the all inserted coins"""
    print("Please insert coins.")
    insert_quarters = int(input("How many quarters?: "))
    insert_demise = int(input("How many demise?: "))
    insert_nickles = int(input("How many nickles?: "))
    insert_pennies = int(input("How many pennies?: "))

    quarter = insert_quarters * 0.25
    demise = insert_demise * 0.10
    nickles = insert_nickles * 0.05
    pennies = insert_pennies * 0.01

    return round(quarter + demise + nickles + pennies, 2)


def transaction_check(coffee , money_inserted):
    """"Check if the user inserted enough money or not"""
    cost = MENU[coffee]["cost"]
    total_coin_inserted = money_inserted

    if total_coin_inserted >= cost:
        returnable_price = total_coin_inserted - cost
        print(f"Here is {returnable_price}$ in change")

        resources["money"] += cost
        drink_recipe = MENU[coffee]["ingredients"]
        for resource in drink_recipe:
            resources[resource] -= drink_recipe[resource]
    else:
        print("Sorry that's not enough money. Money refunded.")


# Ask user to choose the type of coffee
while is_machine_running:
    choice = input("What would you like? (espresso/latte/cappuccino):")

    # Turn off the Coffee Machine by entering “off” to the prompt
    if choice == 'off':
        is_machine_running = False

    report(choice)
    if choice in MENU:
        missing_resource = check_resources(choice)
        if missing_resource:
            print(missing_resource)
        else:
            transaction_check(choice, insert_coin())
            print(f"Here is your {choice} ☕. Enjoy!")
