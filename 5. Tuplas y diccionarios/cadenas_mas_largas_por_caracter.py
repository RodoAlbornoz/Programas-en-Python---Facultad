### Escribir una función que reciba un texto y para cada caracter presente en el texto devuelva la cadena más 
### larga en la que se encuentra ese caracter.
### En el caso de que haya más de una cadena posible para elegir, se debe seleccionar la última.


def obtener_cadenas_largas_por_caracter(texto: str) -> dict:
    '''
    PRE CONDICIONES: Una cadena de caracteres
    POST CONDICIONES: Un diccionario que tiene como llave cada caracter que hay en la cadena, y como valor la palabra mas larga
    de la cadena que contiene a ese caracter.
    '''

    cant_caracteres = len(texto)
    diccionario_palabras_largas = dict()

    ### Por cada caracter de la cadena texto, analizo las palabras de la cadena que la contienen
    for i in range(cant_caracteres):
        ### Variables para analizar cada palabra del texto
        palabra_actual = ""
        cant_caracteres_palabra_actual = -1  ## Nota: Lo empiezo en -1, porque dentro del if, cuando una palabra contiene al caracter que leimos, sumamos por 1, 2 veces,
        contiene_caracter = False            ##       por lo que al final se tendria que la palabra actual leida con el caracter tiene 1 caracter (El leido)
        palabras_con_el_caracter = []

        ### Si el caracter no es un espacio, realizo todo el proceso
        if texto[i].lower() != " ":
            caracter_actual = texto[i].lower()

            for j in range(cant_caracteres):
            ### Si una palabra del la cadena texto tiene al caracter, lo consideramos, y cuando se termina de leer la palabra, lo guardamos. 
                if texto[j].lower() == texto[i].lower():
                    contiene_caracter = True
                    cant_caracteres_palabra_actual += 1

                elif texto[j].lower() == " ":
                    if contiene_caracter:
                        palabras_con_el_caracter.append((palabra_actual, cant_caracteres_palabra_actual))
            
                    ### "Reiniciamos" la palabra            
                    contiene_caracter = False
                    palabra_actual = ""
                    cant_caracteres_palabra_actual = 0

                palabra_actual += texto[j].lower()
                cant_caracteres_palabra_actual += 1

                ### Para la ultima palabra, si contiene al caracter, la considero en el analisis
                if contiene_caracter:
                    palabras_con_el_caracter.append((palabra_actual, cant_caracteres_palabra_actual))

            ### Variables para decidir la cadena mas larga que contiene el caracter
            cant_palabras_con_caracter = len(palabras_con_el_caracter)
            caracteres_cadena_mas_larga = 0
            cadena_mas_larga = ""
        
            for k in range(cant_palabras_con_caracter):
                ## Si la cantidad de caracteres de una palabra que contiene al caracter, es mayor a la cantidad de caracteres
                ## de la cadena mas larga, la palabra leida que contiene al caracter es la nueva cadena mas larga con el caracter.
                if palabras_con_el_caracter[k][1] > caracteres_cadena_mas_larga:
                    cadena_mas_larga = palabras_con_el_caracter[k][0]
                    caracteres_cadena_mas_larga = palabras_con_el_caracter[k][1]
                ### Si 2 palabras tienen igual cantidad de caracteres, considero la ultima
                elif palabras_con_el_caracter[k][1] == caracteres_cadena_mas_larga:
                    cadena_mas_larga = palabras_con_el_caracter[k][0]
                    caracteres_cadena_mas_larga = palabras_con_el_caracter[k][1]

            diccionario_palabras_largas[caracter_actual] = cadena_mas_larga

    return diccionario_palabras_largas