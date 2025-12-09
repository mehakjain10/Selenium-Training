
# from selenium import webdriver
# from time import sleep (1)
# import time #(2)
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach",True)
"""
driver = webdriver.Chrome(options=opts)
driver.get("file:///C:/Users/Admin/Desktop/demo.html")
driver.maximize_window()
time.sleep(3)
# Way2:
# username = driver.find_element("class name","c1")
# username.send_keys()
# Way1:
# driver.find_element("class name","c1").send_keys("Moye Moye")
# driver.find_element("class name","c2").send_keys("Hui Hui")

driver.find_element("class name","user name").send_keys("Sangi weds mangi")
#No Such Element Exception

driver.find_element("class name","user.name").send_keys("Sangi weds mangi")
"""


# without replacing the space
"""
driver = webdriver.Chrome(options=opts)
driver.get("https://demowebshop.tricentis.com/register")
driver.maximize_window()
time.sleep(3)
driver.find_element("class name","text-box single-line").send_keys("Amitabh Mama")
#NoSuchElementException
"""
# With replacing the space with dot:
"""
driver = webdriver.Chrome(opts)
driver.get("https://demowebshop.tricentis.com/register")
driver.maximize_window()
time.sleep(3)
driver.find_element("class name","text-box.single-line").send_keys("Selenium")
"""

# Tag name:
"""
driver = webdriver.Chrome(opts)
driver.get("https://demowebshop.tricentis.com/")
driver.maximize_window()
time.sleep(3)
driver.find_element("tag name","a").click()
"""
"""
driver = webdriver.Chrome(opts)
driver.get("https://demowebshop.tricentis.com/register")
time.sleep(3)
driver.find_element("tag name","input").send_keys("Selenium")
"""
# find_elements():
"""
driver = webdriver.Chrome(opts)
driver.get()
time.sleep(3)
driver.find_element("id","First")
"""

# id:
from selenium import webdriver
import time
opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach",True)

# Possibility 1:
"""
driver = webdriver.Chrome(opts)
driver.get("file:///C:/Users/Admin/Desktop/sample.html")
time.sleep(2)
driver.find_element("id","a1").send_keys("Moye Moye")
"""
# Possibility 2:

"""
driver = webdriver.Chrome(opts)
driver.get("file:///C:/Users/Admin/Desktop/sample.html")
time.sleep(2)
driver.find_element("id","a1").send_keys("Password")
"""
# Possibility 3:

"""
driver = webdriver.Chrome(opts)
driver.get("file:///C:/Users/Admin/Desktop/sample.html")
time.sleep(2)
driver.find_element("id","f1").send_keys("Password")

# NoSuchElementException
"""

"""
driver = webdriver.Chrome(opts)
driver.get("C:/Users/Admin/Desktop/sample.html")
time.sleep(2)
driver.find_element("if","a1").send_keys("Username")

InvalidArgumentException
"""
"""
driver = webdriver.Chrome(opts)
driver.get("www.amazon.in")
# InvalidArgumentException: Message: invalid argument
"""
"""
driver = webdriver.Chrome(opts)
driver.get("https://www.facebook.com/")
time.sleep(3)
driver.find_element("id","email").send_keys("Sangi@gmail.com")
time.sleep(3)
driver.find_element("id","pass").send_keys("mangi@143")
time.sleep(3)
driver.find_element("id","u_0_5_Fo").click()
# No Such Element Exception
"""
"""
driver = webdriver.Chrome(opts)
driver.get("https://www.apple.com/in/")
time.sleep(3)
driver.find_element("link text","Mac").click()
"""
"""
driver = webdriver.Chrome(opts)
driver.get("https://www.udemy.com/?srsltid=AfmBOoo4hmoNb6Wh5YORtxfUokZWS5Ey9-BzMF4T4xB4IKtxnPsFrA_F")
time.sleep(3)
driver.find_element("link text","Sign up").click()
time.sleep(3)
driver.find_element("name","full-name").send_keys("Pookie")
time.sleep(3)
driver.find_element("name","email").send_keys("Pookie@gmail.com")
time.sleep(3)
driver.find_element("class name","ud-icon.ud-icon-xsmall.ud-fake-toggle-input.ud-fake-toggle-checkbox").click()
time.sleep(3)
driver.find_element("class name","ud-btn.ud-btn-large.ud-btn-brand.ud-btn-text-md.passwordless-auth-mx-code-generation-form--submit-button--2vOvZ").click()
"""
# Partial Link text:
#     It is used to find the location of an element by passing some portion of a text value
#     It will work only for anchor tag (it will work for span tag also but not all the time)
#     In this also the text value is case sensitive

# Note:
#     In link text you have to pass the text value completely but in partial link text you have to pass the text value some portion
#     Both link text and partial link text are case sensitive
# Amazon in Ecommerce website
"""
2025 --> Python 3.14.0
2026 --> Python 4.11.0
"""

# 2026:
"""
driver = webdriver.Chrome(opts)
driver.get("file:///C:/Users/Admin/Desktop/sample.html")
time.sleep(3)
driver.find_element("link text","Python 3.14.0").click()
"""
# NoSuchElementException

# Python 3.14.0
"""
driver = webdriver.Chrome(opts)
driver.get("file:///C:/Users/Admin/Desktop/sample.html")
time.sleep(3)
driver.find_element("partial link text","Python").click()
"""
"""
import time

driver = webdriver.Chrome(opts)
driver.get("https://www.selenium.dev/downloads/")
time.sleep(3)
driver.find_element("partial link text","languages").click()
"""

# CSS SELECTOR:
# What is Css?
#     --> Css stands for Cascading style Sheet
#     --> It is used to decorate a webpage like color,font size,Background etc.....

# What is css selector?
#     It is used to find the location of a web element by using css expression

# css expression:
"""
    syntax:
        tagname[attribute name='attribute value']
        Any attribute including id,name,class etcc....
"""

# Where we have to write css expression?
"""
Step 1 : Inspect the element
Step 2 : Press ctrl+f in your keyboard "find my string" search will get appear
Step 3 : type the css expression
"""

# Verify the css expression to check if the expression is valid or not:
"""
1.Element should get highlight
2.code should get highlight in yellow color
3.(1 of 1) Matching you have to get
"""
# Drawbacks of css selector:
"""
1.We can't able to make 1 of 1 matching
2.We can't use this for text value
"""
# Sample code:
"""
driver = webdriver.Chrome(opts)
driver.get("https://demowebshop.tricentis.com/login")
time.sleep(3)
driver.find_element("css selector","input[class='email']").send_keys("Amitabh bachhan@gmail.com")
"""
# Tagname[an = 'av']
"""
driver = webdriver.Chrome(opts)
driver.get("https://www.myntra.com/")
time.sleep(3)
driver.find_element("css selector","input[class='desktop-searchBar']").send_keys("Iphone")
"""

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
driver = webdriver.Chrome(opts)
driver.get("file:///C:/Users/Admin/Desktop/A2_Selenium/xpath.html")
time.sleep(3)
driver.find_element("xpath","html/body/div[1]/input[1]").send_keys("Username1")

"""
"""
driver = webdriver.Chrome(opts)
driver.get("file:///C:/Users/Admin/Desktop/A2_Selenium/xpath.html")
time.sleep(3)
driver.find_element("xpath","html/body/div[2]/input[2]").send_keys("Username4")
"""
"""
driver = webdriver.Chrome(opts)
driver.get("https://demowebshop.tricentis.com/")
time.sleep(3)
driver.find_element("xpath","html/body/div[4]/div[1]/div[1]/div[2]/div[1]/ul/li[1]/a").click()
"""


