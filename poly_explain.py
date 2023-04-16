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
print(driver.title)
driver.maximize_window()

search = driver.find_element(By.NAME, 's')
search.send_keys('test')
search.send_keys(Keys.RETURN)

element = By.ID, 'main'

try:
    main = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(element))
    articles = driver.find_elements(By.TAG_NAME, 'article')

    for article in articles:
        header = article.find_element(By.CLASS_NAME, 'entry-summary')
        print(header.text)



finally:
    driver.quit()



time.sleep(5)

driver.quit()
