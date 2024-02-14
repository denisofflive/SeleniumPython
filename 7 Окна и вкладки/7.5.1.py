import time
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('http://parsinger.ru/blank/modal/2/index.html')
    time.sleep(.5)

    for button in browser.find_elements(By.CLASS_NAME, 'buttons'):
        button.click()
        browser.switch_to.alert.accept()
        result = browser.find_element(By.ID, 'result').text
        if result:
            print("Результат:", result)
            break
