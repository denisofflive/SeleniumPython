from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains, ScrollOrigin
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

URL = 'https://parsinger.ru/infiniti_scroll_2/'

with webdriver.Chrome() as browser:
    browser.get(URL)

    # атрибут top этого элемента будет меняться при прокрутке
    scroll_container = browser.find_element(By.XPATH, '//div[@id="scroll-container"]/div')
    scroll_origin = ScrollOrigin.from_element(scroll_container)

    for _ in range(6):
        ActionChains(browser) \
            .scroll_from_origin(scroll_origin, 0, 1000) \
            .perform()

        # ждём, пока пропадёт спиннер подгрузки (вместо time.sleep)
        WebDriverWait(browser, 5).until(
            EC.invisibility_of_element_located((By.CLASS_NAME, 'spinner')))

    numbers = browser.find_elements(By.XPATH, '//div[@id="scroll-container"]/p')
    res = sum(int(num.text) for num in numbers)
    print(res)
