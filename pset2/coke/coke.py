amount_due = 50

while amount_due>0:
    print("Amount Due:", amount_due)
    coin = int(input("Insert Coin: "))
    match coin:
        case 25 | 10 | 5:
            amount_due = amount_due - coin
    if amount_due <= 0:
        print("Change Owed:", -amount_due)

