import os
import time

from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

# os.environ['PATH'] += r"D:\Drivers\chromedriver_win32"

url = 'https://web.karobarapp.com/login'
num = '9222222222'
otp = '123456'


# test_case = 0


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

    def wait_for_element(self, locator, timeout=5, poll_frequency=2):
        wait = WebDriverWait(self.driver, timeout, poll_frequency)
        return wait.until(EC.visibility_of_element_located(locator))


#     def add_sale(self)
#         login().login()
class login(web):

    def __init__(self, number):
        super().__init__()
        self.number = number
        self.isLogin = False

    def login(self):
        self.driver.get(url)  # Open the website
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
        time.sleep(2)

    def transactions(self):
        if self.isLogin:
            self.driver.get('https://web.karobarapp.com/parties')
            time.sleep(2)
            transactions = self.by_xpath("//ul[@class='parties-list']")
            party = []
            list = [transactions.text.split("\n")]
            # for i in transactions:

            party.append(list[0])

            print(party)

            time.sleep(3)
        else:
            print("User not logged in.")

    def scroll_party(self):
        self.driver.get("https://web.karobarapp.com/parties")
        time.sleep(3)

        self.driver.execute_script("document.querySelector('.content').scrollHeight")


class create_sales(login):
    def click_add_sales_dashboard(self):
        if self.isLogin:
            self.by_xpath('//*[@id="app"]/div[2]/section[1]/div/div[2]/div/div/a[1]').click()
            time.sleep(2)

        else:
            print("User not logged in")


login = login('92222222222')
login.login()
login.scroll_party()

web().driver.quit()
