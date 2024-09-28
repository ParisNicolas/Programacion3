import py5
import random
import time

# Variables globales
array = []
sorted_flag = False
i, j = 0, 0
paused = False

def setup():
    global array, i, j, sorted_flag
    py5.size(600, 400)
    array = [random.randint(10, 350) for _ in range(50)]
    i, j = 0, 0
    sorted_flag = False

def draw():
    global i, j, sorted_flag, paused

    py5.background(255)
    
    # Dibujar los rectángulos representando el array
    for index, value in enumerate(array):
        color = py5.color(100, 100, 250)  # Color básico
        if index == j or index == j + 1:
            color = py5.color(250, 100, 100)  # Color de comparación
        py5.fill(color)
        py5.rect(index * 12, py5.height - value, 10, value)
    
    if sorted_flag or paused:
        return

    # Proceso de Bubble Sort
    if j < len(array) - 1 - i:
        if array[j] > array[j + 1]:
            array[j], array[j + 1] = array[j + 1], array[j]
        j += 1
    else:
        j = 0
        i += 1
        if i >= len(array) - 1:
            sorted_flag = True

def key_pressed():
    global paused
    if py5.key == 'r':
        setup()  # Reiniciar con nueva lista aleatoria
    elif py5.key == ' ':
        paused = not paused  # Pausar o reanudar

py5.run_sketch()