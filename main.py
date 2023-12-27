import json
import time
import pyotp
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service()
option = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=option)
def claimAllkeyshop():
    url = "https://www.allkeyshop.com/blog/reward-program/"
    wait = WebDriverWait(driver, timeout=5)

    driver.get(url)
    time.sleep(2)

#claimAllkeyshop()