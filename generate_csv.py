import csv
from otvalidator import check_one_trust
from gtm import check_gtm_head_tag,check_gtm_body_tag,head_position,body_position,ot_script_position,gtm_script_position,gtm_iframe
from get_comments import get_comments
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


domain_list = ["https://www.knauf.nl","https://www.knauf.de","https://www.knaufceilingsolutions.com/en/","https://www.knauf-performance-materials.com/en"] # lista de dominios
data_one_trust = [check_one_trust(domain) for domain in domain_list] # Identify for each domain if OneTrust is implemented
data_gtm_header = [check_gtm_head_tag(domain) for domain in domain_list] # Identify for each domain if GTM is in the head
data_gtm_body = [check_gtm_body_tag(domain) for domain in domain_list] # Identify for each domain if GTM is in the body
data_head_position = [head_position(domain) for domain in domain_list] # Identify for each domain position of the head label
data_body_position = [body_position(domain) for domain in domain_list]  # Identify for each domain position of the body label
data_comments = [get_comments(domain) for domain in domain_list] # Check if comments from OneTrust and GTM are present and in order expected
data_ot_script_position = [ot_script_position(domain) for domain in domain_list] # Return position of script of OneTrust
data_gtm_script_position = [gtm_script_position(domain) for domain in domain_list] # Return position of script of GTM (first script)
data_gtm_iframe_position = [gtm_iframe(domain) for domain in domain_list]




# Escritura de los datos en formato csv

with open('test.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(["DOMAIN","OT","GTM_HEADER","GTM_BODY","HEAD_POSITION","BODY_POSITION","GET_COMMENTS","OT_SCRIPT_POSITION","GTM_SCRIPT_POSITION","GTM_IFRAME_POSITION"]) # Columnas
    for i in range(len(domain_list)): # Tengo que incluir el largo de las listas (el número de dominios que tengo que analizar)
        writer.writerow([domain_list[i],data_one_trust[i],data_gtm_header[i],data_gtm_body[i],data_head_position[i],data_body_position[i],data_comments[i],data_ot_script_position[i],data_gtm_script_position[i],data_gtm_iframe_position[i]]) # Datos a escribir
    csvfile.close()


