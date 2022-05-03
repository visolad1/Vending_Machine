import json


def read():
    with open('vm_coints.json') as rf:
        coins = json.load(rf)
    return coins


def get_change(balance):
    l = []
    count = 0
    coins = read()

    for i in coins:
        if coins[i] > 0:
            i = int(i)
            while balance // i > 0:
                l.append(i)
                balance -= i

    for i in coins:
        i = int(i)
        count = l.count(i)
        if count > 0:
            print(f"{l.count(i)} coins x {i}")
            i = str(i)
            coins[i] = coins[i] - count

    with open('vm_coints.json', 'w') as f:
        json.dump(coins, f, ensure_ascii=False, indent=4)


def fill_coins():
    with open('vm_coints.json') as rf:
        coins = json.load(rf)

    for i in coins:
        coins[i] = 400

    with open('vm_coints.json', 'w') as f:
        json.dump(coins, f, ensure_ascii=False, indent=4)


def coins_availability():
    count = 0
    with open('vm_coints.json') as rf:
        coins = json.load(rf)
        for i in coins:
            if coins[i] > 0:
                count += 1
    if count == 0:
        return False
