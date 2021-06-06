# Librerias necesarias
from requests import get
from bs4 import BeautifulSoup
from pprint import pprint
# de donde sacamos los datos?
webcc = 'https://www.cinecolombia.com/cali'
# consultamos la pagina y guardamos el HTML
response = get(webcc)
html = response.text
# parseamos el HTML con BS4
bs = BeautifulSoup(html, 'html.parser')
urls=list()
for item in bs.find_all('div', class_='tab-cartelera'):
  #print(item)
  pelicula=item.find_all('div',class_='item_pelicula')
  for peli in pelicula:
    urls.append(peli.a['href'])
print(urls)
for url in urls:
  response = get(url)
  html = response.text
  # parseamos el HTML con BS4
  bs = BeautifulSoup(html, 'html.parser')
  nombre=bs.find('div',class_='field field-name-title')
  sinopsis=bs.find('div',class_='field field-name-field-sinopsis')
  duracion=bs.find('div',class_='field field-name-field-duracion')
  print("------------- {} -------".format(nombre.text))
  print(sinopsis.text)
  try:
    print(duracion.text)
  except AttributeError:
    print("")
  puntuacion=bs.find('div',class_='fivestar-summary fivestar-summary-average-count')
  try:
    print("Puntuacion: {} ".format(puntuacion.span.span.text))
  except AttributeError:
    print()
  for item in bs.find_all('div',class_='cada-teatro-para-funciones'):
    print("\t{}".format(item.h3.text))
    for item2 in item.find_all('div',class_='item-caracteristica'):    
      sala=item2.find_all('div',class_='titulo-caracteristica')
      hora=item2.find_all('div',class_='hora')
      for sal in sala:
        print("\t\t{}".format(sal.text))
        for hor in hora:
          print("\t\t\t{}".format(hor.text))

          