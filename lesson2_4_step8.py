# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# browser = webdriver.Chrome()
#
# # говорим WebDriver искать каждый элемент в течение (до) 5 секунд
# browser.implicitly_wait(5)
#
# browser.get("http://suninjuly.github.io/wait1.html")
#
# button = browser.find_element(By.ID, "verify")
# button.click()
#
# message = browser.find_element(By.ID, "verify_message")
#
# assert "successful" in message.text

# --------------------------------------------------------------------
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
#
# browser = webdriver.Chrome()
#
# browser.get("http://suninjuly.github.io/wait2.html")
#
# # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
# button = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.ID, "verify")))
# button.click()
# message = browser.find_element(By.ID, "verify_message")
#
# assert "successful" in message.text

# --------------------------------------------------------------------
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # говорим Selenium проверять в течение 5 секунд, пока текст в элементе не станет равным $100
    button = WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    # жмем кнопку "Book"
    # book_button = browser.find_element(By.XPATH, '/html/body/div/div/div/button')
    book_button = browser.find_element(By.ID, 'book')
    book_button.click()

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
    answer.send_keys(y)

    # жмем кнопку "Submit"
    # sub = browser.find_element(By.XPATH, '/html/body/form/div/div/button')
    sub = browser.find_element(By.CSS_SELECTOR, 'body > form > div > div > button')
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
