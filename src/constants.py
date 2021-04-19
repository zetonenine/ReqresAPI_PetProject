import requests

baseURL = "https://reqres.in/api"
user_endpoint = f"{baseURL}/users"
list_users_endpoint = f'{user_endpoint}?page='

response_user_endpoint = requests.get(user_endpoint)
response_list_of_users_endpoint = requests.get(list_users_endpoint)

