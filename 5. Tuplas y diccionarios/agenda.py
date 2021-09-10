### Escribir un programa que vaya solicitando al usuario que ingrese nombres.
### Si el nombre se encuentra en la agenda (implementada con un diccionario), debe mostrar el teléfono y, 
### opcionalmente, permitir modificarlo si no es correcto.
### Si el nombre no se encuentra, debe permitir ingresar el teléfono correspondiente.
### El usuario puede utilizar la cadena ”*”, para salir del programa.

### Algunas aclaraciones:
### No se agrega la persona a la agenda si el número ingresado es vacío.
### De la misma forma, no se modifica el número si el nuevo número ingresado es vacío.
### Hay un enter (\n) entre cada iteración que no se muestra en la pantalla de resultados

def agenda():

    ## Defino el telefono como un string para considerar el caso en que sea vacío.
    telefono_persona = ""
    dic_nombres_agenda = dict()

    nombre_agenda = input("Ingrese un nombre, o * para salir: ")

    ## dic_nombres_agenda[nombre_agenda]: Telefono correspondiente a la persona nombre_agenda
    while nombre_agenda != "*":
        if nombre_agenda not in dic_nombres_agenda:
            print("Persona no agendada")
            telefono_persona = input("Ingrese el telefono para {}: ".format(nombre_agenda))

            if telefono_persona != "":
                dic_nombres_agenda[nombre_agenda] = telefono_persona
                print("Nuevo telefono registrado para {}: {}".format(nombre_agenda, telefono_persona))

            print()

        else:
            print("Telefono de", nombre_agenda,"es",dic_nombres_agenda[nombre_agenda])
            telefono_persona = input("Ingrese el nuevo telefono para {}: ".format(nombre_agenda))

            if telefono_persona != "":
                dic_nombres_agenda[nombre_agenda] = telefono_persona
                print("Telefono actualizado para {}: {}".format(nombre_agenda, dic_nombres_agenda[nombre_agenda]))

            print()
       
        nombre_agenda = input("Ingrese un nombre, o * para salir: ")

agenda()