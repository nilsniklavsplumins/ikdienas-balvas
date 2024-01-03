from main import get_solver

def claimmsi(sb, secret):
    url = "https://rewards.msi.com/earn"
    captcha_solver = get_solver()

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