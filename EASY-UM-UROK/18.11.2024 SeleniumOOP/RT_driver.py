# тело парсера
import json
import os
import pickle
import time
from datetime import datetime

import undetected_chromedriver as uc
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from undetected_chromedriver import ChromeOptions


class RTDriver:
    def __init__(self):
        self.cookie = None
        self.options = ChromeOptions()
        self.options.add_argument("--disable-blink-features=AutomationControlled")
        self.options.add_argument("--disable-notifications")
        self.options.add_argument("--mute-audio")
        self.options.add_argument("--user-data-dir=hash")
        self.options.add_argument("--disable-gpu")
        self.options.add_argument("--incognito")
        self.options.add_argument("--disable-dev-shm-usage")
        self.__driver = uc.Chrome(options=self.options, use_subprocess=False, version_main=130)

    def save_cookies(self, filename="cookies.json"):
        """Saves cookies to a JSON file."""
        try:
            with open(filename, "wb") as f:
                pickle.dump(self.cookies, f)
            print(f"Cookies saved to {filename}")
        except Exception as e:
            print(f"Error saving cookies: {e}")

    def load_cookies(self):
        """Loads cookies from a JSON file."""
        try:
            with open("cookies.json", "rb") as f:
                self.cookies = pickle.load(f)
            print(f"Cookies loaded from cookies.json")
        except FileNotFoundError:
            print(f"Cookie file cookies.json not found. No cookies loaded.")
            self.cookies = []  # Initialize as empty list if file not found.
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON in cookies.json: {e}")
            self.cookies = []  # Initialize as empty list if invalid JSON

    def get_link(self, link):
        print(f"Getting link: {link}")
        self.__driver.get(link)
        time.sleep(5)
        self.get_screenshot()

    def get_screenshot(self):
        today_dirname = str(datetime.now()).split(" ")[0]
        now_filename = str(datetime.now()).split(" ")[1]
        image_dir = os.path.join("screenshots", f"{today_dirname}")  # screenshots/2022-08-17
        os.makedirs(image_dir, exist_ok=True)
        file_name = f"{now_filename}.png"
        screenshot_path = os.path.join(
            image_dir, file_name
        )  # screenshots/2022-08-17/2022-08-17.png
        self.__driver.save_screenshot(screenshot_path)
        print(f"Screenshot saved to {screenshot_path}")

    def login_to_rutube(self):
        self.__driver.find_element(
            by=By.CLASS_NAME, value="wdp-header-auth-button-module__wrapper"
        ).click()
        time.sleep(3)
        phone_or_email_login = self.__driver.find_element(by=By.ID, value="phone-or-email-login")
        phone_or_email_login.send_keys("79108649172")
        button_continue = self.__driver.find_element(by=By.ID, value="submit-login-continue")
        button_continue.click()
        time.sleep(3)
        sms = input("Enter sms code: ")  # 1765 [0] -> 1, [1] -> 7, [2] -> 6, [3] -> 5
        for count in range(4):
            self.__driver.find_element(by=By.NAME, value=f"{count}").send_keys(sms[count])
        time.sleep(3)
        self.cookie = self.__driver.get_cookies()
        self.__driver.save_screenshot("cookies.json")

    def find_video(self, video_name):
        search_input = self.__driver.find_element(
            by=By.CLASS_NAME, value="wdp-header-search-module__input"
        )
        search_input.send_keys(video_name)
        search_input.send_keys(Keys.ENTER)
        time.sleep(3)
        self.get_screenshot()

    def quit(self):
        self.__driver.close()
        print(f"Driver quit")
