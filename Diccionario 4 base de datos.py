print("Bienvenido a la base de datos de los clientes de Freddo\n")
# Creamos el diccionario principal
clientes = {}

# Mostramos el menu al usuario y creamos bucle para permitir multiples acciones
while True:
    menu = int(input("""Que desea hacer:
1) Añadir un nuevo cliente
2) Eliminar un cliente
3) Mostrar datos de un cliente
4) Mostrar lista de los clientes existentes
5) Mostrar lista de clientes preferentes
6) Terminar el programa\n"""))
# Creamos el diccionario secundario con los datos personales
    if menu == 1:
        nuevo_cliente = {}
        nif = input("Ingrese el NIF del nuevo cliente: ")
        nuevo_cliente["Nombre"] = input("Ingrese nombre del cliente: ")
        nuevo_cliente["Direccion"] = input("Ingrese dirección del cliente: ")
        nuevo_cliente["Correo"] = input("Ingrese correo eléctronico: ")
        nuevo_cliente["Telefono"] = input("Ingrese teléfono del cliente: ")
        preferente = int(input("""Es un cliente preferente?
1) Si
2) No\n"""))
# Preguntamos si es preferente y lo añadimos al diccionario principal
        if preferente == 1:
            nuevo_cliente["Preferente"] = True

            clientes[nif] = nuevo_cliente
            print("El cliente ha sido añadido satisfactoriamente\n")
            print("\nDesea realizar algo más?\n")
        else:
            nuevo_cliente["Preferente"] = False

            clientes[nif] = nuevo_cliente
            print("El cliente ha sido añadido satisfactoriamente\n")
            print("Desea realizar algo más?\n")
# Pedimos el dato del cliente a eliminar y lo sacamos del diccionario principal, si pone un cliente no existente preguntamos de vuelta
    elif menu == 2:
        while True:
            try:
                eliminar = input(
                    "Ingrese el NIF del cliente que desea eliminar: ")
                clientes.pop(eliminar)
                print(
                    f"El cliente del NIF {eliminar} se ha eliminado satisfactoriamente")
                menu_2 = int(input("""Desea eliminar otro cliente?:
1)Si
2)No\n"""))
                if menu_2 == 2:
                    print("Desea realizar algo más?\n")
                    break

            except KeyError:
                print("Ha introducido un cliente no existente/válido")
                menu_3 = int(input("""Desea intentar nuevamente?:
1)Si
2)No"""))
                if menu_3 == 2:
                    print("Desea realizar algo más?\n")
                    break
# Pedimos el dato del cliente que se quiere consultar y se muestra en pantalla
    elif menu == 3:
        while True:
            mostrar_1 = input(
                "Ingrese el NIF del cliente que quiere consultar: ")
            print("\n")
            print("Nombre: ", clientes[mostrar_1]["Nombre"].title(), end="\n")
            print("Dirección: ", clientes[mostrar_1]["Direccion"], end="\n")
            print("Correo: ", clientes[mostrar_1]["Correo"], end="\n")
            print("Teléfono: ", clientes[mostrar_1]["Telefono"], end="\n")

            i = clientes[mostrar_1]["Preferente"]
            if i == True:
                print("Es un cliente preferente")
            else:
                print("No es un cliente preferente")

            menu_4 = int(input("""\nDesea consultar otro cliente?:
1)Si
2)No\n"""))
            if menu_4 == 2:
                print("Desea realizar algo más?\n")
                break
# Con el bucle imprimimos la lista de los nombres de los clientes
    elif menu == 4:

        for nif in clientes:
            print(clientes[nif]["Nombre"].title())

        print("\nDesea realizar algo más?\n")
# Con el bucle identificamos si se trata de un cliente preferente y en ese caso, lo imprimimos en pantalla
    elif menu == 5:
        print("Los clientes preferentes son: \n")
        for nif in clientes:
            i = clientes[nif]["Preferente"]

            if i == True:
                print("- ", end="")
                print(clientes[nif]["Nombre"].title())

            print("\nDesea realizar algo más?\n")
# Si desea terminar, nos despedimos del cliente y salimos del bucle
    else:
        print("Hasta luego, vuelva pronto")
        break
