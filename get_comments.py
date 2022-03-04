import requests
import re
from bs4 import BeautifulSoup
from bs4 import Comment

# 1. Check OneTrust Cookie Auto Blooking Feature: 
    # 1.1 Check if OneTrust > GTM : Approach based on comments

# 2. Correct implementation of OneTrust and GTM (Extended rules)
    # 2.1 Head tag --> script OneTrust ("At least after head")
    # 2.2 Head tag --> script GTM ("At least After")
    # 2.3 Body tag --> async script ("At least after")

# 1. Function to check if OneTrust > GTM based on comments: 

def get_comments(url):

    check = []
    datos = {0: "OneTrust Cookies Consent Notice start",
         1: "OneTrust Cookies Consent Notice end",
         2: "Google Tag Manager",
         3: "End Google Tag Manager",
         4: "Google Tag Manager (noscript)",
         5: "End Google Tag Manager (noscript)"
         }
    
    page = requests.get(url,verify=False)
    soup = BeautifulSoup(page.text,'html.parser')
    comments = soup.find_all(string=lambda text: isinstance(text, Comment) and bool(re.search("(OneTrust|Tag Manager)",text))) # Comentarios en el html
    comments_list = [str(c).strip() for c in comments]
    for idx, c in enumerate(comments_list):
        for key,value in datos.items():
            if c == value:
                #print(f"Posicion del comentario {idx} | Posicion que le corresponderia {key}")
                if idx == key:
                    #print("estan bien ordenados")
                    check.append(1)
                else:
                    #print("No estan bien ordenados")
                    check.append(0)
            else:
                #print(f"comentario : {c} | datos : {value}" )
                pass 
    return check
 
#print(get_comments("https://www.knauf-performance-materials.com/en"))











 





















