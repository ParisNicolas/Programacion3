import time
import random

class Node:
    def __init__(self, tipo = "cliente", nombre="Annonimous"):
        self.tipo = tipo
        self.nombre = nombre
        self.conecciones = []
        self.buffer = []

    #Enlace de cliente/servidor (1ra coneccion --> Evita stackOverflow)
    #Guarda a el usuario en ambas listas connecciones
    def agregar_conexion(self, host, primeraConexion = True):
        if primeraConexion:
            host.agregar_conexion(self, False)
            print(f"Nuevo dispositivo: {host.nombre}")
        self.conecciones.append(host)

    #Agrega un mensaje a la pila
    def enviar_mensaje(self, msg):
        self.buffer.append(msg)
    
    #Recive un mensaje con probabilidad de perderlos
    def recibir_mensaje(self, msg, nombre, tipo):
        #Se pierden el 30%
        if random.random() < .70:
            print(f"[{self.nombre}] Mensaje recibido de {nombre} ({tipo}): {msg}")
            return True #Feedback
        else:
            print(f"\033[91m*ERROR [{self.nombre}] No se pudo recibir un packete de {nombre} ({tipo})\033[0m")
            return False #Feedback

    #Elimina los usuarios de ambas listas de connecines (desenlace)
    def eliminar_conexion(self, host, primeraConexion = True):
        if primeraConexion:
            host.eliminar_conexion(self, False)
            print(f"Se ha perdido la coneccion con {host.nombre}")
        self.conecciones.remove(host)

    #Procesa el envio de mensajes del buffer
    def procesar_buffer(self):
        packetes_perdidos = 0 #Cuenta los fallidos
        while len(self.buffer) > 0:
            time.sleep(1.5) #Simula retraso
            element = self.buffer.pop() #Vacia el buffer
            for host in self.conecciones:
                if not host.recibir_mensaje(element, self.nombre, self.tipo):
                    packetes_perdidos +=1
        print(f"\nSe perdieron {packetes_perdidos} packetes")

#Crear instancias
Usuario1 = Node("cliente", "Pepe")
Usuario2 = Node("cliente", "Carlos")
Usuario3 = Node("cliente", "Juancho")

Servidor = Node("servidor", "Mister")

#Crear conecciones
Servidor.agregar_conexion(Usuario1)
Servidor.agregar_conexion(Usuario2)
Servidor.agregar_conexion(Usuario3)

print()

#Enviar mensaje
Servidor.enviar_mensaje("Hola mundoooo!!!☺")
Servidor.enviar_mensaje("Como estan")
Servidor.enviar_mensaje("Pueden responderme?")
Servidor.enviar_mensaje("Esto es un mensaje de prueba")

Servidor.procesar_buffer()

print()

#Simular desconeccion y reconeccion
print("Simulando desconexión y reconexión dinámica…")
Servidor.eliminar_conexion(Usuario1)
time.sleep(2.5)
Servidor.agregar_conexion(Usuario1)
print("¡Hola de nuevo a todos!")