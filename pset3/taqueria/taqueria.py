def main():
    cost = 0.00
    items = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
    }
    while True:
        try:
            order = input("Item: ").lower().title()
            cost = cost+items[order]
            print("$%.2f"%cost)
        except EOFError:
            return print()
        except KeyError:
            pass
main()
