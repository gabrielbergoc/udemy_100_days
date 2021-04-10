import requests
import json
import decouple
from twilio.rest import Client
from datetime import date
from datetime import timedelta

YESTERDAY = (date.today() - timedelta(days=2)).strftime("%Y-%m-%d")
DAY_BEFORE = (date.today() - timedelta(days=3)).strftime("%Y-%m-%d")
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
ALPHA_API_KEY = decouple.config("ALPHA_API_KEY")
NEWSAPI_KEY = decouple.config("NEWSAPI_KEY")
TWILIO_ACCOUNT_SID = decouple.config("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = decouple.config("TWILIO_AUTH_TOKEN")
TWILIO_PHONE_NUMBER = decouple.config("TWILIO_PHONE_NUMBER")

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

url = "https://www.alphavantage.co/query"
params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "outputsize": "compact",
    "apikey": ALPHA_API_KEY
}

stock_response = requests.get(url=url, params=params)
stock_response.raise_for_status()

stock_data = stock_response.json()

# with open("tesla.json", mode="w") as file:
#     json.dump(obj=stock_data, fp=file, indent=4)

yesterdays_price = float(stock_data["Time Series (Daily)"][YESTERDAY]["4. close"])
daybefores_price = float(stock_data["Time Series (Daily)"][DAY_BEFORE]["4. close"])

price_diff = yesterdays_price - daybefores_price
percentage = 100 * price_diff / daybefores_price

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

url = "https://newsapi.org/v2/everything"
params = {
    "apiKey": NEWSAPI_KEY,
    "q": COMPANY_NAME,
    "from": DAY_BEFORE,
    "to": YESTERDAY,
    "pageSize": 3,
    # "sortBy": "relevancy"
}
news_response = requests.get(url=url, params=params)
news_data = news_response.json()

# with open("news.json", mode="w") as file:
#     json.dump(obj=news_data, fp=file, indent=4)

## STEP 3: Use https://www.twilio.com
# Send a separate message with the percentage change and each article's title and description to your phone number.

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

if abs(percentage) >= 5:
    for news in news_data["articles"]:
        if percentage > 0:
            msg_body = f"TSLA: 🔺{int(percentage)}%\n" \
                       f"Headline: {news['title']}\n" \
                       f"Brief: {news['description']}"
            message = client.messages.create(
                body=msg_body,
                from_=TWILIO_PHONE_NUMBER,
                to="+5511970119999"
            )
        else:
            msg_body = f"TSLA: 🔻{int(abs(percentage))}%\n" \
                       f"Headline: {news['title']}\n" \
                       f"Brief: {news['description']}"
            message = client.messages.create(
                body=msg_body,
                from_=TWILIO_PHONE_NUMBER,
                to="" # send sms to this phone number
            )
        print(message.status)

else:
    print("No relevant price changes")

#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

