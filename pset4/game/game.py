import random
while True:
    try:
        level = int(input("Level:"))
        if level <= 0:
            raise ValueError
        number = random.randint(1, level)
        break
    except ValueError:
        pass
while True:
    try:
        guess = int(input("Guess:"))
        if guess <= 0 or guess>level:
            raise ValueError

        if number<guess:
            print("Too large!")
        elif number>guess:
            print("Too small!")
        else:
            print("Just right!")
            break

    except ValueError:
        pass


