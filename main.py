import requests
import re
from bs4 import BeautifulSoup
from bs4 import Comment


URL = "https://www.knauf.de"

page = requests.get(URL)

soup = BeautifulSoup(page.text,'html.parser')

def test(s):
    """Return True if this string is the only child of its parent tag."""
    #return (s == re.compile(r"google") and isinstance(s,Comment))
    return (isinstance(s, Comment) and bool(re.search("OneTrust",s)))

comments = soup.find_all(string=test)
# ["The Dormouse's story", "The Dormouse's story", 'Elsie', 'Lacie', 'Tillie', '...']

with open(f'test.txt','w') as file: 
    for c in comments:
        file.write(f"{c} \n")




















