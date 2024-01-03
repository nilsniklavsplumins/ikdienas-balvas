import datetime
import pyotp

def claimAllkeyshop(sb, secret):
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
    sb.sleep(1)
    if "Invalid two-factor code" in sb.get_page_source():
        sb.clear("input[autocomplete='one-time-code']")
        sb.type("input[autocomplete='one-time-code']", pyotp.TOTP(totp_secret).at(datetime.datetime.now(), counter_offset=1))
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