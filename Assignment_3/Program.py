# Importing required libraries

# pip install selenium

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Setting up the webdriver
driver = webdriver.Chrome()

# Navigating to the Amazon.ca homepage
driver.get("https://www.amazon.ca")
time.sleep(10)



mainmenu_link = driver.find_element("xpath","/html/body/div[1]/header/div/div[4]/div[1]/a/i")
mainmenu_link.click()
time.sleep(5)

Newrelease_link = driver.find_element("xpath","/html/body/div[3]/div[2]/div/ul[1]/li[3]/a")
Newrelease_link.click()
time.sleep(4)

HealthCare_link = driver.find_element("xpath","/html/body/div[1]/div[1]/div[2]/div/div/div/div[2]/div/div[1]/div/div[1]/div/div/div/div/div[2]/div/div[2]/div/ol/li/div/div[2]/div/a[2]/span/div")
HealthCare_link.click()
time.sleep(4)

ProductReview_link = driver.find_element("xpath","/html/body/div[2]/div/div[5]/div[3]/div[4]/div[3]/div/span[1]/span/span[1]/a/i[1]")
ProductReview_link.click()
time.sleep(4)

Buynow_link = driver.find_element("xpath","/html/body/div[2]/div/div[5]/div[3]/div[1]/div[5]/div/div[1]/div/div[1]/div/div/div/div/div/form/div/div/div/div/div[4]/div/div[16]/div/div/span[2]/span/input ")
Buynow_link.click()
time.sleep(4)




time.sleep(2)



driver.close()
