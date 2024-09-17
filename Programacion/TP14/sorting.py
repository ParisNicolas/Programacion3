def swap(lista, x1, x2):
    aux = lista[x1]
    lista[x1] = lista[x2]
    lista[x2] = aux
    return lista


# Bubble Sort
def ordenamiento_burbuja(lista):
    """
    Ordena una lista utilizando el algoritmo de Bubble Sort.

    Parámetros:
    lista -- La lista a ordenar.

    Retorna:
    La lista ordenada.
    """
    n = len(lista)
    for i in range(n):
        swapped = False
        # Ordenar por pares
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista = swap(lista, j, j+1)
                swapped = True
        # Si no hubo intercambios, la lista está ordenada
        if not swapped:
            break
    return lista


# Selection Sort
def ordenamiento_seleccion(lista):
    """
    Ordena una lista utilizando el algoritmo de Selection Sort.

    Parámetros:
    lista -- La lista a ordenar.

    Retorna:
    La lista ordenada.
    """
    n = len(lista)
    for i in range(n):
        minimo_x = i
        # Encontrar el índice del mínimo
        for j in range(i+1, n):
            if lista[j] < lista[minimo_x]:
                minimo_x = j
        # Colocar el mínimo al principio
        lista = swap(lista, i, minimo_x)
    return lista


# Insertion Sort
def ordenamiento_insercion(lista):
    """
    Ordena una lista utilizando el algoritmo de Insertion Sort.

    Parámetros:
    lista -- La lista a ordenar.

    Retorna:
    La lista ordenada.
    """
    n = len(lista)
    for i in range(1, n):
        key = lista[i]
        j = i - 1
        # Mover los elementos de lista[0...i-1] que son mayores que 'key'
        while j >= 0 and key < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = key
    return lista


# Quick Sort
def ordenamiento_rapido(lista):
    """
    Ordena una lista utilizando el algoritmo de Quick Sort.

    Parámetros:
    lista -- La lista a ordenar.

    Retorna:
    La lista ordenada.
    """
    if len(lista) <= 1:
        return lista
    else:
        pivot = lista[len(lista) // 2]
        left = [x for x in lista if x < pivot]
        middle = [x for x in lista if x == pivot]
        right = [x for x in lista if x > pivot]
        return ordenamiento_rapido(left) + middle + ordenamiento_rapido(right)


# Merge Sort
def ordenamiento_fusion(lista):
    """
    Ordena una lista utilizando el algoritmo de Merge Sort.

    Parámetros:
    lista -- La lista a ordenar.

    Retorna:
    La lista ordenada.
    """
    if len(lista) <= 1:
        return lista

    # Dividir la lista en dos mitades
    mid = len(lista) // 2
    left_half = lista[:mid]
    right_half = lista[mid:]

    # Ordenar las dos mitades
    left_sorted = ordenamiento_fusion(left_half)
    right_sorted = ordenamiento_fusion(right_half)

    # Combinar las dos mitades ordenadas
    return merge(left_sorted, right_sorted)


def merge(left, right):
    """
    Combina dos listas ordenadas en una sola lista ordenada.

    Parámetros:
    left -- Primera lista ordenada.
    right -- Segunda lista ordenada.

    Retorna:
    La lista combinada y ordenada.
    """
    sorted_list = []
    left_idx, right_idx = 0, 0

    # Combinar las dos listas mientras ambas tengan elementos
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            sorted_list.append(left[left_idx])
            left_idx += 1
        else:
            sorted_list.append(right[right_idx])
            right_idx += 1

    # Agregar cualquier elemento restante en la lista de la izquierda
    while left_idx < len(left):
        sorted_list.append(left[left_idx])
        left_idx += 1

    # Agregar cualquier elemento restante en la lista de la derecha
    while right_idx < len(right):
        sorted_list.append(right[right_idx])
        right_idx += 1

    return sorted_list


import random
import time 


# Ejemplo de uso
lista = [random.randint(0, 10000) for _ in range(5000)]

start_time = time.perf_counter()
ordenamiento_rapido(lista)
end_time = time.perf_counter()

print(end_time-start_time)