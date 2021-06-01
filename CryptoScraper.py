from bs4 import BeautifulSoup
import requests
import pandas as pd
import json
import time

# Set the URI for coin data
cmc = requests.get('https://coinmarketcap.com/')

# Set BS4 for html 
soup = BeautifulSoup(cmc.content, 'html.parser')

# Search for JSON content type(where the coin data is), set to var
data = soup.find('script', id="__NEXT_DATA__",type="application/json")

# Init the dict
coins = {}

# Set var for JSON content
coin_data = json.loads(data.contents[0])

# Add all data in 'data' to a dict
listings = coin_data['props']['initialState']['cryptocurrency']['listingLatest']['data']

# Single out 'id' and 'slug' from listings dict
for i in listings:
    coins[str(i['id'])] = i['slug']

# Pull out key/values separately
coinKeys = list(coins.keys())
coinValues = list(coins.values())

# Get coin name from user
targetCoinName = input("Enter a coin name in lowercase:\n")

# Retrieve key from input value
position = coinValues.index(targetCoinName)
print("The ID number for that coin on coinmarketcap.com is:\n" + coinKeys[position])

# TODO:
# Create function to use the coin Id/slug to get price data and do price data polling per n minutes
# Create function to do simple math on price pulls in order to determine %change over n minutes
# Create SMS mechanism (twilio free account can send SMS. Could also use GMail API (SMS via SMTP)) 

#targetCoinId = 1
#searchCoin = coin_data['props']['initialState']['cryptocurrency']['listingLatest']['data'][targetCoinId]['quotes']



