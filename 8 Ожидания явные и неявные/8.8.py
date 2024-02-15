from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/5.9/7/index.html')

    for container in browser.find_elements(By.CLASS_NAME, 'container'):
        checkbox = container.find_element(By.TAG_NAME, 'input')
        WebDriverWait(browser, 10, poll_frequency=0.1).until(EC.element_to_be_selected(checkbox))
        container.find_element(By.TAG_NAME, 'button').click()

    print("Секретный код:", browser.find_element(By.ID, 'result').text)
