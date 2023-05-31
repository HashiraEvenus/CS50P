from pyfiglet import Figlet
import sys
import random



figlet = Figlet()
if len(sys.argv) == 3 and sys.argv[1] == ("-f" or "--font") and sys.argv[2] in figlet.getFonts():
    s = input("Input: ")
    figlet.setFont(font = sys.argv[2])
    print(figlet.renderText(s))
elif len(sys.argv) == 1:
    s = input("Input: ")
    figlet.setFont(font = random.choice(figlet.getFonts()))
    print(figlet.renderText(s))
else:
    sys.exit(400)

