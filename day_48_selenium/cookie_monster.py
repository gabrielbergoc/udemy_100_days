import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.options import Options

URL = "http://orteil.dashnet.org/experiments/cookie/"

STORE_ITEMS = [
    "buyCursor",
    "buyGrandma",
    "buyFactory",
    "buyMine",
    "buyShipment",
    "buyAlchemy lab",
    "buyPortal",
    "buyTime machine",
]
store = []

options = Options()
options.add_argument("window-size=1920,1080")

driver = webdriver.Edge(options=options)
driver.get(URL)

cps = driver.find_element(By.ID, "cps")
money = driver.find_element(By.ID, "money")
cookie = driver.find_element(By.ID, "cookie")

begin = before = now = time.time()

while now - begin < 120:

    while now - before < 5:

        cookie.click()

        now = time.time()

    for item in STORE_ITEMS:
        new_item = driver.find_element(By.ID, item)
        price = new_item.find_element(By.TAG_NAME, "b").text.split(sep=" - ")[1]
        price = "".join(price.split(sep=","))
        price = int(price)
        store.append({"name": item, "price": price, "element": new_item})

    can_buy = []
    for item in store:
        if item["price"] <= int(money.text):
            can_buy.append(item)

    if len(can_buy) > 0:
        can_buy[-1]["element"].click()

    before = now

print(f"Cookies per second: {cps.text}")
