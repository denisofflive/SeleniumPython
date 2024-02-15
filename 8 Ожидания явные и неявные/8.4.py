from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Создаем экземпляр драйвера
driver = webdriver.Chrome()
# Заходим на сайт
driver.get("https://parsinger.ru/selenium/5.9/2/index.html")
# Ждем, пока появится блок с ID "qQm9y1rk"
wait = WebDriverWait(driver, 130)
block = wait.until(EC.presence_of_element_located((By.ID, "qQm9y1rk")))
# Кликаем по блоку
block.click()
# Ждем появления alert-окна
alert = wait.until(EC.alert_is_present())
# Получаем текст из alert-окна
secret_code = alert.text
# Выводим секретный код
print(f"Секретный код: {secret_code}")
# Подтверждаем alert-окно
alert.accept()
# Закрываем браузер
driver.quit()
