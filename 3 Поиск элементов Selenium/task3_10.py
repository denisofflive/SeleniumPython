from selenium.webdriver.common.by import By
from selenium import webdriver

"""
Операция "Выпадающие списки"
Приветствую, агенты-разработчики! Сегодня наша миссия — "Операция 'Выпадающие списки'".
В этой операции мы сталкиваемся с нечто большим, чем просто чек-боксы или текстовые поля.
Мы имеем дело с выпадающим списком, содержащим ключи к секретному хранилищу данных.

Задачи
Вход в Кодовую Комнату: Откройте сайт с помощью Selenium.
Извлечение Ключей: Получите значения всех элементов выпадающего списка.
Дешифровка Кода: Сложите (плюсуйте) все извлеченные значения.
Использование Кода: Вставьте получившийся результат в поле на сайте и нажмите кнопку.
Получение Конечного Результата: Копируйте длинное число, которое появится после нажатия на кнопку.
"""

with webdriver.Chrome() as browser:
    browser.get('http://parsinger.ru/selenium/7/7.html')
    result = 0
    for el in browser.find_elements(By.TAG_NAME, 'option'):
        result += int(el.text)
    browser.find_element(By.ID, 'input_result').send_keys(result)
    browser.find_element(By.CLASS_NAME, 'btn').click()
    print("Число:", browser.find_element(By.ID, 'result').text)
