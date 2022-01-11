from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

URL = "https://en.wikipedia.org/wiki/Main_Page"

driver = webdriver.Edge()

driver.get(URL)

# article_count = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
# article_count.click()

# all_portals = driver.find_element(By.LINK_TEXT, "All portals")
# all_portals.click()

search_bar = driver.find_element(By.NAME, "search")
search_bar.send_keys("Python")
