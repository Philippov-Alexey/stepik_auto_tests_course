import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class TestWebPages(unittest.TestCase):

    def test_1(self):
        link = 'http://suninjuly.github.io/registration1.html'
        browser = webdriver.Chrome()
        browser.get(link)

        input1 = browser.find_element(By.CSS_SELECTOR,
                                      'body > div > form > div.first_block > div.form-group.first_class > input')
        input1.send_keys('Name')
        input2 = browser.find_element(By.CSS_SELECTOR,
                                      'body > div > form > div.first_block > div.form-group.second_class > input')
        input2.send_keys('Last_Name')
        input3 = browser.find_element(By.CSS_SELECTOR,
                                      'body > div > form > div.first_block > div.form-group.third_class > input')
        input3.send_keys('a1@gmail.com')

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        time.sleep(1)

        welcome_text_elt = browser.find_element(By.TAG_NAME, 'h1')
        welcome_text = welcome_text_elt.text

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, 'Лажа какая-то вышла')

        browser.quit()

    def test_2(self):
        link = 'http://suninjuly.github.io/registration2.html'
        browser = webdriver.Chrome()
        browser.get(link)

        input1 = browser.find_element(By.CSS_SELECTOR,
                                      'body > div > form > div.first_block > div.form-group.first_class > input')
        input1.send_keys('Name')
        input2 = browser.find_element(By.CSS_SELECTOR,
                                      'body > div > form > div.first_block > div.form-group.second_class > input')
        input2.send_keys('Last_Name')
        input3 = browser.find_element(By.CSS_SELECTOR,
                                      'body > div > form > div.first_block > div.form-group.third_class > input')
        input3.send_keys('a1@gmail.com')

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        time.sleep(1)

        welcome_text_elt = browser.find_element(By.TAG_NAME, 'h1')
        welcome_text = welcome_text_elt.text

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, 'Лажа какая-то вышла')

        browser.quit()


if __name__ == "__main__":
    unittest.main()
