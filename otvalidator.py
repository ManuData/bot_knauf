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
    # 1.1 Check if OneTrust > GTM
    # 1.2 Check existence paramether 1
    # 1.3 Check existence paramether 2
    # 1.4 Check paramether 1 = paramether 2


# Check if OneTrust implemented: 

def check_one_trust(url):
    domain = url
    page = requests.get(url,verify=False )
    soup = BeautifulSoup(page.text,'html.parser')
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




# Function to check if Onetrust has the same params

def check_one_trust_params(url):
    domain = url
    page = requests.get(url,verify=False)
    soup = BeautifulSoup(page.text,'html.parser')
    scripts = soup.find_all('script')
    param_1 = None
    param_2 = None
    
    for script in scripts: 
        for atributo in script.attrs:

            searched_value = script[atributo]
            auto_blocking_feature = re.search('https\:\/\/cdn\.cookielaw\.org\/consent\/.*\/OtAutoBlock\.js',searched_value)

            if (auto_blocking_feature):
                param_1 = searched_value.split("/")[-2]
    
    for script in scripts: 
        for atributo in script.attrs:
            searched_value = script[atributo]
            if (param_1 == searched_value):
                param_2 = param_1
    
    if ((param_1 and param_2) == None):
        return False
    elif(param_1==param_1):
        return True
    
    
    

# CALL THE FUNCTIONS: 


test = ["https://www.knauf.nl","https://www.knauf.de","https://www.knaufceilingsolutions.com/en/"]

for domain in test: 
    first_check = check_one_trust(domain)
    second_check = check_one_trust_params(domain)
    print(f"First check:{first_check} | Second check:{second_check}")

