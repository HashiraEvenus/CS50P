

def main():
    text = input()
    print(convert(text))

def convert(txt):
    emoji = "🙂"
    txt = txt.replace(":)",emoji)
    txt = txt.replace(":(","🙁")
    return txt
main()