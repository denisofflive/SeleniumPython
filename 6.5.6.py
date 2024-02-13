from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

link = 'https://parsinger.ru/selenium/5.7/5/index.html'

with webdriver.Chrome() as driver:
    driver.get(link)
    for element in driver.find_elements(By.CLASS_NAME, 'timer_button'):
        ActionChains(driver).click_and_hold(element).pause(float(element.get_attribute('value'))).release(element).perform()
    print(driver.switch_to.alert.text)

