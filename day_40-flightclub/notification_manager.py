import decouple
import smtplib
from twilio.rest import Client

TWILIO_SID = decouple.config("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = decouple.config("TWILIO_AUTH_TOKEN")
TWILIO_VIRTUAL_NUMBER = decouple.config("TWILIO_PHONE_NUMBER")
TWILIO_VERIFIED_NUMBER = "" # number to which send sms

MY_EMAIL = decouple.config("MY_EMAIL")

class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        msg = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        if msg.status == "qeued":
            print(f"sms sent to {TWILIO_VERIFIED_NUMBER}")

    def send_email(self, message, emails):
        with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=decouple.config("PASSWORD"))
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=emails,
                msg=f"Subject:Flight Club\n\n{message}".encode("utf-8")
            )
