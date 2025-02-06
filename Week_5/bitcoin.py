import json
import requests
import sys


bitcoin = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

o = bitcoin.json()
bitcoin_price = o["bpi"]["USD"]["rate"]

converted_price = float(bitcoin_price.replace(",", ""))
argument = sys.argv[1]
print(converted_price  * float(argument))