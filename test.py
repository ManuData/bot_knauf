import requests
import re
import csv
from bs4 import BeautifulSoup
from bs4 import Comment



URL = "https://www.knauf.de"

page = requests.get(URL)

soup = BeautifulSoup(page.text,'html.parser')
comments = soup.find_all(string=lambda text: isinstance(text, Comment) and bool(re.search("(OneTrust|Tag Manager)",text))) 
#print(soup.head.sourceline)
#with open(f'test.txt','w') as file: 
    #for c in comments:
        #file.write(f"{c} \n")
with open('datos.csv','w', encoding='UTF8',) as f:
    writer = csv.writer(f,dialect='excel')
    writer.writerow(comments)




