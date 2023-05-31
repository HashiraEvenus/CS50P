import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if match := re.search(r'(?:<iframe.*?src=")(https?://)?(www\.)?(youtube)\.com/embed(/\w+)?',s):
        link = match.group(4)
        return ("https://youtu.be"+link)
    else:
        return None


if __name__ == "__main__":
    main()