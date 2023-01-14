from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try:
    link = 'http://suninjuly.github.io/selects1.html'
    browser = webdriver.Chrome()
    browser.get(link)

    # считываем число
    x1_element = browser.find_element(By.ID, 'num1')
    x1 = x1_element.text
    x2_element = browser.find_element(By.ID, 'num2')
    x2 = x2_element.text
    print(x1, x2)

    # вычисляем сумму найденных чисел
    y = int(x1) + int(x2)
    print(y)

    # ищем значение в выпадающем списке
    select = Select(browser.find_element(By.TAG_NAME, 'select'))
    select.select_by_value(str(y))

    # жмем кнопку "Submit"
    sub = browser.find_element(By.XPATH, '/html/body/div/form/button')
    sub.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
