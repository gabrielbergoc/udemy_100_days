import decouple
import requests

SHEETY_ENDPOINT = decouple.config("SHEETY_ENDPOINT")
SHEETY_USERS_ENDPOINT = decouple.config("SHEETY_USERS_ENDPOINT")
SHEETY_BEARER_TOKEN = decouple.config("SHEETY_BEARER_TOKEN")

# This class is responsible for talking to the Google Sheet.
class DataManager:

    def __init__(self, endpoint, token):
        self.endpoint = endpoint
        self.token = token
        self.headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }

    def get_rows(self) -> dict:
        response = requests.get(
            url=self.endpoint,
            headers=self.headers,
        )

        return response.json()

    def add_row(self, obj: dict):
        response = requests.post(
            url=self.endpoint,
            headers=self.headers,
            json=obj
        )

        return response.text

    def edit_row(self, obj: dict, row_n: int):
        response = requests.put(
            url=self.endpoint + f"/{row_n}",
            headers=self.headers,
            json=obj
        )

        return response.text

    def delete_row(self, row_n: int):
        response = requests.delete(
            url=self.endpoint + f"/{row_n}",
            headers=self.headers
        )

        return response.text
