#Ejercicio 1
def ej1():
    nombre_archivo = 'tabla-n.txt'
    num = int(input("Escribe un numero entre 1 y 10: "))

    if not (0 < num < 10):
        print("Por favor pasa un numero entre 1 y 10")
    try:
        with open(nombre_archivo, 'w') as archivo:
            #Tabla de multiplicacion
            for x in range(1, 10):
                archivo.write(f"{num}x{x} = {num*x}\n")
    except IOError:
        print(f"No se pudo abrir el archivo '{nombre_archivo}'.")


#Ejercicio 2
def ej2():
    nombre_archivo = 'tabla-n.txt'

    #Crear tabla de mult
    ej1() 

    #Leer la tabla
    try:
        with open(nombre_archivo, 'r') as archivo:
            for linea in archivo:
                print(linea, end='')
    except FileNotFoundError:
        print(f"El archivo '{nombre_archivo}' no fue encontrado.")
    except IOError:
        print(f"No se pudo abrir el archivo '{nombre_archivo}'.")


#Ejercicio 3
def ej3():
    nombre_archivo = 'tabla-n.txt'

    #Crear tabla de mult
    ej1()

    #Leer una linea especifica
    m = int(input("Escribe la linea a leer: "))
    try:
        with open(nombre_archivo, 'r') as archivo:
            contenido = archivo.readlines()
            print(contenido[m-1])

    except FileNotFoundError:
        print(f"El archivo '{nombre_archivo}' no fue encontrado.")
    except IOError:
        print(f"No se pudo abrir el archivo '{nombre_archivo}'.")


#Ejercicio 4
def ej4():
    nombre_archivo = 'listin.txt'

    def consultar_telefono():
        cli = input("Nombre del cliente: ")
        with open(nombre_archivo, 'r') as archivo:
            for linea in archivo:
                contenido = linea.split(',')
                if cli == contenido[0]:
                    print(f"\nTelefono --> {contenido[1]}")
                    input()
                    break
            else:
                print("\nCliente no encontrado")
                input()
    

    def añadir_telefono():
        cli = input("Nombre del cliente: ")
        tel = input("Telefono: ")
        with open(nombre_archivo, 'a') as archivo:
            archivo.write(f"{cli},{tel}\n")


    def eliminar_cliente():
        cli = input("Nombre del cliente: ")
        with open(nombre_archivo, 'r') as archivo:
            lineas = archivo.readlines()

        # Filtrar las líneas para eliminar la que contiene el nombre buscado
        lineas_actualizadas = [linea for linea in lineas if not linea.startswith(cli + ',')]

        # Escribir las líneas actualizadas de nuevo en el archivo
        with open(nombre_archivo, 'w') as archivo:
            archivo.writelines(lineas_actualizadas)

    while True:
        print("Gestion de telefonos:")
        print("1) Consultar telefono")
        print("2) Añadir telefono")
        print("3) Eliminar cliente")
        print("4) Exit")

        opcion = input("Ingresa la operacion: ")
        try:
            if opcion == '1': consultar_telefono()
            elif opcion == '2': añadir_telefono()
            elif opcion == '3': eliminar_cliente()
            else: break
        except FileNotFoundError:
            print(f"El archivo '{nombre_archivo}' no fue encontrado.")
        except IOError:
            print(f"No se pudo abrir el archivo '{nombre_archivo}'.")

ej4()