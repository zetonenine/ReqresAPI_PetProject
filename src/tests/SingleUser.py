from src.constants import response_user_endpoint, user_endpoint
import requests
from Data import Data

data = response_user_endpoint.json()['data']
support = response_user_endpoint.json()['support']


def single_user(num):
    response_data = requests.get(f'{user_endpoint}/{num}')
    try:

        singleUserData = Data.accessParams(response_data.json()['data'])
        for i, j in response_data.json()['data'].items():
            if not i:
                return f"Bug with {i}: {j}"
        return f'GET: {num}. ID = {singleUserData[0]}. Status code - {response_data.status_code}, first_name: {singleUserData[2]}, last_name: {singleUserData[3]}'

    except:
        return f'GET: {num}. No user. Status code - {response_data.status_code}, Payload - {response_data.json()}'