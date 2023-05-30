from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


serv_obj = Service("D:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=Service("D:\Drivers\chromedriver_win32\chromedriver.exe"))


def by_element_xpath(locator):
    return driver.find_element(By.XPATH, locator)


def by_element_id(locator):
    return driver.find_element(By.ID, locator)


def by_element_name(locator):
    return driver.find_element(By.NAME, locator)


def by_element_class_name(locator):
    return driver.find_element(By.CLASS_NAME, locator)


def by_element_css(locator):
    return driver.find_element(By.CSS_SELECTOR, locator)


def by_element_link(locator):
    return driver.find_element(By.LINK_TEXT, locator)


def by_element_partial_link(locator):
    return driver.find_element(By.PARTIAL_LINK_TEXT, locator)


def by_element_tag(locator):
    return driver.find_element(By.TAG_NAME, locator)


def by_element_accessibility(locator):
    return driver.find_element(By.ACCESSIBILITY_ID, locator)


def by_elements_xpath(locator):
    return driver.find_elements(By.XPATH, locator)


def by_elements_id(locator):
    return driver.find_elements(By.ID, locator)


def by_elements_name(locator):
    return driver.find_elements(By.NAME, locator)


def by_elements_class_name(locator):
    return driver.find_elements(By.CLASS_NAME, locator)


def by_elements_css(locator):
    return driver.find_elements(By.CSS_SELECTOR, locator)


def by_elements_link(locator):
    return driver.find_elements(By.LINK_TEXT, locator)


def by_elements_partial_link(locator):
    return driver.find_elements(By.PARTIAL_LINK_TEXT, locator)


def by_elements_tag(locator):
    return driver.find_elements(By.TAG_NAME, locator)


def by_elements_accessibility(locator):
    return driver.find_elements(By.ACCESSIBILITY_ID, locator)


driver.quit()
