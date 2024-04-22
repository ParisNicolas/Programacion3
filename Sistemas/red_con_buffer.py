import time
import random

class Node:
    def __init__(self, tipo = "cliente", nombre="Annonimous"):
        self.tipo = tipo
        self.conecciones = []
        self.buffer = []
        self.nombre = nombre

    def agregar_conexion(self, host, primeraConexion = True):
        if primeraConexion:
            host.agregar_conexion(self, False)
            print(f"Nuevo dispositivo: {host.nombre}")
        self.conecciones.append(host)

    def enviar_mensaje(self, msg):
        for host in self.conecciones:
            
            host.recibir_mensaje(msg, self.nombre, self.tipo)
    
    def recibir_mensaje(self, msg, nombre, tipo):
        print(f"[{self.nombre}] Mensaje recivido de {nombre} ({tipo}): {msg}")

    def eliminar_conexion(self, host, primeraConexion = True):
        if primeraConexion:
            host.eliminar_conexion(self, False)
            print(f"Se ha perdido la coneccion con {host.nombre}")
        self.conecciones.remove(host)

    def procesar_buffer(self):
        pass
        
            

#Crear instancias
Usuario1 = Node("cliente", "Pepe")
Usuario2 = Node("cliente", "Carlos")
Usuario3 = Node("cliente", "Juancho")

Servidor = Node("servidor", "Mister")

#Crear conecciones
Servidor.agregar_conexion(Usuario1)
Servidor.agregar_conexion(Usuario2)
Servidor.agregar_conexion(Usuario3)

#Enviar mensaje
Servidor.enviar_mensaje("Hola mundoooo!!!☺")

#Simular desconeccion y reconeccion
print("Simulando desconexión y reconexión dinámica…")
Servidor.eliminar_conexion(Usuario1)
time.sleep(2.5)
Servidor.agregar_conexion(Usuario1)
print("¡Hola de nuevo a todos!")