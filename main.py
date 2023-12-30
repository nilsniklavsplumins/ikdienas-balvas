import json
import pyotp
from seleniumbase import SB
import os
from twocaptcha import TwoCaptcha

secret = json.load(open("secret.json", "r"))

apikey_2captcha = os.getenv("APIKEY_2CAPTCHA")
captcha_solver = TwoCaptcha(apikey_2captcha)

def claimAllkeyshop(sb):
    url = "https://www.allkeyshop.com/blog/reward-program/"

    sb.open(url)
    sb.maximize_window()
    sb.js_click(".theChampDiscordLogin")

    sb.clear("email", by="name")
    sb.type("email", next(account["username"] for account in secret if account["id"] == "discord"), by="name")
    sb.clear("password", by="name")
    sb.type("password", next(account["password"] for account in secret if account["id"] == "discord"), by="name")
    sb.click("button[type='submit']")

    sb.clear("input[autocomplete='one-time-code']")
    sb.type("input[autocomplete='one-time-code']", pyotp.TOTP(next(account["totp"] for account in secret if account["id"] == "discord")).now())
    sb.click("button[type='submit']")

    sb.click(".button_afdfd9.lookFilled__19298.colorBrand_b2253e.sizeMedium_c6fa98.grow__4c8a4")
    sb.sleep(5)

    sb.refresh()

    for i in range(2):
        sb.refresh()
        sb.sleep(2)
        for i in range(3):
            sb.click(".wheel")
            sb.sleep(0.5)
        sb.sleep(5)

def claimCoinGecko(sb):
    url = "https://www.coingecko.com/account/candy"
        
    sb.open(url)
    sb.maximize_window()

    sb.clear("#user_email")
    sb.type("#user_email", next(account["username"] for account in secret if account["id"] == "coingecko"))
    sb.clear("#user_password")
    sb.type("#user_password", next(account["password"] for account in secret if account["id"] == "coingecko"))
    sb.click("button[type='submit']")
    sb.sleep(1)

    sb.click("button[type='submit']")
    
def claimmsi(sb):
    url = "https://rewards.msi.com/earn"

    sb.open(url)
    sb.maximize_window()

    sb.click("Existing User Login", by="link text")
    sb.clear("email", by="name")
    sb.type("email", next(account["username"] for account in secret if account["id"] == "msi"), by="name")
    sb.clear("password", by="name")
    sb.type("password", next(account["password"] for account in secret if account["id"] == "msi"), by="name")

    captcha = sb.get_image_url("img[alt='Captcha']")
    try:
        result = captcha_solver.normal(captcha, minLen=6, maxLen=6)
    except Exception as e:
        print(e)
    sb.clear("captcha", by="name")
    sb.type("captcha", result["code"], by="name")

    sb.js_click("login_join_reward", by="name")
    sb.click("//span[.='Login']", by="xpath")
    sb.sleep(2)
    sb.refresh()

with SB(uc_cdp=True, guest_mode=True) as sb:
    claimAllkeyshop(sb)
    claimCoinGecko(sb)
    claimmsi(sb)
