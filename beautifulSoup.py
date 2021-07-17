import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

newURL = 'https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38'

# open new .csv file to save data
fileName = "graphicsData.csv"
headers = "brand,currPrice,prevPrice"

with open(fileName, "w") as f:
	# add headers to .csv
	f.write(headers + "\n")

	# open up connection to url, grab page
	uClient = uReq(newURL)
	pageHTML = uClient.read()
	uClient.close()

	# parses html, now it is a soup obj
	pageSoup = soup(pageHTML, "html.parser")

	# grab all containers 
	containers = pageSoup.findAll("div", {"class":"item-container"})

	for container in containers:
		brand = container.div.div.a.img["title"]

		# list comprehension to grab text from each feature in li
		features = [feature.text for feature in container.findAll("ul", {"class": "item-features"})[0].findAll("li")]
		features = "".join(features)
		
		# grab price
		price = "".join(container.findAll("li", {"class":"price-current"})[0].text.split(","))
		prevPrice = container.findAll("li", {"class": "price-was"})[0].text

		print(prevPrice)

		print(f'{brand}')

		print()
		print(features)
		print()
		print(f"{price[:len(price) - 1].strip()}")

		f.write(brand + "," + price[:len(price) - 1].strip() + "," + prevPrice + "\n")

