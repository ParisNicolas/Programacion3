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
        

    def actualizar_informacion(self):
        campos = ["nombre", "edad", "posicion", "equipo", "pais", "numero", "goles","asistencias", "amarillas", "rojas", "premios"]
        campos_estadisticas = ["goles","asistencias", "amarillas", "rojas"]
        obj = {}
        print("Complete el formulario para actualizar los datos del jugador:")
        for campo in campos:
            entrada = input(campo+": ")
            if entrada != "":
                obj[campo] = entrada
        if "premios" in obj: 
            obj["premios"] = obj["premios"].split(" ")
        for key, value in obj.items():
            if key in campos_estadisticas:
                self.estadisticas[key] = int(value)
            else:
                setattr(self, key, value)

    
    def calcular_promedio_goles(self):
        return self.estadisticas["goles"]/5 #Suponiendo que jugo 5 partidos (falta ese atributo)

    def es_goleador(self):
        return (self.estadisticas["goles"]>20) #Goleador si tiene mas de 20
    
    def agregar_premio(self, premio):
        self.premios.append(premio)

    def eliminar_premio(self, premio):
        if premio not in self.premios:
            print("El premio no existe")
        else:
            self.premios.remove(premio) 

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

while True:
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
        if jugadorN > len(jugadores)-1:
            print("\nLongitud erronea")
            break
        jugador = jugadores[jugadorN]


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
            {"goles":obj["goles"], 
             "asistencias": obj["asistencias"],
             "amarillas": obj["amarillas"], 
             "rojas": obj["rojas"]}, 
            obj["premios"])
        )
    elif option == "2":
        jugador.mostrar_informacion()
    elif option == "3":
        jugador.actualizar_informacion()
    elif option == "4":
        print(f"Pomedio de goles de {jugador.nombre} es {jugador.calcular_promedio_goles()}")
    elif option == "5":
        goleador = jugador.es_goleador()
        if goleador:
            print("El jugador es goleador")
        else:
            print("El jugador no es un goleador")
    elif option == "6":
        nuevo_premio = input("Ingresa el premio que quieres agregar: ")
        jugador.agregar_premio(nuevo_premio)
    elif option == "7":
        premio_viejo = input("Ingresa el premio que quieres eliminar: ")
        jugador.eliminar_premio(premio_viejo)

    input("\nToque cualquier tecla para continuar ...")

