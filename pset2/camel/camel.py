word = input("camelCase: ")
print("snake_case: ", end="")
for letter in word:
    if letter.isupper():
        print("_", end="")
    print(letter.lower(), end="")


