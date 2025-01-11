coke_price = 50

while True:
    print(f"Amount Due: {coke_price}")
    cash = int(input("Insert Coin: "))
    if cash == 5 or cash == 10 or cash == 25:
        coke_price = coke_price - cash