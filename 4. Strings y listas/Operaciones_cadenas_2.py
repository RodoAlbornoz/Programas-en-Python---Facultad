### Escribir las siguientes funciones que reciben una cadena, un caracter y devuelven una cadena nueva:
### La función insertar_entre_letras() inserta el caracter entre cada letra de la cadena original.
### La función reemplazar_espacios() reemplaza todos los espacios de la cadena original por el caracter.
### La función reemplazar_digitos() reemplaza todos los dígitos de la cadena original por el caracter.


def insertar_entre_letras(cadena: str, caracter: str) -> str:
    longitud = len(cadena)

    cadena_entre_letras = cadena[0]
    for i in range(1, longitud):
        ## Por cada iteracion, se añade un caracter y luego el caracter que está en medio de todos los caracteres.
        cadena_entre_letras = cadena_entre_letras + caracter + cadena[i]

    return cadena_entre_letras 


def reemplazar_espacios(cadena: str, caracter: str) -> str:
    longitud = len(cadena)

    cadena_sin_espacios = ""
    for i in range(longitud):
        if cadena[i] == " ":
            cadena_sin_espacios = cadena_sin_espacios + caracter
        else:
            cadena_sin_espacios = cadena_sin_espacios + cadena[i]

    return cadena_sin_espacios


def reemplazar_digitos(cadena: str, caracter: str) -> str:
    longitud = len(cadena)

    cadena_reemplazada = ""
    for i in range(longitud):
        if cadena[i].isnumeric():
            cadena_reemplazada = cadena_reemplazada + caracter
        else:
            cadena_reemplazada = cadena_reemplazada + cadena[i]
    return cadena_reemplazada