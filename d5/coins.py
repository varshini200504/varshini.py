def get_change(amount):
    coins = [5, 2, 1]
    change = []

    for coin in coins:
        while amount >= coin:
            amount -= coin
            change.append(coin)
    
    return change
amount = int(input("Enter the amount: "))
change = get_change(amount)
print("5:",change.count(5))
print("2:",change.count(2))
print("1:",change.count(1))