## Crear un programa que:
## Permita ingresar 5 números enteros positivos.    
## Calcule el máximo entre esos números; lo muestre.
## Calcule el mínimo; lo muestre.
## Calcule el promedio; lo muestre.
## Sume el máximo, el mínimo; y el promedio (Resultando en un entero. Para eso pueden castear el resultado a int. Ejemplo: int(resultado)) y en caso de
## que el resultado sea par; salude al usuario tantas veces como número resultante de esa cuenta, si es impar; vuelve a empezar TODO el programa DE NUEVO.

CANT_NUMEROS = 5

## Funcion que calcula un maximo
def calcular_maximo(num: int, max: int) -> int:
    if num > max:
        max = num
    return max

## Funcion que calcula un minimo    
def calcular_minimo(num: int, min: int) -> int:
    if num < min:
        min = num
    return min

## Funcion que calcula un promedio
def calcular_prom(suma_de_numeros: int, cantidad_de_numeros: int) -> float: 
    promedio = suma_de_numeros / cantidad_de_numeros
    return promedio


def main() -> None: 

    ### La inicio en este valor para entrar al while
    suma_total = 1

    ### Mientras que la suma del maximo, el minimo y el promedio de este juego de numeros sea 
    ### impar, volver a pedir 5 numeros y calcular su maximo, minimo y promedio: 
    while (suma_total % 2) == 1:

        ### Inicializo variables o las "reinicio" en caso de que suma_total me de impar
        suma_numeros = 0
        suma_total = 0

        num = int(input("Ingrese el primer numero: "))

        suma_numeros += num 
        minimo = num
        maximo = num

        ### Leo 4 numeros mas y calculo maximo y minimo
        for i in range (1, 5): 

            num = int(input("Ingrese otro numero: "))
            suma_numeros += num

            maximo = calcular_maximo(num, maximo)
            minimo = calcular_minimo(num, minimo)

        prom = calcular_prom(suma_numeros, CANT_NUMEROS)

        print("El maximo de este juego de numeros es: ", maximo)
        print("El minimo de este juego de numeros es: ", minimo)
        print("El promedio de este juego de numeros es: ", prom)

        ### Paso el prom de float a int
        prom = int(prom)

        suma_total = maximo + minimo + prom

    ### Saludo en caso de que la suma sea par
    for j in range (1, suma_total + 1):
        print("¡Hola usuario!")


main()