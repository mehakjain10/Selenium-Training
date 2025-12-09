from itertools import dropwhile

from selenium import webdriver
# from time import sleep (1)
import time #(2)
opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach",True)
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
