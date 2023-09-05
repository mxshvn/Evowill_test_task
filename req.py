import requests


class BoredAPIWrapper:
    def __init__(self):
        self.base_url = "https://www.boredapi.com/api/activity"

    def get_random_activity(self, params=None):
        response = requests.get(self.base_url, params=params)
        return response.json()
