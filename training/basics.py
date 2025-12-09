'''
What is Automation?
- Testing the functionality of the application by using any automation tool is called Automation

Why Automation?
- To reduce the human effort in the repetitive task
- To reduce thr time in the repetitive task
- To maintain the accuracy and consistency of testing
- To sustain in the market
- If the product size is big, the regression test case will get increase, to avoid that we go for automation

When you will go for automation?
- When the application or a software is functionally stable, we go for automation


What is selenium?
Difference between Selenium and Automation?
Advantages of Selenium?
Drawbacks of Selenium?
Browser methods?
Verification methods?

* Basics of HTML

What is locators?
Why locators? - selenium doesn't know where each web element is so we use locators to help selenium locate the element to automate it
Types of locators?
    - id
    - name
    - class name
    - tag name
    - link text
    - partial link text
    - css selector
    - xpath




'''




from selenium import webdriver

## Launching Chrome Browser
# c_driver = webdriver.Chrome()

## To prevent the Chrome browser to close automatically after launching
opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

c_driver = webdriver.Chrome(opts)

#######################################################################################################################################################################

## Launching Firefox Browser
from selenium  import webdriver
f_driver = webdriver.Firefox()

#######################################################################################################################################################################

## Launching Edge Browser
from selenium import webdriver
e_driver = webdriver.Edge()