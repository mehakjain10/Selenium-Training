'''
xpath   :   To locate any web-element on the application uniquely, we go for xpath
            We can locate the elements using attributes, can locate elements using text,
            indexing is possible, can locate dynamically changing elements, backtraversing is possible.
            We can locate any element on the web-application using xpath

            There are 2 types of xpath
            *   absolute xpath  :   Starts from the root of html
                                    We use / to write the absolute xpath
                                    / represents immediate child

            *   relative xpath  :   Doesnot start from the root of html
                                    We use // to write the relative xpath
                                    // represents any child

'''
import time

# ## Eg1
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get(r'C:\Users\Ramya\PycharmProjects\Sel-M15-Aug11\files_\css_selector_dup.html')
# time.sleep(2)
#
# driver.find_element('xpath', 'html/body/input[1]').send_keys('Amit')
# time.sleep(1)
# driver.find_element('xpath', 'html/body/input[2]').send_keys('amit@12345')

###############################################################################

# ## Eg2
#
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://www.saucedemo.com/')
# time.sleep(2)
#
# driver.find_element('xpath', 'html/body/div/div/div[2]/div[1]/div/div/form/div[1]/input').send_keys('standard_user')
# time.sleep(1)
# driver.find_element('xpath', 'html/body/div/div/div[2]/div[1]/div/div/form/div[2]/input').send_keys('secret_sauce')
# time.sleep(1)
# driver.find_element('xpath', 'html/body/div/div/div[2]/div[1]/div/div/form/input').click()


###############################################################################

'''
attributes  :   //tagname[@attr_name="attr_value"]
                @ represents attribute
'''

# ## Eg1
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://www.saucedemo.com/')
# time.sleep(2)
#
# driver.find_element('xpath', '//input[@id="user-name"]').send_keys('standard_user')
# time.sleep(1)
# driver.find_element('xpath', '//input[@id="password"]').send_keys('secret_sauce')
# time.sleep(1)
# driver.find_element('xpath', '//input[@id="login-button"]').click()
# time.sleep(3)
# driver.find_element('xpath', '//button[@id="react-burger-menu-btn"]').click()
# time.sleep(2)
# driver.find_element('xpath', '//a[@id="logout_sidebar_link"]').click()

########################################################################

# ## Eg2
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://www.facebook.com/r.php?entry_point=login')
# time.sleep(2)
#
# driver.find_element('xpath', '//input[@name="firstname"]').send_keys('Harry')
# time.sleep(1)
# driver.find_element('xpath', '//input[@name="lastname"]').send_keys('Potter')
# time.sleep(1)
# driver.find_element('xpath', '//input[@name="reg_email__"]').send_keys('harry@gmail.com')
# time.sleep(1)
# driver.find_element('xpath', '//input[@name="reg_passwd__"]').send_keys('harry@12345')

########################################################################

'''
text()  :   //tagname[text()="text"] 
'''

# ## Eg1
#
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://www.flipkart.com/')
# time.sleep(2)
# driver.find_element('xpath', '//span[text()="Mobiles & Tablets"]').click()
# time.sleep(2)
# driver.find_element('xpath', '//a[text()="Flights"]').click()
# time.sleep(2)
# driver.find_element('xpath', '//a[text()="Login"]').click()

###############################################################################################

# ## Eg2
#
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://www.swarovski.com/')
# time.sleep(2)
#
# driver.find_element('xpath', '//span[text()="Jewelry"]').click()
# time.sleep(2)
# driver.find_element('xpath', '//span[text()="Decorations"]').click()
# time.sleep(2)
# driver.find_element('xpath', '//span[text()="Swarovski Created Diamonds"]').click()

###############################################################################################
'''
Group indexing  :   (any_xpath)[index_num]
'''

# ## Eg1
#
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://www.facebook.com/r.php?entry_point=login')
# time.sleep(2)
#
# driver.find_element('xpath', '(//input[@type="text"])[1]').send_keys('Sherlock')
# time.sleep(1)
# driver.find_element('xpath', '(//input[@type="text"])[2]').send_keys('Holmes')
# time.sleep(1)
# driver.find_element('xpath', '(//input[@id="sex"])[2]').click()
# time.sleep(2)
# driver.find_element('xpath', '(//input[@type="text"])[5]').send_keys('sherlock@gmail.com')

###############################################################################################

# ##Eg2
#
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://www.youtube.com')
# time.sleep(2)
#
# driver.find_element('xpath', '//input[@name="search_query"]').send_keys('Kaantara')
# time.sleep(2)
# driver.find_element('xpath', '//button[@title="Search"]').click()
# time.sleep(2)
# driver.find_element('xpath', '(//a[@id="video-title"])[1]').click()

###############################################################################################

# ##Eg3
#
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://store.steampowered.com/')
# time.sleep(2)
# driver.find_element('xpath', '//a[text()="login"]').click()
# time.sleep(2)
# driver.find_element('xpath', '(//input[@type="text"])[1]').send_keys('saawan_kumar')
# time.sleep(1)
# driver.find_element('xpath', '//input[@type="password"]').send_keys('saawan@12345')
# time.sleep(1)
# driver.find_element('xpath', '//button[text()="Sign in"]').click()


