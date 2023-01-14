from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = 'http://suninjuly.github.io/redirect_accept.html'
    browser = webdriver.Chrome()
    browser.get(link)

    # жмем летающую кнопку
    but = browser.find_element(By.XPATH, '/html/body/form/div/div/button')
    but.click()

    # получаем список открытых вкладок и переключаемся на открывшееся окно
    second_window = browser.window_handles[1]
    browser.switch_to.window(second_window)

    # считываем число
    x_element = browser.find_element(By.XPATH, '//*[@id="input_value"]')
    x = x_element.text
    print(x)

    # вычисляем по формуле
    y = calc(x)
    print(y)

    # заполняем поле значением вычисленного числа
    answer = browser.find_element(By.XPATH, '//*[@id="answer"]')
    answer.send_keys(y)

    # жмем кнопку "Submit"
    sub = browser.find_element(By.XPATH, '/html/body/form/div/div/button')
    sub.click()

    # считываем из всплывающего окна "правильный ответ"
    res = browser.switch_to.alert
    print(res.text)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта (в принципе уже не нужно, так ответ мы уже
    # прочитали)
    time.sleep(1)
    # закрываем браузер после всех манипуляций
    browser.quit()
