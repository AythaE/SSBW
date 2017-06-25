# -*- coding: utf-8 -*-
from django.db import models
from mongoengine import *

# Conectarse a la BD
connect('test', host='mongo', port=27017)


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


class image(EmbeddedDocument):
  extension = StringField()
  img = ImageField(size=(800, 600, True))


class restaurants(Document):
  name = StringField(required=True, max_length=80)
  restaurant_id = IntField()
  cuisine = StringField()
  borough = StringField()
  address = EmbeddedDocumentField(addr)    # en la misma collección
  grades = ListField(EmbeddedDocumentField(likes))
  image = EmbeddedDocumentField(image)
