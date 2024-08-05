from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # считываем число
    # x_element = browser.find_element(By.XPATH, '//*[@id="input_value"]')
    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text
    print(x)

    # вычисляем по формуле
    y = calc(x)
    print(y)

    # заполняем поле значением вычисленного числа
    # answer = browser.find_element(By.XPATH, '//*[@id="answer"]')
    answer = browser.find_element(By.ID, 'answer')
    browser.execute_script("return arguments[0].scrollIntoView(true);", answer)  # скролим до элемента
    answer.send_keys(y)

    # ставим галку в чекбоксе
    # checkbox = browser.find_element(By.XPATH, '//*[@id="robotCheckbox"]')
    checkbox = browser.find_element(By.ID, 'robotCheckbox')
    browser.execute_script("return arguments[0].scrollIntoView(true);", checkbox)  # скролим до элемента
    checkbox.click()

    # выбираем вариант в радиобатоне
    radio = browser.find_element(By.CSS_SELECTOR, '[for="robotsRule"]')
    browser.execute_script("return arguments[0].scrollIntoView(true);", radio)  # скролим до элемента
    radio.click()

    # жмем кнопку "Submit"
    # sub = browser.find_element(By.XPATH, '/html/body/div/form/button')
    sub = browser.find_element(By.CSS_SELECTOR, 'body > div > form > button')
    browser.execute_script("return arguments[0].scrollIntoView(true);", sub)  # скролим до элемента
    sub.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
