import requests
import smtplib
import decouple
from bs4 import BeautifulSoup

FROM = decouple.config("FROM")
PASSWORD = decouple.config("PASSWORD")
TO = decouple.config("TO")

URL = "https://www.amazon.com.br/Monitor-Philips-21-5-com-HDMI/dp/B09BG8BXCK/ref=sr_1_6?__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=monitor&qid=1633385808&refinements=p_36%3A17270759011%2Cp_n_feature_thirteen_browse-bin%3A21165900011&rnid=21165893011&s=computers&sr=1-6&ufe=app_do%3Aamzn1.fos.25548f35-0de7-44b3-b28e-0f56f3f96147"
HEADERS = {
    "accept-encoding": "gzip, deflate",
    "accept-language": "pt-BR,pt;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 Edg/94.0.992.38",
}

try:
    response = requests.get(url=URL, headers=HEADERS)
    response.raise_for_status()
except requests.exceptions.HTTPError as errh:
    raise errh
except requests.exceptions.ConnectionError as errc:
    raise errc
except requests.exceptions.Timeout as errt:
    raise errt
except requests.exceptions.RequestException as err:
    raise err

soup = BeautifulSoup(response.text, "lxml")
price = soup.select(selector="span#priceblock_ourprice")
price = price.pop()
price = str(price.string)
price = price.split()[1]
price = price.replace(",", ".")
price = float(price)
print(price)

if price < 800:
    email_body = f"Product price is now R${format(price, '.2f')}\n" \
                 f"{URL}"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(FROM, PASSWORD)
        connection.sendmail(
                from_addr=FROM,
                to_addrs=TO,
                msg=f"Subject:Price Tracker\n\n"
                    f"{email_body}"
        )
