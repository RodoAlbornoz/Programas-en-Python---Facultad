### Escribir una función que reciba una cadena de unos y ceros (es decir, un número en representación binaria) 
### y devuelva el valor decimal correspondiente.

def convertir_a_decimal(n_binario: str) -> int:
    longitud = len(n_binario)

    ### Invierto el numero binario
    binario_inverso = n_binario[::-1]

    representacion_decimal = 0

    for i in range(longitud):
        if binario_inverso[i] == "1":
            representacion_decimal += 2**i
            
    return representacion_decimal