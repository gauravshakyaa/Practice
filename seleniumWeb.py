import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

# os.environ['PATH'] += r"D:\Drivers\chromedriver_win32"

url = 'https://web.karobarapp.com/login'
num = '9222222222'
otp = '123456'
test_case = 0


class weblogin:
    def __init__(self):
        serv_obj = Service("D:\Drivers\chromedriver_win32\chromedriver.exe")
        self.driver = webdriver.Chrome(service=serv_obj)
        self.driver.maximize_window()

    def wait_for_element(self, locator, timeout=5):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.visibility_of_element_located(locator))

    def login(self):
        self.driver.get(url)  # Open the website
        self.driver.implicitly_wait(3)  # Wait the website to load

        # Check whether user is on right page
        assert self.driver.title == 'Login - Karobar', f'Expected Result: "Login - Karobar", Actual Result: {self.driver.title}'

        # Find the textbox locator of number field and pass number
        self.driver.find_element(By.XPATH, '//input[@type="text" and @placeholder="Enter your Phone Number" and '
                                           '@class="input"]').send_keys(num)

        # Find the submit button locator and click it
        self.driver.find_element(By.CSS_SELECTOR, '.button').click()

        # Find the OTP textbox locator and send default OTP code

        wait_for_otp = (By.CLASS_NAME, "otp-input")

        otp_element = self.wait_for_element(wait_for_otp)

        # Check whether user is on right page
        assert self.driver.title == 'Enter OTP Code - Karobar', f'Expected Result: "Enter OTP Code - Karobar", Actual Result: {self.driver.title}'

        time.sleep(1)
        self.driver.quit()


driver_karobar = weblogin()

driver_karobar.login()

print(test_case)
