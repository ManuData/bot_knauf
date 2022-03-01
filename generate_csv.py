import csv
from otvalidator import check_one_trust
from gtm import check_gtm_head_tag,check_gtm_body_tag

domain_list = ["https://www.knauf.nl","https://www.knauf.de","https://www.knaufceilingsolutions.com/en/"] # lista de dominios
data = [check_one_trust(domain) for domain in domain_list] # lista de datos a registar

# Escritura de los datos en formato csv

with open('test.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(["OT", "DOMAIN"])
    for i in range(3): # Tengo que incluir el largo de las listas (el número de dominios que tengo que analizar)
        writer.writerow([data[i], domain_list[i]])
    csvfile.close()
