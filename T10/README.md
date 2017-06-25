# Tarea 10
## Enunciado
<h3>Despliegue</h3>
<p>
   La última práctica consiste en tener una aplicación web desplegada en un ambiente de 'producción',
   es decir funcionando con la depuración en 'OFF' y conectada
   a un servidor web como <a href="https://www.nginx.com/">ngix</a> o <a href="http://httpd.apache.org/">apache</a> en
   el puerto 80
</p>
<p>
   El despliegue de una aplicación con django, está contada en:
   <a href="https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/">How to deploy with WSGI
   </a>, <a href="https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/gunicorn/">How to use Django with Gunicorn</a>,
   <a href="http://docs.gunicorn.org/en/latest/deploy.html">Deploying Gunicorn</a>,
   <a href="http://docs.gunicorn.org/en/latest/deploy.html#supervisor">Supervisor</a>, y en las transparencias de clase.
</p>


<p>
Básicamente consiste en poner la configuración de producción, es decir en el archivo
<b>settings.py</b> estarán las variables:
</p>
<pre>
DEBUG = False

ALLOWED_HOSTS = ['\*']
</pre>
<p>

Con esto dejará de funcionar el servidor de desarrollo, y de servir los contenidos de <b>/static</b>, que tendrán
que pasar a servirse desde el servidor web de producción. Django tiene un script: <a href="https://docs.djangoproject.com/en/1.10/ref/contrib/staticfiles/">collectstatic</a>
para facilitar pasar los contenidos a otro directorio.
</p>

<p>
  Después habrá que poner funcionar la aplicación con un servidor web <a href="https://en.wikipedia.org/wiki/Web_Server_Gateway_Interface">wsgi</a>,
  (p.e. <a href="http://gunicorn.org/">gunicorn</a>)
  y conectar la aplicación, y el resto de servicios que pudiera haber (los arhivos static), a un servidor
   web que también
  funcione como <a href="https://en.wikipedia.org/wiki/Reverse_proxy">proxy inverso</a> (p.e. <a href="https://www.nginx.com/">nginx</a>)
  en el puerto 80
</p>

<p>
  Para automatizar el proceso, podremos hacer algún script con <a href="https://en.wikipedia.org/wiki/Makefile">Makefile</a>,
</p>
<p>
   El despliegue se puede hacer en un contenedor usando <a href="https://www.docker.com/">docker</a>, y
   <a href="https://docs.docker.com/compose/">docker-compose</a> (ejemplo con <a href="https://docs.docker.com/compose/django/">django</a>)
</p>

## Uso
#### Preparación del entorno
Es necesario instalar [docker (communuty edition)](https://docs.docker.com/engine/installation/) y [docker-compose](https://docs.docker.com/compose/install/) para probar este despliegue, tras esto basta con acceder a este directorio y ejecutar
```
docker-compose up
```
Una vez levantados todos los contenedores podemos acceder a la aplicación usando el siguiente enlace <http://localhost/restaurantes>


## Dependencias
- "node": "8.1.2"
- "bootstrap": "^3.3.7",
- "bootswatch": "^3.3.7",
- "react": "^15.6.1",
- "react-bootstrap": "^0.31.0",
- "react-dom": "^15.6.1",
- "string": "^3.3.3"
