import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.saucedemo.com")
time.sleep(3)
login_input = driver.find_element(by=By.ID, value="user-name")
login_input.send_keys("standard_user")

pass_input = driver.find_element(by=By.ID, value="password")
pass_input.send_keys("secret_sauce")

button_auth = driver.find_element(by=By.ID, value="login-button")
button_auth.click()

buttons_add = driver.find_elements(by=By.CLASS_NAME, value="btn_primary")
print(len(buttons_add))
for button in buttons_add:
    button.click()
    time.sleep(1)

basket_shop = driver.find_element(by=By.CLASS_NAME, value="shopping_cart_link")
basket_shop.click()
time.sleep(3)

checkout_button = driver.find_element(by=By.ID, value="checkout")
checkout_button.click()
time.sleep(2)

driver.quit()
