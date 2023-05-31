#Input text
def main():
    text = input("Input: ")
    print("Output: ",check(text))


#Loop through text and delete vowels
def check(text):
    vowels = ['a','e','i','o','u']
    for char in text:
        if char.lower() in vowels:
            text = text.replace(char,"")
    #Return the new text without vowels
    return text
main()


