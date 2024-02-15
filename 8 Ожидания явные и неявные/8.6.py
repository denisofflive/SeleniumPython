from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

URL = "https://parsinger.ru/selenium/5.9/5/index.html"


class Locators:
    box_button = By.CLASS_NAME, "box_button"
    close_btn = By.ID, "close_ad"


def wait_quiz() -> str:
    with webdriver.Chrome() as browser:
        browser.get(URL)
        code_parts = []
        boxes = browser.find_elements(*Locators.box_button)
        ad_close_btn = browser.find_element(*Locators.close_btn)
        for box in boxes:
            box.click()
            ad_close_btn.click()
            WebDriverWait(browser, 10).until(lambda _: box.text != '')
            code_parts.append(box.text)
        return '-'.join(code_parts)


print(wait_quiz())
