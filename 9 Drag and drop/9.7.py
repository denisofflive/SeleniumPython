import time
from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/draganddrop/3/index.html')
    time.sleep(1)
    drag = browser.find_element(By.ID, 'block1')
    actions = ActionChains(browser)
    lst = [10]*400
    actions.click_and_hold(drag)
    for x in lst:
        actions.move_by_offset(x, 0)
    actions.perform()
    time.sleep(3)