###############################################################################################

# ##Eg4
#
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://www.primevideo.com/')
# time.sleep(2)
# driver.find_element('xpath', '//a[text()="Sign in to join Prime"]').click()
# time.sleep(2)
# driver.find_element('xpath', '//a[@id="createAccountSubmit"]').click()
# time.sleep(2)
# driver.find_element('xpath', '//input[@id="ap_customer_name"]').send_keys('Sai Nagesh')
# time.sleep(1)
# driver.find_element('xpath', '//input[@id="ap_phone_number"]').send_keys('9080706050')
# time.sleep(1)
# driver.find_element('xpath', '//input[@id="ap_password"]').send_keys('Nagesh@12345')
# time.sleep(1)
# driver.find_element('xpath', '//input[@id="continue"]').click()
# time.sleep(7)

###############################################################################################
#
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://www.instagram.com/accounts/emailsignup/')
# time.sleep(2)
# driver.find_element('xpath', '(//input[@class="_aa4b _add6 _ac4d _ap35"])[2]').send_keys('supreethi@12345')
# time.sleep(2)
# driver.find_element('xpath', '(//input[@class="_aa4b _add6 _ac4d _ap35"])[1]').send_keys('Supreethi@gmail.com')
#

###############################################################################################

'''
contains    :   Locate the partial text of any tagname.
                SYNTAX  :   //tagname[contains(text(), "partial_text")]

'''
#
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://www.giva.co/')
# time.sleep(2)
#
# driver.find_element('xpath', '//span[contains(text(), "Gold with Lab Diamonds")]').click()
# time.sleep(2)
# driver.find_element('xpath', '//span[contains(text(), "Collections")]').click()
# time.sleep(2)
# driver.find_element('xpath', '//span[contains(text(), "GIVA Gift Card")]').click()
#
# ###############################################################################################
# ## Eg2
#
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://www.malabargoldanddiamonds.com/')
# time.sleep(2)
#
# driver.find_element('xpath', '//a[contains(text(), "Uncut Diamond")]').click()
# time.sleep(2)
# driver.find_element('xpath', '(//a[contains(text(), "Silver")])[1]').click()
# time.sleep(2)
# driver.find_element('xpath', '//a[contains(text(), "jewellery")]').click()


###############################################################################################
'''
Dependent-Independent xpath
    *   Identify the dependent-independent xpath
    *   Write the xpath of the independent element
    *   Traverse back(/..) until we get the common match for dependent-independent element 

'''

'''
Eg1. wap to click on the checkbox of Ruby in demo.html
'''
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get(r'C:\Users\Ramya\PycharmProjects\Sel-M15-Aug11\files_\demo.html')
# time.sleep(2)
#
# driver.find_element('xpath', '//td[text()="Ruby"]/..//input[@name="download"]').click()
#
# ###############################################################################################
#
'''
Eg2.    wap to click on the download link of windows in demo.html
'''
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get(r'C:\Users\Ramya\PycharmProjects\Sel-M15-Aug11\files_\demo.html')
# time.sleep(2)
# driver.find_element('xpath', '//td[text()="Windows"]/..//a[text()="Download"]').click()


###############################################################################################
'''
Eg3.    wap to click on the release notes of python 3.13.4 in https://www.python.org/
'''

# from selenium import webdriver
#
# driver = webdriver.Firefox()
#
# driver.get('https://www.python.org/')
# time.sleep(2)
#
# ## clicking on downloads
# driver.find_element('xpath', '(//a[text()="Downloads"])[1]').click()
# time.sleep(2)
#
# driver.find_element('xpath', '//a[text()="Python 3.13.4"]/../..//a[text()="Release Notes"]').click()

###############################################################################################

'''
Eg4.    wap to print the sellprice and buyprice of Gold in https://www.iforex.in/tools/live-rates   
'''
#
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://www.iforex.in/tools/live-rates')
# time.sleep(4)
#
# gold_sellprice = driver.find_element('xpath', '(//div[text()="Gold"]/../..//span)[2]')
# # print(gold_sellprice)       ## web-element
# print(f"Sell price of Gold is {gold_sellprice.text}")
#
# gold_buyprice = driver.find_element('xpath', '(//div[text()="Gold"]/../..//span)[3]')
# print(f"Buy price of Gold is {gold_buyprice.text}")


###############################################################################################

'''
Eg5.    wap to print the price of Tatamotors in https://in.tradingview.com/
'''
#
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://in.tradingview.com/')
# time.sleep(2)
#
# driver.find_element('xpath', '//span[text()="Search"]').click()
# time.sleep(2)
#
# driver.find_element('xpath', '//input[@name="query"]').send_keys('Tatamotors')
# time.sleep(2)
#
# driver.find_element('xpath', '(//button[@aria-label="Search"])[3]').click()
# time.sleep(2)
#
# tatamotors = driver.find_element('xpath', '//span[text()="TATAMOTORS"]/../../..//span[@class="priceWrapper-qWcO4bp9"]')
# print(tatamotors.text)






































