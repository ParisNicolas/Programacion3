from contextlib import contextmanager


@contextmanager
def gestionar_archivo(ruta_archivo, modo):
    archivo = open(ruta_archivo, modo)
    try:
        yield archivo
    finally:
        archivo.close()


def leer_archivo(ruta_archivo):
    try:
        with gestionar_archivo(ruta_archivo, 'r') as archivo:
            for linea in archivo:
                print(linea, end='')
    except FileNotFoundError:
        print(f'Error: El archivo {ruta_archivo} no fue encontrado.')


def escribir_archivo(ruta_archivo):
    with gestionar_archivo(ruta_archivo, 'w') as archivo:
        archivo.write('Línea 1\n')
        archivo.write('Línea 2\n')
        archivo.write('Línea 3\n')


# Ejemplo de uso
escribir_archivo('archivo.txt')
leer_archivo('archivo.txt')