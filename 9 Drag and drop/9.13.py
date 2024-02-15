from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Используйте контекстный менеджер для автоматического закрытия браузера
with webdriver.Chrome() as driver:
    # Перейти на сайт
    driver.get("https://parsinger.ru/selenium/5.10/6/index.html")

    # Получить список всех контейнеров слайдеров
    slider_containers = driver.find_elements(By.CLASS_NAME, "slider-container")

    for container in slider_containers:
        # Найти слайдер внутри контейнера
        slider = container.find_element(By.CLASS_NAME, "volume-slider")

        # Получить текущее и целевое значение слайдера
        current_value = int(slider.get_attribute("value"))
        target_value = int(container.find_element(By.CLASS_NAME, "target-value").text)

        # Передвигаем слайдер к целевому значению
        while current_value != target_value:
            if current_value < target_value:
                # Увеличиваем значение
                slider.send_keys(Keys.ARROW_RIGHT)
                current_value += 1
            else:
                # Уменьшаем значение
                slider.send_keys(Keys.ARROW_LEFT)
                current_value -= 1

    # Ожидаем появления сообщения в теге <p id="message"></p>
    message_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "message"))
    )

    # Копируем сообщение
    message = message_element.text
    print("Секретный код:", message)
