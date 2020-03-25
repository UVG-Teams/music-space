# uvg-db-proyecto1

<h2 align="center">Music Streaming</h2>
<h3 align="center">Proyecto UVG Base de Datos</h3>

## Configuración de entorno

* [Instalar Python](https://www.python.org/)
* [Instalar Postgres](https://www.postgresql.org/)
* Instalar Python Enviorment
    ```shell
    $ sudo apt install python3-env
    ```
* Clonar repo
* Crear, activar y desactivar python env
    ```shell
    $ python3 -m venv venv
    $ source venv/bin/activate
    $ deactivate
    ```
* [Instalar Django](https://docs.djangoproject.com/en/3.0/topics/install/)
    ```shell
    $ python -m pip install Django
    ```
* [Instalar psycopg2](https://www.psycopg.org/)
    * Instalar y comprobar instalación
    ```shell
    $ pip install psycopg2
    $ python -c "import psycopg2" --verbose
    ```
* Instalar ipython 
    ```shell
    $ pip install ipython
    ```

## Configuración de Base de Datos

* Conexión
    ```shell
    $ psql -h localhost -U postgres -W
    ```
    ```sql
    CREATE DATABASE connect;
    ```

* Crear archivo /music_site/credentials.py
    ```python
        DATABASE = {
            'NAME': 'proyecto1dbuvg',
            'USER': 'tu-usuario',
            'PASSWORD': 'tu-contraseña',
            'HOST': 'tu-host',
            'PORT': 'tu-puerto',
        }
    ```

* Cargar data
    ```shell
    $ python load_data.py
    ```

* Run Server
    ```shell
    $ python manage.py runserver
    ```


## Desarrollo

* Crear app
    ```shell
    $ django-admin startproject my_site
    $ python manage.py startapp myapp
    ```
* Abrir shell
    ```shell
    $ python manage.py shell
    ```