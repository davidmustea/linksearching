import requests
from bs4 import BeautifulSoup
import time

linkraw = input("Site-ul: ")

#Vedem daca site-ul incepe cu 'www'
while not linkraw.startswith('www'):
    print("Link-ul trebuie sa inceapa cu 'www'")
    linkraw = input("Site-ul: ")

#Adaugare 'https://' la inceputul linkului
link = f'https://{linkraw}'
httprequest = requests.get(link)

#Verificam daca site-ul e valid
if httprequest.status_code == 200:
    print("Valid")
if httprequest.status_code != 200:
    print("Invalid")

#Obiectul soup
src = httprequest.content
soup = BeautifulSoup(src,'lxml')

#afisare logo

print("""
   __ _       _                            _     _             
  / /(_)_ __ | | _____  ___  __ _ _ __ ___| |__ (_)_ __   __ _ 
 / / | | '_ \| |/ / __|/ _ \/ _` | '__/ __| '_ \| | '_ \ / _` |
/ /__| | | | |   <\__ \  __/ (_| | | | (__| | | | | | | | (_| |
\____/_|_| |_|_|\_\___/\___|\__,_|_|  \___|_| |_|_|_| |_|\__, |
                                                         |___/ 
""")



time.sleep(1)
ceVreaUser = input("Ce facem cu linkul?\nScrie 'help' pentru optiuni.\n")

listaComenzi = ['1','2','3','4','5','help','stareNeutra']
dacaUserScrisHelp = 0

if ceVreaUser not in listaComenzi:
    ceVreaUser = input("Comanda invalida.\nPune comanda din nou\n")
    
#main loop
while ceVreaUser in listaComenzi:
    
    #"help" pentru user
    if ceVreaUser.lower() == "help":
        print("[1] Cautare linkuri")
        print("[2] Cautare poze")
        ceVreaUser = input("Pune numarul comenzii: \n")
        dacaUserScrisHelp = 1


    #daca user-ul pune comanda invalida 0
    if ceVreaUser == '0' and dacaUserScrisHelp == 1:
        print("Amuzantule")
        time.sleep(1)
        ceVreaUser = input("Pune o comanda valida de data asta \n")

    if ceVreaUser == '0' and dacaUserScrisHelp == 0:
        print("Comanda invalida.")
        ceVreaUser = input("Scrie 'help' pentru comenzi \n")

    #Varianta 1: Cautare linkuri
    if ceVreaUser == '1':
        ceVreaUser = 'stareNeutra'
        print("Cautam linkuri...")
        print("Rezultate:")
        print(str(soup.find_all('a')).replace(',','\n'))
        
        #intrebam user-ul daca vrea sa salveze intr-un fisier rezultatele
        dacaUserVreaSaScrieRezFisierText = input("Vrei sa salvam rezultate intr-un fisier text? (y or n) ")

        #salvare fisier cu linkuri
        if dacaUserVreaSaScrieRezFisierText == 'y':
            try:
                f = open(linkraw + '_links.txt','x',encoding="utf-8")
                f.write(str(soup.find_all('a')).replace(',','\n'))
                f.close()
            except:
                print("Exista deja un fisier cu aceeasi nume\nSterge fisierul si incearca din nou ")

        if dacaUserVreaSaScrieRezFisierText == 'n':
            pass


