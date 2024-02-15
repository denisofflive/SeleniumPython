from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


with webdriver.Chrome() as browser:
    browser.get(url='https://parsinger.ru/draganddrop/3/index.html')
    actions = ActionChains(browser)

    block = browser.find_element(By.ID, 'block1')
    actions.click_and_hold(block).perform()

    for point in browser.find_elements(By.CLASS_NAME, 'controlPoint'):
        actions.move_to_element(point).perform()

    actions.click(block).perform()
    print("Секретный код:", browser.find_element(By.ID, 'message').text)

