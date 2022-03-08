
import requests
from bs4 import Comment
from requests.adapters import HTTPAdapter
from urllib3.util import Retry
import re
import csv
from bs4 import BeautifulSoup
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from data_domains import data


#data = ["https://www.knauf.nl","https://www.knauf.de","https://www.knaufceilingsolutions.com/en/","https://www.knauf-performance-materials.com/en"] # lista de dominios


# Check if OneTrust implemented:
def check_one_trust(url,page,soup):

    scripts = soup.find_all('script')
    one_trust_implemented = False
    
    for script in scripts: 
        for atributo in script.attrs:
            searched_value = script[atributo]
            auto_blocking_feature = re.search('https\:\/\/cdn\.cookielaw\.org\/consent\/.*\/OtAutoBlock\.js',searched_value)

            if (auto_blocking_feature):
                one_trust_implemented = True
                return one_trust_implemented
    return one_trust_implemented


# Check if gtm is implemented in the head:
def check_gtm_head_tag(url,page,soup):

    gtm_head_tag_implemented = False
    gtm_main_tag = soup.find_all(string=lambda text:bool(re.search("googletagmanager",text))) # Main Tag GTM

    if (gtm_main_tag != []):

        gtm_head_tag_implemented = True
        return gtm_head_tag_implemented
    return gtm_head_tag_implemented


# Check if gtm is implemented in the body:
def check_gtm_body_tag(url,page,soup): # Check if gtm is implemented in the body
    gtm_body_tag_implemented = False
    gtm_iframe_tag = soup.find_all(src=re.compile("GTM-")) # Iframe Tag GTM
    if (gtm_iframe_tag != []):
        gtm_body_tag_implemented = True
        return gtm_body_tag_implemented
    return gtm_body_tag_implemented


# Return head position (line number)
def head_position(url,page,soup): # Return line where head label is placed
    head = soup.head
    #body = soup.body
    if (head != None):
        return head.sourceline
    return False


# Return body position (line number)

def body_position(url,page,soup):# Return the position of label body
    body = soup.body
    if (body != None):
        return body.sourceline
    return False


# Return the comments in the html (OneTrust and GTM)
def get_comments(url,page,soup):

    check = []
    datos = {0: "OneTrust Cookies Consent Notice start",
         1: "OneTrust Cookies Consent Notice end",
         2: "Google Tag Manager",
         3: "End Google Tag Manager",
         4: "Google Tag Manager (noscript)",
         5: "End Google Tag Manager (noscript)"
         }
    
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


#Return line where OneTrust is implemented (else False)
def ot_script_position(url,page,soup): # Return position of the script of OneTrust
   
    scripts = soup.find_all('script')
    
    for script in scripts: 
        for atributo in script.attrs:
            searched_value = script[atributo]
            auto_blocking_feature = re.search('https\:\/\/cdn\.cookielaw\.org\/consent\/.*\/OtAutoBlock\.js',searched_value)

            if (auto_blocking_feature):
                return script.sourceline
    return False


#Return line where gtm script is implemented
def gtm_script_position(url,page,soup): # Return line where the script is placed
   
    scripts = soup.find_all('script')
    
    scripts_list = [script for script in scripts]
    for script in scripts_list:
        if(bool(re.search("googletagmanager",str(script)))): # Check if GTM script in header is found. If not return False
            return script.sourceline
    return False



def gtm_iframe(url,page,soup): # Return line where iframe is placed
    scripts = soup.find_all('noscript')
    for script in scripts:
        if(bool(re.search("googletagmanager",str(script)))): # Check if GTM iframe is in the code
            return script.sourceline
    return False


def scrapping(domain_list):

    data_one_trust = [] # Identify if oneTrust is implemented
    data_gtm_header = [] # Identify for each domain if GTM is in the head
    data_gtm_body = [] # Identify for each domain if GTM is in the body
    data_head_position = [] # Identify for each domain position of the head label
    data_body_position = []  # Identify for each domain position of the body label
    data_comments = [] # Check if comments from OneTrust and GTM are present and in order expected
    data_ot_script_position = [] # Return position of script of OneTrust
    data_gtm_script_position = [] # Return position of script of GTM (first script)
    data_gtm_iframe_position = [] # Return the position of the iframe script GTM (body)


    for domain in domain_list:
        url = domain
        session = requests.Session()
        retry = Retry(connect=3, backoff_factor=0.5)
        adapter = HTTPAdapter(max_retries=retry)
        session.mount('http://', adapter)
        session.mount('https://', adapter)
        s = session.get(url,verify=False)
        #page = requests.get(url,verify=False)
        soup = BeautifulSoup(s.text,'html.parser')
        data_one_trust.append(check_one_trust(url,s,soup))
        data_gtm_header.append(check_gtm_head_tag(url,s,soup))
        data_gtm_body.append(check_gtm_body_tag(url,s,soup))
        data_head_position.append(head_position(url,s,soup))
        data_body_position.append(body_position(url,s,soup))
        data_comments.append(get_comments(url,s,soup))
        data_ot_script_position.append(ot_script_position(url,s,soup))
        data_gtm_script_position.append(gtm_script_position(url,s,soup))
        data_gtm_iframe_position.append(gtm_iframe(url,s,soup))

    return data_one_trust,data_gtm_header,data_gtm_body,data_head_position,data_body_position,data_comments,data_ot_script_position,data_gtm_script_position,data_gtm_iframe_position

#print(scrapping(data))

def generate_csv():
   
    data_one_trust,data_gtm_header,data_gtm_body,data_head_position,data_body_position,data_comments,data_ot_script_position,data_gtm_script_position,data_gtm_iframe_position = scrapping(data)
    with open('test.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(["DOMAIN","OT","GTM_HEADER","GTM_BODY","HEAD_POSITION","BODY_POSITION","GET_COMMENTS","OT_SCRIPT_POSITION","GTM_SCRIPT_POSITION","GTM_IFRAME_POSITION"]) # Columnas
        for i in range(len(data)): # Tengo que incluir el largo de las listas (el número de dominios que tengo que analizar)
            writer.writerow([data[i],data_one_trust[i],data_gtm_header[i],data_gtm_body[i],data_head_position[i],data_body_position[i],data_comments[i],data_ot_script_position[i],data_gtm_script_position[i],data_gtm_iframe_position[i]]) # Datos a escribir
        csvfile.close()
    return False

generate_csv()



