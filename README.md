# Pre-entrega: Extracción y Almacenamiento Seguro de Datos vía API

## Descripción

En este proyecto realicé la extracción de datos desde una API pública mediante una solicitud HTTP GET, procesé la información obtenida y la almacené en un archivo CSV.

El objetivo es aplicar un flujo básico de extracción, transformación y almacenamiento de datos utilizando Python.

## API utilizada

Utilicé la API pública **JSONPlaceholder**:

`https://jsonplaceholder.typicode.com/posts`

Esta API no requiere una clave de acceso para realizar las consultas.

## Tecnologías utilizadas

* Python
* Requests
* Pandas
* Python-dotenv
* Git y GitHub

## Configuración

La URL de la API se almacena en un archivo `.env`:

```text
API_URL=https://jsonplaceholder.typicode.com/posts
```

El archivo `.env` está incluido en `.gitignore` para evitar subir variables de configuración al repositorio.

## Instalación

Instalé las dependencias necesarias ejecutando:

```bash
py -m pip install -r requirements.txt
```

## Ejecución

Para ejecutar el programa:

```bash
py main.py
```

En el script realizo una solicitud GET a la API, obtengo los datos en formato JSON y los transformo en un DataFrame de Pandas.

## Transformación y almacenamiento

De la respuesta de la API seleccioné los siguientes campos:

* `userId`
* `id`
* `title`

Los datos procesados se almacenan en:

```text
data_extracted.csv
```

El archivo contiene los registros obtenidos desde la API en formato tabular.

## Manejo de errores

El programa utiliza `try/except` y `response.raise_for_status()` para detectar y manejar errores relacionados con la solicitud HTTP y otros errores inesperados durante la ejecución.

## Seguridad

El archivo `.env` no se incluye en el repositorio gracias a la configuración de `.gitignore`. Esto permite separar la configuración del código fuente y evitar publicar información que pudiera ser sensible en otros proyectos que utilicen credenciales o claves de API.
