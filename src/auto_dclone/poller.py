import requests

class Poller:
    def __init__(self, region, ladder, hardcore):
        self.region = region
        self.ladder = ladder
        self.hardcore = hardcore

    def poll_api(self):
        response = requests.get('https://dcnotify.app/api/uberdiablo/')
        return response.json()
