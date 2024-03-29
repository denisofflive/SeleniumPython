from selenium import webdriver
from selenium.webdriver.common.by import By

"""
Поход за сокровищами в Цифровом Лабиринте
Привет, юные искатели данных и загадок! Перед вами лежит миссия, которая проверит ваше умение внимательно
 "читать" веб-страницы и извлекать из них нужную информацию.
 На таинственной странице скрыты фрагменты артефакта — всего их 100.
 Они зашифрованы и размещены во вторых абзацах каждого из 200 блоков текста.
 Ваша задача — собрать их и воссоздать артефакт.

Задачи
Вход в Цифровой Лабиринт: Используйте Selenium для открытия указанного веб-сайта.
Извлечение Фрагментов: Найдите и извлеките данные из каждого второго тега <p> на странице.
Воссоздание Артефакта: Просуммируйте все числовые значения, полученные из этих тегов.
Ключ к Загадке: Запишите полученную сумму в предназначенное для этого поле или выведите на экран.
"""

# URL веб-страницы для парсинга
url = 'https://parsinger.ru/selenium/3/3.html'
# Инициализируем драйвер Chrome
with webdriver.Chrome() as browser:
    # Открываем веб-страницу по заданному URL
    browser.get(url)
    # Переменной result присваиваем переменную x, считываем функцией text число, прогоняем в цикле через поиск элемента
    print("Сумма чисел:", sum([int(x.text) for x in browser.find_elements(By.XPATH, "//div[@class='text']/p[2]")]))
    # Закрываем браузер
    browser.quit()
