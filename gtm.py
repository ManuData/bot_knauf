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
        gtm_main_tag_implemented = True
        return gtm_main_tag_implemented
    return gtm_main_tag_implemented



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
