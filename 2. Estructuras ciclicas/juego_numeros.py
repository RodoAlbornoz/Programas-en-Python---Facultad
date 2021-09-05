# Se pide hacer un programa que ingrese 8 juegos de n valores positivos cada uno.
# Considerar un condiciòn de corte para el n.
# Calculando el promedio de cada juego, el máximo de cada juego y el mínimo de todos los juegos.

def main() -> None:

    cant_num_por_juego = 0
    suma_numeros_por_juego = 0

    ### Primera lectura
    num = int(input("Ingrese el primer numero del primer juego: "))

    ## El máximo y minimo tanto de la primera jugada como de todas las jugadas, son iguales al primer número leido
    max_por_juego = num
    min_por_juego = num
    min_todos_los_juegos = num
    cant_num_por_juego += 1
    suma_numeros_por_juego += num

    num = int(input("Ingrese el proximo numero de este juego o 0 para pasar al proximo juego: "))

    for i in range (8): 

        ### Operaciones sobre un juego mientras que el numero ingresado no sea 0 (Condicion de corte)
        while (num != 0):
            cant_num_por_juego += 1
            suma_numeros_por_juego += num

            if num > max_por_juego: 
                max_por_juego = num       ### Nuevo maximo por juego
            elif num < min_por_juego:
                min_por_juego = num       ### Nuevo minimo por juego

            num = int(input("Ingrese el proximo numero de este juego o 0 para pasar al proximo juego: "))

        if cant_num_por_juego != 0:
            prom_por_juego = suma_numeros_por_juego / cant_num_por_juego
            print("El promedio de este juego fue:",prom_por_juego)
            print("El maximo de este juego fue:",max_por_juego)
        elif cant_num_por_juego == 0:
            prom_por_juego = 0           ### No se ingresaron numeros en este juego (Evito dividir por 0)
            print("No hubo maximo en este juego")

        ### Operaciones sobre todos los juegos
        if min_por_juego < min_todos_los_juegos:
            min_todos_los_juegos = min_por_juego   ### Nuevo minimo absoluto (Para todos los juegos)

        ### Lectura del proximo juego
        cant_num_por_juego = 0
        suma_numeros_por_juego = 0

        print("*--------------SEPARADOR DE JUEGOS--------------*")

        if i < 7:    ### Pregunto por el proximo numero siempre que sepa que van a haber mas juegos
            num = int(input("Ingrese el primer numero del proximo juego o 0 para pasar al otro juego: "))
            max_por_juego = num
            min_por_juego = num

    ### Muestro los resultados (Minimo de todos los juegos)
    print("El minimo absoluto de todos los juegos es el", min_todos_los_juegos)


main()