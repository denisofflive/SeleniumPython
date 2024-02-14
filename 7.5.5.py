# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# link = 'http://parsinger.ru/window_size/2/index.html'
#
# options_chrome = webdriver.ChromeOptions()
# options_chrome.add_argument('--headless') ## Безголовый режим в браузере
#
# with webdriver.Chrome(options=options_chrome) as driver:
#     driver.get(link)
#     window_size_x = [616, 648, 680, 701, 730, 750, 805, 820, 855, 890, 955, 1000]
#     window_size_y = [300, 330, 340, 388, 400, 421, 474, 505, 557, 600, 653, 1000]
#     for x in window_size_x:
#         for y in window_size_y:
#             driver.set_window_size(x, y)
#             result = driver.find_element(By.ID, 'result').text
#             if len(result) > 0:
#                 print("Результат:", result)
#                 exit()

"""ВТОРОЙ СПОСОБ - ЗАПУСК В БРАУЗЕРЕ """

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
            try:
                result = browser.find_element(By.ID, 'result').text
                if result:
                    print("Результат:", result)
            except:
                pass
