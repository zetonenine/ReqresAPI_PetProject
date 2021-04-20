import requests
from src.constants import user_endpoint
from SingleUser import single_user
from Support import Support


def cycle_of_users_test(num):
    for j in range(1, num+1):
        print(single_user(j))

    response_json = requests.get(f'{user_endpoint}').json()['support']
    singleUserSupport = Support.accessParams(response_json)
    for i, q in response_json.items():
        if not i:
            return f'Bug with {i}'
    print(f'\nGET: support: url: {singleUserSupport[0]}, text: {singleUserSupport[1]}')


NUM = 15
cycle_of_users_test(NUM)