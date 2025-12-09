'''



'''

'''
MOUSE HOVER OPERATION : 
- uses ActionChains class and move_to_element(element to be hovered) function. 
- for ActionChains object, obj.function_name will get the operation ready. In order to perform it in automation, 
  perform() function must be given after the operation
'''
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options)
actionChain = ActionChains(driver)

# driver.get('https://www.myntra.com/')
# sleep(2)
#
# navigation_elements = driver.find_elements('xpath', '//a[@class="desktop-main"]')
#
# for element in navigation_elements[:-1]:
#     actionChain.move_to_element(element).perform()
#     sleep(1)

#######################################################################################################################
'''
MOUSE HOVER OPERATION : 
- uses ActionChains class and drag_and_drop(element to be dragged, element where dragged element should go) function. 
'''
# driver.get('https://testautomationpractice.blogspot.com/')
# sleep(2)
#
# ele = driver.find_element('xpath', '//h2[text()="SVG Elements"]')
# actionChain.scroll_to_element(ele).perform()
# sleep(2)
#
# drag = driver.find_element('xpath', '//div[@id="draggable"]')
# drop = driver.find_element('xpath', '//div[@id="droppable"]')
#
# actionChain.drag_and_drop(drag, drop).perform()

'''
Go to https://crossbrowsertesting.github.io/drag-and-drop.html, perform drag and drop
'''

driver.get('https://crossbrowsertesting.github.io/drag-and-drop.html')
sleep(2)

drag = driver.find_element('xpath', '//div[@id="draggable"]')
drop = driver.find_element('xpath', '//div[@id="droppable"]')

actionChain.drag_and_drop(drag, drop).perform()
