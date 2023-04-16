import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

serv_obj = Service("D:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get('https://www.techwithtim.net/')
driver.back()
time.sleep(2)
driver.forward()
time.sleep(2)

driver.refresh()
driver.close()
driver.quit()
