import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/get_attribute.html")
    x_element = browser.find_element(By.TAG_NAME, "img").get_attribute("valuex")
    x = int(x_element)
    y = calc(x)

    answer = browser.find_element(By.CSS_SELECTOR, '#answer')
    answer.send_keys(y)

    option1 = browser.find_element(By.CSS_SELECTOR, "[type='checkbox']")
    option1.click()

    option2 = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    option2.click()

    button = browser.find_element(By.TAG_NAME, 'button')
    button.click()

finally:
    sleep(10)
    browser.quit()
