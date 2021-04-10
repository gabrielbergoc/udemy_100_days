import datetime as dt
import smtplib
import random
import decouple

MY_EMAIL = decouple.config("MY_EMAIL")
PASSWORD = decouple.config("PASSWORD")

# ----------------- GET QUOTES ------------------------ #
with open("quotes.txt") as file:
    quotes = file.readlines()

quote = random.choice(quotes)

# ----------------- GET DATE -------------------------- #
monday = 0
thursday = 3
today = dt.datetime.now().weekday()

# ----------------- SEND EMAIL ------------------------ #
if today == thursday:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="gabspython@yahoo.com",
            msg=f"Subject:Weekly Motivational\n\n"
                f"{quote}"
        )