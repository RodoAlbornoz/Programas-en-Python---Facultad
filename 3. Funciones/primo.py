### Escribir una función que indique si un número natural es primo.

def es_primo(n: int) -> bool:
    '''
    PRE CONDICIONES: Un numero entero positivo, que es el numero que se evaluara si es primo o no
    POST CONDICIONES: Un valor booleano que dirá si el numero es primo (True) o no (False)
    '''
    primo = True
    i = 2

    ### No incluyo ni al 1 ni al numero mismo para evaluar como divisores
    while (i < n) and (primo == True):
        ### Si al dividir el numero por algun numero, el resto da 0, ya no es primo.
        if (n % i) == 0:
            primo = False
        i += 1

    return primo