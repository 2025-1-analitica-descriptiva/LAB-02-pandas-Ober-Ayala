"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""


import pandas as pd

def pregunta_01():
    
    df = pd.read_csv("files/input/tbl0.tsv", delimiter="\t")
    
    # Contar las filas
    total_filas = len(df)
    
    return total_filas

# Prueba rápida
print(pregunta_01())

"""
    ¿Cuál es la cantidad de filas en la tabla `tbl0.tsv`?

    Rta/
    40

    """
