from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains, ScrollOrigin
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


link = 'https://parsinger.ru/selenium/5.7/4/index.html'

with webdriver.Chrome() as driver:
    driver.get(link)
    driver.fullscreen_window()
    main_container = driver.find_element(By.ID, 'main_container')
    scroll_origin = ScrollOrigin.from_element(main_container)

    for _ in range(10):
        ActionChains(driver).scroll_from_origin(scroll_origin, 0, 1000).perform()
        WebDriverWait(driver, 5).until(
            EC.invisibility_of_element_located((By.CLASS_NAME, 'spinner')))

    for element in driver.find_elements(By.TAG_NAME, 'input'):
        if int(element.get_attribute('value')) % 2 == 0:
            element.click()

    driver.find_element(By.CLASS_NAME, 'alert_button').click()
    print("Результат:", driver.switch_to.alert.text)
