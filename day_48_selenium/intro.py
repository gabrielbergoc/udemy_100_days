from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "https://www.python.org/"

driver = webdriver.Edge()

driver.get(URL)

# events_list = driver.find_element(By.XPATH, '//*[@id="content"]/div/section/div[3]/div[2]/div/ul')
# event_times = events_list.find_elements(By.TAG_NAME, "time")
# event_titles = events_list.find_elements(By.TAG_NAME, "a")

event_times = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
event_titles = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")

events = []
for time, event in zip(event_times, event_titles):
    events.append({"time": time.text, "event": event.text})

print(events)
