### Escribir una función que reciba una cadena y devuelva un diccionario con la cantidad de apariciones de cada palabra 
### en la cadena. 
### Por ejemplo, si recibe ”Qué lindo día que hace hoy” debe devolver { 'qué': 2, 'lindo': 1, 'día': 1, 'hace': 1, 'hoy': 1}.

def contar_palabras(cadena: str) -> dict:

    longitud_cadena = len(cadena)
    diccionario_palabras = dict()

    palabra_actual = ""
    palabras = []
    
    for i in range(longitud_cadena):
        if cadena[i] != " ":
            palabra_actual += cadena[i].lower()
        else:
            ## Al leer un espacio, leo la proxima palabra, y la que ya tenía, la guardo.
            palabras.append(palabra_actual)
            palabra_actual = ""

    ## La ultima palabra no está incluida en el if/else al no haber espacio en el caracter final, asi que lo incluyo acá.
    palabras.append(palabra_actual)

    for i in range(len(palabras)):
        
        ## La llave de la palabra guarda como valor la cantidad de veces que aparece la palabra en la lista.
        palabra_en_cadena = palabras[i]
        diccionario_palabras[palabra_en_cadena] = palabras.count(palabra_en_cadena)

    ## Si se insertó una cadena vacía, el diccionario no contiene nada.
    if longitud_cadena == 0:
        diccionario_palabras = {}

    return diccionario_palabras