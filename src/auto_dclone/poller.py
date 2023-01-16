import requests

URL = 'https://diablo2.io/dclone_api.php'

class Poller:
    def __init__(self, region, ladder, hardcore):
        self.region = region
        self.ladder = ladder
        self.hardcore = hardcore

    def poll_api(self):
        response = requests.get(URL, params={
            "region": self.region,
            "ladder": self.ladder,
            "hc": self.hardcore,
        })
        return response.json()
