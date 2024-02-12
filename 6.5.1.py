from selenium.webdriver import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By

result = []
with webdriver.Chrome() as browser:
        browser.get('http://parsinger.ru/scroll/2/')

        for tag_input in browser.find_elements(By.TAG_NAME, 'input'):
            tag_input.send_keys(Keys.DOWN)
            tag_input.click()

        for x in browser.find_elements(By.TAG_NAME, 'span'):
            if x.text.isdigit():
                result.append(int(x.text))
print(sum(result))

