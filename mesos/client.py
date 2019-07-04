import requests

from settings import MARATHON_PORT, MARATHON_SERVER, MARATHON_RELATIVE_URL


class MarathonClient:
    def __init__(self):
        self.url = 'http://' + MARATHON_SERVER + ':' + MARATHON_PORT + MARATHON_RELATIVE_URL

    def get(self, relative_url=''):
        complete_url = self.url + relative_url
        return requests.get(
            url=complete_url
        )

    def post(self, json={}):
        return requests.post(
            url=self.url,
            json=json
        )

    def put(self, relative_url='', json={}):
        complete_url = self.url + relative_url
        return requests.put(
            url=complete_url,
            data=json
        )

    def delete(self, relative_url=''):
        complete_url = self.url + relative_url
        return requests.delete(
            url=complete_url
        )
