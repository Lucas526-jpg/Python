import requests
from bs4 import BeautifulSoup

respuesta = requests.get('https://quotes.toscrape.com/')
if respuesta.status_code == 200 :
    sopa = BeautifulSoup(respuesta.text, 'html.parser')
    texto = sopa.find_all('span', class_='text')
    autores = sopa.find_all('small', class_="author")

    #opcion 1
    #contador = 0
    #for frase in texto:
    #    print(f"{frase.text} - {autores[contador].text}")
    #    contador = contador + 1

    #opcion 2
    for frase, autor in zip(texto,autores):
        print(f"{frase.text} - {autor.text}")
else :
    print("malio sal")