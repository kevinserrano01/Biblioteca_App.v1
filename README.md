
# Readme app 

¡Bienvenido a la Biblioteca App! Esta aplicación es una solución completa para gestionar una biblioteca, permitiendo realizar un seguimiento de los socios, autores, empleados, libros y préstamos de libros.

# Características principales

* **Gestión de socios:** Registra a los socios de la biblioteca, incluyendo su información personal y detalles de contacto.
* **Gestión de autores:** Mantén un registro de los autores de los libros presentes en la biblioteca.
* **Gestión de empleados:** Administra la información de los empleados encargados de la biblioteca.
* **Gestión de libros:** Agrega y actualiza información sobre los libros disponibles en la biblioteca, incluyendo título, autor, género, y estado de disponibilidad.
* **Préstamos de libros:** Registra los préstamos de libros realizados a los socios, controlando las fechas de inicio y finalización de los préstamos.
* **Búsqueda avanzada desde el admin:** Permite buscar libros por título, autor, brindando una forma rápida de encontrar los libros deseados.




# Licencia
Este proyecto está licenciado bajo la ALKEMY.

¡Esperamos que disfrutes utilizando la README App! Si tienes alguna pregunta o sugerencia, no dudes en contactarnos.

# Requisitos de instalación

Antes de comenzar, asegúrate de tener instalado lo siguiente:

* Python 3.11

**Tecnologías utilizadas en el proyecto:**
* Django 4.2.1
* Jinja 
* Html 
* CSS
* Bootstrap 5.0
* Python
* JavaScript
* SQL

# Configuración para Windows 

* Clona este repositorio en tu máquina local.
* Crea una carpeta env fuera de la carpeta del proyecto  
* Crea un entorno virtual usando el comando: **python -m venv env**.
* Activa el entorno virtual usando el comando: **.\env\Scripts\activate**.
* Instala las dependencias ejecutando el comando: **pip install -r requirements.txt**.
* Realiza las migraciones de la base de datos con el comando: **python manage.py migrate**.
* Inicia el servidor de desarrollo local con: **python manage.py runserver**.
* Accede a la aplicación en tu navegador web ingresando la URL http://localhost:8000.

# Configuración para Linux 

* Clona este repositorio en tu máquina local.
* Crea una carpeta env fuera de la carpeta del proyecto  
* Crea un entorno virtual usando el comando: **python3 -m venv env**.
* Activa el entorno virtual usando el comando: **source env/bin/activate**.
* Instala las dependencias ejecutando el siguiente comando: **pip install -r requirements.txt**.
* Realiza las migraciones de la base de datos con el comando: **python3 manage.py migrate**.
* Inicia el servidor de desarrollo local con **python3 manage.py runserver**.
* Accede a la aplicación en tu navegador web ingresando la URL http://localhost:8000.

Estos pasos son similares a los de Windows, pero algunos comandos pueden variar ligeramente en Linux. Asegúrate de tener instalado Python 3 en tu sistema antes de seguir estos pasos.
    
## Autores

- [@Andrea Chungara](https://www.github.com/AndreaChungara)
- [@Gustavo Ledesma](https://www.github.com/GusLed1870)
- [@Naira Medina](https://www.github.com/Naikl12)
- [@kevin Serrano](https://www.github.com/kevinserrano01)
- [@Luis Quiroga](https://www.github.com/LuisQN)

## Contribuciones

Si deseas contribuir a la Biblioteca Readme, por favor sigue estos pasos:

* Realiza un fork de este repositorio.
* Crea una rama con un nombre descriptivo relacionado a la función que implementarás: git checkout -b mi-nueva-funcion.
* Realiza los cambios y realiza commits descriptivos: git commit -m "Agregar mi nueva función".
* Envía tus cambios al repositorio remoto: git push origin mi-nueva-funcion.
Abre una pull request en este repositorio principal.

## Documentación de la API

#### Para obtener todos los libro

```http
  GET /api/libros
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `api_key` | `string` | **Required**. Your API key |


![App Screenshot](https://via.placeholder.com/468x300?text=App+Screenshot+Here)

#### Get item

```http
  GET /api/libros/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `int`    | **Required**. Id del Libro   |



## Screenshots

![App Screenshot](https://via.placeholder.com/468x300?text=App+Screenshot+Here)


## Documentation

[Documentation](https://linktodocumentation)

