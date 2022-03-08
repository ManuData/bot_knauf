
import requests
from requests.adapters import HTTPAdapter
from urllib3.util import Retry
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from data_domains import data
import csv

# Test how many domains accepts requests



def check_live(data):
    domains_ok = []
    domains_ko = []
    error_type = {}
    for i in range(50):
        url = data[i]
        print(url)
        try:
            #timeout=(10, 10)
            r = requests.get(url,timeout=(10, 5))
            print(f"intentando {url}")
        except:
            domains_ko.append(url)
            pass
        else:
            if r.status_code == 200:
                print(f"El dominio {url} es OK")
                domains_ok.append(url)
    return domains_ok

    
check_live(data)

def domains_csv():
    domains_ok = check_live(data)
    with open('dominios_ok.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(["DOMINIOS_OK"]) # Columnas
        for i in range(len(domains_ok)): # Tengo que incluir el largo de las listas (el número de dominios que tengo que analizar)
            writer.writerow([domains_ok[i]]) # Datos a escribir
        csvfile.close()


domains_csv()
