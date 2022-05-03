from GET_CHANGE import *
from SHOW_PRODUCTS import *
from SELECT_PRODUCTS import *
from INSERT_BANKNOTE import *


def print_options():
    print('''
1. Insert banknote 💲
2. Show available products 🍫
3. Choose a product 🛍️
4. Get change
''')

while True:
    print_options()

    option = input("Enter option: ")
    balance = check_balance()

    if product_availability() is False or coins_availability() is False:
        pas = ''
        while pas != '178234':
            pas = input("Please enter service password: ")
        fill_coins()
        fill_products()
        continue

    if option == '1':
        banknote = insert_banknote()
        balance = check_balance() + int(banknote)
        update_balance(balance)
        print(f"Balance - {balance}")
        total_amount(banknote)

    if option == '2':
        show_products()

    if option == '3':
        if show_available_products(balance) is not True:
            try:
                costs = int(select_product())
            except:
                continue

            if balance >= costs:
                balance = balance - costs
                update_balance(balance)
                print(f"Balance - {balance}")
            else:
                print("Insufficient funds!!")
                print(f"Balance - {balance}")
        else:
            print(f"Balance - {balance}")

    if option == '4':
        get_change(balance)
        update_balance('0')

    if option == '178234':
        show_banknotes()
        print("Total amount:", total_amount(0))
        update_sum()
        write_update_banknotes()
        fill_coins()
        fill_products()

