# Bits-and-Bots
A brief excursion into the world of web scraping and bot development.

*Beautiful Soup*: beautifulSoup.py
This script is an exploration of web scraping using the bs4 module which contains BeautifulSoup. The script itself scrapes data from a url specified by the newURL variable and (in this particular example) grabs various information about graphics cards listed on the website and saves that in a new .csv file. 

*NOTE*: it would seem that many websites, especially sites that have bot inhibiting features, prevents webscraping and attempts to parse it using BeautifulSoup will fail. This can be circumvented using Selenium though it is not as easy to perform scraping-related actions.
  
*Selenium*: seleniumTest.py, warhammerBot.py
Selenium is an automated test software useful for interacting remotely with webpages and is useful for limited web scraping applications. 

seleniumTest.py: this script uses Selenium to log the user into UO's recweb, the online service through which reservations for the UO recreation center can be made. The script does thisby reading the user's username and password from a local file ("recwebInfo.txt") and then sending the information within it as keys to the site. Afterwards it navigates to the lap pool reservation page and registers the user for the earliest slot. While not very useful it does provide a good intro to the Selenium software's capabilities.

warhammerBot.py: this script is the more rigorous test of Selenium and has a more direct and intersting application. This script opens a connection to a site which sells Warhammer 40k figuringes (a popular and lucrative table-top game) and navigates the user to the pre-orders page. Afterwards, it preorders an item which contains or is closely related to the key word provided in "localInfo.txt" or, if the keyword doesn't match any of the available items, the item in the default position (1-indexed). Afterwards it logs the user in using information from "localInfo.txt". This script makes better use of the Selenium library in that it uses the "WebDriverWait" functionality which allows the script to wait until an item can be interacted with. This improves on the implementation of seleniumTest.py which uses the inefficient and unreliable time.sleept() to wait.

*Misc*: botAux.py
This script contains functions that are useful in the implementation of the bot contained in warhammerBot.py. 
