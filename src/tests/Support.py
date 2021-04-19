from src.constants import response_user_endpoint

support = response_user_endpoint.json()['support']


class Support:
    def __init__(self, url, text):
        self.url = url
        self.text = text

    @classmethod
    def accessParams(cls, support):
        return support['url'], support['text']
