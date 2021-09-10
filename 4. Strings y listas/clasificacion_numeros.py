### Dada una lista de números enteros y un entero k, escribir una función que:
### a) Devuelva tres listas, una con los menores, otra con los mayores y otra con los iguales a k.
### b) Devuelva una lista con aquellos que son múltiplos de k.


def menores_mayores_iguales(enteros: list, k: int) -> list:
    '''
    Pre condiciones: Se recibe una lista de numeros enteros, no necesariamente positivos, a partir de los cuales
    se evaluan si son mayores, iguales o menores a un numero entero k, otro parametro que se recibe
    Post condiciones: Se devuelve una matriz, que está conformada por 3 listas, una que tiene los numeros de la 
    lista mayores a k, otra con los menores a k, y otra con los iguales a k
    '''

    menores = []
    mayores = []
    iguales = []

    for i in range(len(enteros)): 
        if enteros[i] > k:
            mayores.append(enteros[i])
        elif enteros[i] < k:
            menores.append(enteros[i])
        else:
            iguales.append(enteros[i])

    return [menores, mayores, iguales]


def multiplos(enteros: list, k: int) -> list:
    '''
    Pre condiciones: Se recibe una lista de numeros enteros, no necesariamente positivos, los cuales se evaluaran si son multiplos
    de un numero entero k, otro parametro que se recibe
    Post condiciones: Se devuelve una lista que es sublista de la lista de la precondicion, la cual contiene los elementos de la
    lista que son multiplos de k
    '''

    multiplos_k = []

    for i in range(len(enteros)):

        if (enteros[i] % k) == 0:
            multiplos_k.append(enteros[i])

    return multiplos_k