##################### Extra Hard Starting Project ######################
import datetime as dt
import pandas
import random
import smtplib
import decouple

MY_EMAIL = decouple.config("MY_EMAIL")
PASSWORD = decouple.config("PASSWORD")

# 1. Update the birthdays.csv - DONE

# 2. Check if today matches a birthday in the birthdays.csv
print("Getting today's time...")
today = dt.datetime.today()
print("Done!")

print("Getting birthdays from file...")
birthdays = pandas.read_csv("birthdays.csv")
print("Done!")

print("Filtering receivers...")
receivers = []
for row in birthdays.iterrows():
    if row[1]["month"] == today.month and row[1]["day"] == today.day:
        receivers.append(row[1])
print("Done!")

print("Choosing random letter template...")
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
template = random.choice(["letter_1.txt", "letter_2.txt", "letter_3.txt"])
print("Done!")

print("Getting letter template...")
with open(file=f"letter_templates/{template}") as file:
    letter = file.read()
print("Done!")


for person in receivers:
    print(f"Sending email to {person['name']}...")
    email_body = letter.replace("[NAME]", person["name"])

# 4. Send the letter generated in step 3 to that person's email address.

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=person["email"],
            msg=f"Subject:Happee Birthdae\n\n"
                f"{email_body}"
        )
    print("Done!")
print("All done :)")