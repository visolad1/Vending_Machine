from turtle import update


def insert_banknote():
    denominations = []
    with open('banknotes.txt', 'r') as file:
        line = file.readlines()
        for i in range(1, len(line)):
            line[i] = line[i].strip().split(';')
            denominations.append(line[i][0])
        while True:
            print("Correct banknotes - " + ', '.join(denominations))
            banknote = input("Enter banknote: ")
            if banknote in denominations:
                for i in range(1, len(line)):
                    if banknote in line[i]:
                        line[i][1] = str(int(line[i][1]) + 1)
                    line[i] = ';'.join(line[i]) + '\n'

                open('banknotes.txt', 'w').close()

                with open('banknotes.txt', 'a') as wf:
                    for i in line:
                        wf.write(i)
                return int(banknote)
            else:
                print("Incorrect banknote. Please try again!!!")


def check_balance():
    with open('balance.txt', 'r') as rf:
        balance = rf.readline()
    return int(balance)


def update_balance(balance):
    with open('balance.txt', 'w') as wf:
        wf.write(str(balance))


def total_amount(banknote):
    with open('sum.txt', 'r') as rf:
        line = rf.readline()
    summ = int(line) + banknote
    with open('sum.txt', 'w') as wf:
        wf.write(str(summ))
    return summ


def show_banknotes():
    with open('banknotes.txt', 'r') as file:
        banknotes = file.readlines()
        for i in banknotes:
            i = i.strip().split(';')
            print(f"{i[0]} : {i[1]}")


def update_sum():
    with open('sum.txt', 'w') as wf:
        wf.write('0')


def update_banknotes():
    with open('banknotes.txt', 'r') as rf:
        line = rf.readlines()
        for i in range(1, len(line)):
            line[i] = line[i].strip().split(';')
            line[i][1] = '0'
            line[i] = ';'.join(line[i]) + '\n'
    
    return line

def write_update_banknotes():
    line = update_banknotes()
    open('banknotes.txt', 'w').close
    with open('banknotes.txt', 'a') as wf:
        for i in line:
            wf.write(i)

