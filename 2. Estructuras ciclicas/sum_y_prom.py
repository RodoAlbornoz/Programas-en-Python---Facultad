# Crear un programa que permita ingresar N números enteros positivos y luego mostrar por pantalla
# la suma total de esos números y el promedio.
# Una vez hecho, crear otro programa que utilice lo anterior pero que permita hacerlo 3 veces.
# Es decir, calcular 3 sumas totales y 3 promedios, una vez hecho eso, verificar en que repetición se obtuvo el mejor promedio
# Ejemplo:
# Primera iteración: Suma total = 50, Promedio = 10.
# Segunda iteración: Suma total = 50, Promedio = 5.
# Tercera iteración: Suma total = 100, Promedio = 4
# El mayor promedio se obtuvo en la primera iteración.

def main() -> None:

    prom = 0
    mejor_promedio = 0
    suma = 0
    cant = 0
    num_iteracion = 0
    mejor_iteracion = 0

    for i in range(3):

        num = int(input("Ingrese el primer numero de la proxima iteracion: "))  ### PRIMERA LECTURA

        while(num > 0):
            suma += num
            cant += 1
            num = int(input("Ingrese el proximo numero: "))

        num_iteracion += 1
        print("La suma total de los numeros de esta iteracion es: ", suma)
        ## Si no se ingresaron números en la serie, la suma y el promedio son 0.
        if cant == 0:
            print("No se ingresaron numeros en esta iteracion")
        elif cant > 0:
            prom = suma / cant
            print("El promedio de los numeros ingresados de esta iteracion es: ", prom)

        if prom > mejor_promedio:
            mejor_promedio = prom            ### SE ESTABLECE NUEVO MEJOR PROMEDIO
            mejor_iteracion = num_iteracion  ### SE ESTABLECE EL NUMERO DE LA ITERACION CON EL MEJOR PROMEDIO
        
        print("*------------------SEPARADOR------------------*")  ### PARA SEPARAR ESTOS NUMEROS DE LOS DE LA PROXIMA ITERACION

        suma = 0      
        cant = 0        ### REINICIO EL VALOR DE LAS VARIABLES PARA LAS PROXIMAS ITERACIONES
        prom = 0


    print("El mejor promedio es:",mejor_promedio, ", y se obtuvo en la iteracion numero", mejor_iteracion)

main()