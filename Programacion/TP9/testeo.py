from main import busqueda_binaria, busqueda_lineal
import timeit
from random import randint
n = 0
lista = []
for i in range(10000):
    n+=randint(3,9)
    lista.append(n)

#lista = [1,4,5,7,9,10,13,14,17,24,28,43,204,443,459]

tiempo_transcurrido1 = timeit.timeit(lambda: busqueda_lineal(lista, 7), number=1)
tiempo_transcurrido2 = timeit.timeit(lambda: busqueda_binaria(lista, 7, 0, len(lista)-1), number=1)

print(f"Tiempo de ejecución: {tiempo_transcurrido1:.6f} segundos (lineal)")
print(f"Tiempo de ejecución: {tiempo_transcurrido2:.6f} segundos (binario)")