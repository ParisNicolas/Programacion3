"""
Para esta modificacion no me encontre poblemas mayores, a lo sumo un par de errores:
- Primero me olvide de acceder a la segunda capa de las tareas --> tareas[pos] --> ["Completadas"]
- Luego tuve que buscar como funciona el tipo "None" y al parecer se puede comparar ademas de usando "==", usando
    "is" ya que una variable vacia apunta a None
- Tuve que tomarme el timpo de verificar las salidas a la terminal para un buen registro del proceso (color a la salida de error)
- Por ultimo intente buscar una mejor manera de tomar una entrada de "si/no/-" y pasarlo a booleano sin tantos IFs, al final lo deje asi.
    No se podia usuar un operador ternario ya que son 3 posibles salidas
"""


def agregar_tarea(tareas, tarea, fecha_limite, prioridad, completada = False):
    nueva_tarea = {
        "Tarea": tarea, 
        "Fecha límite": fecha_limite, 
        "Prioridad": prioridad,
        "Completada": completada
    }
    tareas.append(nueva_tarea)
    print("Tarea agregada exitosamente.")

def mostrar_tareas(tareas, completadas):
    if not tareas:
        print("No hay tareas pendientes.")
    else:
        for i, tarea in enumerate(tareas, 1):
            if tarea["Completada"] == completadas or completadas == None:
                print(f"\nTarea {i}:")
                for clave, valor in tarea.items():
                    print(f"{clave}: {valor}")

def marcar_completada(tareas, posicion):
    if posicion <= len(tareas):
        tareas[posicion-1]["Completada"] = True
        print(f"Tarea {posicion} marcada como completada.")
    else:
        print(f"\033[91m [Error] La tarea {posicion} no existe \033[0m")

if __name__ == "__main__":
    lista_tareas = []
    while True:
        print("\n1. Agregar tarea")
        print("2. Mostrar tareas")
        print("3. Marcar tarea como completada")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            tarea_nueva = input("Ingrese la descripción de la tarea: ")
            fecha_limite_nueva = input("Ingrese la fecha límite (formato: dd/mm/yyyy): ")
            prioridad_nueva = input("Ingrese la prioridad: ")
            agregar_tarea(lista_tareas, tarea_nueva, fecha_limite_nueva, prioridad_nueva)

        elif opcion == "2":
            entrada = input("Filtrar tareas completadas? (si/no/-): ")
            if entrada == "si": completada = True
            elif entrada == "no": completada = False
            else: completada = None
            mostrar_tareas(lista_tareas, completada)

        elif opcion == "3":
            tarea = int(input("Ingrese la tarea a marcar: "))
            marcar_completada(lista_tareas, tarea)
        elif opcion == "4":
            break
        else:
            print("Opción no válida. Intente nuevamente.")