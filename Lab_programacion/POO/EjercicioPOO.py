# Encapsulamiento: Se asegura de que los atributos de la clase no se puedan modificar directamente desde fuera de la clase.
class Vehiculo():
    def __init__(self, marca, modelo, año):
        self.__marca = marca  # Atributo encapsulado
        self.__modelo = modelo  # Atributo encapsulado
        self.__año = año  # Atributo encapsulado

    # Métodos para acceder y modificar los atributos privados
    def get_marca(self):
        return self.__marca

    def set_marca(self, marca):
        self.__marca = marca

    def get_modelo(self):
        return self.__modelo

    def set_modelo(self, modelo):
        self.__modelo = modelo

    def get_año(self):
        return self.__año

    def set_año(self, año):
        self.__año = año

    # Método de instancia
    def detener(self):
        print(f"El vehiculo {self.get_marca()} {self.get_modelo()} se detiene.")

# Herencia: Auto hereda de Vehiculo
class Auto(Vehiculo):
    def __init__(self, marca, modelo, año, puertas):
        super().__init__(marca, modelo, año)  # Hereda atributos de Vehiculo
        self.__puertas = puertas  # Atributo encapsulado

    # Métodos para acceder y modificar los atributos privados
    def get_puertas(self):
        return self.__puertas

    def set_puertas(self, puertas):
        self.__puertas = puertas

    def acelerar(self):
        print(f"El auto {self.get_marca()} {self.get_modelo()} está acelerando.")

    # Polimorfismo: Sobrescribe el método detener de la clase base
    def detener(self):
        print(f"El auto {self.get_marca()} {self.get_modelo()} se detiene.")

# Herencia: Motocicleta hereda de Vehiculo
class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, año, cilindrada):
        super().__init__(marca, modelo, año)  # Hereda atributos de Vehiculo
        self.__cilindrada = cilindrada  # Atributo encapsulado

    # Métodos para acceder y modificar los atributos privados
    def get_cilindrada(self):
        return self.__cilindrada

    def set_cilindrada(self, cilindrada):
        self.__cilindrada = cilindrada

    def acelerar(self):
        print(f"La motocicleta {self.get_marca()} {self.get_modelo()} con cilindrada de {self.get_cilindrada()}cc está acelerando.")

    # Polimorfismo: Sobrescribe el método acelerar y detener de la clase base
    def detener(self):
        print(f"La motocicleta {self.get_marca()} {self.get_modelo()} se detiene.")

# Herencia: Camion hereda de Vehiculo
class Camion(Vehiculo):
    def __init__(self, marca, modelo, año, capacidad_carga):
        super().__init__(marca, modelo, año)  # Hereda atributos de Vehiculo
        self.__capacidad_carga = capacidad_carga  # Atributo encapsulado

    # Métodos para acceder y modificar los atributos privados
    def get_capacidad_carga(self):
        return self.__capacidad_carga

    def set_capacidad_carga(self, capacidad_carga):
        self.__capacidad_carga = capacidad_carga

    def acelerar(self):
        print(f"El camion {self.get_marca()} {self.get_modelo()} con capacidad de carga de {self.get_capacidad_carga()}kg está acelerando.")

    # Polimorfismo: Sobrescribe el método acelerar y detener de la clase base
    def detener(self):
        print(f"El camion {self.get_marca()} {self.get_modelo()} se detiene.")



if __name__ == "__main__":
    vehiculos = {
        "Corolla": Auto("Toyota", "Corolla", 2020, 4),
        "MT-07": Motocicleta("Yamaha", "MT-07", 2019, 689),
        "Actroz": Camion("Mercedes-Benz", "Actroz", 2015, 2000)
    }

    #Simplificacion y abstracion con las clases previas
    for vehiculo in vehiculos.values():
        vehiculo.acelerar()  # Llamada al método polimórfico
        vehiculo.detener()  # Llamada al método polimórfico


# Para mejorar este codigo e incluir mas tipos de vehiculos 
# sin tener que definir una clase nueva para cada vehiculo se podria
# hacer uso de los **kwards
# con esto se puede generalizar y acceder a las propiedades especiales de cada vehiculo
# con solo un metodo especial que recive la clave u nombre de la propiedad