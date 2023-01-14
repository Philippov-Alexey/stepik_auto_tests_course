from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # заполняем поля
    input1 = browser.find_element(By.XPATH, '/html/body/div/form/div/input[1]')
    input1.send_keys("Name")
    input2 = browser.find_element(By.XPATH, '/html/body/div/form/div/input[2]')
    input2.send_keys("Family_Name")
    input3 = browser.find_element(By.XPATH, '/html/body/div/form/div/input[3]')
    input3.send_keys("e-mail@gmail.com")

    # прикрепляем файл
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = "Privet.txt"
    file_path = os.path.join(current_dir, file_name)
    print(file_path)
    element = browser.find_element(By.CSS_SELECTOR, "[type='file']")
    element.send_keys(file_path)

    # жмем кнопку "Submit"
    sub = browser.find_element(By.XPATH, '/html/body/div/form/button')
    sub.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
