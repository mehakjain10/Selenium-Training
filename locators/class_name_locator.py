'''

CLASS NAME LOCATOR:
- find a web element using class attribute of a web element if present
- if any space present in the value of the locator, it should be replaced with '.'
- class and class name are different
- class is an attribute in html whereas class name is the locator used in selenium


** difference between selenium 3 and selenium 4
'''

import time

from selenium.webdriver import Chrome, ChromeOptions

options = ChromeOptions()
options.add_experimental_option("detach", True)

driver = Chrome(options)
driver.get("https://demowebshop.tricentis.com/register")
time.sleep(3)

driver.find_element('class name', 'text-box.single-line').send_keys('Mehak')
