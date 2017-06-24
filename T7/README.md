# Tarea 7
## Enunciado
<h3>jQuery y AJAX</h3>
<p>
   En esta tarea mejoraremos el <a href="https://en.wikipedia.org/wiki/Front_and_back_ends">'fron'-end'</a> de nuestra
   aplicación incorporando código con jQuery y llamadas AJAX
</p>
<br />
<h4>1.- Resaltado de opción de menú</h4>
<p>
 Pasaar una nueva variable a los templates que sirva para resaltar la opción de menú. Esto se puede hacer
 <a href="http://api.jquery.com/css/">cambiando una propiedad css</a>, o
 <a href="http://fellowtuts.com/jquery/change-class-using-jquery/">cambiando clases</a> usando jQuery
</p>
<br />
<h4>2.- AJAX</h4>
<p>
   Añadir una <a href="https://v4-alpha.getbootstrap.com/components/modal/"> ventana modal</a> para mostrar la dirección
   completa del restaurante haciendo una llamada <a href="https://learn.jquery.com/ajax/jquery-ajax-methods/">AJAX</a> para conseguir los datos,
   incluso poniendo una foto de streetview:

   <pre>

      <a href="https://maps.googleapis.com/maps/api/streetview?size=600x300&location=37.1765359,-3.596629699999999">https://maps.googleapis.com/maps/api/streetview?size=600x300&location=37.1765359,-3.596629699999999</a>
   </pre>

## Uso
#### Preparación del entorno
Lo primero será instalar MongoDB siguiendo las siguientes [instrucciones](https://docs.mongodb.com/getting-started/shell/installation/) si aún no lo hemos hecho, tras esto hay que [importar la base de datos de prueba](https://docs.mongodb.com/getting-started/python/import-data/)

```
virtualenv -p python3 <Directorio> # Directorio donde se desee desplegar
cd <Directorio>
source /bin/activate # Activa el entorno virtual
pip install -r requirements.txt # Instala mongoengine, Django y debería instalar las dependencias que se pueden ver abajo

```

#### Ejecución
```
python <Directorio>/app/manage.py runserver
```

## Dependencias
- Python==3.4.2
- Django==1.10.6
- Pillow==4.0.0
- django-registration-redux==1.6
- mongoengine==0.11.0
- olefile==0.44
- pymongo==3.4.0
- six==1.10.0
