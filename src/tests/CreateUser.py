import requests
from src.constants import user_endpoint
from SingleUser import single_user

data = {
    "name": "morpheus",
    "job": "leader"
}


def createUser(data):
    try:
        r = requests.post(user_endpoint, data)
        id = r.json()['id']
        msg = f"POST: Status: {r.status_code}, {r.json()}"

        return msg + '\n ' + single_user(id)
        # given api doesn't save new user data, so method GET can't show us new user
    except:
        "Unknown error"


print(createUser(data))