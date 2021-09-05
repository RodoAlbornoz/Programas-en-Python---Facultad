
def main() -> None:
    numero = int(input("Ingrese el numero para calcular su factorial: "))
    factorial = 1

    if numero == 0 or numero == 1:
        print("El resultado del factorial es 1")
    elif numero > 1:
        while numero > 1:
            factorial *= numero
            numero -= 1
        print("El resultado del factorial es: ", factorial)

main