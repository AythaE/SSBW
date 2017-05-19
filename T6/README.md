# Tarea 6
## Enunciado
<h3>Autentificación de usuarios y registro (logs)</h3>
<p>
   En esta tarea completaremos el <a href="https://en.wikipedia.org/wiki/Front_and_back_ends">'back-end'</a> de nuestra
   aplicación añadiendo la autentificación de usarios y un sistema de registro (logs)
</p>
<p>
   Django tiene todo lo necesario para el autentificar usuarios, incluyendo tablas, formularios, etc. Pero hay
   un plugin para Django que facilita todo esto:  <a href="https://django-registration-redux.readthedocs.io/en/latest/">django-registration-redux</a>,
   que incluye también las plantillas, el registro en uno o dos pasos (con activación de la cuenta por e-mail), gestión de la contraseña olividada con tokens, etc.
   <br /><br />
   <pre><code class="language-bash" data-lang="bash">
    $ pip install django-registration-redux
   </code></pre>
</p>

<p>
   Y seguimos los pasos de <a href="http://www.tangowithdjango.com/book17/chapters/login_redux.html">
   User Authentication with Django-Registration-Redux</a>, incluyendo <code>'registration'</code>
   en las <b>INSTALLED_APPS</b> de <code>settings.py</code>, y las rutas en <code>urls.py</code>
</p>
<p>
   Como indica el tutorial, las plantillas las podemos coger de
   <a href="https://github.com/macdhuibh/django-registration-templates">macdhuibh/django-registration-templates</a>
   y las modificamos con boostrap, para que queden como <a href="http://getbootstrap.com/examples/signin/">esta</a> o similar
</p>

<p>
   Ahora ya podremos gestinar la autorización de usuarios en las vistas, simplemente incluyendo el decorador
   <code>@login_required</code> antes de cada 'vista' de Django:
   <a href="https://docs.djangoproject.com/en/1.10/topics/auth/default/#the-login-required-decorator">login required decorator</a>
</p>
<br /><br />
<h4>Registro</h4>

<p>
   Django tiene un módulo para registro (<a href="https://docs.djangoproject.com/en/1.10/topics/logging/">Django Logging</a>),
   basado en el de <a href="https://docs.python.org/3.6/library/logging.html">python</a>
</p>

<p> La configuración del registro, se pone el archivo <code>settings.py</code>, y puede
   ser algo así:
   <br /><br />
   <pre><code class="language-python" data-lang="python">
      LOG_FILE = 'mi_archivo_de.log'

      LOGGING = {
          'version': 1,

          'disable_existing_loggers': False,

          'formatters': {

              'verbose': {
                  'format' : "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
                  'datefmt' : "%d/%b/%Y %H:%M:%S"
              },

              'simple': {
                  'format': '%(levelname)s [%(name)s:%(lineno)s] %(message)s'
              },
          },

          'handlers': {

              'file': {
                  'level': 'INFO',
                  'class': 'logging.FileHandler',
                  'filename': os.path.join(BASE_DIR, LOG_FILE),
                  'formatter': 'verbose',
                  'mode':'w'
              },

              'console': {
                  'level': 'DEBUG',
                  'class': 'logging.StreamHandler',
                  'formatter': 'simple'
              }
          },

          'loggers': {
              'django': {
                  'handlers':['file'],
                  'propagate': True,
                  'level':'ERROR',
              },

              'restaurantes': {
                  'handlers': ['file', 'console'],
                  'level': 'DEBUG',
              },
          }
      }
   </code></pre>
</p>

## Uso
#### Preparación del entorno
Lo primero será instalar MongoDB siguiendo las siguientes [instrucciones](https://docs.mongodb.com/getting-started/shell/installation/) si aún no lo hemos hecho, tras esto hay que [importar la base de datos de prueba](https://docs.mongodb.com/getting-started/python/import-data/)

Crear el
```
virtualenv -p python3 <Directorio>/venv # Directorio donde se desee desplegarpip
cd <Directorio>
source venv/bin/activate # Activa el entorno virtual
pip install -r requirements.txt # Instala mongoengine, Django y debería instalar las dependencias que se pueden ver abajo

```

#### Ejecución
```
python <Directorio>/app/manage.py runserver
```

## Dependencias
- Python==3.4.2
- Django==1.10.6
- django-registration-redux==1.6
- mongoengine==0.11.0
- pymongo==3.4.0
- six==1.10.0
- Pillow==4.0.0
