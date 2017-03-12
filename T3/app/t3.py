import datetime
from operator import itemgetter

from lxml import etree

from mongoengine import *


def printsMenu():
  menu = {}
  menu['1'] = "Descarga restaurantes y muestralos usando lxml"
  menu['2'] = "Realiza una consulta con la BD por defecto"
  menu['3'] = "Guarda los restaurantes de Granada en la BD y recuperalos"
  menu['4'] = "Salir"
  while True:
    options = sorted(menu, key=itemgetter(0))

    print("\nTarea 3 - SSBW")

    for entry in options:
      print(entry, menu[entry])
    print()

    optionSelected = input("Elija su opción: ")

    if optionSelected == '1':
      print('\n' + menu[optionSelected])
      downloadRestaurants()
    elif optionSelected == '2':
      print('\n' + menu[optionSelected])
      queryDB()
    elif optionSelected == '3':
      print('\n' + menu[optionSelected])
      insertDBAndRetrieve()
    elif optionSelected == '4':
      print("\nSaliendo...")
      break
    else:
      print("Opción desconocida")
      print("\n\n")

  return


def downloadRestaurants():

  api_base_url = 'http://maps.googleapis.com/maps/api/geocode/xml?address='

  for bar in bares:
    req = api_base_url + bar + ' Granada'
    tree = etree.parse(req)

    # todos los campos formatted_address
    dire = tree.xpath('//formatted_address/text()')

    print(bar + " - " + dire[0])


def queryDB():

  for r in restaurants.objects[:3]:
    print (r.name, r.address.coord, r.borough)

  return


def insertDBAndRetrieve():
  api_base_url = 'http://maps.googleapis.com/maps/api/geocode/xml?address='

  for bar in bares:
    req = api_base_url + bar + ' Granada'
    tree = etree.parse(req)

    direccionXML = tree.xpath('//address_component')
    localizacionXML = tree.xpath('//location')

    # FIXME Porque es necesario indicar los indices en ambos lados??
    calle = direccionXML[1].xpath(
        '//long_name/text()')[1] + ", " + direccionXML[0].xpath(
        '//long_name/text()')[0]

    codigoPostal = int(direccionXML[6].xpath('//long_name/text()')[6])

    coordenadas = [float(localizacionXML[0].xpath(
        '//lat/text()')[0]), float(localizacionXML[0].xpath(
            '//lng/text()')[0])]

    direccionBD = addr(street=calle, city="Granada",
                       zipcode=codigoPostal, coord=coordenadas)

    r = restaurants(name=bar, cuisine='Granaina', address=direccionBD)

    r.save()

    print(bar)
    print("Calle: " + calle)
    print("Código postal: " + str(codigoPostal))
    print(coordenadas)
    print()

  print("\nRecuperando los restaurantes de la BD")

  for r in restaurants.objects(cuisine='Granaina'):
    print (r.name + ", " + r.address.street)
  return


# Bares que se descargarán
bares = ['El Nido Del Buho', 'Abaco Té',
         'Los Diamantes', 'Taberna 22', 'La Parada']
# Conectarse a la BD
connect('test', host='localhost', port=27017)


# Esquema para la BD de pruebas de mongoDB
class addr(EmbeddedDocument):
  building = StringField()
  street = StringField()
  city = StringField()   # añadido
  zipcode = IntField()
  coord = GeoPointField()  # OJO, al BD de test estan a revés
  # [long, lat] en vez de [lat, long]


class likes(EmbeddedDocument):
  grade = StringField(max_length=1)
  score = IntField()
  date = DateTimeField()


class restaurants(Document):
  name = StringField(required=True, max_length=80)
  restaurant_id = IntField()
  cuisine = StringField()
  borough = StringField()
  address = EmbeddedDocumentField(addr)    # en la misma collección
  grades = ListField(EmbeddedDocumentField(likes))


printsMenu()
