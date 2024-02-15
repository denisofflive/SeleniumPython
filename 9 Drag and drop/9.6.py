import time
from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/draganddrop/1/index.html')
    time.sleep(3)
    drag = browser.find_element(By.XPATH, '//*[@id="draggable"]')
    final = browser.find_element(By.XPATH, '//*[@id="field2"]')
    actions = ActionChains(browser)

    actions.drag_and_drop(drag, final).perform()
    result = browser.find_element(By.ID, 'result').text
    print(result)
