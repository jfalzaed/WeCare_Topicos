# WeCare
## Requisitos

- Verifica que tu versión de python sea 3.8 o superior con el siguiente comando:
```bash
python --version
```
or
```bash
python -V
```

- Verifica que cuentes con pip, la herramienta de gestión de paquetes de Python, con el siguiente comando:
```bash
pip --version
```

- Git

### Clonar el Repositorio

Puedes clonar este repositorio utilizando el siguiente comando:
```bash
git clone https://github.com/Salome-Serna-R/WeCare.git
```
O simplemente descargando el paquete .zip

Luego de clonarlo se deben aplicar las migraciones iniciales para configurar la base de datos y esto se hace a través del siguiente comando en la terminal ubicados en la carpeta donde se encuentra clonado el proyecto
```bash
python manage.py migrate
```

Finalmente, verificando que estes en la ruta adecuada, puedes ejecutar el servidor de desarrollo de Django con el siguiente comando:
```bash
python manage.py runserver
```
Luego, abre tu navegador web y ve a http://127.0.0.1:8000 para ver la aplicación en funcionamiento.

Adicional, para la verificación del chat, debes acceder al la vista de administrador http://127.0.0.1:8000/admin/ 
Luego de iniciar sesión con un usuario, debes pegar la siguiente ruta http://127.0.0.1:8000/ms/nombre y en "nombre" poner el nombre de la persona con la que desea iniciar o continuar una conversación.
