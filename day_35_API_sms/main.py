import requests
import decouple
from twilio.rest import Client
from geopy.geocoders import Nominatim

def get_city_coords(city):
    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.geocode(city)
    lat = location.latitude
    lon = location.longitude
    return lat, lon

city = "São Paulo"
city_coords = get_city_coords(city)

url = f"https://api.openweathermap.org/data/2.5/onecall"
appid = decouple.config("OPENWEATHER_API_KEY")

params = {
    # "lat": -27,   # test
    # "lon": -58.5, # test
    "lat": city_coords[0],
    "lon": city_coords[1],
    "appid": appid,
    "exclude": "minutely,current,daily"
}

response = requests.get(url=url, params=params)
response.raise_for_status()


# with open("weather.json", mode="w") as file:
#     json.dump(obj=response.json(), fp=file, indent=4)

n_hours = 12
weather_forecast = [response.json()["hourly"][i]["weather"][0]["id"] for i in range(n_hours)]

umbrella = False

i = 0
while not umbrella and i < len(weather_forecast):
    if weather_forecast[i] < 700:
        umbrella = True
    i += 1

if umbrella:
    msg_body = "Good morning :)\nPrecipitation forecast.\nToday you'll probably need an umbrella."
else:
    msg_body = "Good morning :)\nToday you'll probably NOT need an umbrella."

# Your Account Sid and Auth Token from twilio.com/console
# and set the environment variables. See http://twil.io/secure
phone_number = decouple.config("TWILIO_PHONE_NUMBER")
account_sid = decouple.config("TWILIO_ACCOUNT_SID")
auth_token = decouple.config("TWILIO_AUTH_TOKEN")
client = Client(account_sid, auth_token)
sms_to = "" # send sms to this number

message = client.messages \
                .create(
                     body=msg_body,
                     from_=phone_number,
                     to=sms_to
                 )

print(message.status)