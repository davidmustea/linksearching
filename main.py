import requests
from bs4 import BeautifulSoup


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

ceVreaUser = input("Ce facem cu linkul?\nScrie 'help' pentru optiuni.\n")

#"help" pentru user
if ceVreaUser.lower() == "help":
    print("[1] Cautare linkuri")
    print("[2] Cautare poze")

#Varianta 1: Cautare linkuri
if ceVreaUser == '1':
    print("Cautam linkuri...")
    print("Rezultate:")
    print(soup.find_all('a'))


