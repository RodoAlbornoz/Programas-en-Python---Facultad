### Escribir una función que dada una cadena de caracteres, indique si se trata de un palíndromo 
### (se lee igual de izquierda a derecha que de derecha a izquierda).

def palindromo(cadena: str) -> bool:
    longitud_cadena = len(cadena)

    ## Le saco los espacios a la cadena
    cadena_sin_espacios = ""
    for i in range(longitud_cadena):
        if cadena[i] != " ":
            cadena_sin_espacios = cadena_sin_espacios + cadena[i]

    cadena_inversa = cadena[::-1]
    longitud_cadena_inversa = len(cadena_inversa)
    cadena_inversa_sin_espacios = ""
    ## Le saco los espacios a la cadena inversa
    for i in range(longitud_cadena_inversa):
        if cadena_inversa[i] != " ":
            cadena_inversa_sin_espacios = cadena_inversa_sin_espacios + cadena_inversa[i]

    ## Si ambas cadenas sin espacios son iguales, la palabra es palíndromo
    if cadena_sin_espacios == cadena_inversa_sin_espacios:
        return True
    else:
        return False