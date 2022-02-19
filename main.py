from random import betavariate
import requests
from bs4 import BeautifulSoup
from bs4 import Comment


URL = "https://www.knauf.de"

page = requests.get(URL)

soup = BeautifulSoup(page.text,'html.parser')
comments = soup.find_all(string=lambda text: isinstance(text, Comment))
for c in comments:
    print(c)
    print("===========")
    c.extract()


















