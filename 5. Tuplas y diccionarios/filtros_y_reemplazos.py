### Escribir funciones que dada una cadena de caracteres:
### a) Devuelva solamente las letras consonantes.
### b) Devuelva solamente las letras vocales.
### c) Reemplace cada vocal por su siguiente vocal.

LISTA_VOCALES = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

def consonantes(cadena: str) -> str:

    cadena_consonantes = ""
    longitud_cadena = len(cadena)

    for i in range(longitud_cadena):
        if cadena[i] not in LISTA_VOCALES:
            cadena_consonantes = cadena_consonantes + cadena[i]

    return cadena_consonantes


def vocales(cadena: str) -> str:
    cadena_vocales = ""
    longitud_cadena = len(cadena)

    for i in range(longitud_cadena):
        ## Considero si la lista tiene espacios
        if (cadena[i] in LISTA_VOCALES) or (cadena[i] == " "):
            cadena_vocales = cadena_vocales + cadena[i]

    return cadena_vocales


def avanzar_vocales(cadena: str) -> str:
    cadena_avanzar_vocales = ""
    longitud_cadena = len(cadena) 

    ## Diccionario que tiene como llave la vocal y como valor la proxima vocal que le sigue.
    diccionario_avanzar_vocales = {"a": "e", "e": "i", "i": "o", "o": "u", "u": "a", "A": "E", "E": "I", "I": "O", "O": "U", "U": "A"}

    for i in range(longitud_cadena):
        ## Si la letra leida es una vocal, al string de vocales avanzadas le añado la vocal que le sigue a la leida, que en el diccionario
        ## es la llave (Vocal leida) cuyo valor es la vocal a poner al string de vocales avanzadas (Vocal siguiente)
        if cadena[i] in LISTA_VOCALES:
            cadena_avanzar_vocales = cadena_avanzar_vocales + diccionario_avanzar_vocales[cadena[i]]
        else:
            cadena_avanzar_vocales = cadena_avanzar_vocales + cadena[i]

    return cadena_avanzar_vocales