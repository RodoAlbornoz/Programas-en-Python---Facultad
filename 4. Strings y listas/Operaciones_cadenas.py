### Escribir las siguientes funciones que reciben una cadena y devuelven una nueva:
### La función primeros_dos_c() devuelve sus dos primeros caracteres.
### La función ultimos_tres_c() devuelve sus tres últimos caracteres.
### La función cada_dos_c() devuelve solo cada dos caracteres de la cadena.
### La función sentido_inverso() devuelve la cadena en sentido inverso.
### La función normal_e_inversa() devuelve la cadena en sentido normal seguida de la misma en sentido inverso.


def primeros_dos_c(cadena: str) -> str:
    return cadena[0:2]


def ultimos_tres_c(cadena: str) -> str:
    longitud = len(cadena)
    return cadena[longitud - 3:longitud]


def cada_dos_c(cadena: str) -> str:
    longitud = len(cadena)
    return cadena[0:longitud:2]


def sentido_inverso(cadena: str) -> str:
    longitud = len(cadena)
    return cadena[::-1]


def normal_e_inversa(cadena: str) -> str:
    longitud = len(cadena)
    return cadena + cadena[::-1]