import re
import requests
from bs4 import BeautifulSoup

r = requests.get("http://webscraper.io/test-sites/e-commerce/allinone/phones").content
soup = BeautifulSoup(r, "lxml")
tags = soup.findAll("div", {"class":re.compile('(raitings)')})
for p in tags:
    a = p.findAll("p",{"class":"pull-right"})
    print(a[0].string)