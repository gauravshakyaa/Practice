import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support import expected_conditions as EC

desired_caps = {
    # "deviceName": "RF8M703BZXW",  # device name for s10 phone
    "deviceName": "A00000K580160801364",  # device name for nokia phone
    "platformName": "Android",
    "appPackage": "com.bytecaretech.merokarobar",
    "appActivity": "com.bytecaretech.merokarobar.MainActivity",
    "platformVersion": "11"
    # "noReset": True
    # "app": "C:/Users/acer/Downloads/Karobar.apk"
    # "automationName": "UiAutomator2"
}
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

time.sleep(3)

floating_button = driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout'
                                                '/android.widget.FrameLayout/android.widget.FrameLayout/android'
                                                '.widget.FrameLayout/android.view.View/android.view.View/android.view'
                                                '.View/android.view.View/android.view.View[3]/android.widget.Button')

floating_button.click()

add_party_floating = driver.find_element(By.XPATH, '//android.view.View[@content-desc="New Party"]')
add_party_floating.click()
time.sleep(2)
ok_contacts = driver.find_element(By.XPATH, '//android.widget.Button[@content-desc="OK"]')

ok_contacts.click()

allow_permission = driver.find_element(By.ID, 'com.android.permissioncontroller:id/permission_allow_button')

allow_permission.click()
time.sleep(2)

add_partyname = driver.find_element(By.XPATH, '//android.view.View[@content-desc="PARTY INFORMATION Party Name Phone '
                                              'Number Email Party Type"]/android.widget.EditText[1]')

add_partyname.click()
add_partyname.send_keys('AutomateTestCase')
time.sleep(2)
new_party_save = driver.find_element(By.XPATH, '//android.widget.Button[@content-desc="Save"]')

new_party_save.click()

listitems = []

element_list = driver.find_elements(By.XPATH, '//android.view.View')

for i in element_list:
    listitems.append(element_list)

print(listitems)


# party_dashboard = driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout"
#                                                 "/android.widget.FrameLayout/android.widget.FrameLayout/android"
#                                                 ".widget.FrameLayout/android.view.View/android.view.View/android.view"
#                                                 ".View/android.view.View/android.view.View["
#                                                 "2]/android.widget.ScrollView/android.view.View[3]/android.view.View")
#
#
# def swipe_party_dashboard():
#     actions = ActionChains(driver)
#     actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
#     actions.w3c_actions.pointer_action.move_to_location(336, 1049)
#     actions.w3c_actions.pointer_action.pointer_down()
#     actions.w3c_actions.pointer_action.move_to_location(336, 966)
#     actions.w3c_actions.pointer_action.release()
#     actions.perform()
#
#
# lists = party_dashboard.find_elements(By.XPATH, '//android.view.View[@content-desc]')
#
# for i in lists:
#     swipe_party_dashboard()
#     print(i.get_attribute("content-desc"))
# # swipe_party_dashboard(lists)
#
# # for i in range(3):
# #     # party_list = (lists.get_attribute("content-desc").split())
# #     #
# #     # party_real = str(party_list[1]) + ' ' + str(party_list[2])
# #     # print(party_real)
#
# dup_party = []
# unique_party = []
#
# # for i in lists:
# #     x = (i.get_attribute("content-desc").split())
# #     party_real = (x[1] + " " + x[2])
# #
# #     if party_real not in unique_party:
# #         unique_party.append(party_real)
# #     else:
# #         dup_party.append(party_real)
# #
# #     swipe_party_dashboard()
# #     time.sleep(2)
# #
# # print(dup_party)
# # print(unique_party)
