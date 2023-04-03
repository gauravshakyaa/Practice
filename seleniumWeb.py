import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# os.environ['PATH'] += r"D:\Drivers\chromedriver_win32"

driver = webdriver.Chrome(executable_path="D:\Drivers\chromedriver_win32\chromedriver.exe")

# driver = webdriver.Chrome()

driver.get("web.karobarapp.com/login")  # Open the website

driver.implicitly_wait(3)  # Wait the website to load

print(driver.title)

assert driver.title == 'Yuwahub Community', f'Expected Result: "Yuwahub Community", Actual Result: {driver.title}'
