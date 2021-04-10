import requests
from datetime import datetime, timedelta
import time
from geopy.geocoders import Nominatim

# convert utc timestamp to local time
def utc_to_localtz(utc):
    timestamp = datetime.fromtimestamp(utc)
    local_time = timestamp - timedelta(seconds=time.timezone) # subtract timezone offset
    return local_time.strftime("%Y-%m-%d %H:%M:%S")

# get times of sunsets and sunrises at chosen city and date
def get_sunset_sunrise(city, date):
    coords = get_city_coords(city)

    params = {
        "lat": coords[0],
        "lng": coords[1],
        "date": date,
        "formatted": 0
    }

    # all times are in UTC
    response = requests.get(f"https://api.sunrise-sunset.org/json", params=params)
    response.raise_for_status()

    results = response.json()["results"]

    # convert utc to local time
    for key, value in results.items():
        if type(value) == str:
            results[key] = datetime.strptime(value[:19], "%Y-%m-%dT%H:%M:%S") # parse date-time string
            results[key] = datetime.utctimetuple(results[key])                # transform into tuple
            results[key] = time.mktime(results[key])                          # make it a time object
            results[key] = utc_to_localtz(results[key])  # convert to local time

        elif type(value) == int:
            hours = value // 3600
            minutes = (value % 3600) // 60
            seconds = (value % 3600) % 60

            results[key] = f"{hours}h {minutes}min {seconds}s"

    return results

# get coordinates of cities
def get_city_coords(city):
    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.geocode(city)
    lat = location.latitude
    lon = location.longitude
    return lat, lon

