from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

URL = "http://secure-retreat-92358.herokuapp.com/"

driver = webdriver.Edge()

driver.get(URL)

name_field = driver.find_element(By.NAME, "fName")
name_field.send_keys("Gabs")

lastname_field = driver.find_element(By.NAME, "lName")
lastname_field.send_keys("Bergs")

email_field = driver.find_element(By.NAME, "email")
email_field.send_keys("gabs@bergs.com")

button = driver.find_element(By.TAG_NAME, "button")
button.click()
