def claimCoinGecko(sb, secret):
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