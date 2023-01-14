from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # считываем число
    number = browser.find_element(By.ID, "treasure")
    x = number.get_attribute("valuex")
    print(x)
    # вычисляем по формуле
    y = calc(x)
    print(y)
    # заполняем поле значением вычисленного числа
    answer = browser.find_element(By.XPATH, '//*[@id="answer"]')
    answer.send_keys(y)

    # ставим галку в чекбоксе
    checkbox = browser.find_element(By.XPATH, '//*[@id="robotCheckbox"]')
    checkbox.click()

    # выбираем вариант в радиобатоне
    radio = browser.find_element(By.XPATH, '//*[@id="robotsRule"]')
    radio.click()

    # жмем кнопку "Submit"
    sub = browser.find_element(By.XPATH, '/html/body/div/form/div/div/button')
    sub.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
