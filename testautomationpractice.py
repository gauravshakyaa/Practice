import os
import time
import requests as requests

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

serv_obj = Service("D:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

# driver.get('https://testautomationpractice.blogspot.com/')
# driver.maximize_window()

actions = ActionChains(driver)


def search_bar_send_selenium_open_links():
    search = driver.find_element(By.CLASS_NAME, "wikipedia-search-input")

    search.send_keys('selenium')

    search.submit()
    time.sleep(1)
    links = driver.find_elements(By.XPATH, "//div[@id='wikipedia-search-result-link']//a")

    for link in links:
        link.click()
        time.sleep(2)

    windows = driver.window_handles
    parent_window = windows[0]

    driver.switch_to.window(parent_window)


def speed_dropdown():
    drp = Select(driver.find_element(By.XPATH, "//select[@id='speed']"))
    drp.select_by_visible_text("Fast")
    # drp.select_by_index()
    # drp.select_by_value('')


def file_dropdown():
    drp = Select(driver.find_element(By.ID, 'files'))
    drp.select_by_value('3')


def dbl_click():
    dblclick = driver.find_element(By.CSS_SELECTOR, "button[ondblclick='myFunction1()']")
    actions.double_click(dblclick).perform()


def drag_drop():
    source = driver.find_element(By.ID, "draggable")
    target = driver.find_element(By.ID, "droppable")
    actions.drag_and_drop(source, target).perform()

    print(target.text)


def slider():
    slider = driver.find_element(By.ID, 'slider')

    actions.move_to_element(slider).click_and_hold().move_by_offset(50, 50).release().perform()
    print(slider.location)  # {'x': 1179, 'y': 742}
    print(slider.location_once_scrolled_into_view)  # {'x': 1179, 'y': 1}


def alert():
    driver.find_element(By.CSS_SELECTOR, "button[onclick='myFunction()']").click()
    alert = driver.switch_to.alert
    alert.dismiss()


def date_picker():
    driver.find_element(By.ID, 'datepicker').click()


def frame():
    driver.switch_to.frame('frame-one1434677811')



def scrollParty():
    driver.get("https://web.karobarapp.com/login")
    driver.maximize_window()

    driver.find_element(By.XPATH, '//input[@type="text" and @placeholder="Enter your Phone Number" and '
                                  '@class="input"]').send_keys('9222222222')
    time.sleep(2)
    # Find the submit button locator and click it
    # driver.find_element(By.CLASS_NAME, '.button').click()
    driver.find_element(By.XPATH, '//*[@id="app"]/div/section/div[2]/div/div[1]/div/button').click()
    time.sleep(2)
    driver.find_element(By.CLASS_NAME, 'otp-input').send_keys('123456')  # Send otp code, automatically pass through login page
    time.sleep(2)
    # Select admin account and click it
    driver.find_element(By.XPATH, "//small[normalize-space()='Admin']").click()
    time.sleep(2)

    driver.get("https://web.karobarapp.com/parties")
    time.sleep(2)
    party = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/section[2]/div/div[1]/article/div[3]')

    driver.execute_script("document.querySelector('.content').scrollTop=500")
    # driver.execute_script("arguments[0].scrollIntoView();", party)
    time.sleep(5)
    driver.quit()


scrollParty()


time.sleep(3)
driver.quit()
