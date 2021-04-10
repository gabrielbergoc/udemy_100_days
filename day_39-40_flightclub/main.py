# This file will need to use the DataManager,FlightSearch, FlightData,
# NotificationManager classes to achieve the program requirements.
import decouple
import json
from data_manager import DataManager
from flight_search import FlightSearch

SHEETY_PRICES_ENDPOINT = decouple.config("SHEETY_PRICES_ENDPOINT")
SHEETY_USERS_ENDPOINT = decouple.config("SHEETY_USERS_ENDPOINT")
SHEETY_BEARER_TOKEN = decouple.config("SHEETY_BEARER_TOKEN")

prices_sheet = DataManager(endpoint=SHEETY_PRICES_ENDPOINT, token=SHEETY_BEARER_TOKEN)
prices_sheet_data = prices_sheet.get_rows()["lowestPrice"]

users_sheet = DataManager(endpoint=SHEETY_USERS_ENDPOINT, token=SHEETY_BEARER_TOKEN)
users_sheet_data = users_sheet.get_rows()["users"]

searcher = FlightSearch()

def get_IATACodes():
    for row in prices_sheet_data:
        if not row.get("iataCode"):
            row["iataCode"] = searcher.search_location(row["city"])
            payload = {"price": row}
            status = prices_sheet.edit_row(obj=payload, row_n=row["id"])
            print(status)

def get_flights():
    cheap_flights = {"cheap flights": []}
    for row in prices_sheet_data:
        city = {row["city"]: []}

        if row.get("lowestPrice"):
            lowest_price = row["lowestPrice"]
        else:
            lowest_price = 100000
        price_data = searcher.search_flights(destination=row, max_price=lowest_price)["data"]


        lp_index = None
        for i in range(len(price_data)):
            if price_data[i]["price"] < lowest_price:
                lowest_price = price_data[i]["price"]
                row["lowestPrice"] = lowest_price
                lp_index = i

        if lp_index:
            city[row["city"]].append(price_data[lp_index])

        cheap_flights["cheap flights"].append(city)

        payload = {"price": row}
        status = prices_sheet.edit_row(obj=payload, row_n=row["id"])
        print(status)

    with open("all_cities.json", mode="w") as file:
        json.dump(obj=cheap_flights, fp=file, indent=4)

def user_subscription():
    print("Welcome to GabsBergs's Flight Club :)")
    first_name = input("First name: ")
    last_name = input("Last name: ")
    email = input("Email: ")
    conf_email = input("Put your email again for confirmation: ")
    if email == conf_email:
        user_data = {
            "firstName": first_name,
            "lastName": last_name,
            "email": email,
        }
        response = users_sheet.add_row(obj={"user": user_data})
        print("Congrats! You're in the club :)")
        print(response)

user_subscription()