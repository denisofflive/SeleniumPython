from selenium import webdriver
from selenium.webdriver.common.by import By

link = 'https://parsinger.ru/selenium/5.7/1/index.html'

with webdriver.Chrome() as driver:
    driver.get(link)
    for element in driver.find_elements(By.CLASS_NAME, 'button-container'):
        driver.execute_script("return arguments[0].scrollIntoView(true);", element)
        element.click()
    print(driver.switch_to.alert.text)