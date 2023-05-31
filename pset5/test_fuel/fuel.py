def main():
    math = convert("1/4")
    print(gauge(math))


def convert(fraction):
    while True:
        try:
            x,y = fraction.split("/")
            if int(x)>int(y):
                raise ValueError
            return round((int(x)/int(y))*100)

        except (ZeroDivisionError, ValueError):
            pass


def gauge(percentage):

    percentage = int(percentage)
    if percentage>=99:
        return("F")
    elif percentage<=1:
        return("E")
    else:
         return(f"{percentage}%")


if __name__ == "__main__":
    main()