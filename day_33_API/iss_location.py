import requests, json, time, smtplib
from datetime import datetime, timedelta
from geopy.geocoders import Nominatim
import decouple

decouple.

MY_EMAIL = decouple.config("MY_EMAIL")
PASSWORD = decouple.config("PASSWORD")
N = 100

RECEIVERS = {
    "city":
        [{"name": "name", "email": "email"}]
}

# get coordinates of city
def get_city_coords(city):
    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.geocode(city)
    lat = location.latitude
    lon = location.longitude
    return lat, lon

# converts utc to local time
def utc_to_localtz(utc):
    timestamp = datetime.fromtimestamp(utc)
    local_time = timestamp - timedelta(seconds=10800) # subtract timezone offset
    local_time_str = local_time.strftime("%Y-%m-%d %H:%M:%S")
    return local_time_str

# converts unix timestamp to local time
def utc_to_local(utc):
    timestamp = datetime.fromtimestamp(utc)
    local_time_str = timestamp.strftime("%Y-%m-%d %H:%M:%S")
    return local_time_str


def get_sunset_sunrise(date, city_coords):
    print(f"Getting sunrise & sunset times for {date} ...")
    params = {
        "lat": city_coords[0],
        "lng": city_coords[1],
        "date": date,
        "formatted": 0
    }

    # all times are in UTC
    response = requests.get(f"https://api.sunrise-sunset.org/json", params=params)
    response.raise_for_status()

    results = response.json()["results"]

    # parse and manipulate data from Sunrise Sunset API
    for key, value in results.items():
        # convert utc to local time
        if type(value) == str:
            results[key] = datetime.strptime(value[:19], "%Y-%m-%dT%H:%M:%S")  # parse date-time string
            results[key] = datetime.utctimetuple(results[key])                 # transform into tuple
            results[key] = time.mktime(results[key])                           # make it a time object
            results[key] = utc_to_localtz(results[key])                        # convert to local time

        # converts seconds to hours, minutes, seconds for convenience
        elif type(value) == int:
            hours = value // 3600
            minutes = (value % 3600) // 60
            seconds = (value % 3600) % 60

            results[key] = f"{hours}h {minutes}min {seconds}s"

    print("Done!")

    return results  # dict


# get current ISS location
def get_iss_location():
    print("Getting ISS current location...")
    response_iss_location = requests.get(url="http://api.open-notify.org/iss-now.json")
    response_iss_location.raise_for_status()
    iss_location = json.loads(response_iss_location.text)["iss_position"]
    return iss_location

# get future ISS overflights
def get_future_overflights(city, lat, lon, n):
    print(f"Getting future {n} ISS overflights at {city}...")
    params = {
        "lat": lat,
        "lon": lon,
        "n": n
    }
    response_iss_overflights = requests.get(url=f"http://api.open-notify.org/iss-pass.json", params=params)
    iss_overflights_dict = response_iss_overflights.json()
    overflights = iss_overflights_dict["response"]

    for overfly in overflights:
        utc_time = overfly["risetime"]
        overfly["risetime"] = utc_to_localtz(utc_time)

        minutes = overfly['duration'] // 60
        seconds = overfly['duration'] % 60
        overfly["duration"] = f"{minutes}min {seconds}s"

    print("Done!")

    return overflights

def get_future_visible_overflights(city, city_coords):
    future_overflights = get_future_overflights(city=city, lat=city_coords[0], lon=city_coords[1], n=N)

    future_overflights_sorted_by_date = {}
    for overfly in future_overflights:
        dt_overfly = datetime.strptime(overfly["risetime"], "%Y-%m-%d %H:%M:%S")
        dt_overfly_date = dt_overfly.date().strftime("%Y-%m-%d")

        if future_overflights_sorted_by_date.get(dt_overfly_date):
            future_overflights_sorted_by_date[dt_overfly_date].append(overfly)
        else:
            future_overflights_sorted_by_date[dt_overfly_date] = [overfly]

    print("Calculating which future overflights will (probably) be visible...")
    visible_overflights = []
    for date, overfly_list in future_overflights_sorted_by_date.items():
        sunset_sunrise = get_sunset_sunrise(date=date, city_coords=city_coords)
        sunset_sunrise_sunrise = datetime.strptime(sunset_sunrise["sunrise"], "%Y-%m-%d %H:%M:%S").time()
        sunset_sunrise_sunset = datetime.strptime(sunset_sunrise["sunset"], "%Y-%m-%d %H:%M:%S").time()
        sunset_sunrise_dawn = datetime.strptime(sunset_sunrise["astronomical_twilight_begin"], "%Y-%m-%d %H:%M:%S").time()
        sunset_sunrise_dusk = datetime.strptime(sunset_sunrise["astronomical_twilight_end"], "%Y-%m-%d %H:%M:%S").time()

        for overfly in overfly_list:
            dt_overfly = datetime.strptime(overfly["risetime"], "%Y-%m-%d %H:%M:%S")
            dt_overfly_time = dt_overfly.time()

            if sunset_sunrise_dawn < dt_overfly_time < sunset_sunrise_sunrise or sunset_sunrise_sunset < dt_overfly_time < sunset_sunrise_dusk:
                visible_overflights.append(str(overfly) + "\n")

    with open("iss_email.txt", mode="w") as file:
        file.writelines(visible_overflights)
    print("Done!")

    return visible_overflights  # list

def send_email(emails, city):
    city_coords = get_city_coords(city)
    overflights = get_future_visible_overflights(city, city_coords)
    print("Sending email...")
    with open("iss_email.txt") as file:
        text = file.read()
    with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=emails,
            msg=f"Subject: Next ISS spottings\n\n"
                f"{text}"
        )
    print("Done!!!")

for city, receivers in RECEIVERS.items():
    emails = [receivers[i]["email"] for i in range(len(receivers))]
    send_email(emails, city)