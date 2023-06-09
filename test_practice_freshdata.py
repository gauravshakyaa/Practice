import os
import time

from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
import pytest

# os.environ['PATH'] += r"D:\Drivers\chromedriver_win32"
# locationChromeDriver = "D:\Drivers\chromedriver_win32\chromedriver.exe"
baseUrl = 'https://web.karobarapp.com/login'
num = '9333333333'
otp = '123456'


# test_case = 0


def timee():
    time.sleep(1)


def timee4():
    time.sleep(4)


class web:
    def __init__(self):
        # serv_obj = Service(locationChromeDriver)
        self.driver = webdriver.Chrome()
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

    def wait_for_element(self, locator, timeout=5, poll_frequency=2):
        wait = WebDriverWait(self.driver, timeout, poll_frequency)
        return wait.until(EC.visibility_of_element_located(locator))


#     def add_sale(self)
#         login().login()
class fresh_data(web):

    def __init__(self):
        super().__init__()

        self.isLogin = False

    def test_login(self):
        self.driver.get(baseUrl)  # Open the website
        time.sleep(2)
        print(self.driver.current_url)
        assert "login" in self.driver.current_url

        self.driver.implicitly_wait(3)  # Wait the website to load

        # Check whether user is on right page
        assert self.driver.title == 'Login - Karobar', f'Expected Result: "Login - Karobar", Actual Result: {self.driver.title}'

        # Click get OTP code button

        self.by_css('button[type="button"]').click()
        time.sleep(1)
        # Click get OTP code with empty number field
        validation_msg = self.by_xpath("//span[@class='help is-danger']").text

        assert validation_msg == 'Enter Valid Phone Number', f"Expected output: 'Enter Valid Phone Number', actual " \
                                                             f"result: {validation_msg}"

        # Find the textbox locator of number field and pass number

        self.by_xpath('//input[@type="text" and @placeholder="Enter your Phone Number" and '
                      '@class="input"]').send_keys(num)

        # Find the submit button locator and click it

        self.by_css('.button').click()

        time.sleep(2)
        self.by_class_name('otp-input').send_keys(otp)  # Send otp code
        # Find the OTP textbox locator and send default OTP code
        wait_for_otp = (By.CLASS_NAME, "otp-input")
        self.wait_for_element(wait_for_otp)
        time.sleep(2)
        # Check whether user is on right page
        # assert self.driver.title == 'Enter OTP Code - Karobar', f'Expected Result: "Enter OTP Code - Karobar", Actual Result: {self.driver.title}'

        # Find Continue button of OTP page
        self.by_class_name('button').click()
        time.sleep(2)

        # Select admin account and click it
        self.by_xpath("//*[text()='Admin']").click()
        # WebDriverWait(self.driver, timeout=6, poll_frequency=2).until(EC.url_matches('https://web.karobarapp.com'))
        time.sleep(3)

        if 'https://web.karobarapp.com/' in self.driver.current_url:
            print("Login successful!")
            self.isLogin = True
        else:
            print("Login failed!!!")
            self.isLogin = False

    def test_add_party(self):
        if self.isLogin:
            timee()
            self.by_xpath("//span[normalize-space()='Parties']").click()  # Click parties button from navigation bar
            timee()
            assert 'https://web.karobarapp.com/parties' in self.driver.current_url, "Parties page is not opened"  # Validate the redirected page
            timee()
            self.by_xpath("//button//span[text()='Add New Party']").click()
            add_party_popup = self.by_css(".animation-content").is_displayed()
            if add_party_popup:
                self.by_css("input[type='text'][placeholder='Enter Party Name']").send_keys("Gaurav Shakya")
                self.by_xpath("//button[@type='button']//span[text()='SAVE']").click()
                snackbar = self.by_xpath("//div[@class='text']").text
                snackbar_msg = "Party was added successfully"
                assert snackbar == snackbar_msg, "Snackbar is not displayed or is not correct"
            else:
                assert "Add Party pop up is not seen"
            timee()

            party_name = self.by_xpath("//div[@class='left-box column is-12-mobile']//h1").text
            assert party_name == "Gaurav Shakyaa", "Party does not match with the entered party name. Please Check it"
            timee()

        else:
            print("You are not logged in")

    def test_add_sales(self, party, bill=None, month=None, year=None, item=None, note=None, total=None, recieved=None):
        if self.isLogin:
            self.by_xpath("//span[normalize-space()='Add Sale Invoice']").click()
            self.by_xpath(
                '//*[@id="app"]/div[2]/section[2]/div[1]/div/div[1]/div/div[1]/div/div/div[1]/input').click()
            timee()

            assert 'https://web.karobarapp.com/saleInvoice' in self.driver.current_url

            self.by_xpath(
                "//div[@class='dropdown-content']//div[@class='item-left']//*[contains(normalize-space(),'Cash Sale')]").click()

            invoice_input = self.by_css("input[placeholder='Enter Invoice No.']")
            invoice_input.send_keys(bill)
            self.by_xpath("//input[@class='date_picker_page']").click()
            Select(self.by_xpath("//select[1]")).select_by_visible_text(month)

            year = self.by_xpath("//div[@class='calendar__year']")
            total_amount = self.by_xpath(
                "//div[@class='field has-addons']//div[@class='control is-expanded is-clearfix']//input")
            total_amount.send_keys(total)

            self.by_xpath("//button[@class='button is-success']").click()
            timee4()

            print(self.by_xpath("//div[@class='text']").text)
            self.by_xpath("//table[@class='table is-hoverable']/descendant::td[1]")

        else:
            print("You are not logged in")


fresh_data = fresh_data()
fresh_data.test_login()
fresh_data.test_add_sales(party="cash", total=500)

web().driver.quit()
