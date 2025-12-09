## Package Imports
import time
from selenium import webdriver

## Launch The Browser
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options)

## Launch The Application On The Browser
driver.get("https://www.myntra.com")
time.sleep(2)

## Maximize Window
driver.maximize_window()
time.sleep(2)

## Minimize Window
driver.minimize_window()
time.sleep(2)

## Go Back To Previous Window
driver.back()
time.sleep(2)

## Go Forward To Next Window
driver.forward()
time.sleep(2)

## Refresh The Pages
driver.refresh()
time.sleep(2)

## Properties Of The Application
print(driver.title)
print(driver.current_url)
print(driver.name)
print(driver.page_source)

## Take A Screenshot In Same Directory
driver.save_screenshot('myntra_home.png')

## Take A Screenshot In Different Directory
driver.save_screenshot(r'C:\Users\Mehak Jain\PycharmProjects\SeleniumTraining\screenshots\myntra_home.png')

## Close The Browser
driver.close()