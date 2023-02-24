from .api.base_webaction import Gettable, Postable
import requests
#api.lines.line.Straight()
#api.lines.odds.Straight()


class PS3838:
    def __init__(self, credentials):
        self.credentials = credentials

    def get(self, data: Gettable):
        return requests.get(url=data.url, params=data.params, auth=self.credentials).json()

    def post(self, data: Postable):
        pass

