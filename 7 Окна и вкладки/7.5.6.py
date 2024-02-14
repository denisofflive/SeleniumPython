from selenium.webdriver.common.by import By
from selenium import webdriver

url = 'http://parsinger.ru/window_size/2/index.html'
size_x = [516, 648, 680, 701, 730, 750, 805, 820, 855, 890, 955, 1000]
size_y = [270, 300, 340, 388, 400, 421, 474, 505, 557, 600, 653, 1000]

with webdriver.Chrome() as browser:
    browser.get(url)

    for x in size_x:
        for y in size_y:
            browser.set_window_size(16 + x, 138 + y)
            if browser.find_element(By.ID, 'result').text.isdigit():
                print('{'  f"'width': {x}, 'height': {y}"  '}')
