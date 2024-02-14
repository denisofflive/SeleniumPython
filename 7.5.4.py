from selenium import webdriver
from selenium.webdriver.common.by import By
with webdriver.Chrome() as browser:
    browser.get('http://parsinger.ru/window_size/1/index.html')
    browser.set_window_size(555 + 16, 555 + 138)
    print("Результат:", browser.find_element(By.ID, 'result').text)
