class Node:
    def __init__(self, tipo = "cliente", nombre="Annonimous"):
        self.tipo = tipo
        self.conecciones = []
        self.nombre = nombre

    
    def agregar_conexion(self, host, primeraConexion = False):
        if primeraConexion:
            self.conecciones.append(host)
            host.agregar_conexion(self)

    def enviar_mensaje(self, msg):
        for host in self.conecciones:
            host.recibir_mensaje(msg, self.nombre, self.tipo)
    
    def recibir_mensaje(self, msg, nombre, tipo):
        print(f"[{self.nombre}] Mensaje recivido de {nombre} ({tipo}): {msg}")

#Crear instancias
Usuario1 = Node("cliente", "Pepe")
Usuario2 = Node("cliente", "Carlos")
Usuario3 = Node("cliente", "Juancho")

Servidor = Node("servidor", "Mister")

#Crear conecciones
Servidor.agregar_conexion(Usuario1, True)
Servidor.agregar_conexion(Usuario2, True)
Servidor.agregar_conexion(Usuario3, True)

#Enviar mensaje
Servidor.enviar_mensaje("Hola mundoooo!!!☺")
