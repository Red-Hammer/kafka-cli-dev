from selenium import webdriver


import time



driver = webdriver.Chrome()
driver.get('https://knotfest.com/cto-voting/')

button = driver.find_element_by_xpath("//form[input/@value='4083']")

print(button)