from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

login = "*****"
password = "****#"


def auto_log_in() -> None:
    driver = webdriver.Chrome()
    driver.get("https://passport.yandex.ru/auth/")

    time.sleep(5)

    elem_input_login = driver.find_element(By.NAME, "login")
    elem_input_login.clear()
    elem_input_login.send_keys(login)
    elem_input_login.send_keys(Keys.ENTER)

    time.sleep(5)

    elem_input_password = driver.find_element(By.NAME, "passwd")
    elem_input_password.clear()
    elem_input_password.send_keys(password)
    elem_input_password.send_keys(Keys.RETURN)

    time.sleep(40)


auto_log_in()
