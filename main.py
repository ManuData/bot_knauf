import requests
import re
from bs4 import BeautifulSoup
from bs4 import Comment


URL = "https://www.knauf.de"

page = requests.get(URL)

soup = BeautifulSoup(page.text,'html.parser')

def test(s):
    return (isinstance(s, Comment) and bool(re.search("OneTrust",s)))

comments = soup.find_all(string=test)

with open(f'test.txt','w') as file:
#with open(f'datos.csv','w') as file: 
    for c in comments:
        file.write(f"{c},\n")




















