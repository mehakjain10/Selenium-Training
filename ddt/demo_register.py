import time

from selenium import webdriver

from ddt.reading_excel import reading_testdata

path = r'C:\Users\Mehak Jain\PycharmProjects\SeleniumTraining\ddt\testdata.xlsx'
sheet = 'register'
data = reading_testdata(path, sheet)

## data = {'firstname': 'Mehak', 'lastname': 'Jain', 'email': 'mehak@gmail.com', 'pwd': 'mehak@123', 'confirm_pwd': 'mehak@123'}

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)

driver = webdriver.Chrome(opts)

driver.get('https://demowebshop.tricentis.com/')
time.sleep(2)

driver.find_element('xpath', '//a[text()="Register"]').click()
time.sleep(2)

driver.find_element('id', 'gender-female').click()
time.sleep(1)
driver.find_element('id', 'FirstName').send_keys(data['firstname'])
time.sleep(1)
driver.find_element('id', 'LastName').send_keys(data['lastname'])
time.sleep(1)
driver.find_element('id', 'Email').send_keys(data['email'])
time.sleep(1)
driver.find_element('id', 'Password').send_keys(data['pwd'])
time.sleep(1)
driver.find_element('id', 'ConfirmPassword').send_keys(data['confirm_pwd'])