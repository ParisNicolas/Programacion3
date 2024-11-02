import networkx as nx
import random

def generar_laberinto(tamano):
    # Crear un grafo vacío
    laberinto = nx.Graph()

    # Agregar nodos al grafo (en un cuadrado de tamaño `tamano`)
    for x in range(tamano):
        for y in range(tamano):
            laberinto.add_node((x, y))

    # Agregar posibles aristas (conexiones) entre nodos
    for x in range(tamano):
        for y in range(tamano):
            if x < tamano - 1:  # Conectar con el nodo de la derecha
                laberinto.add_edge((x, y), (x + 1, y), weight=random.random())
            if y < tamano - 1:  # Conectar con el nodo de abajo
                laberinto.add_edge((x, y), (x, y + 1), weight=random.random())

    # Utilizar el algoritmo de Kruskal para generar un árbol de expansión
    # que representará el laberinto
    mst = nx.minimum_spanning_tree(laberinto)

    return mst

# Crear un laberinto de 5x5
if __name__ == "__main__":
    laberinto = generar_laberinto(5)