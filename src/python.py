import requests

from constants import baseURL, user_endpoint

response = requests.get(f'{baseURL}{user_endpoint}?page=2')

print(response.json())
