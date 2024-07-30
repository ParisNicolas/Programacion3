### Informe sobre el Context Manager y su uso en la gestión de archivos

#### Introducción
En Python, el manejo de recursos, especialmente los que necesitan ser explícitamente abiertos y cerrados, como los archivos, puede ser complicado y propenso a errores. Para simplificar esta tarea, Python proporciona los context managers, que aseguran que los recursos sean gestionados adecuadamente, incluso si se producen excepciones durante su uso. En este informe, exploraremos cómo funciona un context manager, específicamente mediante el uso del decorador `@contextmanager` del módulo `contextlib`, y cómo se puede utilizar para gestionar la apertura y cierre de archivos, así como el manejo de excepciones.

#### Funcionamiento del Context Manager

Un context manager es un objeto que define el contexto de un bloque de código. Este contexto se crea al principio del bloque y se destruye al final, gestionando automáticamente la adquisición y liberación de recursos. Los context managers se implementan mediante los métodos especiales `__enter__` y `__exit__`, o usando el decorador `@contextmanager` que simplifica su creación.

##### Implementación de un Context Manager con `@contextmanager`

El decorador `@contextmanager` permite definir un context manager usando una función generadora. Veamos un ejemplo práctico:

```python
from contextlib import contextmanager

@contextmanager
def gestionar_archivo(ruta_archivo, modo):
    archivo = open(ruta_archivo, modo)
    try:
        yield archivo
    finally:
        archivo.close()
```

1. **Apertura del archivo**: La función `gestionar_archivo` abre un archivo en el modo especificado (`'r'` para lectura, `'w'` para escritura, etc.) y asigna el manejador de archivo a la variable `archivo`.
2. **Yield**: El uso de `yield` proporciona el manejador de archivo al bloque `with` que utiliza este context manager. El código del bloque `with` se ejecuta en este punto.
3. **Cierre del archivo**: El bloque `finally` asegura que el archivo se cierre correctamente, incluso si se produce una excepción en el bloque `with`.

#### Uso del Context Manager en Operaciones de Archivo

A continuación, se muestran dos funciones que utilizan el context manager `gestionar_archivo` para leer y escribir archivos:

##### Escritura en un Archivo

```python
def escribir_archivo(ruta_archivo):
    with gestionar_archivo(ruta_archivo, 'w') as archivo:
        archivo.write('Línea 1\n')
        archivo.write('Línea 2\n')
        archivo.write('Línea 3\n')
```

Esta función abre un archivo en modo escritura (`'w'`) y escribe tres líneas de texto. El context manager se asegura de que el archivo se cierre después de que se complete el bloque `with`.

##### Lectura de un Archivo

```python
def leer_archivo(ruta_archivo):
    try:
        with gestionar_archivo(ruta_archivo, 'r') as archivo:
            for linea in archivo:
                print(linea, end='')
    except FileNotFoundError:
        print(f'Error: El archivo {ruta_archivo} no fue encontrado.')
```

Esta función abre un archivo en modo lectura (`'r'`) y lee su contenido línea por línea. Si el archivo no se encuentra, se captura la excepción `FileNotFoundError` y se imprime un mensaje de error.

#### Manejo de Excepciones

El manejo de excepciones es una parte integral del uso de context managers. En el ejemplo de lectura de archivo, el context manager no solo gestiona la apertura y cierre del archivo, sino que también permite capturar y manejar excepciones:

1. **Captura de `FileNotFoundError`**: Si el archivo especificado no existe, se lanza una excepción `FileNotFoundError`. Esta excepción se captura en el bloque `try-except`, permitiendo al programa continuar y manejar el error adecuadamente.
2. **Cierre Seguro del Archivo**: Incluso si ocurre una excepción durante la lectura del archivo, el bloque `finally` en el context manager asegura que el archivo se cierre correctamente, evitando fugas de recursos.

#### Ejemplo de Uso

```python
# Escritura en el archivo
escribir_archivo('archivo.txt')

# Lectura del archivo
leer_archivo('archivo.txt')
```

En este ejemplo, la función `escribir_archivo` crea y escribe en un archivo llamado `archivo.txt`. Luego, la función `leer_archivo` lee y imprime el contenido del archivo. Gracias al context manager `gestionar_archivo`, no es necesario preocuparse por cerrar manualmente el archivo en cada operación, ni por el manejo de excepciones durante la apertura y lectura del archivo.

#### Conclusión

El uso de context managers, especialmente mediante el decorador `@contextmanager`, proporciona una manera eficiente y segura de manejar recursos en Python. Simplifica el código, asegurando que los recursos sean liberados apropiadamente, incluso en presencia de excepciones. Este enfoque es particularmente útil para operaciones de archivo, donde la gestión adecuada de la apertura y cierre de archivos es crucial para evitar fugas de recursos y asegurar la integridad de los datos.