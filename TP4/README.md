# TP4

Clase constructora de Jugador y menu contextual para operar sobre sus metodos

## Proceso

Primero se definen todos los atributos de la clase: nombre, edad, posicion en el
campo, equipo actual, pais de origen, numero de camiseta, estadisticas y premios

Y luego sus respectivos metodos: actualizar_informacion, calcular_promedio_goles, es_goleador, agregar_premio, eliminar_premio, y actualizacion_informacion.

Por ultimo el menu dinamico con cierta logica para poder manipular y ver los atributos de cada instancia de un jugador.
El menu pide primero el numero del jugador (expepto para la opc. N°1).

### Funcionalidades
1) Crea un usuario, solicitando todos sus datos y creando una instancia nueva. Por cierto las estadisticas se toman por separado y luego se unen en un solo objeto
2) Muestra la inf. con un metodo
3) Actualiza la inf. con un metodo: pide toda la informacion de vuelta como cuando creas un nuevo jugador. Pero en este caso si no rellenas un campo, lo omite y deja el valor por defecto. Al final modifica los atributos utilizando el objeto Self
4) Calcula el promedio de goles (suponiendo que jugo 5 partidos, debido a que no se dispone de ese dato)
5) Avisa si el jugador es goleador en caso que halla realizado mas de 20 goles
6) Agrega un premio al jugador simplemente pusheando a una lista
7) Elimina un premio buscandolo en la lista de premios de ese jugador

**Creator:**
Paris Nicolas
