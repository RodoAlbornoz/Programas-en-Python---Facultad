### Un numero de Armstrong es aquel cuya suma de digitos, cada uno elevado a la potencia de la cantidad de digitos 
### del numero, es igual al numero. 
### Por ejemplo, 153 es numero de Armstrong, porque 153 = 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
### Escribir una funcion que, dado un numero ingresado por el usuario, retorne si es numero de Armstrong.
### Despues escribir otra funcion que calcule todos los numeros de Armstrong que hay entre 1 y un numero ingresado por el usuario.

from math import pow

### Funcion que evalua si un numero es de Armstrong o no.
def es_armstrong(num: str) -> bool:
    '''
    PRE CONDICIONES: Un numero entero positivo, tomado como un string, que es el que se evaluará si es de Armstrong
    POST CONDICIONES: Un valor booleano que dirá si el numero es de Armstrong o no.
    '''

    digito_elevado = 0
    suma_digitos_elevados = 0
    cant_digitos = len(num)

    for i in range(cant_digitos):
        ### El i-esimo digito, tomando el 0 como inicio, se castea a entero. El numero elevado a la i-esima posicion segun la la posicion 
        ### en el string (Numero a evaluar como de Armstrong), se suma a una variable que va acumulando la suma de los digitos elevados.
        digito_elevado = pow(int(num[i]), cant_digitos)
        suma_digitos_elevados += digito_elevado

    ### Si el string (Numero a evaluar como de Armstrong) es igual a la suma de los digitos elevados, el numero es de Armstrong.
    if suma_digitos_elevados == int(num):
        armstrong = True
    else:
        armstrong = False

    return armstrong


### Funcion que evalua la cantidad de Armstrong en un rango.
def cantidad_armstrongs(tope: int) -> None:
    '''
    PRE CONDICIONES: Un numero entero positivo, el cual será el techo para la cantidad de numeros a evaluar si son de Armstrong
    POST CONDICIONES: Nada. Se imprime por pantalla los numeros de Armstrong.
    '''

    for num in range(1, tope + 1):
        ### Casteo del numero a string para poder tomar sus digitos. Despues realizo lo mismo que en la funcion es_armstrong
        num = str(num)
        digito_elevado = 0
        suma_digitos_elevados = 0
        cant_digitos = len(num)

        for j in range(cant_digitos):
            digito_elevado = pow(int(num[j]), cant_digitos)
            suma_digitos_elevados += digito_elevado

        if suma_digitos_elevados == int(num):
            print(num,"es Armstrong")


def main() -> None:

    num = input("Ingrese un numero para evaluar si es de Armstrong: ")
    armstrong = es_armstrong(num)
    print(armstrong)

    cant_armstrongs = int(input("Ingrese un numero, para imprimir todos los armstrongs desde el 1 hasta ese numero: "))
    cantidad_armstrongs(cant_armstrongs)


main()