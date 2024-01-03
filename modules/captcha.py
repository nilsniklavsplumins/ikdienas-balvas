import os
from twocaptcha import TwoCaptcha

apikey_2captcha = os.getenv("APIKEY_2CAPTCHA")
if apikey_2captcha is None:
    raise Exception("APIKEY_2CAPTCHA nav atrasts")
captcha_solver = TwoCaptcha(apikey_2captcha)

def get_solver():
    return captcha_solver