coke = 50
insert_coin = 0

while coke > 0:
    print("Amount Due:", coke)
    insert_coin = int(input("Insert Coin: "))
    if insert_coin == 5 or insert_coin == 10 or insert_coin == 25:
        coke -= insert_coin

if insert_coin > coke:
    print("Change Owed:", abs(coke))
