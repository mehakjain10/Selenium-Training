'''

Sample HTML: <a href=link>Text</a>

An HTML code consists of three components:
    a) Tag name
    b) Attribute
    c) Text

In find_element, if the locator matches with multiple elements, it will return the first matching element
That's why for tag name, find_element is not preferred. We use find_elements instead.
'''
import time
from selenium.webdriver import Chrome, ChromeOptions

opts = ChromeOptions()
opts.add_experimental_option("detach", True)

driver = Chrome(opts)
driver.get(r'C:\Users\Mehak Jain\PycharmProjects\SeleniumTraining\html files\sample.html')
time.sleep(2)

driver.find_element('tag name', 'a').click()

