import requests
from src.constants import list_users_endpoint


def list_of_users(num):
    response_data = requests.get(f'{list_users_endpoint}{num}')
    try:
        response_data_json = response_data.json()
        return f"{num}. Page: {response_data_json['page']}, status: {response_data.status_code}, users_per_page: {len(response_data_json['data'])}"
        print(len(response_data_json['data']))

    except:
        return f"{num} Unknown error"


def test_list(num):
    for i in range(1, num+1):
        print(list_of_users(i))


NUM = 3
test_list(NUM)