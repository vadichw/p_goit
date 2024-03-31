import requests
from pprint import pprint

#response = requests.get('https://api.privatbank.ua/p24api/pubinfo?exchange&coursid=5')
#exchange_rate = response.json()
#pprint(exchange_rate)

# 68ca564d5628cec686f1024ad4add03f
response = requests.get('https://api.openweathermap.org/data/2.5/weather?lat=33&lon=66&appid=68ca564d5628cec686f1024ad4add03f')
exchange_rate = response.json()
pprint(exchange_rate)
pprint(f"The city is {exchange_rate['name']}")


