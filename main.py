import os
import requests
import pandas as pd
from dotenv import load_dotenv

#Cargar variables de entorno
load_dotenv()

API_URL = os.getenv("API_URL")

try:
    # Realizar la solicitud GET a la API
    response = requests.get(API_URL)
    response.raise_for_status()  # Lanza un error si la respuesta no es exitosa

    # Convertir la respuesta JSON en un DataFrame de pandas
    data = response.json()

    #Transoformacion basica
    datos_limpios = []

    for post in data:
        datos_limpios.append({
            "userId": post["userId"],
            "id": post["id"],
            "title": post["title"],
        })

     # Crear dataframe
    df = pd.DataFrame(datos_limpios)

    # Guardar el DataFrame en un archivo CSV
    df.to_csv("data_extracted.csv", index=False)

    print("Datos extraidos correctamente")
    print(f"Se guardaron {len(df)} registros en 'data_extracted.csv'.")

except requests.exceptions.RequestException as error:
    print("Error al realizar la peticion a la API:")
    print(error)

except Exception as error:
    print("Ocurrió un error inesperado:")
    print(error)

