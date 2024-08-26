# WeCare
## Requisitos

- Python 3.8 o superior
- pip (la herramienta de gestión de paquetes de Python)
- Git

### Clonar el Repositorio

Puedes clonar este repositorio utilizando el siguiente comando:

git clone https://github.com/Salome-Serna-R/WeCare.git


Luego de clonarlo se deben aplicar las migraciones iniciales para configurar la base de datos y esto se hace a través del siguiente comando en la terminal ubicados en la carpeta donde se encuentra clonado el proyecto
python manage.py migrate

Finalmente, puedes ejecutar el servidor de desarrollo de Django con el siguiente comando:

python manage.py runserver

Luego, abre tu navegador web y ve a http://127.0.0.1:8000 para ver la aplicación en funcionamiento.
