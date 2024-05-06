#Divicion por cero 
class TP5:
    def ejecutar(self, ejercicio):
        while True:
            if ejercicio == 1: self.ej1()
            if ejercicio == 2: self.ej2()
            if ejercicio == 3: self.ej3()
            if ejercicio == 4: self.ej1()
                

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

    def ej2():
        #Conversión de Tipo de Datos
        try:
            n = int(input("Digite un numero: "))
            print(f"El numero es \"{n}\"")
        except ValueError:
            #Se reniega al usuario, que habeces le falla
            print("Disculpa amigo pero eso no es un numero")
            print("Por favor ingresa un numero valido")

    def ej3():
        #Acceso a un Índice Fuera de Rango
        lista = []
        try:
            index = int(input("Extraer valor: "))
            print(lista[index])
        except IndexError:
            print(f"El elemento en la posicion {index} no existe")
            print("Vuelve a intentarlo")

