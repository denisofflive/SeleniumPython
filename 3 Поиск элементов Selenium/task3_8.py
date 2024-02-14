import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

"""
Операция 'Кодовый Замок 
Добро пожаловать, агенты! Сегодня перед нами стоит задача не просто извлечь данные,
но и взаимодействовать с интерфейсом веб-сайта, чтобы добраться до скрытой информации.
Представьте, что перед вами замок с комбинацией в виде чек-боксов.
Ваша миссия — активировать все чек-боксы и открыть секретный компартмент, в котором хранится нужная нам информация.

Задачи
Взлом Кодового Замка: Откройте веб-сайт с помощью Selenium.
Активация Чек-боксов: Найдите все чек-боксы на странице и установите их в положение checked с помощью .click().
Открывание Секрета: Как только все чек-боксы будут активированы, нажмите на кнопку.
Доступ к Секретным Данным: Скопируйте число, которое появится в теге <p id="result">Result</p>.
"""

# URL веб-страницы для парсинга
url = 'https://parsinger.ru/selenium/4/4.html'
# Инициализируем драйвер Chrome
with webdriver.Chrome() as browser:
    # Открываем веб-страницу по заданному URL
    browser.get(url)
    # Находим все чек-боксы по имени класса и кликаем по ним -  устанавливаем их в положение checked
    [x.click() for x in browser.find_elements(By.CLASS_NAME, 'check')]
    # Кликаем по кнопке "Отправить"
    browser.find_element(By.CLASS_NAME, 'btn').click()
    # Считываем и выводим result на экран
    print("Результат:", browser.find_element(By.ID, 'result').text)
    time.sleep(3)

