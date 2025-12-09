'''
CSS SELECTOR

What is CSS?
- CSS stands for Cascading style Sheet
- It is used to decorate a webpage like color,font size,Background etc.....

What is CSS selector?
- It is used to find the location of a web element by using CSS expression

How to write a CSS expression?
tag name[attribute name='attribute value']

Note: Any attribute including id,name,class, value etc. can be used


Where we have to write css expression?

Step 1 : Inspect the element
Step 2 : Press ctrl+f in your keyboard; "find my string" search dialog box will be highlighted
Step 3 : Type the CSS expression for the element you want to locate


How to VERIFY the CSS expression to check if the expression is valid or not?

1. Element should get highlighted
2. Code should get highlighted in yellow color
3. (1 of 1) found should be there

Drawbacks of CSS Selector
- Getting 1 of 1 found is difficult. If we don't get it, we have to move to a different selector
- We can't go for any occurrence other than the first occurrence
- CSS Selector Locator doesn't work with text value of an HTML element. So elements with no attributes and only text can't be taken
'''

import time
from selenium.webdriver import Chrome, ChromeOptions

options = ChromeOptions()
options.add_experimental_option("detach", True)

driver = Chrome(options)

# EXAMPLE

driver.get("https://demowebshop.tricentis.com/login")
time.sleep(3)
driver.find_element("css selector","input[class='email']").send_keys("Amitabh mailto:bachhan@gmail.com")


########################################################################################################################

## Facebook SignUp Page Example :

driver.get("https://www.facebook.com/")
time.sleep(2)

driver.find_element('link text', 'Create new account').click()
time.sleep(2)

driver.find_element('name', 'firstname').send_keys('abc')
time.sleep(2)

driver.find_element('name', 'lastname').send_keys('pqr')
time.sleep(2)

driver.find_element('css selector', "input[value='1']").click()
time.sleep(2)

driver.find_element('name', 'reg_email__').send_keys('abc@gmail.com')
time.sleep(2)

driver.find_element('name', 'reg_passwd__').send_keys('pqr@123')
time.sleep(2)