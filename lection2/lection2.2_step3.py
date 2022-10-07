import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import Select


try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/selects1.html"
    link2 = "http://suninjuly.github.io/selects2.html"
    browser.get(link2)

    num1 = browser.find_element(By.ID, 'num1').text
    num2 = browser.find_element(By.ID, 'num2').text
    sum_names = int(num1) + int(num2)

    select = Select(browser.find_element(By.TAG_NAME, 'select'))
    select.select_by_visible_text(str(sum_names))

    button = browser.find_element(By.TAG_NAME, 'button')
    button.click()

finally:
    sleep(10)
    browser.quit()
