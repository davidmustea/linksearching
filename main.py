import requests
from bs4 import BeautifulSoup


linkraw = input("Site-ul: ")

while not linkraw.startswith('www'):
    print("Link-ul trebuie sa inceapa cu 'www'")
    linkraw = input("Site-ul: ")


link = f'https://{linkraw}'
httprequest = requests.get(link)

if httprequest.status_code == 200:
    print("Valid")
if httprequest.status_code != 200:
    print("Invalid")

src = httprequest.content
soup = BeautifulSoup(src,'lxml')

print(soup.find_all('a'))

