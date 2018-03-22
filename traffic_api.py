from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By

def test_xpath():
 
    capabilities = DesiredCapabilities.FIREFOX
    capabilities['marionette'] = True
 
    driver = webdriver.Remote(command_executor='http://sel01:4444/wd/hub',desired_capabilities=capabilities)
    driver.get("https://www.google.com/maps/dir/41.9147798,12.3850072/41.8650296,12.6014119/data=!3m1!4b1!4m2!4m1!5i1")
    driver.save_screenshot('screenshot.png')
    
    driver.close()    