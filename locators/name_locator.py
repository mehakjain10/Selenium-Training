'''

NAME LOCATOR: find a web element using name attribute of a web element if present

'''

## Name Locator: Facebook Sign Up Page Example
# import time
#
# from selenium import webdriver
#
# options = webdriver.ChromeOptions()
# options.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(options)
#
# driver.get("https://www.facebook.com/r.php?entry_point=login")
# time.sleep(2)
#
# driver.find_element('name', 'firstname').send_keys('Mehak')
# time.sleep(1)
#
# driver.find_element('name', 'lastname').send_keys('Jain')
# time.sleep(1)
#
# driver.find_element('name', 'reg_email__').send_keys('meak@gmail.com')
# time.sleep(1)
#
# driver.find_element('name', 'reg_passwd__').send_keys('mehak@123')
# time.sleep(1)
#
# driver.close()

######################################################################################################################################################################

## Name Locator: Instagram Sign In Page Example
# import time
#
# from selenium import webdriver
#
# options = webdriver.ChromeOptions()
# options.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(options)
#
# driver.get("https://www.instagram.com/")
# time.sleep(2)
#
# driver.find_element('name', 'username').send_keys('abcde')
# time.sleep(1)
#
# driver.find_element('name', 'password').send_keys('abcd@123')
# time.sleep(1)

####################################################################################################################################################################

## Name Locator: DemoWebShop Register Page Example

import time

from selenium.webdriver import Chrome, ChromeOptions

options = ChromeOptions()
options.add_experimental_option("detach", True)

driver = Chrome(options)
driver.get("https://demowebshop.tricentis.com/register")
time.sleep(3)

driver.find_element('id', 'gender-female').click()
time.sleep(2)

driver.find_element('name', 'FirstName').send_keys('Mehak')
time.sleep(2)

driver.find_element('name', 'LastName').send_keys('Jain')
time.sleep(2)

driver.find_element('name', 'Email').send_keys('mehak@gmail.com')
time.sleep(2)

driver.find_element('name', 'Password').send_keys('abc')
time.sleep(2)

driver.find_element('name', 'ConfirmPassword').send_keys('abc@123')
time.sleep(2)

driver.find_element('name', 'register-button').click()
time.sleep(2)