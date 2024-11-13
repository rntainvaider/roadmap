# import undetected_chromedriver as uc

# options = uc.ChromeOptions()
# # options.headless = True
# # options.add_argument( '--headless' )
# chrome = uc.Chrome()
# chrome.get(
#     "https://datadome.co/customers-stories/toppreise-ends-web-scraping-and-content-theft-with-datadome/"
# )


import codecs
import sys
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

algorithm = {
    1: {
        "find": "rfytdcrbq",
        "watch": "20",
        "count_comments": 5,
    }
}

options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)
try:
    driver.get("https://rutube.ru/")
    time.sleep(10)
    driver.get_screenshot_as_file("images/rutube_video.png")
except Exception as error:
    print(f"Critical error: {error}")
finally:
    driver.quit()
