import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from twocaptcha import TwoCaptcha

api_key = "b26c1cfaf4386620ee694aacc0e24897"
driver = webdriver.Chrome()
solver = TwoCaptcha(api_key)

try:
    driver.get("https://2captcha.com/demo/recaptcha-v2")
    time.sleep(10)
    site_key = driver.find_element(by=By.ID, value="g-recaptcha").get_attribute("data-sitekey")
    result_dey = solver.
    print(site_key)
except Exception as error:
    print(f"Critical error: {error}")
finally:
    driver.quit()


#
#
# import sys
# import os
#
# sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
#
#
#
# api_key = os.getenv('APIKEY_2CAPTCHA', 'YOUR_API_KEY')
#
# solver = TwoCaptcha(api_key)
#
# try:
#     result = solver.recaptcha(
#         sitekey='6LfD3PIbAAAAAJs_eEHvoOl75_83eXSqpPSRFJ_u',
#         url='https://2captcha.com/demo/recaptcha-v2')
#
# except Exception as e:
#     sys.exit(e)
#
# else:
#     sys.exit('solved: ' + str(result))
