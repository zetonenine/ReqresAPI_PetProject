import requests
from src.constants import user_endpoint
from SingleUser import single_user

data = {
    "name": "morpheus",
    "job": "zion leader"
}


def createUser(data, num):
    try:
        r = requests.put(f'{user_endpoint}/{num}', data)
        msg = f" PUT: Status: {r.status_code}, {r.json()}"

        return msg + '\n ' + single_user(num)
        # given api doesn't save new user data, so method GET can't show us new user
    except:
        "Unknown error"


print(createUser(data, 2))