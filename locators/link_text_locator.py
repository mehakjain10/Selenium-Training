'''
LINK TEXT

- It is used to find the location of an element using text.
- It will only work for anchor tag (It will work for span tag too but not all the time)
- The text value is case-sensitive.

HTML Code:

<a href='https://www.google.com'>Google</a>
<span>...</span>


'''

import time

from selenium.webdriver import Chrome, ChromeOptions

options = ChromeOptions()
options.add_experimental_option("detach", True)

driver = Chrome(options)

## DEMO HTML Code Example

# driver.get(r'C:\Users\Mehak Jain\PycharmProjects\SeleniumTraining\html_files\sample.html')
# time.sleep(2)
# driver.find_element('link text', 'Amazon').click()

## Real Time Website Example

# driver.get('https://www.flipkart.com')
# time.sleep(2)
# driver.find_element('link text', 'Minutes').click()

'''
TASK 1:
apple website -> click on Mac using link text
'''
# driver.get('https://www.apple.com/in/')
# time.sleep(2)
# driver.maximize_window()
# time.sleep(2)
# driver.find_element('link text', 'Mac').click()

'''
TASK 2:
udemy website -> click on sign up then give all the details as well
'''

driver.get('https://www.udemy.com/')
time.sleep(2)
driver.find_element('link text', 'Sign up').click()
time.sleep(2)
driver.find_element('name', 'full-name').send_keys('Mehak')
time.sleep(2)
driver.find_element('name', 'email').send_keys('mehak@gmail.com')
time.sleep(2)
driver.find_element('class name', 'ud-btn.ud-btn-large.ud-btn-brand.ud-btn-text-md.passwordless-auth-mx-code-generation-form--submit-button--2vOvZ').click()
