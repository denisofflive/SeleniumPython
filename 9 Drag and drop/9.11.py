from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = 'https://parsinger.ru/selenium/5.10/4/index.html'
options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
with webdriver.Chrome(options=options) as driver:
    driver.get(url)
    time.sleep(5)
    elements = driver.find_elements(By.CLASS_NAME, 'ball_color')
    targets = driver.find_elements(By.CLASS_NAME, 'basket_color')

    action = ActionChains(driver)

    for element in sorted(elements, key=lambda x: x.value_of_css_property('background-color')):
        element_color = element.value_of_css_property('background-color')

        for target in sorted(targets, key=lambda x: x.value_of_css_property('background-color')):
            target_color = target.value_of_css_property('background-color')
            if element_color == target_color:
                action.drag_and_drop(element, target).perform()
                break

    print("Секретный код:", WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, 'message'))).text)
