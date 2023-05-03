from selenium import webdriver
from selenium.webdriver.chrome.service import Service

import time

from selenium.webdriver.common.by import By

serv_obj = Service("D:\Drivers\chromedriver_win32\chromedriver.exe")

driver = webdriver.Chrome(service=serv_obj)

driver.get("https://web.karobarapp.com/login")
driver.maximize_window()

driver.find_element(By.XPATH, '//input[@type="text" and @placeholder="Enter your Phone Number" and '
                              '@class="input"]').send_keys('9222222222')
time.sleep(2)
# Find the submit button locator and click it
# driver.find_element(By.CLASS_NAME, '.button').click()
driver.find_element(By.XPATH, '//*[@id="app"]/div/section/div[2]/div/div[1]/div/button').click()
time.sleep(2)
driver.find_element(By.CLASS_NAME, 'otp-input').send_keys('123456')  # Send otp code
# Find the OTP textbox locator and send default OTP code
wait_for_otp = (By.CLASS_NAME, "otp-input")

time.sleep(2)
# Check whether user is on right page

# assert self.driver.title == 'Enter OTP Code - Karobar', f'Expected Result: "Enter OTP Code - Karobar",
# Actual Result: {self.driver.title}'

# Find Continue button of OTP page
driver.find_element(By.CLASS_NAME, 'button').click()
time.sleep(2)

# Select admin account and click it
driver.find_element(By.CLASS_NAME, "//*[text()='Admin']").click()
time.sleep(2)

driver.get("https://web.karobarapp.com/parties")
party = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/section[2]/div/div[1]/article/div[3]')

driver.execute_script("arguments[0].scrollIntoView();", party)

# driver.execute_script("window.scrollBy(0, 1000)", "")

# flag = driver.find_element(By.XPATH, '//*[@id="content"]/div[2]/div[2]/table[2]/tbody/tr[23]/td[2]')
# driver.execute_script("arguments[0].scrollIntoView();", flag)
# print(flag.location_once_scrolled_into_view)

# driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")
driver.execute_script("document.querySelector('').scrollTop=500")

time.sleep(5)

driver.quit()
