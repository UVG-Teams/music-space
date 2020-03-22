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
* [Instalar psycopg2](https://www.psycopg.org/)
    * Comprobar instalación
    ```shell
    $ python -c "import psycopg2" --verbose
    ```
* Instalar ipython 
    ```shell
    $ pip install ipython
    ```

## Configuración de Base de Datos

* Conexión
    ```shell
    $ psql -h localhost(host) -U postgres(user) -W
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
    $ python manage.py makemigrations
    $ python manage.py migrate
    ```

* Run Server
    ```shell
    $ python manage.py runserver
    ```


## Desarrollo

* Crear app
    ```shell
    $ python manage.py startapp myapp
    ```
* Abrir shell
    ```shell
    $ python manage.py shell
    ```