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

time.sleep(1)
ceVreaUser = input("Ce facem cu linkul?\nScrie 'help' pentru optiuni.\n\n[1] Cautare linkuri\n[2] Cautare poze\n")

listaComenzi = ['1','2','3','4','5','help']
dacaUserScrisHelp = 0

#in caz de comanda invalida
while ceVreaUser not in listaComenzi:
    print("Comanda invalida")
    ceVreaUser = input("Introdu comanda: \n")

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
    print("Cautam linkuri...")
    print("Rezultate:")
    print(soup.find_all('a'))


