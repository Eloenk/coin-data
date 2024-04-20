import requests
url = "https://api.coingecko.com/api/v3/simple/price"

coin = "ethereum"
curr = "usd"

params = {  
         'ids': coin,
         'vs_currencies': curr
}

response = requests.get(url, params = params)
print(response)

if response.status_code == 200:
         data = response.json()
         Ethereum_price = data[coin][curr]
         print(f"The price of Ethereum in USD is ${Ethereum_price}")
else:
         print("Failed to retrieve data from the API")