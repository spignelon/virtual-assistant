# Import libraries
import json
import requests

# Defining Binance API URL
key = "https://api.binance.com/api/v3/ticker/price?symbol="

# Making list for multiple crypto's
currencies = ["BTCUSDT", "DOGEUSDT", "LTCUSDT"]
j = 0

# running loop to print all crypto prices
for i in currencies:
    # completing API for request
    url = key + currencies[j]
    data = requests.get(url)
    data = data.json()
    j = j + 1
    print(f"{data['symbol']} price is {data['price']}")
# Import libraries
import json
import requests

# Defining Binance API URL
key = "https://api.binance.com/api/v3/ticker/price?symbol="

# Making list for multiple crypto's
currencies = ["BTCUSDT", "DOGEUSDT", "LTCUSDT"]
j = 0

# running loop to print all crypto prices
for i in currencies:
    # completing API for request
    url = key + currencies[j]
    data = requests.get(url)
    data = data.json()
    j = j + 1
    print(f"{data['symbol']} price is {data['price']}")
