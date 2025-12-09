# xpath :
#     xpath is used to find the location of a webelement in a html tree structure or in DOM(Document object Model)

# xpath classified into two types:
# 1.Absolute xpath
# 2.Relative xpath

# 1.Absolute xpath
#     -->It will traverse from parent to its own child
#     -->It is Denoted as (/)
# Drawbacks of Absolute xpath
#     -->Absolute xpath is very lengthy comparing to relative xpath
#     --> Always it will traverse from parent to its own child
# 2.Relative xpath
#     -->It will traverse from parent to any of the child
#     -->It is Denoted as (//)

# Sample for Absolute xpath
"""
driver = http://webdriver.Chrome(opts)
driver.get("file:///C:/Users/Admin/Desktop/A2_Selenium/xpath.html")
time.sleep(3)
driver.find_element("xpath","html/body/div[1]/input[1]").send_keys("Username1")

"""
"""
driver = http://webdriver.Chrome(opts)
driver.get("file:///C:/Users/Admin/Desktop/A2_Selenium/xpath.html")
time.sleep(3)
driver.find_element("xpath","html/body/div[2]/input[2]").send_keys("Username4")
"""
"""
driver = http://webdriver.Chrome(opts)
driver.get("https://demowebshop.tricentis.com/")
time.sleep(3)
driver.find_element("xpath","html/body/div[4]/div[1]/div[1]/div[2]/div[1]/ul/li[1]/a").click()
"""

# Xpath By Attribute:(imp)
#     Finding the location of a web element by using attributes is called xpath by attribute
#     Including id,name,class etc... you can use as a attributes in xpath by attribute


# Sample html code:

# <a href="https://www.amazon.in/" id="a1" name="n1" class="c1">Amazon</a>

# Syntax:

# //tagname[@attribute_name='attribute value']

# //a[@href='https://www.amazon.in/']








'''
None of the seven selectors support indexing
can't locate text between any tag other than anchor
can't locate partial link text between any tag other than anchor

to overcome these drawbacks, we have xpath

XPATH:

- Absolute xpath
    - start from root
    - traverse every element from parent to child
    - meaning of / -> immediate child
    Drawbacks
    - not reusable
    - very lengthy
    - can't find the issue without doing it all over again
    - if UI changes, all xpaths should  be changed
- Relative xpath
    - have pre-defined syntax
    - meaning of // -> any child
    TYPES
        - xpath using attributes
            //tagname[@attribute name = 'attribute value']
            - @ -> represents attribute name and attribute value
        - xpath using text
            //tagname[text()='text']
            - text() is inbuilt
        - xpath using contains
            //tagname[contains(text(), 'partial_text')]
            - to locate the partial text of any tag
'''

from time import sleep
from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

# Relative - Attribute and Text

## Flipkart Example

# driver.get('https://www.flipkart.com/')
# sleep(2)
#
# driver.find_element('xpath', "//span[text()='TVs & Appliances']").click()
# sleep(2)
# driver.find_element('xpath', "//span[text()='Become a Seller']").click()
# sleep(2)
# driver.find_element('xpath', "//button[text()='Start Selling']").click()
# sleep(2)
# driver.find_element('xpath', "//input[@name='mobileNumber']").send_keys('9876543210')
# sleep(1)
# driver.find_element('xpath', "//input[@name='email']").send_keys('abc@gmail.com')
# sleep(1)
# driver.find_element('xpath', "//input[@name='gst']").send_keys('8888888888')
# sleep(1)
# driver.find_element('xpath', '//span[text()="Register & Continue"]').click()

################################################################

## Amazon Example
# driver.get('https://www.amazon.in')
# sleep(2)
#
# driver.find_element('xpath', "//a[text()='BestSeller']").click()
# sleep(2)
# driver.find_element('xpath', "//a[text()='Most Gifted']").click()
# sleep(2)
# driver.find_element('xpath', "//a[text()='Amazon Launchpad']").click()

################################################################

## Amazon Example 2
# driver.get('https://www.amazon.in')
# sleep(2)
#
# driver.find_element('xpath', '''//a[text()="Today's Deals"]''').click()
# sleep(2)
#
# driver.find_element('xpath', "//button[text()='Coupons']").click()
# sleep(2)
#
# driver.find_element('xpath', "//span[text()='Appliances']").click()
# sleep(2)

################################################################

## Group Indexing - used when a xpath is matching with multiple web elements

# Step 1: Write Down the xpath
# Step 2: Group the xpath by adding () around the xpath
# Step 3: Give index

# Eg:

# driver.get('https://www.facebook.com/r.php?entry_point=login')
# sleep(2)
#
# driver.find_element('xpath', '(//input[@type="text"])[1]').send_keys('Radha')
# sleep(1)
# driver.find_element('xpath', '(//input[@type="text"])[2]').send_keys('Goel')
# sleep(1)
# driver.find_element('xpath', '(//input[@type="text"])[5]').send_keys('radha@gmail.com')

# Relative - contains

# driver.get("https://www.giva.co/")
# sleep(2)
#
# driver.find_element('xpath', '//span[contains(text(), "Gold with Lab Diamonds")]').click()
# sleep(2)
#
# driver.find_element('xpath', '//span[contains(text(), "GIVA Gift Cards")]').click()
# sleep(2)

##########################################################################

## Dependent - Independent Xpath - used when one element is dependent on the behaviour or position of another element

# Identify the dependent and independent elements
# Write the xpath of the independent element
# Traverse back (going to the common parent of the dependent and independent element. it will represent both the elements) until we get the common match for the dependent-independent element - this is done using /.. -> immediate parent
# Continue writing the xpath of the dependent element

## Eg:

# driver.get("https://www.python.org/")
# sleep(2)
#
# driver.find_element('xpath', '//a[text()="Downloads"]').click()
# sleep(2)
#
# driver.find_element('xpath', '(//a[text()="Python 3.14.0"])[2]/../..//a[text()="Release Notes"]').click()



## Printing Text of web element

# Locate the web element
# Get the element using selenium
# Save the element in a variable
# use var_name.text to get the text of the element

# driver.get('https://in.tradingview.com/')
# sleep(2)
#
# driver.find_element('xpath', '//span[text()="Search"]').click()
# sleep(2)
#
# driver.find_element('xpath', '//input[@name="query"]').send_keys('HAL')
# sleep(2)
#
# driver.find_element('xpath', '(//button[@aria-label="Search"])[3]').click()
# sleep(2)
#
# hal_price = driver.find_element('xpath', '//span[text()="HAL"]/../../..//span[@class="priceWrapper-qWcO4bp9"]')
# print(hal_price.text)

########################################################################

# driver.get("https://www.iforex.in/tools/live-rates")
# sleep(2)
#
# driver.find_element('xpath', '(//div[@id="ai-chat-bubble-close")[2]').click()
# sleep(2)
#
# gold_sellprice = driver.find_element('xpath', '(//div[text()="Gold"]/../..//span)[2]')
# gold_buyprice = driver.find_element('xpath', '(//div[text()="Gold"]/../..//span)[3]')
#
# print(f"Sell price of Gold is {gold_sellprice.text}")
# print(f"Buy price of Gold is {gold_buyprice.text}")

#####################################################################

