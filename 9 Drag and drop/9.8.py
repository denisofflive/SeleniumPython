from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

url = "https://parsinger.ru/selenium/5.10/2/index.html"

with webdriver.Chrome() as driver:
    # Переходим на сайт
    driver.get(url)

    # Ожидаем загрузки страницы (в реальном коде лучше использовать WebDriverWait)
    time.sleep(2)

    # Находим все элементы, которые нужно перетащить
    draggable_elements = driver.find_elements(By.CLASS_NAME, "draganddrop")

    # Находим целевой элемент (серую зону)
    target_element = driver.find_element(By.CLASS_NAME, "draganddrop_end")

    # Инициализируем объект ActionChains
    actions = ActionChains(driver)

    # Перетаскиваем каждый элемент
    for draggable in draggable_elements:
        actions.drag_and_drop(draggable, target_element).perform()
        # Ожидаем завершения анимации перетаскивания (в реальном коде лучше использовать WebDriverWait)
        time.sleep(0.1)

    # Получаем и выводим сообщение
    message = driver.find_element(By.ID, "message").text
    print("Секретный код:", message)
