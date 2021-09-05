# Un número perfecto es aquel número que es igual a la suma de todos sus divisores positivos excepto el mismo.
# El primer número perfecto es 6, ya que 1 + 2 + 3 = 6.
# Escribir un programa que muestre todos los números perfectos hasta un número dado por el usuario.
# Ayuda: Entre 0-10.000 hay solo 3 números perfectos.

import math

def main() -> None:

    cant_perfectos = 0
    suma_divisores = 0

    numero = int(input("Ingrese un numero, para buscar todos los perfectos desde 1 hasta ese numero: "))

    ### Busco todos los numeros perfectos desde 1 hasta el numero ingresado por el usuario
    for posible_perfecto in range(1, numero + 1):

        ### Si el posible perfecto es par, se buscan sus divisores SOLO desde 1 hasta la mitad del numero (Pues mas allá de la mitad, ningun numero será
        ### divisor del posible perfecto), o sea, hasta lim.
        ### Si es impar, se buscan sus divisores desde 1 hasta lim = (Posible perfecto - 1) / 2. En este caso, se redondea la mitad para abajo para que
        ### NO se pregunte si el proximo numero que le sigue al redondeado sea un divisor del mismo.
        
        if (posible_perfecto % 2) == 0:
            lim = math.floor(posible_perfecto // 2)
        elif (posible_perfecto % 2) == 1:
            lim = math.floor((posible_perfecto - 1) // 2)

        ### Evaluo si cada numero en el rango del usuario es perfecto
        for divisor_posible in range(1, lim + 1):
            if (posible_perfecto % divisor_posible) == 0:
                suma_divisores += divisor_posible
        
        if suma_divisores == posible_perfecto:
            print("El numero", posible_perfecto, "es perfecto")
            cant_perfectos += 1

        ### "Reseteo" el valor que almacena la suma de los divisores del perfecto anterior, porque ahora voy a leer uno nuevo
        suma_divisores = 0


    ### Muestro la cantidad de perfectos
    print("En ese rango, hay en total ", cant_perfectos, "numeros perfectos")


main()