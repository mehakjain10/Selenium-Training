from time import sleep
from selenium import webdriver

# options = webdriver.ChromeOptions()
# options.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(options)

''' Upload Single File'''

# driver.get('https://testautomationpractice.blogspot.com/')
# sleep(2)
#
# file_path = r'C:\Users\Mehak Jain\PycharmProjects\SeleniumTraining\training\basics.py'
#
# driver.find_element('xpath', '//input[@id="singleFileInput"]').send_keys(file_path)

########################################################################

''' Upload Multiple Files '''

# driver.get('https://testautomationpractice.blogspot.com/')
# sleep(2)
#
# file1 = r'C:\Users\Mehak Jain\PycharmProjects\SeleniumTraining\training\alerts.py'
# file2 = r'C:\Users\Mehak Jain\PycharmProjects\SeleniumTraining\training\attributes.py'
# file3 = r'C:\Users\Mehak Jain\PycharmProjects\SeleniumTraining\training\basics.py'
#
# driver.find_element('xpath', '//input[@id="multipleFilesInput"]').send_keys(f'{file1}\n{file2}\n{file3}')

####################################################################

''' Download Files '''

# CHROME BROWSER

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

prefs = {
    "download.default_directory" : r'C:\Users\Mehak Jain\PycharmProjects\SeleniumTraining\screenshots',
    "download.prompt_for_download" : False,
    "safebrowsing.enabled" : True,
    "plugins.always_open_pdf_externally" : True
}

options.add_experimental_option("prefs", prefs)

driver = webdriver.Chrome(options)

driver.get('https://demoqa.com/upload-download')
sleep(2)

driver.find_element('xpath', '//a[text()="Download"]').click()

##------------------------------------------------------------

# FIREFOX BROWSER

# options = webdriver.FirefoxOptions()
#
# options.set_preference("browser.download.folderList", 2)
# options.set_preference("browser.download.dir", r'C:\Users\Mehak Jain\PycharmProjects\SeleniumTraining\screenshots')
# options.set_preference('pdfjs.disabled', True)
#
#
# driver = webdriver.Firefox(options)
#
# driver.get('https://demoqa.com/upload-download')
# sleep(2)
#
# driver.find_element('xpath', '//a[text()="Download"]').click()

