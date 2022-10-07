import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


# print(os.path.abspath(__file__))
# print(os.path.abspath(os.path.dirname(__file__)))


try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)

    first = browser.find_element(By.NAME, 'firstname')
    first.send_keys('m')

    last = browser.find_element(By.NAME, 'lastname')
    last.send_keys('m')

    email = browser.find_element(By.NAME, 'email')
    email.send_keys('m')

    file = browser.find_element(By.ID, 'file')
    loc = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(loc, 'lection2.2_step8_file.txt')
    file.send_keys(file_path)

    button = browser.find_element(By.TAG_NAME, 'button')
    button.click()

finally:
    sleep(10)
    browser.quit()