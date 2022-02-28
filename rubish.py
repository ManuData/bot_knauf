

# TO DO: 

# 1. Check OneTrust Cookie Auto Blooking Feature: 
    # 1.1 Check if OneTrust > GTM
    # 1.2 Check existence paramether 1
    # 1.3 Check existence paramether 2
    # 1.4 Check paramether 1 = paramether 2

# 2. GTM implementation
    # 2.1 GTM snippet in the <head> tag
    # 2.2 GTM non script in the <bod> tag
    # 2.3 DataLayer variables in OneTrust
    # Extra: Validate number of cookies implemented ? (note: with beautifulsoup div class ot-chkbox)

# 3. OneTrust configuration in GTM --> Technical implementation


# 4. Google Analytics --> Technical implementation



# Obtener cunado comienza y acaba el script :
soup = BeautifulSoup(page.text,'html.parser')

comments = soup.find_all(string=lambda text: isinstance(text, Comment) and bool(re.search("(OneTrust|Tag Manager)",text)))

# Obtener la posicion de los tags de apertura: 

soup = BeautifulSoup(page.text,'html.parser')
print(soup.head.sourceline)
print(soup.body.sourceline)


# LISTA DE ATRIBUTOS DEL TAG DE SCRIPT: 

print(soup.script.get_attribute_list('src'))


#   PENDING DESCRIPCIÓN

test = soup.find_all('script')
for script in test: 
    print(script.sourceline)



# Me devuelve el atributo del parámetro
    
    scripts = soup.find_all('script')
for s in scripts: 
    #print(s.attrs)
    for dato in s.attrs:
        print(s[dato])


# Pintar todos los scr de los scripts
scripts = soup.find_all('script')
for s in scripts: 
    #print(s.attrs)
    print(s['src'])
    #print(s.sourceline)



# FOR WRITE INFO: 

#with open(f'test.txt','w') as file: 
    #for c in comments:
        #file.write(f"{c} \n")
#with open('datos.csv','w', encoding='UTF8',) as f:
    #writer = csv.writer(f,dialect='excel')
    #writer.writerow(comments)



# NOTES: 
#print(soup.find(string=re.compile("GTM-")))
#print(soup.find_all(src=re.compile("GTM-")).sourceline) # obtengo el script de GTM del iframe
#print(soup.find_all(src=re.compile("cookielaw")))

# ENCONTRAR EL SCRIPT DE GTM: 
#test = soup.find_all(string=lambda text:bool(re.search("GTM-",text)))
#elementos = test[0].split(",")
#for data in elementos: 
    #print(data)

# Encontrar GTM:
gtm_finder = [s for s in scripts if s.attrs == {}]
gtm = gtm_finder[1].string # Pasar el tag a string