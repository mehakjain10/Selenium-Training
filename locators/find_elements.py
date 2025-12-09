# Never use HREF to locate a web element because it is pointing to some other link and they can change

# find_element -> locates one web element
# find_elements -> located multiple elements
from time import sleep
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options)

# driver.get("https://demowebshop.tricentis.com/")
# sleep(2)
#
# footer_elements = driver.find_elements('xpath', '//div[@class="footer-menu-wrapper"]//a')
# print(footer_elements)
#
# for element in footer_elements:
#     print(element.text)

#######################################################################

# driver.get("https://demowebshop.tricentis.com/")
# sleep(2)


########################################################################

# driver.get(r'C:\Users\Mehak Jain\PycharmProjects\SeleniumTraining\RamyaMamNotes\demo.html')
# sleep(2)
#
# all_textboxes = driver.find_elements('xpath', '//input[@name="fname"]')
#
# data_text = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
#
# for textbox, text in zip(all_textboxes, data_text):
#     textbox.send_keys(text)

##################################################################################

# driver.get("https://www.python.org")
# sleep(2)
#
# links = driver.find_elements('tag name', 'a')
#
# for link in links:
#     print(link.get_attribute('href'))

