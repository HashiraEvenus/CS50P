#Input text
def main(text):

    print("Output:",shorten(text))


#Loop through text and delete vowels
def shorten(txt):
    vowels = ['a','e','i','o','u']
    for char in txt:
        if char.lower() in vowels or not char.isalpha():
            txt = txt.replace(char,"")
    #Return the new text without vowels
    return txt
