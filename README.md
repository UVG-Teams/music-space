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
* Instalar dependencias
    ```shell
    $ pip install -r requirements.txt
    ```
* [psycopg2](https://www.psycopg.org/)
    * Comprobar instalación
    ```shell
    $ python -c "import psycopg2" --verbose
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


## Para ejecucion

* Clonar repo
* Configurar entorno (instalar dependencias de requirements.txt)
    * Borrar pkg-resources==0.0.0 y psycopg si es necesario e instalarlo manualmente (Cambia por SO)
* Configuracion de DB y credenciales
* python load_data.py
    * Sirve para resetear la db si se necesita, cargar la db inicial y migraciones de Django
    * Con seleccionar la opcion 2 del menu y marcar si a todo es suficiente
* python manage.py runserver
* Para cargar urls de reproduccion ir a la ruta: /user-track/load/
    * Tarda un par de minutos, luego redirecciona a home
    * Tomar en cuenta que sin este paso no se podra "reproducir" las canciones
* Listo!
