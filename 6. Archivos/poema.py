'''
Se pide hacer un programa que abra un archivo de texto llamado entrada.txt el mismo contiene el siguiente poema de Ruben Dario:

"Señora, Amor es violento,
y cuando nos transfigura
nos enciende el pensamiento
la locura.
No pidas paz a mis brazos
que a los tuyos tienen presos:
son de guerra mis abrazos
y son de incendio mis besos;
y sería vano intento
el tornar mi mente obscura
si me enciende el pensamiento
la locura.
Clara está la mente mía
de llamas de amor, señora,
como la tienda del día
o el palacio de la aurora.
Y el perfume de tu ungüento
te persigue mi ventura,
y me enciende el pensamiento
la locura.
Mi gozo tu paladar
rico panal conceptúa,
como en el santo Cantar:
Mel et lac sub lingua tua*.
La delicia de tu aliento
en tan fino vaso apura,
y me enciende el pensamiento
la locura."

Y permita al usuario poder buscar palabras. Si las mismas se encuentran deberá:
a- indicar cuántas veces aparece y en qué línea del poema está.
b- copiar la línea a un archivo llamado salida.txt
'''

def buscar_palabra(palabra_usuario: str, archivo_entrada: str, archivo_salida: str) -> None:
    '''
    PRE CONDICIONES: 3 cadenas: Una, la palabra insertada por el usuario; La segunda: El nombre del archivo de entrada, 
    determinado por el usuario; La tercera: El nombre del archivo de salida, tambien determinado por el usuario
    POST CONDICIONES: Una impresion por pantalla que dice la cantidad de veces que aparece la palabra, en qué lineas, y
    una escritura en el archivo de salida de las lineas en las que aparece la palabra.
    '''

    num_lineas_aparicion = []
    palabras_por_linea = []

    ## Como el poema contiene caracteres extras que pueden complicarme para buscar la palabra, los meto en un string para eliminarlos luego.
    caracteres_a_eliminar = ".*:;,\n"
    cant_caracteres_a_eliminar = len(caracteres_a_eliminar)
    
    cant_apariciones_palabra = 0
    num_linea = 0

    with open(archivo_entrada, "r") as archivo_entrada:

        with open(archivo_salida, "w") as archivo_salida:

            for linea_entrada in archivo_entrada:
                linea_entrada.strip()
                num_linea += 1

                ## En cada linea, reemplazo los caracteres a eliminar por caracteres vacios.
                for i in range(cant_caracteres_a_eliminar):
                    linea_entrada = linea_entrada.replace(caracteres_a_eliminar[i], "")

                ## En la lista palabras_por_linea, meto las palabras de la linea leida, separadas por espacios.
                palabras_por_linea = linea_entrada.split(" ")

                for palabra in palabras_por_linea:
                    if palabra == palabra_usuario:
                        cant_apariciones_palabra += 1
                        ## Meto el numero de linea en que apareció la palabra en la lista num_lineas_aparicion
                        num_lineas_aparicion.append(num_linea)

                        linea_de_salida = linea_entrada + "\n"
                        archivo_salida.write(linea_de_salida)

            print("La palabra aparece", cant_apariciones_palabra, "veces, en las lineas:", end=" ")
            for i in range(cant_apariciones_palabra):
                ## Imprimo las lineas en que aparece la palabra
                print(num_lineas_aparicion[i], end = ", ")


def main() -> None:

    archivo_entrada = "entrada.txt"
    archivo_salida = "salida.txt"

    palabra = input("Ingrese una palabra a buscar en el poema: ")

    buscar_palabra(palabra, archivo_entrada, archivo_salida)

main()