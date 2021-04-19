from src.constants import response_user_endpoint

data = response_user_endpoint.json()['data']


class Data:
    def __init__(self, id=0, email=0, first_name=0, last_name=0, avatar=0):
        self.id = id
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.avatar = avatar

    @classmethod
    def accessParams(cls, data):
        return data['id'], data['email'], data['first_name'], data['last_name'], data['avatar']


