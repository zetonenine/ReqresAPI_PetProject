import requests
from src.constants import user_endpoint
from SingleUser import single_user


def deleteUser(num):
    try:
        r = requests.delete(f'{user_endpoint}/{num}')
        msg = f" DEL: Status: {r.status_code}"

        return msg + '\n ' + single_user(num)
        # given api doesn't save new user data, so method GET can't show us new user
    except:
        "Unknown error"


NUM = 2
print(deleteUser(NUM))