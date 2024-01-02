import json
import pyotp
from seleniumbase import SB
import os
from twocaptcha import TwoCaptcha

try:
    secret = json.load(open("secret.json", "r"))
except:
    raise Exception("secret.json nav atrasts")

apikey_2captcha = os.getenv("APIKEY_2CAPTCHA")
if apikey_2captcha is None:
    raise Exception("APIKEY_2CAPTCHA nav atrasts")
captcha_solver = TwoCaptcha(apikey_2captcha)

def claimAllkeyshop(sb):
    url = "https://www.allkeyshop.com/blog/reward-program/"
    
    try:
        username = next(account["username"] for account in secret if account["id"] == "discord")
        password = next(account["password"] for account in secret if account["id"] == "discord")
        totp_secret = next(account["totp"] for account in secret if account["id"] == "discord")
    except:
        raise Exception("kļūda discord pieejas datos")

    sb.open(url)
    sb.maximize_window()
    sb.js_click(".theChampDiscordLogin")

    sb.clear("email", by="name")
    sb.type("email", username, by="name")
    sb.clear("password", by="name")
    sb.type("password", password, by="name")
    sb.click("button[type='submit']")

    sb.clear("input[autocomplete='one-time-code']")
    sb.type("input[autocomplete='one-time-code']", pyotp.TOTP(totp_secret).now())
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

    try:
        captcha = sb.get_image_url("img[alt='Captcha']")
        result = captcha_solver.normal(captcha, minLen=6, maxLen=6)
    except Exception as e:
        print(e)
    sb.clear("captcha", by="name")
    sb.type("captcha", result["code"], by="name")

    sb.js_click("login_join_reward", by="name")
    sb.click("//span[.='Login']", by="xpath")
    sb.sleep(2)

status = {
    "allkeyshop": False,
    "coingecko": False,
    "msi": False
}

def prompt():
    os.system("cls")
    print("Izvēlieties, kuras balvas savākt.")
    print("1) Allkeyshop " + ("✅" if status["allkeyshop"] else "❌"))
    print("2) CoinGecko " + ("✅" if status["coingecko"] else "❌"))
    print("3) MSI " + ("✅" if status["msi"] else "❌"))
    choice = input("Ievadiet ciparu, burtu S (sākt) vai burtu A (sākt un savākt visu): ").lower().strip()
    match choice:
        case "s":
            start(status)
        case "a":
            start(True)
        case "1":
            status["allkeyshop"] = not status["allkeyshop"]
            prompt()
        case "2":
            status["coingecko"] = not status["coingecko"]
            prompt()
        case "3":
            status["msi"] = not status["msi"]
            prompt()
        case _:
            prompt()

def start(sites):
    with SB(uc_cdp=True, guest_mode=True) as sb:
        if type(sites) is bool:
            claimAllkeyshop(sb)
            claimCoinGecko(sb)
            claimmsi(sb)
        else:
            if sites["allkeyshop"]:
                claimAllkeyshop(sb)
            if sites["coingecko"]:
                claimCoinGecko(sb)
            if sites["msi"]:
                claimmsi(sb)

prompt()
