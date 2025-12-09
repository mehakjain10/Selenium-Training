'''
QUESTIONS:

1.  wap to fetch all the popular searches from https://www.myntra.com/
2.  wap to print all the colors available for adidas original shoes in https://www.myntra.com/
3.  Go to https://www.zomato.com/Bengaluru/, search for pizza, select pizza-delivery, select any cafe/restraunt which serves pizza,
    wap to print the name and price of each food item in available
4.  Go to https://in.bookmyshow.com/, select the location. Print all the movie names available.
'''
from time import sleep
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options)

#######################################################################################################################

'''
QUESTION 1: wap to fetch all the popular searches from https://www.myntra.com/
'''

# driver.get("https://www.myntra.com/")
# sleep(2)
#
# search_links = driver.find_elements('xpath', '//div[@class="desktop-pSearchlinks"]/a')
#
# for link in search_links:
#     print(link.text, "=", link.get_attribute('href'))

#######################################################################################################################

'''
QUESTION 2: wap to print all the colors available for adidas original shoes in https://www.myntra.com/
'''

# driver.get('https://www.myntra.com/')
# sleep(2)
#
# driver.find_element('xpath', '//input[@class="desktop-searchBar"]').send_keys('adidas')
# sleep(2)
#
# driver.find_element('xpath', '//li[text()="Adidas Originals Shoes"]').click()
# sleep(2)
#
# driver.find_element('xpath', '//div[@class="colour-more"]').click()
# sleep(2)
#
# colors = driver.find_elements('xpath', '//li[@class="colour-listItem"]')
#
# for color in colors:
#     print(color.text)

#######################################################################################################################

'''
QUESTION 3: Go to https://www.zomato.com/Bengaluru/, search for pizza, select pizza-delivery, select any cafe/restraunt which serves pizza,
    wap to print the name and price of each food item in available
    
    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! NOT DONE !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
'''

# driver.get('https://www.zomato.com/Bengaluru/')
# sleep(2)
#
# driver.find_element('xpath', '//input[@placeholder="Search for restaurant, cuisine or a dish"]').send_keys('pizza')
# driver.find_element('xpath', '//input[@placeholder="Search for restaurant, cuisine or a dish"]').click()
# sleep(2)
#
# driver.find_element('xpath', '//p[text()="Pizza - Delivery"]').click()
# sleep(2)
#
# driver.find_element('xpath', '//div[@class="jumbo-tracker"]').click()
# sleep(2)
#
# dishes = driver.find_elements('xpath', '//div[@class="sc-bcdylZ hQCfYM"]/h4')
# prices = driver.find_elements('xpath', '//span[@class="sc-17hyc2s-1 cCiQWA"]')
#
# # for dish, price in zip(dishes, prices):
# #     print(dish.text, "=", price.text)
#

'''
QUESTION 4: Go to https://in.bookmyshow.com/, select the location. Print all the movie names available.
'''

# driver.get('https://in.bookmyshow.com/')
# sleep(2)
#
# driver.find_element('xpath', '//p[text()="Delhi-NCR"]').click()
# sleep(2)
#
# driver.find_element('xpath', '//div[text()="See All ›"]').click()
# sleep(4)
#
# movie_names = driver.find_elements('xpath', '//div[@class="sc-7o7nez-0 elfplV"]')
#
# for movie in movie_names:
#     print(movie.text)