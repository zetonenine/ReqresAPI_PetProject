from src.constants import response_user_endpoint, user_endpoint
import requests
from Data import Data
from Support import Support

data = response_user_endpoint.json()['data']
support = response_user_endpoint.json()['support']


def single_user(num):
    response_data = requests.get(f'{user_endpoint}/{num}')
    try:
        response_data_json = response_data.json()['data']
        singleUserData = Data.accessParams(response_data_json)

        for i in singleUserData:
            if not i:
                return f"Bug with {i}"
        return f'{num}. ID = {singleUserData[0]}. Status code - {response_data.status_code}, '

    except:
        return f'{num}. No user. Status code - {response_data.status_code}, Payload - {response_data.json()}'


def test_every_user(num):
    for j in range(1, num+1):
        print(single_user(j))

    response_support = requests.get(f'{user_endpoint}').json()['support']
    singleUserSupport = Support.accessParams(response_support)
    for i in singleUserSupport:
        if not i:
            return f'Bug with {i}'
    print('\n"support" is good')


NUM = 15
test_every_user(NUM)