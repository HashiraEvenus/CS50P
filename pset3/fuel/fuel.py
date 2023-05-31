def main():
    fraction = get_fraction("Fraction: ")
    perc = round(fraction*100)
    if perc>=99:
        print("F")
    elif perc<=1:
        print("E")
    else:
         print(perc,"%",sep='')


def get_fraction(frac):
    while True:
        try:
            x,y = input(frac).split("/")
            if int(x)>int(y):
                raise ValueError
            return int(x)/int(y)

        except (ZeroDivisionError, ValueError):
            pass

main()