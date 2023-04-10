import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


# os.environ['PATH'] += r"D:\Drivers\chromedriver_win32"
class weblogin:
    def __init__(self):
        self.driver = webdriver.Chrome("D:\Drivers\chromedriver_win32\chromedriver.exe")
        self.driver.maximize_window()

    def login(self, num):
        self.driver.get("https://web.karobarapp.com/login")  # Open the website
        self.driver.implicitly_wait(3)  # Wait the website to load

        assert self.driver.title == 'Login - Karobar', f'Expected Result: "Login - Karobar", Actual Result: {self.driver.title}'

        num_textbox_locator = self.driver.find_element(By.XPATH,
                                                       '//input[@type="text" and @placeholder="Enter your Phone '
                                                       'Number" and @class="input"]')
        num_textbox_locator.send_keys(num)
        time.sleep(4)
        self.driver.quit()


driver_karobar = weblogin()
driver_karobar.login("9222222222")
