# Hacer un programa que permita el ingreso de los alumnos y las notas correspondiente a 3 cátedras de la materia 
# Algoritmos de FIUBA. Para esto sabemos que cada cátedra tiene inscriptos a un número indeterminado a priori de alumnos, 
# y que los datos que poseemos de cada alumno son Nombre y Apellido, padrón, nota final. Se pide:
#    a- Calcular la nota más alta de cada curso y a qué alumno pertenece (mostrar padrón)
#    b- Calcular la nota más baja entre todos los cursos.
#    c- Calcular la cátedra cuyo promedio de nota sea el máximo.
#    d- Mostrar la cantidad total de alumnos de los 3 cursos.

# Datos:
# -Nombre
# -Apellido
# -Padron
# -Nota final

###################### LEO LOS DATOS DE LA PRIMERA CATEDRA  ######################

def main() -> None:

    cant_alumnos_por_catedra = 0
    suma_notas_por_catedra = 0
    prom_por_catedra = 0
    cant_alumnos_total = 0
    prom_max_total_catedras = 0
    num_catedra = 0
    num_catedra_de_mayor_prom = 0
    hay_mas_catedras = "Si"

    ### LEO LOS DATOS DEL PRIMER ALUMNO
    print("Ingrese los datos de los alumnos de la primera catedra: ")
    nombre_catedra = input("Ingrese el nombre del primer alumno: ")
    apellido_catedra = input("Ingrese el apellido del primer alumno: ")
    padron_catedra = int(input("Ingrese el padron del primer alumno: "))
    nota_final_catedra = int(input("Ingrese la nota final del primer alumno: "))

    ## Inicializo variables. La primera nota leida es el maximo y minimo en la catedra, y la minima nota leida de todas hasta ahora
    suma_notas_por_catedra += nota_final_catedra
    nota_max_por_catedra = nota_final_catedra
    nota_min_por_catedra = nota_final_catedra
    padron_alumno_nota_max_por_catedra = padron_catedra
    cant_alumnos_por_catedra += 1
    nota_min_total_catedras = nota_final_catedra  

    ### PREGUNTO POR EL NOMBRE DEL PROXIMO ALUMNO PARA VER SI ENTRA A LA CONDICION DEL WHILE MAS INTERNO
    if (hay_mas_catedras == "Si" or hay_mas_catedras == "si"):
        nombre_catedra = input("Ingrese el nombre del proximo alumno o presione Enter para terminar con esta catedra: ")
    else:
        print("Ya no hay mas catedras.")


    while (hay_mas_catedras == "Si" or hay_mas_catedras == "si"):

        ### OPERACIONES SOBRE EL WHILE INTERNO (UNICA CATEDRA)
        while (nombre_catedra != ""):
            apellido_catedra = input("Ingrese el apellido del alumno: ")
            padron_catedra = int(input("Ingrese el padron del alumno: "))
            nota_final_catedra = int(input("Ingrese la nota final del alumno: "))

            if nota_final_catedra > nota_max_por_catedra:
                nota_max_por_catedra = nota_final_catedra
                padron_alumno_nota_max_por_catedra = padron_catedra
            elif nota_final_catedra < nota_min_por_catedra:
                nota_min_por_catedra = nota_final_catedra

            suma_notas_por_catedra += nota_final_catedra
            cant_alumnos_por_catedra += 1
            nombre_catedra = input("Ingrese el nombre del proximo alumno de esta catedra o presione Enter para pasar a otra catedra: ")

        if cant_alumnos_por_catedra != 0: 
            prom_por_catedra = suma_notas_por_catedra / cant_alumnos_por_catedra
            print("La nota mas alta de esta catedra es", nota_max_por_catedra, "y pertenece al alumno de padron ",padron_alumno_nota_max_por_catedra)
        else:
            print("No se ingresaron alumnos en esta catedra")
            prom_por_catedra = 0

        num_catedra += 1

        ### OPERACIONES SOBRE EL WHILE EXTERNO (TODAS LAS CATEDRAS)
        if (nota_min_por_catedra < nota_min_total_catedras):  ### SE ESTABLECE EL "MINIMO ABSOLUTO" DE TODAS LAS CATEDRAS
            nota_min_total_catedras = nota_min_por_catedra    

        if prom_por_catedra > prom_max_total_catedras:        ### SE ESTABLECE EL "PROMEDIO MAYOR DE CATEDRAS" DE TODAS LAS CATEDRAS. 
            prom_max_total_catedras = prom_por_catedra        ### TAMBIEN PONGO EL NUMERO DE ESTA CATEDRA CON MAYOR PROMEDIO HASTA AHORA                                        
            num_catedra_de_mayor_prom = num_catedra            

        cant_alumnos_total += cant_alumnos_por_catedra


        ### EMPIEZA UNA NUEVA CATEDRA
        print("*---------------------NUEVA CATEDRA---------------------*")
        cant_alumnos_por_catedra = 0
        suma_notas_por_catedra = 0        
        nota_max_por_catedra = 0         ### REINICIO EL VALOR DE LAS VARIABLES PARA LEER LOS DATOS DE LA PROXIMA CATEDRA
        prom_por_catedra = 0
        padron_alumno_nota_max_por_catedra = 0

        hay_mas_catedras = input("¿Hay mas catedras? Ingrese 'Si' o 'si' si es así. Si no, ingrese cualquier otra cosa: ")
        if (hay_mas_catedras == "Si" or hay_mas_catedras == "si"):
            print("Ingrese los datos de los alumnos de la proxima catedra: ")
            nombre_catedra = input("Ingrese el nombre del primer alumno de la nueva catedra o presione Enter para terminar con la catedra: ")
        else:
            print("Ya no hay mas catedras.")
        

    print("*--------------------RESULTADOS--------------------*")

    print("La nota mas baja de todos los cursos es: ", nota_min_total_catedras)     
    print("El promedio mas grande de todas las catedras es:",prom_max_total_catedras, ", y lo obtuvo la catedra:",num_catedra_de_mayor_prom)
    print("La cantidad total de alumnos en todas las catedras es: ", cant_alumnos_total) 


main()