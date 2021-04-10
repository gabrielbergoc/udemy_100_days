import requests
import decouple
from pprint import pprint

SHEETY_PRICES_ENDPOINT = decouple.config("SHEETY_PRICES_ENDPOINT")
SHEETY_USERS_ENDPOINT = decouple.config("SHEETY_USERS_ENDPOINT")
SHEETY_BEARER_TOKEN = decouple.config("SHEETY_BEARER_TOKEN")
SHEETY_HEADERS = {"Authorization": f"Bearer {SHEETY_BEARER_TOKEN}"}


class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT, headers=SHEETY_HEADERS)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data,
                headers = SHEETY_HEADERS
            )
            print(response.text)

    def get_emails(self):
        response = requests.get(url=SHEETY_USERS_ENDPOINT, headers=SHEETY_HEADERS)
        data = response.json()["users"]
        emails = [row["email"] for row in data]

        return emails
