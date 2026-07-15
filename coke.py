amount = 50

while amount > 0:
    print(f"Amount Due: {amount}")
    x = int(input("Insert Coin: "))
    if x == 25 or x == 10 or x == 5:
        amount = amount - x

if amount <= 0:
    print(f"Change Owed: {abs(amount)}")