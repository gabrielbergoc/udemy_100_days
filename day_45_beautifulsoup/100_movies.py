import requests
import re
import csv
from bs4 import BeautifulSoup

URL = "https://www.timeout.com/newyork/movies/best-movies-of-all-time"


try:
    response = requests.get(URL)
    response.raise_for_status()
except requests.exceptions.HTTPError as errh:
    print(errh)
except requests.exceptions.ConnectionError as errc:
    print(errc)
except requests.exceptions.Timeout as errt:
    print(errt)
except requests.exceptions.RequestException as err:
    print(err)

soup = BeautifulSoup(response.text, "html.parser")
# print(soup.prettify())

movies = soup.select(selector="h3")

with open("100-movies.csv", mode="w", encoding="utf-8", newline="\n") as file:
    for movie in movies:
        try:
            title, year = movie.getText().split(sep='.')[1].split(sep="(")
        except IndexError:
            continue
        except ValueError:
            continue

        title = title.strip("  ")
        year = year.strip(") ")
        print(f"{title}|{year}")
        csvwriter = csv.writer(file)
        csvwriter.writerow((title, year))
