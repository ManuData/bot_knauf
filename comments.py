
from doctest import script_from_examples
from enum import auto
import requests
import re
import csv
import time
from bs4 import BeautifulSoup
from bs4 import Comment
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)




# 1. Check OneTrust Cookie Auto Blooking Feature: 
    # 1.1 Check if OneTrust > GTM : Approach based on comments

# 2. Correct implementation of OneTrust and GTM (Extended rules)
    # 2.1 Head tag --> script OneTrust ("At least after head")
    # 2.2 Head tag --> script GTM ("At least After")
    # 2.3 Body tag --> async script ("At least after")



#URL = "https://www.knauf.de"
URL = "https://www.knaufceilingsolutions.com/en"


page = requests.get(URL)

soup = BeautifulSoup(page.text,'html.parser')

head_position = soup.head.sourceline # Línea en la que se encuentra el HEAD
body_position = soup.body.sourceline # Línea en la que se encuentra el BODY
comments = soup.find_all(string=lambda text: isinstance(text, Comment) and bool(re.search("(OneTrust|Tag Manager)",text))) # Comentarios en el html

print("HEAD POSITION {} | BODY POSITION {}".format(head_position,body_position))
for c in comments: 
        print(c)

# Encontrar la linea donde se encuentra el script

scripts = soup.find_all('script')
# Encontrar GTM:
gtm_finder = [s for s in scripts if s.attrs == {}] # Econtrar el script de GTM porque no tiene ningun atributo

for gtm in gtm_finder: 
    gtm_found = bool(re.search("GTM",gtm.string))
    print(gtm_found)
    if (gtm_found):
        print(gtm.sourceline) # NOTA: Punto donde encuentro el script de gtm

    #print(bool(re.search("GTM",gtm.string)))
    














       








