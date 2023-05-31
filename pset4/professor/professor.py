import random

def main():

    score = 0
    lvl = get_level()

    for i in range(10):
        mistake = 0
        x = generate_integer(lvl)
        y = generate_integer(lvl)

        while True:
            print(f"{x} + {y} = ",end ="")
            answer = input()
            if answer.isdigit() and x + y == int(answer):
                score +=1
                break
            else:
                mistake += 1
                print("EEE")
            if mistake == 3:
                print(x+y)
                break

    print(score)
def get_level():
    while True:
        try:
            x = int(input("Level:"))
            if x<1 or x>3:
                raise ValueError
            break
        except ValueError:
            pass
    return x
def generate_integer(level):
    if level == 1:
        number = random.randint(0,9)
    elif level == 2:
        number = random.randint(10,99)
    elif level == 3:
        number = random.randint(100,999)
    return number
if __name__ == "__main__":
    main()