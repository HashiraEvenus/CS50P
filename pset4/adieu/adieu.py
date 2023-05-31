import inflect
p = inflect.engine()

names = []
while True:
    try:
        name = input("Name: ")
        names.append(name)

    except EOFError:
        names = p.join(names)
        print()
        print("Adieu, adieu, to",names)
        break