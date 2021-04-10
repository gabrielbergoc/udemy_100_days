from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
menu = Menu()
cash_register = MoneyMachine()
menu_items = menu.get_items()


def main():
    option = input(f"What would you like? ({menu_items}) ")

    if option == 'off':
        exit()

    elif option == 'report':
        coffee_maker.report()
        cash_register.report()
        main()

    else:
        order = menu.find_drink(option)
        if not order:
            main()
        else:
            if not coffee_maker.is_resource_sufficient(order):
                main()
            else:
                if not cash_register.make_payment(order.cost):
                    main()
                else:
                    coffee_maker.make_coffee(order)
                    main()


if __name__ == '__main__':
    main()