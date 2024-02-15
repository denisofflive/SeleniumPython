from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

link = 'https://parsinger.ru/selenium/5.9/6/index.html'

with webdriver.Chrome() as driver:
    driver.get(link)
    WebDriverWait(driver, poll_frequency=0.01, timeout=5).until(
        EC.element_located_to_be_selected((By.ID, 'myCheckbox')))
    driver.find_element(By.TAG_NAME, 'button').click()
    print("Секретный код:", driver.find_element(By.ID, 'result').text)
