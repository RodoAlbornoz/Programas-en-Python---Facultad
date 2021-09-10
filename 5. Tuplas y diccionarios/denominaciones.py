### Escriba una función que dada una lista de denominaciones de billetes de la moneda corriente de un país, permita 
### descomponer un importe otorgado por el usuario en las cantidades correspondientes a cada una de las denominaciones 
### cual si fuera un cajero automático y suponiendo que siempre elige otorgar billetes del mayor valor posible. La 
### función debe controlar que el importe sea factible de ser descompuesto y devolver un diccionario con la descomposición.    
### Ej: 
### Lista = [10,20,50,100,200,500,1000]  
### Valor = 1690  
### Diccionario = {10:0,20:2,50:1;100:1;200:0;500:1;1000:1}

def billetes(denominaciones: list, importe: int) -> dict:
    '''
    PRE CONDICIONES: Una lista que contiene las denominaciones, y un valor entero positivo del importe
    POST CONDICIONES: Un diccionario con la denominacion como llave y la cantidad como valor.
    '''
    
    cant_denominaciones = len(denominaciones)
    dic_importes = {}
    ## Valor para determinar la denominacion a partir de la posicion, desde 0 hasta i.
    i = cant_denominaciones - 1

    while importe != 0:
        ## Se toma el valor de la denominacion del mas grande al mas chico. Se guarda en un diccionario la cantidad de billetes
        ## correspondientes a una denominacion. Finalmente Nos quedamos con el resto de dividir el importe por la denominacion.
        cant_de_denominacion = importe // denominaciones[i]
        dic_importes[denominaciones[i]] = cant_de_denominacion
        importe = (importe % denominaciones[i])
        i -= 1

    return dic_importes