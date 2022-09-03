from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffe_make = CoffeeMaker()
menu = Menu()
money = MoneyMachine()

coffe_make.report()
i_want_more= True

while i_want_more is True:

    print(f"{menu.get_items()}")
    escolha = input("What you want to drink ?\n")
    check_if_exist = menu.find_drink(escolha)

    while check_if_exist == None:
        print(f"Choose one of the three!!! {menu.get_items()}")
        escolha = input("What you want to drink ?\n")
        check_if_exist = menu.find_drink(escolha)

    check_if_can_do = coffe_make.is_resource_sufficient(drink=check_if_exist)
    if check_if_can_do == False:
        break

    do_payment = money.make_payment(check_if_exist.cost)

    while do_payment is not True:
        do_payment = money.make_payment(check_if_exist.cost)

    if do_payment:
        coffe_make.make_coffee(order=check_if_exist)
        money.report()
        stop_or_note = input("Do you want more coffee ? yes/no\n")

        if stop_or_note == "yes":
            i_want_more = True
        elif stop_or_note == "no":
            i_want_more = False