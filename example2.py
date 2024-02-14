# import time
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# # Открыть страницу
# driver = webdriver.Chrome()
# driver.get("https://parsinger.ru/window_size/2/index.html")

# window_size_x = [616, 648, 680, 701, 730, 750, 805, 820, 855, 890, 955, 1000]
# window_size_y = [300, 330, 340, 388, 400, 421, 474, 505, 557, 600, 653, 1000]
#
# driver = webdriver.Chrome()
#
# for x in window_size_x:
#     for y in window_size_y:
#         driver.set_window_size(x, y)
#         time.sleep(2)
#         result_element = driver.find_element('id', 'result')
#         print(result_element.text)
#
# driver.quit()


# # Установить размер окна браузера
# window_size_x = 616+16
# window_size_y = 300 + 138
# driver.set_window_size(window_size_x, window_size_y)
#
# result = driver.find_element('xpath', "//span[@id='result']").text
# print(result)
#
# time.sleep(20)

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time
import itertools

from selenium.webdriver.common.by import By

window_size_x = [516, 648, 680, 701, 730, 750, 805, 820, 855, 890, 955, 1000]
window_size_y = [270, 300, 340, 388, 400, 421, 474, 505, 557, 600, 653, 1000]


def apply_window_sizes():
    # Установка сервиса ChromeDriver
    service = Service()

    # Установка настроек браузера
    options = Options()
    options.add_argument("--start-maximized")

    # Инициализация объекта WebDriver
    driver = webdriver.Chrome(service=service, options=options)

    # Открытие сайта
    driver.get('https://parsinger.ru/window_size/2/index.html')

    # Получение всех сочетаний размеров окна
    window_sizes = list(itertools.product(window_size_x, window_size_y))

    # Изменение размера окна и проверка содержимого элемента с id="result"
    for size_x in window_size_x:
        for size_y in window_size_y:
            driver.set_window_size(16 + size_x, 138 + size_y)
            # time.sleep(1)  # Задержка, чтобы страница успевала загрузиться
            result_element = driver.find_element(By.ID, 'result')
            print(f'Window size: {size_x}, {size_y} Result: {result_element.text}')
            # print('{'  f"'width': {size_x}, 'height': {size_y}"  '}')

    # Закрытие браузера
    driver.quit()


apply_window_sizes()
