def verify_success(sb):
    sb.assert_element("#user_email", timeout=8)
    sb.sleep(4)

def claimCoinGecko(sb, secret):
    url = "https://www.coingecko.com/account/candy"
        
    sb.open(url)
    sb.maximize_window()

    try:
        verify_success(sb)
    except Exception:
        if sb.is_element_visible('input[value*="Verify"]'):
            sb.click('input[value*="Verify"]')
        elif sb.is_element_visible('iframe[title*="challenge"]'):
            sb.switch_to_frame('iframe[title*="challenge"]')
            sb.click("span.mark")
        else:
            raise Exception("Neizdevās apiet Cloudflare!")
        try:
            verify_success(sb)
        except Exception:
            raise Exception("Neizdevās apiet Cloudflare!")

    sb.clear("#user_email")
    sb.type("#user_email", next(account["username"] for account in secret if account["id"] == "coingecko"))
    sb.clear("#user_password")
    sb.type("#user_password", next(account["password"] for account in secret if account["id"] == "coingecko"))
    sb.click("button[type='submit']")
    sb.sleep(1)

    sb.click("button[type='submit']")