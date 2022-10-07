from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/redirect_accept.html")

    button = browser.find_element(By.TAG_NAME, 'button')
    button.click()

    window2 = browser.window_handles[1]

    browser.switch_to.window(window2)

    value = browser.find_element(By.ID, 'input_value').text
    res = calc(int(value))

    answer = browser.find_element(By.ID, 'answer')
    answer.send_keys(res)

    submit = browser.find_element(By.TAG_NAME, 'button')
    submit.click()


finally:
    sleep(10)
    browser.quit()
