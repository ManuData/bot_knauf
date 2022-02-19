import requests
import re
from bs4 import BeautifulSoup
from bs4 import Comment


URL = "https://www.knauf.de"

page = requests.get(URL)

soup = BeautifulSoup(page.text,'html.parser')
comments = soup.find_all(string=lambda text: isinstance(text, Comment) and bool(re.search("OneTrust",text))) 
with open(f'test.txt','w') as file: 
    for c in comments:
        file.write(f"{c} \n")
