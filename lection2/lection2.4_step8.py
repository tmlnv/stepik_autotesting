from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, 'price'), "$100"))

    book = browser.find_element(By.ID, 'book')
    book.click()

    value = browser.find_element(By.ID, 'input_value').text
    res = calc(int(value))

    answer = browser.find_element(By.ID, 'answer')
    answer.send_keys(res)

    submit = browser.find_element(By.ID, 'solve')
    submit.click()



finally:
    sleep(10)
    browser.quit()
