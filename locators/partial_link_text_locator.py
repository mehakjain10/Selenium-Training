'''
PARTIAL LINK TEXT

- It is used to find the location of an element by passing some portion of a text value
- It will work only for anchor tag (it will work for span tag also but not all the time
- In this also, the text value is casse-sensitive
NOTE:
- In link text, you have to pass the text value completely, but in partial link text you have to pass some portion.
- Both link text and partal link text are case-sensitive.
'''

import time
from selenium.webdriver import Chrome, ChromeOptions

options = ChromeOptions()
options.add_experimental_option("detach", True)

driver = Chrome(options)

## Demo HTML Example

# driver.get(r'C:\Users\Mehak Jain\PycharmProjects\SeleniumTraining\html_files\sample.html')
# time.sleep(2)
#
# # driver.find_element('link text', 'Python 3.14.0') ---------> the version is dynamic so we will get NoSuchElementException
# driver.find_element('partial link text', 'Python').click()

#####################################################################################################################

## Real Time Website Example

driver.get("https://www.selenium.dev/downloads/")
time.sleep(3)
driver.find_element("partial link text","languages").click()
