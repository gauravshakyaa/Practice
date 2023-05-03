import os
import time
import requests as requests

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

serv_obj = Service("D:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

# driver.get('https://demo.nopcommerce.com/')
driver.get('http://www.deadlinkcity.com/')

driver.maximize_window()

# driver.find_element(By.LINK_TEXT, "Register")
links = driver.find_elements(By.TAG_NAME, "a")
print(len(links))
count = 0

for link in links:
    url = link.get_attribute('href')
    try:
        res = requests.head(url)
    except:
        var = None

    if res.status_code >= 400:
        print(url, '-is broken link')
        count += 1
    else:
        print(url, '-is valid link')

print(count)
time.sleep(2)

driver.quit()
