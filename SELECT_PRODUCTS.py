from INSERT_BANKNOTE import *


def read(src):
    with open(src, 'r', encoding='utf-8') as file:
        products = file.readlines()
    return products


def choose_product(products):
    while True:
        num = input('Enter a number of product: ')
        try:
            num = int(num)
            break
        except:
            print('Incorrect! Please enter a number!!!')

    update_products(num)
    for i in products:
        i = i.split(';')
        if int(i[0]) == num and int(i[3]) > 0:
            print('Number: ' + i[0])
            print('Name: ' + i[1])
            print('Costs: ' + i[2])
            print('Quantity: ' + i[3])
            return i[2]


def update_products(n):
    products = read('vm_products.txt')
    n -= 1
    products[n] = products[n].strip().split(';')
    products[n][3] = str(int(products[n][3]) - 1)
    products[n] = ';'.join(products[n])
    products[n] = products[n] + '\n'

    open('vm_products.txt', 'w').close()

    with open('vm_products.txt', 'a') as wf:
        for i in products:
            wf.write(str(i))


def product_availability():
    count = 0
    products = read('vm_products.txt')
    for i in products:
        i = i.strip().split(';')
        if int(i[3]) > 0:
            count += 1
    if count == 0:
        return False


def fill_products():
    with open('vm_products.txt', 'r', encoding='utf-8') as file:
        products = file.readlines()
    for n in range(len(products)):
        products[n] = products[n].strip().split(';')
        products[n][3] = str(15)
        products[n] = ';'.join(products[n])
        products[n] = products[n] + '\n'

    open('vm_products.txt', 'w').close()

    with open('vm_products.txt', 'a') as wf:
        for i in products:
            wf.write(str(i))


def select_product():
    products = read('vm_products.txt')
    return choose_product(products)
