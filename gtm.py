# Encontrar GTM:
import requests
import re
from bs4 import BeautifulSoup
from bs4 import Comment


# Objetivo generar una lista que tenga true o false dependiendo si tiene GTM por cada dominio

def check_gtm_head_tag(url):
    gtm_head_tag_implemented = False
    domain = url
    page = requests.get(url,verify=False )
    soup = BeautifulSoup(page.text,'html.parser')
    gtm_main_tag = soup.find_all(string=lambda text:bool(re.search("googletagmanager",text))) # Main Tag GTM
    if (gtm_main_tag != []):
        gtm_head_tag_implemented = True
        return gtm_head_tag_implemented
    return gtm_head_tag_implemented



def check_gtm_body_tag(url):
    gtm_body_tag_implemented = False
    domain = url
    page = requests.get(url,verify=False )
    soup = BeautifulSoup(page.text,'html.parser')
    gtm_iframe_tag = soup.find_all(src=re.compile("GTM-")) # Iframe Tag GTM
    if (gtm_iframe_tag != []):
        gtm_body_tag_implemented = True
        return gtm_body_tag_implemented
    return gtm_body_tag_implemented




def head_position(url):
    domain = url
    page = requests.get(url,verify=False )
    soup = BeautifulSoup(page.text,'html.parser')
    head = soup.head
    #body = soup.body
    if (head != None):
        return head.sourceline
    return False



def body_position(url):
    domain = url
    page = requests.get(url,verify=False )
    soup = BeautifulSoup(page.text,'html.parser')
    body = soup.body
    if (body != None):
        return body.sourceline
    return False



def ot_script_position(url):
   
    domain = url
    page = requests.get(url,verify=False )
    soup = BeautifulSoup(page.text,'html.parser')
    scripts = soup.find_all('script')
    
    for script in scripts: 
        for atributo in script.attrs:
            searched_value = script[atributo]
            auto_blocking_feature = re.search('https\:\/\/cdn\.cookielaw\.org\/consent\/.*\/OtAutoBlock\.js',searched_value)

            if (auto_blocking_feature):
                return script.sourceline
    return False

def gtm_script_position(url):
   
    domain = url
    page = requests.get(url,verify=False )
    soup = BeautifulSoup(page.text,'html.parser')
    scripts = soup.find_all('script')
    
    scripts_list = [script for script in scripts]
    for script in scripts_list:
        if(bool(re.search("googletagmanager",str(script)))): # Check if GTM script in header is found. If not return False
            return script.sourceline
    return False
        

    
def gtm_iframe(url):
    page = requests.get(url,verify=False )
    soup = BeautifulSoup(page.text,'html.parser')
    scripts = soup.find_all('noscript')
    for script in scripts:
        if(bool(re.search("googletagmanager",str(script)))): # Check if GTM iframe is in the code
            return script.sourceline
    return False
           
        
  


# Test funciones: 
#print(check_gtm_head_tag("https://www.knauf.nl"))
#print(check_gtm_body_tag("https://www.knauf.nl"))
#print(head_position("https://www.knauf.nl"))
#print(body_position("https://www.knauf.nl"))
#print(gtm_script_position("https://www.knauf.de"))
#print(gtm_iframe("https://www.knauf.de"))



