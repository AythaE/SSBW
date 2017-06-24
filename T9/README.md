# Tarea 8_bis
## Enunciado
<h3>Autentificación con API</h3>
<p>
   En esta tarea añadiremos al autentificación de usuarios a al API REST, según pone en
   <a href="http://www.django-rest-framework.org/api-guide/authentication/">Authentication</a>, y siguiendo
   el código de <a href="https://chrisbartos.com/articles/how-to-implement-token-authentication-with-django-rest-framework/">How to Implement Token Authentication with Django REST Framework</a>,
   y de <a href="http://geezhawk.github.io/user-authentication-with-react-and-django-rest-framework">Token-based authentication with Django and React</a>
</p>

<p>
   Usaremos autentificación con token simple, para que también valga para apliaciones móviles nativas, que no se llevan bien con las sesiones.
   Consiste en añadir a la cabecera un token distinto para cada usuario
</p>

<div class="highlight"><pre><code data-trim class="language-markup" >Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b
</code></pre></div>
<br />
 Ponemos en <b>settings.py</b>
<pre>
<code class="language-python" data-lang="python"><span class="n">INSTALLED_APPS</span> <span class="o">=</span> <span class="p">(</span>
  <span class="s">...</span><span class="p">,</span>
  <span class="s">'registration'</span><span class="p">,</span>
  <span class="s">'rest_framework'</span><span class="p">,</span>
  <span class="s">'rest_framework.authtoken'</span><span class="p">,</span>
  <span class="s">'rest_framework_mongoengine'</span><span class="p">,</span>
  <span class="s">'restaurantes'</span><span class="p">,</span>
<span class="p">)</span></code>
</pre>
y
<pre><code class="language-python">
   REST_FRAMEWORK = {
       'DEFAULT_AUTHENTICATION_CLASSES': (
           'rest_framework.authentication.TokenAuthentication',
       ),
       'DEFAULT_PERMISSION_CLASSES': (
           'rest_framework.permissions.IsAuthenticated',
       )
   }
</code></pre>

<p>
   Para no tener interferencias montaremos la API de autentificación en otra aplicación:
</p>
<pre><code class="language-bash">$ python manage.py startapp tokenauth
</code></pre>

<p>
   Ahora procederemos a generar los tokens para cada usuario de la BD, con un script
</p>

<pre><code class="language-python">
   from django.contrib.auth.models import User
   from rest_framework.authtoken.models import Token

   users = User.objects.all()
   for user in users:
       token, created = Token.objects.get_or_create(user=user)
       print user.username, token.key
</code></pre>
<p>
   Lógicamente también tendriamos que añdir el código para generar el token  cuando se cree un usuario, como está en
   los enlaces del principio
</p>
<p>
   Y ahora hacemos el código para que se devuelva el token con los datos adecuados:
</p>
En <b>urls.py</b>
<pre><code class="language-python">    #urls.py
   from django.conf.urls import url
   from django.views.decorators.csrf import csrf_exempt

   from rest_framework.routers import DefaultRouter
   from rest_framework.authtoken.views import obtain_auth_token

   router = DefaultRouter()

   urlpatterns = router.urls

   urlpatterns += [
       url(r'^obtain-auth-token/$', csrf_exempt(obtain_auth_token))
   ]
</code></pre>
<p>
   Y ya podremos comprobar que funciona
</p>
<pre><code class="language-bash">$ curl localhost:8000/restaurantes/api/restaurants/

$ curl -X POST -d "username=user&password=pass" localhost:8000/tokenauth/obtain-auth-token/

$ curl -H "Authorization: Token asdfq4tegasgq365ew35dfg" localhost:8000/restaurantes/api/restaurants/
</code></pre>
(No olvidar la barra al final)


## Uso
#### Preparación del entorno
Lo primero será instalar MongoDB siguiendo las siguientes [instrucciones](https://docs.mongodb.com/getting-started/shell/installation/) si aún no lo hemos hecho, tras esto hay que [importar la base de datos de prueba](https://docs.mongodb.com/getting-started/python/import-data/)

```
virtualenv -p python3 <Directorio> # Directorio donde se desee desplegar
cd <Directorio>
source /bin/activate # Activa el entorno virtual
pip install -r requirements.txt # Instala mongoengine, Django y debería instalar las dependencias que se pueden ver abajo

```
#### Generación de tokens para usuarios.
Tras modificar settings.py y arrancar una nueva aplicación hay que ejecutar el script `createToken.py` invocándolo de la siguiente manera:
```
python app/manage.py migrate

python app/manage.py shell
>>> exec(open('app/createToken.py').read())
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
- django-rest-framework-mongoengine==3.3.1
- djangorestframework==3.6.3
- mongoengine==0.11.0
- olefile==0.44
- pymongo==3.4.0
- six==1.10.0
