import json
import requests
import sys

if len(sys.argv) == 2 and sys.argv[1]:
    try:
        coins = float(sys.argv[1])
    except ValueError:
        sys.exit(1,"The program has exitted")
    try:
        price = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        o = price.json()
        no_comma = o['bpi']['USD']['rate'].replace(',', '')
        rate = float(no_comma)
        print(f'${rate*coins:,.4f}')


    except requests.RequestException:
        print("ss")

elif len(sys.argv) == 1:
    sys.exit(1,"Missing command-line argument")
else:
    sys.exit(1,"Command-line argument is not a number")


