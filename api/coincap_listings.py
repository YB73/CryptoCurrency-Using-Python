import json
import requests

listings_url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest' # listings ap endpoint - so cryptocurrency/listings and so on

api_key = '6c814755-e654-446a-a4d1-57244e738a24'
headers = {'X-CMC_PRO_API_KEY': api_key}
curr = 'USD'
sym = '$'

request = requests.get(listings_url,headers= headers)
result = request.json()


print(json.dumps(result, sort_keys=True, indent=4))

data = result['data']

for currency in data:
    name = currency['name']
    symbol = currency['symbol']
    price = currency['quote'][curr]['price']
    percent_change_24h = currency['quote'][curr]['percent_change_24h']
    market_cap = currency['quote'][curr]['market_cap']

    price = round(price, 2)
    percent_change_24h = round(percent_change_24h, 2)
    market_cap = round(market_cap, 2)

    price_string = sym + '{:,}'.format(price)
    percent_change_24h_string = sym + '{:,}'.format(percent_change_24h)
    market_cap_string = sym + '{:,}'.format(market_cap)

    print(name + '{'+ symbol + '}')
    print('Price: '+ price_string)
    print('24H Change: ' + percent_change_24h_string)
    print('Market Cap: ' + market_cap_string)
    print()
