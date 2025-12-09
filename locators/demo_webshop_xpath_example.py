from time import sleep
from selenium.webdriver import Chrome, ChromeOptions

options = ChromeOptions()
options.add_experimental_option("detach", True)

driver = Chrome(options)
driver.get("https://demowebshop.tricentis.com/")
sleep(2)

## Clicking on Register Link
driver.find_element('xpath', "//a[@href='/register']").click()
sleep(2)

## Filling all the fields on Register Page with Valid Inputs
driver.find_element('xpath', "//input[@id='gender-female']").click()
sleep(2)
driver.find_element('xpath', "//input[@id='FirstName']").send_keys("John")
sleep(2)
driver.find_element('xpath', "//input[@id='LastName']").send_keys("Doe")
sleep(2)
driver.find_element('xpath', "//input[@id='Email']").send_keys("johndoe987654@gmail.com")
sleep(2)
driver.find_element('xpath', "//input[@id='Password']").send_keys("johndoe@123")
sleep(2)
driver.find_element('xpath', "//input[@id='ConfirmPassword']").send_keys("johndoe@123")
sleep(2)
driver.find_element('xpath', "//input[@id='register-button']").click()
sleep(3)

## Clicking on Continue Button
driver.find_element('xpath', "//input[@class='button-1 register-continue-button']").click()
sleep(3)

## Clicking on Logout Link
driver.find_element('xpath', "//a[@href='/logout']").click()
sleep(2)

## Clicking on Login Link
driver.find_element('xpath', "//a[@href='/login']").click()
sleep(2)

## Filling all the fields on Login Page with Valid Inputs
driver.find_element('xpath', "//input[@id='Email']").send_keys("johndoe987654@gmail.com")
sleep(2)
driver.find_element('xpath', "//input[@id='Password']").send_keys("johndoe@123")
sleep(2)
driver.find_element('xpath', "//input[@class='button-1 login-button']").click()
sleep(2)