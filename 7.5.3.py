import time
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('http://parsinger.ru/blank/modal/4/index.html')
    pin_code = [x.text for x in browser.find_elements(By.CLASS_NAME, 'pin')]
    for pin in pin_code:
        browser.find_element(By.ID, 'check').click()
        confirm = browser.switch_to.alert
        time.sleep(.3)
        confirm.send_keys(pin)
        confirm.accept()
        result = browser.find_element(By.ID, 'result').text
        if result.isdigit():
            print("Результат:", result)
