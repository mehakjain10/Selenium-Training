from time import sleep
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options)

driver.get('https://testautomationpractice.blogspot.com/')
sleep(2)

# Without any loop

## Table Header
print(driver.find_element('xpath', f'//table[@name="BookTable"]//tr[1]/th[1]').text, end=' ')
print(driver.find_element('xpath', f'//table[@name="BookTable"]//tr[1]/th[2]').text, end=' ')
print(driver.find_element('xpath', f'//table[@name="BookTable"]//tr[1]/th[3]').text, end=' ')
print(driver.find_element('xpath', f'//table[@name="BookTable"]//tr[1]/th[4]').text, end=' ')
print()

## Table Data
print(driver.find_element('xpath', f'//table[@name="BookTable"]//tr[2]/td[1]').text, end=' ')
print(driver.find_element('xpath', f'//table[@name="BookTable"]//tr[2]/td[2]').text, end=' ')
print(driver.find_element('xpath', f'//table[@name="BookTable"]//tr[2]/td[3]').text, end=' ')
print(driver.find_element('xpath', f'//table[@name="BookTable"]//tr[2]/td[4]').text, end=' ')
print()

print(driver.find_element('xpath', f'//table[@name="BookTable"]//tr[3]/td[1]').text, end=' ')
print(driver.find_element('xpath', f'//table[@name="BookTable"]//tr[3]/td[2]').text, end=' ')
print(driver.find_element('xpath', f'//table[@name="BookTable"]//tr[3]/td[3]').text, end=' ')
print(driver.find_element('xpath', f'//table[@name="BookTable"]//tr[3]/td[4]').text, end=' ')
print()

print(driver.find_element('xpath', f'//table[@name="BookTable"]//tr[4]/td[1]').text, end=' ')
print(driver.find_element('xpath', f'//table[@name="BookTable"]//tr[4]/td[2]').text, end=' ')
print(driver.find_element('xpath', f'//table[@name="BookTable"]//tr[4]/td[3]').text, end=' ')
print(driver.find_element('xpath', f'//table[@name="BookTable"]//tr[4]/td[4]').text, end=' ')
print()

print(driver.find_element('xpath', f'//table[@name="BookTable"]//tr[5]/td[1]').text, end=' ')
print(driver.find_element('xpath', f'//table[@name="BookTable"]//tr[5]/td[2]').text, end=' ')
print(driver.find_element('xpath', f'//table[@name="BookTable"]//tr[5]/td[3]').text, end=' ')
print(driver.find_element('xpath', f'//table[@name="BookTable"]//tr[5]/td[4]').text, end=' ')
print()

print(driver.find_element('xpath', f'//table[@name="BookTable"]//tr[6]/td[1]').text, end=' ')
print(driver.find_element('xpath', f'//table[@name="BookTable"]//tr[6]/td[2]').text, end=' ')
print(driver.find_element('xpath', f'//table[@name="BookTable"]//tr[6]/td[3]').text, end=' ')
print(driver.find_element('xpath', f'//table[@name="BookTable"]//tr[6]/td[4]').text, end=' ')
print()

print(driver.find_element('xpath', f'//table[@name="BookTable"]//tr[7]/td[1]').text, end=' ')
print(driver.find_element('xpath', f'//table[@name="BookTable"]//tr[7]/td[2]').text, end=' ')
print(driver.find_element('xpath', f'//table[@name="BookTable"]//tr[7]/td[3]').text, end=' ')
print(driver.find_element('xpath', f'//table[@name="BookTable"]//tr[7]/td[4]').text, end=' ')
print()
print()

##---------------------------------------------------------------------------------------------------------------------

# Using for loop

## Table Header
for i in range(1,5):
    print(driver.find_element('xpath', f'//table[@name="BookTable"]//tr[1]/th[{i}]').text, end=' ')
print()

## Table Data
for i in range(2,8):
    for j in range(1,5):
        print(driver.find_element('xpath', f'//table[@name="BookTable"]//tr[{i}]/td[{j}]').text, end=' ')
    print()