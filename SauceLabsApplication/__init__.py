from typing import Any

from selenium.webdriver import Keys
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

# code to maximize screen
chrome_options = Options()
chrome_options.add_argument("--start-maximized")

#Location to chromedriver
service = Service(r"C:\Users\lenevo\Pictures\chromedriver-win64")

#initialize the driver
driver = webdriver.Chrome(service=service, options=chrome_options)

#open SauceLabs
driver.get("https://sauce-demo.myshopify.com/")
time.sleep(50)

UserName= "//input[@id='idToken1']"
EC.visibility_of_element_located()
driver.find_element(By.XPATH,UserName).clear()
driver.find_element(By.XPATH,UserName).send_keys("")

