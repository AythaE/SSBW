# Tarea 2
## Enunciado
#### Usando boostrap

[Boostrap](https://v4-alpha.getbootstrap.com/) es un ['responsive framework'](https://colorlib.com/wp/free-css3-frameworks/) para facilitar el CSS de nuestras páginas, que además se adaptan al tamaño de pantalla que se use en el navegador (móvil, tablet, y distintos anchos de escritorio).

En concreto usaremos su versión 4. En [Quick start](https://v4-alpha.getbootstrap.com/getting-started/introduction/), tenemos una plantilla básica. También podemos usar los snippets de [atom-bootstrap4](https://atom.io/packages/atom-bootstrap4) para ir más rápido.

##### Pantalla de login y menú

En esta tarea haremos dos pantallas, una como esta: [sign in](http://v4-alpha.getbootstrap.com/examples/signin/), que de paso a otra con un menú arriba, como esta: [starter template](http://v4-alpha.getbootstrap.com/examples/starter-template/), que tenga opciones de menú para los enlaces de la tarea anterior, y en el que aparezca el nombre usado en el login, y una última opción de logout. De momento no comprobamos ni el username ni el password.

[Flask](http://flask.pocoo.org/) usa las plantillas de [Jinja2](http://jinja.pocoo.org/docs/2.9/templates/). Para tener en esta segunda pantalla una salida uniforme en todas opciones de los menús, usamos la herencia de plantillas, tal como plantea [An Introduction to Python’s Flask Framework](https://code.tutsplus.com/tutorials/an-introduction-to-pythons-flask-framework--net-28822).

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
python <Directorio>/app/t2.py
```
- Opción 2
```
export FLASK_APP=<Directorio>/app/t2.py
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
