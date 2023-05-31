def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    first = s[0:1]
    second = s[2:len(s)]

    #See valid length
    if 2<=len(s)<=6 and first.isalpha():
        if second.isalnum():
            for i in range(len(second)):
                if second[i] == '0':
                    return False
                elif second[i].isdigit():
                    if second[i:len(s)].isnumeric():
                        return True
                    else:
                        return False
            else:
                return True


        else:
            return False
    else:
        return False





main()
