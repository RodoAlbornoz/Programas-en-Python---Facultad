from math import floor

def busqueda_binaria(numero_a_buscar: int, lista: list, cant_numeros_lista: int) -> int:
    '''
    Pre condiciones: Un numero entero, el numero a buscar en la lista (La cual debe estar previamente 
    ordenada), la lista que contiene los numeros y la cantidad de numeros que tiene la lista
    Post condiciones: Un numero entero positivo que da la posicion del numero buscado en la lista.
    '''

    piso = 0
    pos_numero = -1
    techo = cant_numeros_lista

    while piso <= techo:
        ## Tomo la posicion de la mitad
        pos_mitad = floor((piso + techo) / 2)
        numero_en_mitad = lista[pos_mitad]
        
        ## Si se encontró el numero, se termina el ciclo. La posición del piso se toma como 0, pero al mostrar
        ## por pantalla, se considera que la posicion del piso es 1.
        if numero_en_mitad == numero_a_buscar:
            pos_numero = pos_mitad + 1
            piso += techo

        if numero_a_buscar > numero_en_mitad:
            piso = pos_mitad + 1
        else:
            techo = pos_mitad - 1

    return pos_numero


def main() -> None:
    ## Lista de prueba
    lista = [-3, 4, 9, -1, 0, 7, 11, -2]
    lista.sort()
    cant_numeros = len(lista)

    num = int(input("Ingrese el numero a buscar: "))
    pos = busqueda_binaria(num, lista, cant_numeros)

    ### Si el numero no está en la lista, se añade el numero, se vuelve a ordenar la lista, se
    ### vuelve a realizar la busqueda binaria y se devuelve la posicion del numero añadido
    if pos != -1:
        print("El numero esta en la posicion",pos)
    else:
        print("El numero no esta en la lista")
        lista.append(num)
        lista.sort()
        cant_numeros = len(lista)
        pos = busqueda_binaria(num, lista, cant_numeros)
        print("El numero ahora está en la posicion",pos)


main()