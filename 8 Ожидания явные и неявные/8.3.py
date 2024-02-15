from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Создаем экземпляр драйвера
driver = webdriver.Chrome()
# Открываем страницу
driver.get("https://parsinger.ru/expectations/6/index.html")
# Находим и нажимаем кнопку
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "btn"))).click()

# Ожидаем появления элемента с классом "bmh21yy"
locator = (By.XPATH, "//div[@class='BMH21YY']")
element = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, 'BMH21YY')))

# Выводим результат
print("Результат:", element.text)

# Закрываем драйвер
driver.quit()

