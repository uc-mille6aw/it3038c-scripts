import re
import requests
from bs4 import BeautifulSoup
#import and format the data from the store page I selected
data = requests.get("http://books.toscrape.com/catalogue/sapiens-a-brief-history-of-humankind_996/index.html").content
soup = BeautifulSoup(data, "html.parser")
#get the book's title
title = soup.find('h1')
title = title.text.strip()
#get the book's price
price = soup.find("p", {"class":"price_color"})
price = price.text.strip()
#get the book's availbility
stock = soup.find("p", {"class":"instock availability"})
stock = stock.text.strip()

print ("Title - %s, Price - %s, Status - %s" % (title, price, stock))

