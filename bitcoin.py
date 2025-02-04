import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

bitcoin = requests.get(" https://api.coindesk.com/v1/bpi/currentprice.json" + sys.argv[1])
print(json.dumps(bitcoin.json(), indent=2))