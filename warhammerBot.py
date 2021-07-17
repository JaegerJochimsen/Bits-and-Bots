from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from botAux import approxName

PATH = "C:\Program Files (x86)\chromedriver.exe"
EMAIL = None
PASS = None
DEFAULT_POS = None
NAME_OF_PRODUCT = None

pageURL = 'https://www.games-workshop.com/en-US/Warhammer-40-000?N=2562756967+3206404541&Nr=AND%28sku.siteId%3AUS_gw%2Cproduct.locale%3Aen_US_gw%29&Nrs=collection%28%29%2Frecord%5Bproduct.startDate+%3C%3D+1625419080000+and+product.endDate+%3E%3D+1625419080000%5D'

# link path to driver
driver = webdriver.Chrome(PATH)

# opens tab with supplied link
driver.get("https://www.games-workshop.com/en-US/Warhammer-40-000?N=2562756967+3206404541&Nr=AND%28sku.siteId%3AUS_gw%2Cproduct.locale%3Aen_US_gw%29&Nrs=collection%28%29%2Frecord%5Bproduct.startDate+%3C%3D+1625419080000+and+product.endDate+%3E%3D+1625419080000%5D")

# grab password and email for use later
with open("localInfo.txt", 'r') as f:
	EMAIL = f.readline().strip()
	PASS = f.readline().strip()
	DEFAULT_POS = int(f.readline().strip())
	NAME_OF_PRODUCT = f.readline().strip()

# deal with cookie pop-up
try:
    cookie = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'onetrust-reject-all-handler')))
    cookie.click()
finally:
	pass

# wait until our desired element is available
# allLi = []
# while len(allLi) < DESIRED_POS:
# 	allLi = driver.find_elements_by_xpath("//*[contains(@id,'item-')]")

allLi = driver.find_elements_by_xpath("//*[contains(@id, 'item-')]")
# check to 
for li in allLi:
	txt = li.text.split("\n")[0]
	if approxName(NAME_OF_PRODUCT, txt):
		DEFAULT_POS = allLi.index(li) + 1
		break

# once it becomes available
try:
	desiredLi = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, f'./html/body/div/div/div/section[2]/div[2]/ul/li[{DEFAULT_POS}]/section/button[1]/span')))
	desiredLi.click()

	try:
		checkout = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="container"]/header/div[2]/div/div[3]/a/div')))
		checkout.click()


		try:
			checkout2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main"]/section[1]/button')))
			checkout2.click()

			try:
				login = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div/div/div[1]/div/section/section/a/span[1]')))
				login.click()
				
				driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div[1]/form/div[3]/div/div[2]/div[1]/div/div/input').send_keys(f"{EMAIL}")

				password = driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div[1]/form/div[3]/div/div[2]/div[2]/div/div/input')
				password.send_keys(f'{PASS}')
				password.send_keys(Keys.RETURN)

			finally:
				pass

		finally:
			pass
	finally:
		pass
finally:
	pass






