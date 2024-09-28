import py5
import random

array = []
i = 1  # Índice para el elemento actual
j = 0  # Índice para comparación en Insertion Sort
current = 0
paused = False

def setup():
    global array, i, j, current, paused
    py5.size(600, 400)
    array = [random.randint(10, 350) for _ in range(50)]
    i = 1
    j = 0
    current = array[i]
    paused = False

def draw():
    global i, j, current, paused

    py5.background(255)
    
    # Dibujar los rectángulos representando el array
    for index, value in enumerate(array):
        color = py5.color(100, 100, 250)  # Color normal
        if index == j or index == j + 1:
            color = py5.color(250, 100, 100)  # Color de comparación
        if index == i:
            color = py5.color(100, 250, 100)  # Color del elemento actual
        py5.fill(color)
        py5.rect(index * 12, py5.height - value, 10, value)
    
    if paused:
        return

    # Proceso de Insertion Sort
    if i < len(array):
        if j >= 0 and array[j] > current:
            array[j + 1] = array[j]  # Desplazar elementos mayores
            j -= 1
        else:
            array[j + 1] = current  # Insertar el elemento
            i += 1
            if i < len(array):
                current = array[i]
            j = i - 1
    else:
        paused = True  # Pausar cuando el array esté ordenado

def key_pressed():
    global paused
    if py5.key == 'r':
        setup()  # Reiniciar con nueva lista aleatoria
    elif py5.key == ' ':
        paused = not paused  # Pausar o reanudar

py5.run_sketch()
