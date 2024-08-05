from selenium.webdriver.common.by import By
from selenium import webdriver
import time



try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/cats.html')

    book_button = browser.find_element(By.ID, 'button')
    book_button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта (в принципе уже не нужно, так ответ мы уже
    # прочитали)
    time.sleep(1)
    # закрываем браузер после всех манипуляций
    browser.quit()
