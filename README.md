# Pre-entrega: Extracción y Almacenamiento Seguro de Datos vía API

## Descripción

Este proyecto realiza la extracción de datos desde una API pública mediante una solicitud HTTP GET, procesa la información obtenida y la almacena en un archivo CSV estructurado.

El objetivo es aplicar un flujo básico de extracción, transformación y almacenamiento de datos utilizando Python.

## API utilizada

Se utiliza la API pública **JSONPlaceholder**:

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

Instalar las dependencias necesarias ejecutando:

```bash
py -m pip install -r requirements.txt
```

## Ejecución

Para ejecutar el programa:

```bash
py main.py
```

El script realiza una solicitud GET a la API, obtiene los datos en formato JSON y los transforma en un DataFrame de Pandas.

## Transformación y almacenamiento

De la respuesta de la API se seleccionan los siguientes campos:

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

El archivo `.env` no se incluye en el repositorio gracias a la configuración de `.gitignore`.

Esto permite separar la configuración del código fuente y evitar publicar información que pudiera ser sensible en otros proyectos que utilicen credenciales o claves de API.
