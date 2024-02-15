import time
from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/draganddrop/2/index.html')
    time.sleep(1)
    drag = browser.find_element(By.ID, 'draggable')
    actions = ActionChains(browser)
    bloks = browser.find_elements(By.CLASS_NAME, "box")
    for x in bloks:
        actions.drag_and_drop(drag, x).perform()
    print("Секретный код:", browser.find_element(By.ID, 'message').text)

