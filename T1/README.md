# Tarea 1
## Enunciado
#### 1.- Sirviendo contenidos

En esta tarea serviremos distintos tipos de contenidos al navegador: texto plano, html, imágenes. Para esto hay que cambiar la cabecera de HTTP ['Content-Type'](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Type), donde se especifica el [tipo mime](https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types) del envío

La aplicación que hagamos, servirá:

Url                            | Contenido
-------------------------------|---------------------------------------------
"/"                            | Una página de inicio
"/un_texto_plano"              | 'Un texto plano cañon'
"/un_texto_html"               | 'Un texto <b>HTML</b> cañon'
"/una_imagen"                  | La imágen, para visualizarla en el navegador
"/este_texto_plano/lo que sea" | 'lo que sea'
Cualquier otra cosa            | Mensaje de error personalizado 



Para ello usaremos [Flask](http://flask.pocoo.org/), un 'microframework' de python. En [Quickstart](http://flask.pocoo.org/docs/0.12/quickstart/), hay una introducción a su uso.

Es conveniente, activar el ambiente de depuración durante la fase de desarrollo: [Configuration Handling](http://flask.pocoo.org/docs/0.12/config/)

Las cabeceras se pueden cambiar con la función [make_response](http://flask.pocoo.org/docs/0.12/quickstart/#about-responses)

#### 2.- Sitio web estático con plantillas

Lo normal es usar [plantillas](http://flask.pocoo.org/docs/0.12/tutorial/templates/) para generar el html. Flask usa las plantillas de [Jinja2](http://jinja.pocoo.org/docs/2.9/templates/)

Podemos hacerlo siguiendo el tutorial de [An Introduction to Python’s Flask Framework](https://code.tutsplus.com/tutorials/an-introduction-to-pythons-flask-framework--net-28822)

Y lo podemos completar añadiendo [una página de error](http://flask.pocoo.org/docs/0.12/patterns/errorpages/)

## Uso
#### Preparación del entorno
```
virtualenv -p python3 <Directorio> # Directorio donde se desee desplegar
cd <Directorio>
source /bin/activate # Activa el entorno virtual
pip install Flask # Instala Flask y debería instalar las dependencias que se pueden ver abajo

```
#### Ejecución
- Opción 1
```
python <Directorio>/app/t1.py
```
- Opción 2
```
export FLASK_APP=<Directorio>/app/t1.py
flask run
```


## Dependencias
- Python==3.4.2
- Flask==0.12
- Jinja2==2.9.5
- MarkupSafe==0.23
- Werkzeug==0.11.15
- click==6.7
- itsdangerous==0.24
