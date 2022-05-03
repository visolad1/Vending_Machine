from SELECT_PRODUCTS import *


def show_products():
    line = read('vm_products.txt')
    for i in range(len(line)):
        line[i] = line[i].strip().split(';')
    for i in line:
        if int(i[3]) > 0:
            print(f"{i[0]}.{i[1]} - {i[2]} - {i[3]}")


def show_available_products(balance):
    count = 0
    products = read('vm_products.txt')
    for i in products:
        i = i.strip().split(';')
        if int(i[2]) <= balance and int(i[3]) > 0:
            print(f"{i[0]}.{i[1]} - {i[2]} - {i[3]}")
            count += 1
    if count == 0:
        return False
