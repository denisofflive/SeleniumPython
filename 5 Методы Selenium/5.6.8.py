
"""
Числовая Добыча: Операция 'Чекбокс'
Привет, исследователи данных и веб-магистры! Сегодня перед нами стоит задача,
которая требует от нас не только технических навыков, но и умения быстро анализировать ситуацию на лету.
Эта задача имитирует реальный сценарий, где не всё так просто, как кажется на первый взгляд.
Нам нужно будет применить наши навыки веб-парсинга, чтобы выделить конкретные данные из большого массива.

Задачи
Случайная Локация: Откройте указанный сайт с помощью Selenium.
Здесь вас встретят 100 текстовых полей, и рядом с некоторыми из них будут чекбоксы.
Главная загвоздка: чекбоксы и их состояние ("checked" или нет) определяются случайным образом.

Числовая Сборка: Пройдитесь по всем 100 текстовым полям и соберите числа только из тех,
которые имеют рядом "checked" чекбоксы.

Особенности и Условности
Поля и чекбоксы могут загружаться в разных комбинациях, поэтому рассчитывать на конкретную последовательность
или паттерн не стоит.

Чекбоксы могут быть в двух состояниях: checked (отмечены) и unchecked (не отмечены).
Мы интересуемся только числами из полей с отмеченными чекбоксами.

Собранные числа необходимо суммировать и полученный результат вставить в поле ответа степик.
"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# Открываем сайт
driver = webdriver.Chrome()
driver.get("https://parsinger.ru/selenium/5.5/3/1.html")
time.sleep(0.3)

nums = []
for div in driver.find_elements(By.CLASS_NAME, "parent"):
    if div.find_element(By.CLASS_NAME, "checkbox").is_selected():
        nums.append(int(div.find_element(By.TAG_NAME, "textarea").text))
print("Результат:", sum(nums))
