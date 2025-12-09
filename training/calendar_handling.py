from time import sleep
from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

# driver.get("https://www.makemytrip.com/flights/")
# sleep(2)
# driver.maximize_window()
# sleep(2)
#
# driver.find_element('xpath', '//span[@class="commonModal__close"]').click()
# sleep(2)
#
# driver.find_element('xpath', '//span[text()="Departure"]').click()
# sleep(2)
#
# def select_date(month, date):
#     while True:
#         try:
#             driver.find_element('xpath', f'//div[text()="{month}"]/../..//p[text()="{date}"]').click()
#             break
#         except:
#             driver.find_element('xpath', '//span[@aria-label="Next Month"]').click()
#
# select_date('August 2026', '20')

'''
Go to https://www.irctc.co.in/nget/train-search, select the travel date
Go to https://www.redbus.in/, select the date of journey
Go to https://www.booking.com/, select the check-in date
'''

## Eg1

# driver.get('https://www.irctc.co.in/nget/train-search')
# sleep(2)
#
# driver.find_element('xpath', '//button[text()="OK"]').click()
# sleep(2)
#
# driver.find_element('xpath', '//span[@class="ng-tns-c69-9 ui-calendar"]').click()
# sleep(2)
#
# def select_date(month, date):
#     while True:
#         try:
#             driver.find_element('xpath', f'//span[text()="{month}"]/../../..//a[text()="{date}"]').click()
#             break
#         except:
#             driver.find_element('xpath', '//span[@class="ui-datepicker-next-icon pi pi-chevron-right ng-tns-c69-9"]').click()
#
# select_date('January', '10')

## Eg2

# driver.get('https://www.redbus.in/')
# sleep(2)
#
# driver.find_element('xpath', '//div[@class="dateInputWrapper___c8345a"]').click()
# sleep(2)
#
# while True:
#     month_year = driver.find_element('xpath', '//p[@class="monthYear___2b924f"]')
#
#     if month_year.text == 'May 2026':
#         driver.find_element('xpath', '//span[text()="17"]').click()
#         break
#     else:
#         driver.find_element('xpath', '//i[@class="icon icon-arrow arrow___2dd861 right___841620 "]').click()

## Eg3

driver.get('https://www.booking.com/')
sleep(2)

driver.find_element('xpath', '//button[@aria-label="Dismiss sign-in info."]').click()
sleep(2)

driver.find_element('xpath', '//button[@data-testid="searchbox-dates-container"]').click()
sleep(2)

while True:
    try:
        driver.find_element('xpath', '//h3[text()="December 2025"]/..//span[text()="21"]').click()
        break
    except:
        driver.find_element('xpath', '//button[@aria-label="Next month"]').click()

