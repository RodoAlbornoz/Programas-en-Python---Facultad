### Escribir una función que reciba una cantidad de iteraciones de una tirada de 2 dados a realizar y devuelva la cantidad 
### de veces que se observa cada valor de la suma de los dos dados.
### Nota: utilizar el módulo random para obtener tiradas aleatorias.

import random

def contar_resultados_dados(n: int) -> dict:
    '''
    PRE CONDICIONES: Un numero entero que es la cantidad de iteraciones
    POST CONDICIONES: Un diccionario con la cantidad de veces que salió un valor (Suma de valores de 2 dados) en una iteracion
    '''
    
    diccionario_tiradas = dict()

    for i in range(n):
        dado_aleatorio_1 = random.randint(1, 6)
        dado_aleatorio_2 = random.randint(1, 6)

        suma_dados = dado_aleatorio_1 + dado_aleatorio_2

        ## Si el valor de la suma no salió previamente, lo inicializo.
        if suma_dados not in diccionario_tiradas:
            diccionario_tiradas[suma_dados] = 0

        diccionario_tiradas[suma_dados] += 1

        ## "Reinicio" el valor de los dados
        dado_aleatorio_1 = 0
        dado_aleatorio_2 = 0

    return diccionario_tiradas