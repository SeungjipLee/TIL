import requests

url = 'https://fakestoreapi.com/carts'
response = requests.get(url).json()

print(type(response))