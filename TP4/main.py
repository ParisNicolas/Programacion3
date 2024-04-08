class JugadorFutbol:
    def __init__(self, nombre, edad, posicion, equipo, pais, numero, estadisticas, premios):
        self.nombre = nombre
        self.edad = edad
        self.posicion = posicion
        self.equipo = equipo
        self.pais = pais
        self.numero = numero
        self.estadisticas = estadisticas
        self.premios = premios

    def mostrar_informacion(self):
        print("\nData del jugador")
        print("Nombre:", self.nombre)
        print("Edad:", self.edad)
        print("Posicion en el campo:", self.posicion)
        print("Equipo:", self.equipo)
        print("Pais:", self.pais)
        print("Numero de camiseta:", self.numero)
        print("Estadisticas:", self.estadisticas)
        print("Premios:", self.premios)
        print()


    def actualizar_informacion(self):
       print(self)
    
    def calcular_promedio_goles(self):
        self.estadisticas.goles

    def es_goleador():
        pass
    
    def agregar_premio():
        pass

    def eliminar_premio():
        pass

Jugador1 = JugadorFutbol(
    "pepe",25,"Delantero","River","Argentina",10,
    {"goles": 20, "asistencias":6, "amarillas":50, "rojas":10},
    ["Copa America", "Mayor goleador"]
    )

Jugador2 = JugadorFutbol(
    "Marcos",19,"Defensor","PSG","Francia",14,
    {"goles": 4, "asistencias":2, "amarillas":30, "rojas":4},
    []
    )

jugadores = [Jugador1,Jugador2]


print()
print("Elige que operacion quieres realizar:")
print("\t1. Nuevo jugador de futbol")
print("\t2. Mostrar info de un jugador")
print("\t3. Actualizar info de un jugador")
print("\t4. Calcular prom. de goles por partido de un jugador")
print("\t5. Verificar si un jugador es goleador")
print("\t6. Agregar un premio a un jugador")
print("\t7. Eliminar un premio de un jugador")
print()
option = input("Introduzca un numero:")

if option != "1":
    jugadorN = int(input(f"Elige un jugador(total {len(jugadores)}):"))-1

if option == "1":
    campos = ["nombre", "edad", "posicion", "equipo", "pais", "numero", "goles","asistencias", "amarillas", "rojas", "premios"]
    obj = {}
    print("Complete el formulario para crear un nuevo usuario:")
    for campo in campos:
        obj[campo] = input(campo+": ")
    obj["premios"] = obj["premios"].split(" ")

    jugadores.append(JugadorFutbol(
        obj["nombre"], 
        obj["edad"], 
        obj["posicion"], 
        obj["equipo"], 
        obj["pais"], 
        obj["numero"], 
        {obj["goles"], obj["asistencias"],obj["amarillas"],obj["rojas"]}, 
        obj["premios"])
    )
elif option == "2":
    jugadores[jugadorN].mostrar_informacion()
elif option == "3":
    jugadores[jugadorN].actualizar_informacion()
elif option == "4":
    pass
elif option == "5":
    pass
elif option == "6":
    pass
elif option == "7":
    pass