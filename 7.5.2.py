import time
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('http://parsinger.ru/blank/modal/3/index.html')
    time.sleep(.5)

    for button in browser.find_elements(By.CLASS_NAME, 'buttons'):
        button.click()
        confirm = browser.switch_to.alert
        title = confirm.text
        confirm.accept()
        browser.find_element(By.ID, 'input').send_keys(title)
        browser.find_element(By.ID, 'check').click()
        result = browser.find_element(By.ID, 'result').text
        if result == 'Неверный пин-код':
            continue
        elif result != 'Неверный пин-код':
            print("Результат:", result)
            break
