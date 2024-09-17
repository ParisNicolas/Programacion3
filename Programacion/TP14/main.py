import time
import matplotlib.pyplot as plt
import random

#from listas import matriz_datos
from sorting import *


def medir_tiempo(funcion, lista, repeticiones=5):
    tiempos = []
    for _ in range(repeticiones):
        start_time = time.perf_counter()
        funcion(lista.copy())
        end_time = time.perf_counter()
        tiempos.append(end_time - start_time)
    return sum(tiempos) / len(tiempos)  # Tiempo promedio


tiempos_burbuja = []
tiempos_seleccion = []
tiempos_insercion = []
tiempos_rapido = []
tiempos_fusion = []


tamanos = [100, 500, 1000, 2000, 5000]

for tamano in tamanos:
    lista = [random.randint(0, 10000) for _ in range(tamano)]

    tiempos_burbuja.append(medir_tiempo(ordenamiento_burbuja, lista))
    tiempos_seleccion.append(medir_tiempo(ordenamiento_seleccion, lista))
    tiempos_insercion.append(medir_tiempo(ordenamiento_insercion, lista))
    tiempos_rapido.append(medir_tiempo(ordenamiento_rapido, lista))
    tiempos_fusion.append(medir_tiempo(ordenamiento_fusion, lista))

print(tiempos_burbuja)
print(tiempos_seleccion)
print(tiempos_insercion)
print(tiempos_rapido)
print(tiempos_fusion)

# Graficar resultados
plt.figure(figsize=(12, 8))
plt.plot(tamanos, tiempos_burbuja, label='Bubble Sort', marker='o')
plt.plot(tamanos, tiempos_seleccion, label='Selection Sort', marker='o')
plt.plot(tamanos, tiempos_insercion, label='Insertion Sort', marker='o')
plt.plot(tamanos, tiempos_rapido, label='Quick Sort', marker='o')
plt.plot(tamanos, tiempos_fusion, label='Merge Sort', marker='o')

plt.xlabel('Tamaño de la lista')
plt.ylabel('Tiempo de ejecución (segundos)')
plt.title('Comparación del tiempo de ejecución de algoritmos de ordenamiento')
plt.legend()
plt.grid(True)
plt.show()