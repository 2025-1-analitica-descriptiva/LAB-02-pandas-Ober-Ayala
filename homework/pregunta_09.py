"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""

import pandas as pd #

def pregunta_09(): #
    # Lee el archivo tbl0.tsv para el DataFrame principal
    df = pd.read_csv("files/input/tbl0.tsv", delimiter="\t") 
    
    # Convierte la columna 'c3' a tipo datetime. Se usa errors='coerce'
    # para convertir fechas inválidas (como 1999-02-29) a NaT,
    # lo cual es importante si otras preguntas dependen del tipo datetime de 'c3'.
    df["c3"] = pd.to_datetime(df["c3"], errors='coerce') 
    
    # Para la columna 'year', se vuelve a leer el archivo tbl0.tsv temporalmente
    # para asegurar que se extrae el año como string directamente de la cadena original.
    # Esto evita los problemas de 'NaT' o los sufijos '.0' que pueden aparecer
    # al extraer el año de una columna datetime que contiene NaT.
    df_temp = pd.read_csv("files/input/tbl0.tsv", delimiter="\t") #
    df["year"] = df_temp["c3"].astype(str).str[:4] # Extrae los primeros 4 caracteres (el año) como string
    
    return df #

# La línea 'print(pregunta_09())' está aquí para depuración local
# y no es necesaria para que el script funcione con los tests.
# Puedes comentarla o dejarla si te ayuda a probar la función por separado.
# print(pregunta_09())

"""
    Agregue el año como una columna al dataframe que contiene el archivo
    `tbl0.tsv`.

    Rta/
        c0 c1  c2          c3  year
    0    0  E   1  1999-02-28  1999
    1    1  A   2  1999-10-28  1999
    2    2  B   5  1998-05-02  1998
    ...
    36  36  B   8  1997-05-21  1997
    37  37  C   9  1997-07-22  1997
    38  38  E   1  1999-09-28  1999
    39  39  E   5  1998-01-26  1998
    """