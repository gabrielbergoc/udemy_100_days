from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
from pprint import pprint

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()
notification_manager = NotificationManager()

emails = data_manager.get_emails()

ORIGIN_CITY_IATA = "LON"

if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet_data:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )
    if flight and flight.price < destination["lowestPrice"]:
        message = f"Low price alert!" \
                  f" Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport}" \
                  f" to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date}" \
                  f" to {flight.return_date}: https://www.google.co.uk/flights?hl=en#flt={ORIGIN_CITY_IATA}.{destination['iataCode']}.{flight.out_date}*{destination['iataCode']}.{ORIGIN_CITY_IATA}.{flight.return_date}\n"

        if flight.stop_overs > 0:
            message += f"Flight has {flight.stop_overs} stop over, via {flight.via_city}"

        notification_manager.send_sms(message=message)
        notification_manager.send_email(message=message, emails=emails)