#DIVICION POR CERO 
def ej1():
    print("Divicion de numeros:")
    n1 = int(input("Digite numero 1: "))
    n2 = int(input("Digite numero 2: "))
    try:
        print("Resultado:",n1/n2)
    except ZeroDivisionError:
        #Dando advertencia al usuario
        print("Apa no quieras romper el programa que dividir por cero es peligroso")
        print("Resultado: No Existe")
    finally:
        print()



#TIPO DE DATO INCORRECTO
def ej2():
    #Conversión de Tipo de Datos
    try:
        n = int(input("Digite un numero: "))
        print(f"El numero es \"{n}\"")
    except ValueError:
        #Se reniega al usuario, que habeces le falla
        print("Disculpa amigo pero eso no es un numero")
        print("Por favor ingresa un numero valido")



#ACCESO A UN ÍNDICE FUERA DE RANGO
def ej3():
    #Acceso a un Índice Fuera de Rango
    lista = []
    try:
        index = int(input("Extraer valor: "))
        print(lista[index])
    except IndexError:
        print(f"El elemento en la posicion {index} no existe")
        print("Vuelve a intentarlo")


#OPERACIONES CON TIPO DE DATO INCORRECTO
def ej4():
    def potencia(n, exp):
        try:
            res = n**exp
        except TypeError:
            print("Al parecer los datos son incorrectos")
        else:
            return res

    print("Elevar un nunero")
    n = int(input("Ingrese un numero: "))
    exp = int(input("Ingrese el exponente: "))
    print(potencia(n, exp))



while True:
    ejs = [ej1, ej2, ej3]
    n = int(input("Elige el ejercicio 1-4: "))
    try:
        ejs[n-1]()
    except IndexError:
        print(f"La funcion {n} no existe")
        print("Vuelve a intentarlo")
    print()