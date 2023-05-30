from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import openpyxl
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from Practice import find


serv_obj = Service("D:\Drivers\chromedriver_win32\chromedriver.exe")

driver = webdriver.Chrome(service=serv_obj)

driver.maximize_window()

driver.get("https://web.karobarapp.com/login")

find.by_element_xpath("//input[@placeholder='Enter your Phone Number']").send_keys('9860725577')

find.by_element_xpath("//button[@type='button']").click()
otpPage = find.by_element_xpath("//h1[normalize-space()='Enter OTP Code']")
wait = WebDriverWait(driver, timeout=5, poll_frequency=2).until(EC.visibility_of_element_located(otpPage))

driver.quit()

