from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
import time

def test_xpath():
 
    capabilities = DesiredCapabilities.FIREFOX
    capabilities['marionette'] = True
 
    driver = webdriver.Remote(command_executor='http://sel01:4444/wd/hub',desired_capabilities=capabilities)
    driver.get("https://www.google.com/maps/dir/41.9147798,12.3850072/41.8650296,12.6014119")
    km = driver.find_element_by_xpath("//div[@id='pane']")
    #locator2 = "//div[@id='section-directions-trip-0']"
    locator2 = "/html/body/jsl/div[3]/div[8]/div[8]/div/div[1]/div/div/div[5]/div[1]/div[2]/div[1]/div[1]/div[1]/span[1]"
    km2 = driver.find_element_by_xpath(locator2)
    print km2
    print km
    #time.sleep( 10 )
    #driver.save_screenshot('screenshot.png')
    
    
    driver.close()    
