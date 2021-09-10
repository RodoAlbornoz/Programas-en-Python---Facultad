### Escribir una función que cuente la cantidad de apariciones de cada caracter en una cadena de texto, y los devuelva 
### en un diccionario.

def contar_caracteres(cadena: str) -> dict:

    diccionario_letras = dict()
    longitud_cadena = len(cadena)

    for i in range(longitud_cadena):
        ## Si el caracter leido no es un espacio, lo considero.
        if cadena[i] != " ":
            ## Si el caracter leido no está en el diccionario, inicializo la cantidad de veces que aparece.
            if cadena[i].lower() not in diccionario_letras.keys():
                diccionario_letras[cadena[i].lower()] = 0

            diccionario_letras[cadena[i].lower()] += 1

    return diccionario_letras