import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import Select


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    link = "https://suninjuly.github.io/execute_script.html"
    browser.get(link)

    value = browser.find_element(By.ID, 'input_value').text
    res = calc(int(value))

    answer = browser.find_element(By.CSS_SELECTOR, '#answer')
    answer.send_keys(res)

    button = browser.find_element(By.TAG_NAME, 'button')
    browser.execute_script("window.scrollBy(0, 100);")

    option1 = browser.find_element(By.CSS_SELECTOR, "[type='checkbox']")
    option1.click()

    option2 = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    option2.click()

    button.click()

finally:
    sleep(10)
    browser.quit()
