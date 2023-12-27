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

secret = json.load(open("secret.json", "r"))

def claimAllkeyshop():
    url = "https://www.allkeyshop.com/blog/reward-program/"
    wait = WebDriverWait(driver, timeout=5)

    driver.get(url)
    time.sleep(2)

    discord_login = driver.find_elements(By.CLASS_NAME, "theChampDiscordLogin")[1]
    driver.execute_script("arguments[0].click()", discord_login)
    time.sleep(2)

    username = driver.find_element(By.NAME, "email")
    password = driver.find_element(By.NAME, "password")
    username.clear()
    username.send_keys(next(account["username"] for account in secret if account["id"] == "discord"))
    password.clear()
    password.send_keys(next(account["password"] for account in secret if account["id"] == "discord"))
    login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    login_button.click()
    time.sleep(2)

    totp_field = driver.find_element(By.CSS_SELECTOR, "input[autocomplete='one-time-code']")
    totp_field.clear()
    totp = pyotp.TOTP(next(account["totp"] for account in secret if account["id"] == "discord")).now()
    totp_field.send_keys(totp)
    confirm_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    wait.until(lambda d: confirm_button.is_enabled())
    confirm_button.click()
    time.sleep(1)

    authorize_button = driver.find_element(By.CSS_SELECTOR, ".button_afdfd9.lookFilled__19298.colorBrand_b2253e.sizeMedium_c6fa98.grow__4c8a4")
    wait.until(lambda d: authorize_button.is_enabled())
    authorize_button.click()
    time.sleep(10)

    for i in range(2):
        driver.refresh()
        time.sleep(2)

    for i in range(2):
        spin = driver.find_element(By.CLASS_NAME, "wheel")
        for i in range(3):
            spin.click()
            time.sleep(0.5)
        time.sleep(5)

    time.sleep(10)

#claimAllkeyshop()