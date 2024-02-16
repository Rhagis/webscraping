import bs4
import requests

#crear una url sin numero de pagina
url_base = 'https://books.toscrape.com/catalogue/page-{}.html'

#lista titulos con 4 o 5 estrellas
titulos_rating_alto = []

#iterar paginas

for paginas in range(1,51):
    
    #crear sopa
    url_pagina = url_base.format(paginas)
    resultado = requests.get(url_pagina)
    sopa = bs4.BeautifulSoup(resultado.text,'lxml')
    
    #seleccionar datos libros
    libros = sopa.select('.product_pod')
    
    #iterar en los libros
    for libro in libros:
        
        #chequear rating
        if len(libro.select('.star-rating.Four')) != 0 or len(libro.select('.star-rating.Five')) != 0:
            
            #guardar titulo en variable
            titulo_libro = libro.select('a')[1]['title']
            
            
            #agregar libro a la lista
            titulos_rating_alto.append(titulo_libro)
            
#ver libros rating alto
for t in titulos_rating_alto:
    print(t)