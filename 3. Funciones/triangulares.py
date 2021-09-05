# Escribir un programa que le pregunte al usuario un número n e imprima los primeros n números triangulares, junto con su índice.
# Los números triangulares se obtienen mediante la suma de los números naturales desde 1 hasta n.
# Por ejemplo:
#    >>> Ingrese un numero: 5
#    1 - 1
#    2 - 3
#    3 - 6
#    4 - 10
#    5 - 15
# Tip: hacerlo usando y sin usar la ecuación T_n = n(n+1) / 2
# ¿Cuál realiza más operaciones?

def calcular_numero_triangular(n: int) -> None:
    '''
    PRE CONDICIONES: Se recibe un numero entero positivo, que representa el numero a partir del cual
    se calcularan y mostraran los numeros triangulares
    POST CONDICIONES: Se devuelve cada numero triangular con su respectivo indice
    '''
    suma_naturales = 0

    for i in range(1, n + 1):
        suma_naturales += i
        print(i, "-", suma_naturales)


### Ahora utilizo la formula de T_n
def calcular_numero_triangular_2(n: int) -> None:
    triangular = 0

    for i in range(1, n + 1):
        triangular = int((i * (i + 1)) / 2)
        print(i, "-", triangular)


### La funcion que realiza mas operaciones es la que usa la formula de T_n, porque en cada 
### iteracion se debe hacer un producto y una division, mientras que en la otra funcion solo
### hay que hacer una suma
        

def main() -> None:
    numero = int(input("Ingrese un numero: "))
    calcular_numero_triangular(numero)
    calcular_numero_triangular_2(numero)

main()