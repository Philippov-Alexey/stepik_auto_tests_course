from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = 'http://suninjuly.github.io/get_attribute.html'
    browser = webdriver.Chrome()
    browser.get(link)

    # text = browser.find_element(By.CSS_SELECTOR, 'body > div > form > div > div > div:nth-child(1) > h2 > span').text
    # print(text)

    # считываем число
    number = browser.find_element(By.ID, 'treasure')
    x = number.get_attribute('valuex')
    print(x)
    # вычисляем по формуле
    y = calc(x)
    print(y)
    # заполняем поле значением вычисленного числа
    # answer = browser.find_element(By.XPATH, '//*[@id="answer"]')
    answer = browser.find_element(By.ID, 'answer')
    answer.send_keys(y)

    # ставим галку в чекбоксе
    # checkbox = browser.find_element(By.XPATH, '//*[@id="robotCheckbox"]')
    checkbox = browser.find_element(By.ID, 'robotCheckbox')
    checkbox.click()

    # выбираем вариант в радиобатоне
    # radio = browser.find_element(By.XPATH, '//*[@id="robotsRule"]')
    radio = browser.find_element(By.ID, 'robotsRule')
    radio.click()

    # жмем кнопку "Submit"
    # sub = browser.find_element(By.XPATH, '/html/body/div/form/div/div/button')
    sub = browser.find_element(By.CSS_SELECTOR, 'body > div > form > div > div > button')
    sub.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
