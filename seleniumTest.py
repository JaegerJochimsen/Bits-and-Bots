import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

PATH = "C:\Program Files (x86)\chromedriver.exe"

# link path to driver
driver = webdriver.Chrome(PATH)

# opens tab with supplied link
driver.get("https://recweb.uoregon.edu/")

# interact with login button
loginLink = driver.find_element_by_id("loginLink")
loginLink.click()

time.sleep(0.5)

# fill out username field
userName = driver.find_element_by_id('txtUsername')
userName.click()
userName.send_keys("jaegerj")

# fill out password field
passWord = driver.find_element_by_id("txtPassword")
passWord.click()
passWord.send_keys("EmMyDak9910")

logInButton = driver.find_element_by_id("btnLogin")
logInButton.click()

time.sleep(0.5)

# select reservation button and subsequent reservation category
reservationButton = driver.find_element_by_xpath('//*[@id="mainContent"]/div[2]/div/div[1]/a/span[1]/img')
reservationButton.click()

time.sleep(0.5)

specificReserve = driver.find_element_by_xpath('//*[@id="list-group"]/div[1]/div/div[1]/img')
specificReserve.click()

time.sleep(0.5)

acknowledgement = driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[1]/div/p[2]/button[1]')
acknowledgement.click()

time.sleep(0.1)

earlySlot = driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/section/div[1]/div/div/div[2]/button')
earlySlot.click()

time.sleep(0.5)

checkout = driver.find_element_by_id('checkoutButton')
checkout.click()

time.sleep(0.5)

confirmCheckout = driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/div[5]/div/div/div[2]/div/div[2]/button')
confirmCheckout.click()

# closes current tab, use .quit() to close browser
driver.close()