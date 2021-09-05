# 1. Escribir una función que permita calcular la duración en segundos de un intervalo dado en horas, minutos
#    y segundos.
# 2. Usando la función del ejercicio anterior, escribir un programa que pida al usuario dos intervalos expresados
#    en horas, minutos y segundos, sume sus duraciones, y muestre por pantalla la duración total en horas,
#    minutos y segundos.


def convertir_a_segundos(hora: int, min: int, seg: int) -> int:
    seg_totales = (seg) + (min * 60) + (hora * 3600)
    return seg_totales


def main() -> None:

    print("DATOS DEL PRIMER INTERVALO: ")
    horas_interv_1 = int(input("Ingrese la cantidad de horas del primer intervalo: "))
    min_interv_1 = int(input("Ingrese la cantidad de minutos del primer intervalo: "))
    seg_interv_1 = int(input("Ingrese la cantidad de segundos del primer intervalo: "))
    duracion_interv_1 = convertir_a_segundos(horas_interv_1, min_interv_1, seg_interv_1)

    print("DATOS DEL SEGUNDO INTERVALO: ")
    horas_interv_2 = int(input("Ingrese la cantidad de horas del segundos intervalo: "))
    min_interv_2 = int(input("Ingrese la cantidad de minutos del segundo intervalo: "))
    seg_interv_2 = int(input("Ingrese la cantidad de segundos del segundo intervalo: "))
    duracion_interv_2 = convertir_a_segundos(horas_interv_2, min_interv_2, seg_interv_2)

    duracion_total = duracion_interv_1 + duracion_interv_2

    ### HAGO LOS CALCULOS PARA DEVOLVER LAS HORAS, MINUTOS Y SEGUNDOS DE LA DURACION TOTAL

    horas_suma_duraciones = duracion_total // 3600
    duracion_total = duracion_total % 3600

    min_suma_duraciones = duracion_total // 60
    duracion_total = duracion_total % 60

    # Los segundos restantes son iguales a los segundos de la duracion
    seg_suma_duraciones = duracion_total

    print("La suma de los intervalos es igual a ",horas_suma_duraciones, "horas, ",min_suma_duraciones, "minutos y ",seg_suma_duraciones, "segundos")


main()