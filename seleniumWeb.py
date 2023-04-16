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


class web:
    def __init__(self):
        serv_obj = Service("D:\Drivers\chromedriver_win32\chromedriver.exe")
        self.driver = webdriver.Chrome(service=serv_obj)
        self.driver.maximize_window()

    def by_xpath(self, locator):
        return self.driver.find_element(By.XPATH, locator)

    def by_id(self, locator):
        return self.driver.find_element(By.ID, locator)

    def by_name(self, locator):
        return self.driver.find_element(By.NAME, locator)

    def by_class_name(self, locator):
        return self.driver.find_element(By.CLASS_NAME, locator)

    def by_css(self, locator):
        return self.driver.find_element(By.CSS_SELECTOR, locator)

    def by_link(self, locator):
        return self.driver.find_element(By.LINK_TEXT, locator)

    def by_partial_link(self, locator):
        return self.driver.find_element(By.PARTIAL_LINK_TEXT, locator)

    def by_tag(self, locator):
        return self.driver.find_element(By.TAG_NAME, locator)

    def by_accessibility(self, locator):
        return self.driver.find_element(By.ACCESSIBILITY_ID, locator)

    def wait_for_element(self, locator, timeout=5):
        try:
            wait = WebDriverWait(self.driver, timeout)
            return wait.until(EC.visibility_of_element_located(locator))
        except:
            return self.driver.quit()

class login(web):
    def login(self):
        self.driver.get(url)  # Open the website
        self.driver.implicitly_wait(3)  # Wait the website to load

        # Check whether user is on right page
        assert self.driver.title == 'Login - Karobar', f'Expected Result: "Login - Karobar", Actual Result: {self.driver.title}'

        # Find the textbox locator of number field and pass number
        self.by_xpath('//input[@type="text" and @placeholder="Enter your Phone Number" and '
                      '@class="input"]').send_keys(num)

        # Find the submit button locator and click it
        self.by_css('.button').click()

        time.sleep(2)
        # Find the OTP textbox locator and send default OTP code
        wait_for_otp = (By.CLASS_NAME, "otp-input")
        self.wait_for_element(wait_for_otp)
        self.by_class_name('otp-input').send_keys(otp)  # Send otp code
        time.sleep(2)
        # Check whether user is on right page
        assert self.driver.title == 'Enter OTP Code - Karobar', f'Expected Result: "Enter OTP Code - Karobar", Actual Result: {self.driver.title}'

        # Find Continue button of OTP page
        self.by_class_name('button').click()

        time.sleep(5)
        # Select admin account
        self.by_xpath("//*[text='admin']").click()

        # self.by_link('/saleInvoice').click()

        self.by_link('/transactions').click()

        time.sleep(2)

        self.driver.quit()


# class sale(web):
#     def add_sale(self):
#         login().login()
#         self.by_link('/saleInvoice').click()
#
#         self.driver.quit()


web_driver = login()

web_driver.login()
