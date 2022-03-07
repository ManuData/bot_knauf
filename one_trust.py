from enum import auto
import requests
import re
import csv
import time
from bs4 import BeautifulSoup
from bs4 import Comment
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)



#with open(f'test.txt','w') as file: 
    #for c in comments:
        #file.write(f"{c} \n")
#with open('datos.csv','w', encoding='UTF8',) as f:
    #writer = csv.writer(f,dialect='excel')
    #writer.writerow(comments)

# 1. Check OneTrust Cookie Auto Blooking Feature: 
    # 1.1 Check if OneTrust > GTM
    # 1.2 Check existence paramether 1
    # 1.3 Check existence paramether 2
    # 1.4 Check paramether 1 = paramether 2


URL = "https://www.knauf.de"


    
# FUNCTION: one_trust_validation: Check the attributes from One Trust implementation
# atributo = "src"
# atributo = "data-domain-script"


def one_trust_validation(url,atributo):

    page = requests.get(url,verify=False)
    soup = BeautifulSoup(page.text,'html.parser')
    scripts = soup.find_all('script')
    datos_scripts = [script.attrs for script in scripts]

    param_1 = None
    param_2 = None

    if(atributo == 'src'): # 1.1  Find 1st paramether of OneTrust
        for i in range(len(datos_scripts)):
            try:
                searched_param_1 = datos_scripts[i][atributo]
                auto_blocking_feature = re.search('https\:\/\/cdn\.cookielaw\.org\/consent\/.*\/OtAutoBlock\.js',searched_param_1)

            except:
                pass

            else: # This code executes if the try block has no errors.
                if(auto_blocking_feature):
                    param_1 = searched_param_1.split("/")[-2]
                    return param_1
        return param_1


    if(atributo =='data-domain-script'): # 1.2 Find 2st paramether of OneTrust
        for i in range(len(datos_scripts)):
            try:
                searched_param_2 = datos_scripts[i][atributo]

            except:
                pass

            else:
                param_2 = searched_param_2
                return param_2
        return param_2


