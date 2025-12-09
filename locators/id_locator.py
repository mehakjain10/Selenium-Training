'''

ID LOCATOR: find a web element using id attribute of a web element if present

'''

## Saucedemo Website Example

# import time
# from selenium import webdriver
#
# options = webdriver.ChromeOptions()
# options.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(options)
#
# driver.get("https://www.saucedemo.com/")
# time.sleep(2)
#
# driver.find_element('id', 'user-name').send_keys('standard_user')
# time.sleep(1)
#
# driver.find_element('id', 'password').send_keys('secret_sauce')
# time.sleep(1)
#
# driver.find_element('id', 'login-button').click()
# time.sleep(3)
#
# driver.find_element('id', 'react-burger-menu-btn').click()
# time.sleep(2)
#
# driver.find_element('id', 'logout_sidebar_link').click()
#
# driver.close()

####################################################################################################################################################################

## TestAutomationPractice Website Example

import time
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options)

driver.get("https://testautomationpractice.blogspot.com/")
time.sleep(2)

driver.find_element('id', 'name').send_keys('Mehak')
time.sleep(1)

driver.find_element('id', 'email').send_keys('mehak@gmail.com')
time.sleep(1)

driver.find_element('id', 'phone').send_keys('9876543210')
time.sleep(1)

driver.find_element('id', 'textarea').send_keys('Delhi')
time.sleep(1)

driver.find_element('id', 'female').click()
time.sleep(1)

driver.find_element('id', 'wednesday').click()