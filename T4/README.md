# Tarea 4
## Enunciado


## Uso
#### Preparación del entorno
Lo primero será instalar MongoDB siguiendo las siguientes [instrucciones](https://docs.mongodb.com/getting-started/shell/installation/) si aún no lo hemos hecho, tras esto hay que [importar la base de datos de prueba](https://docs.mongodb.com/getting-started/python/import-data/)

```
virtualenv -p python3 <Directorio> # Directorio donde se desee desplegar
cd <Directorio>
source /bin/activate # Activa el entorno virtual
pip install mongoengine django # Instala mongoengine, Django y debería instalar las dependencias que se pueden ver abajo

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
