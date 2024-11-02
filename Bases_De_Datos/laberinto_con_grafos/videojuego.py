import py5
import time
import networkx as nx
from generar_laberinto import generar_laberinto

# Configuración inicial
n = 15  # Tamaño del laberinto (n x n)
cell_size = 40  # Tamaño de cada celda en píxeles
jugador_pos = (0, 0)  # Posición inicial del jugador
laberinto = generar_laberinto(n)
inicio = (0, 0)
salida = (n - 1, n - 1)
tiempo_inicio = time.time()
tiempo_limite = 30  # Tiempo límite de 30 segundos

def mostrar_cronometro():
    tiempo_restante = max(0, tiempo_limite - (time.time() - tiempo_inicio))
    py5.fill(0)
    py5.text_size(20)
    py5.text(f'Tiempo restante: {int(tiempo_restante)} s', 10, 30)

def setup():
    py5.size(n * cell_size, n * cell_size)  # Ajustar el tamaño de la ventana
    py5.background(255)
    py5.stroke(0)

def draw():
    py5.background(255)
    dibujar_laberinto(laberinto)
    dibujar_jugador(jugador_pos)
    mostrar_cronometro()
    dibujar_salida()  # Dibuja la salida en la pantalla

    tiempo_actual = time.time()
    if tiempo_actual - tiempo_inicio > tiempo_limite:
        mostrar_solucion()  # Mostrar solución si se vence el tiempo

def dibujar_laberinto(grafo):
    for (nodo1, nodo2) in grafo.edges():
        x1, y1 = nodo1
        x2, y2 = nodo2
        py5.line(x1 * cell_size + cell_size // 2, y1 * cell_size + cell_size // 2,
                 x2 * cell_size + cell_size // 2, y2 * cell_size + cell_size // 2)

def dibujar_jugador(pos):
    x, y = pos
    py5.fill(0, 0, 255)
    py5.ellipse(x * cell_size + cell_size // 2, y * cell_size + cell_size // 2, 20, 20)

def dibujar_salida():
    x, y = salida
    py5.fill(255, 0, 0)  # Color rojo para la salida
    py5.ellipse(x * cell_size + cell_size // 2, y * cell_size + cell_size // 2, 30, 30)  # Dibuja la salida

def mostrar_solucion():
    py5.stroke(255, 0, 0)
    camino = nx.shortest_path(laberinto, source=inicio, target=salida)
    for i in range(len(camino) - 1):
        x1, y1 = camino[i]
        x2, y2 = camino[i + 1]
        py5.line(x1 * cell_size + cell_size // 2, y1 * cell_size + cell_size // 2,
                 x2 * cell_size + cell_size // 2, y2 * cell_size + cell_size // 2)
    py5.stroke(0, 0, 0)

def key_pressed():
    global jugador_pos
    x, y = jugador_pos
    if py5.key == py5.CODED:
        if py5.key_code == py5.UP and (x, y - 1) in laberinto.neighbors((x, y)):
            jugador_pos = (x, y - 1)
        elif py5.key_code == py5.DOWN and (x, y + 1) in laberinto.neighbors((x, y)):
            jugador_pos = (x, y + 1)
        elif py5.key_code == py5.LEFT and (x - 1, y) in laberinto.neighbors((x, y)):
            jugador_pos = (x - 1, y)
        elif py5.key_code == py5.RIGHT and (x + 1, y) in laberinto.neighbors((x, y)):
            jugador_pos = (x + 1, y)

py5.run_sketch()
