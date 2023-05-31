answer1 = input("Expression: ").rstrip().lstrip()

x,y,z = answer1.rsplit()
x = float(x)
z = float(z)


match y:
    case "+":
        print(x + z)
    case "-":
        print(x - z)
    case "/":
        print(x / z)
    case "*":
        print(x * z)

