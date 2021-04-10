import decouple
import requests
import json
from datetime import date
from datetime import timedelta

API_KEY = decouple.config("TEQUILA_API_KEY")
URL = "http://tequila-api.kiwi.com/"

ORIGIN = {
    "origins":
        [
            {
                "city": "São Paulo",
                "iataCode": "SAO"
            },
            {
                "city": "London",
                "iataCode": "LON"
            }
        ]
    }

DATE_FROM = date.today()
DATE_TO = (DATE_FROM + timedelta(days=182))

MIN_STAY = 7
MAX_STAY = 28

CURRENCY = "GBP"

#This class is responsible for talking to the Flight Search API.
class FlightSearch:

    def __init__(self):
        self.location_endpoint = URL + "locations/query"
        self.flights_endpoint = URL + "v2/search"
        self.apikey = API_KEY
        self.headers = {"apikey": self.apikey}


    def search_flights(self, destination, max_price):
        params = {
            "fly_from": f"city:{ORIGIN['origins'][1]['iataCode']}",
            "fly_to": destination['iataCode'],
            "date_from": DATE_FROM.strftime("%d/%m/%Y"),
            "date_to": DATE_TO.strftime("%d/%m/%Y"),
            "nights_in_dst_from": MIN_STAY,
            "nights_in_dst_to": MAX_STAY,
            "flight_type": "round",
            "adults": 1,
            "adult_hold_bag": 1,
            "adult_hand_bag": 1,
            "curr": CURRENCY,
            "max_stopovers": 0,
            "price_to": max_price,
            # "limit": 1000,
        }
        return self.requests_get(self.flights_endpoint, params)

    def search_location(self, location):
        params = {
            "term": location
        }
        response = self.requests_get(self.location_endpoint, params)

        return response["locations"][0]["code"]

    def requests_get(self, url, params):
        response = requests.get(url=url, headers=self.headers, params=params)
        response.raise_for_status()

        return response.json()
