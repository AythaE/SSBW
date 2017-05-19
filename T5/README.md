# Tarea 5
## Enunciado

<h3>Entrada de datos con formularios</h3>
<p>
   En esta tarea usaremos la clase <a href="https://docs.djangoproject.com/en/1.10/topics/forms/">Forms</a> de Django
   para añadir datos. Incluiremos también una foto del restaurante aprovechando el tipo de campo
   <a href="http://docs.mongoengine.org/apireference.html#mongoengine.fields.ImageField">ImageField</a>, de
   mongoengine. <span style="color:grey">(Para usarlo hay que instalar la librería <a href="https://python-pillow.org/">pillow</a>)</span>
</p>
<p>
También haremos una página de detalle con los datos de cada restaurante, incluyendo la foto, a la que se acceda:
<pre><code class="language-bash" data-lang="bash">
   http://localhost:8000/restaurante/nombre_del_restaurante

   ó mejor

   http://localhost:8000/restaurante/restaurante_id  (que debe ser único)
</code></pre>
Django <a href="https://docs.djangoproject.com/en/1.10/topics/http/urls/#named-groups">URL dispatcher</a>
</p>
<br /><br />
<h4>Pasos:</h4>
<p>
   1.- Hacer un form compatble con la clase de mongoengine, que incluya algún validador y subir una imagen
</p>
<p>
   2.- A la vuelta del form, tener en cuenta la <a href="https://docs.djangoproject.com/en/1.10/topics/http/file-uploads/">subida de archivos</a> en el formulario
   (<a href="https://docs.djangoproject.com/en/1.10/ref/forms/api/#binding-uploaded-files">Binding uploaded files to a form</a>), y
   que haya un campo de clave única en la BD (puede ser <i>restaurant_id</i> o el nombre).
   Para guardar la imágen en mongo, simplemente:
   <pre><code class="language-python" data-lang="python">
      restaruante = restaurants(
         name = form.cleaned_data.get('name')  # después de validar
         ...
         foto = request.FILES.get('foto')
      )
   </code></pre>
</p>

<p>
   3.- Hacer una salida con los datos cada restaurante. Para leer la imágen de la BD:
   <a href="http://docs.mongoengine.org/guide/gridfs.html#gridfs">GridFs</a>
</p>
<p>
   Para que quede mejor, se puede utilizar <a href="https://github.com/GabrielUlici/django-bootstrap4">
   django-boostrap4</a> o similar
   </p>

## Uso
#### Preparación del entorno
Lo primero será instalar MongoDB siguiendo las siguientes [instrucciones](https://docs.mongodb.com/getting-started/shell/installation/) si aún no lo hemos hecho, tras esto hay que [importar la base de datos de prueba](https://docs.mongodb.com/getting-started/python/import-data/)

```
virtualenv -p python3 <Directorio> # Directorio donde se desee desplegar
cd <Directorio>
source /bin/activate # Activa el entorno virtual
pip install mongoengine django pillow # Instala mongoengine, Django y debería instalar las dependencias que se pueden ver abajo

```

#### Ejecución
```
python <Directorio>/app/manage.py runserver
```

## Dependencias
- Python==3.4.2
- Django==1.10.6
- mongoengine==0.11.0
- pymongo==3.4.0
- six==1.10.0
- Pillow==4.0.0
