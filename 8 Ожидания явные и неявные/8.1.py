from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
url = 'http://parsinger.ru/expectations/3/index.html'
with webdriver.Chrome() as browser:
    browser.get(url)
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, "btn"))).click()
    if WebDriverWait(browser, 20).until(EC.title_is('345FDG3245SFD')):
        print("Результат:", browser.find_element(By.ID, 'result').text)

