import requests
import re
from bs4 import BeautifulSoup
from bs4 import Comment


URL = "https://www.knauf.de"
page = requests.get(URL,verify=False)
print(page.status_code)

if (page.status_code == 200):
    print("la request es correcta")
else:
    print("la request no es correcta")



# Encontrar GTM:

URL = "https://www.knauf.de"
page = requests.get(URL,verify=False)
soup = BeautifulSoup(page.text,'html.parser')
scripts = soup.find_all('script')
gtm_main_tag = soup.find_all(string=lambda text:bool(re.search("googletagmanager",text))) # Main Tag GTM
gtm_iframe_tag = soup.find_all(src=re.compile("GTM-")) # Iframe Tag GTM

#gtm_finder = [s for s in scripts if s.attrs == {}]
#gtm = gtm_finder[1] # Pasar el tag a string

test = soup.find_all(string=lambda text:bool(re.search("bla",text))) # Main Tag GTM
print(test)
print(test == [])










