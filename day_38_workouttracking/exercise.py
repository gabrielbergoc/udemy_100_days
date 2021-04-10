import requests
import decouple
from datetime import datetime

TODAY = datetime.today()
DATE = TODAY.strftime("%d/%m/%Y")
TIME = TODAY.strftime("%H:%M:%S")

NUTRITIONIX_APP_ID = decouple.config("NUTRITIONIX_APP_ID")
NUTRITIONIX_API_KEY = decouple.config("NUTRITIONIX_API_KEY")
NUTRITIONIX_URL = "https://trackapi.nutritionix.com/v2"

SHEETY_BEARER_TOKEN = decouple.config("SHEETY_BEARER_TOKEN")
SHEETY_URL = decouple.config("SHEETY_URL")
SHEETY_HEADERS = {
    "Authorization": f"Bearer {SHEETY_BEARER_TOKEN}",
    "Content-Type": "application/json"
}

class Exercise:

    def __init__(self, gender, weight, height, age):
        self.gender = gender
        self.weight = weight
        self.height = height
        self.age = age

    # get exercise details
    def get_exercise(self, query: str):
        nutritionix_header = {
            "x-app-id": NUTRITIONIX_APP_ID,
            "x-app-key": NUTRITIONIX_API_KEY,
        }

        exercise_params = {
            "query": query,
            "gender": self.gender,
            "weight_kg": self.weight,
            "height_cm": self.height,
            "age": self.age,
        }

        exercise_url = NUTRITIONIX_URL + "/natural/exercise"

        response = requests.post(url=exercise_url, headers=nutritionix_header, json=exercise_params)
        response.raise_for_status()

        exercise_data = response.json()["exercises"][0]

        new_row = {
            "workout": {
                "date": DATE,
                "time": TIME,
                "exercise": exercise_data["user_input"].title(),
                "duration": exercise_data["duration_min"],
                "calories": exercise_data["nf_calories"]
            }
        }

        return new_row

    # post new row into prices_sheet
    def post_new_row(self, query: str):
        response = requests.post(url=SHEETY_URL, headers=SHEETY_HEADERS, json=self.get_exercise(query))
        response.raise_for_status()

        print(response.text)

    def get_row(self, row_number=None):
        if row_number:
            url = SHEETY_URL + "/" + str(row_number)
        else:
            url = SHEETY_URL
        response = requests.get(url=url, headers=SHEETY_HEADERS)
        response.raise_for_status()

        print(response.text)
