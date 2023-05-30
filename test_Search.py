import time

from selenium import webdriver
from webbrowser import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv = Service("D:\Drivers\chromedriver_win32\chromedriver.exe")

driver = webdriver.Chrome(service=serv)


def test_search():
    driver.get("https://tutorialsninja.com/demo/index.php?route=common/home")
    driver.maximize_window()
    time.sleep(2)
    driver.find_element(By.XPATH, "//input[@placeholder='Search']").send_keys("apple")
    time.sleep(2)
    driver.find_element(By.XPATH, "//button[@class='btn btn-default btn-lg']").click()
    time.sleep(2)
    text = driver.find_element(By.LINK_TEXT, "Apple Cinema 30").text
    assert 'Apple Cinema 30"' in text

    driver.quit()
