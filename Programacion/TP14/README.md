# Algoritmos de Ordenamiento

Este repositorio contiene implementaciones en Python de varios algoritmos de ordenamiento clásicos. Los algoritmos incluidos son:

1. **Bubble Sort**
2. **Selection Sort**
3. **Insertion Sort**
4. **Quick Sort**
5. **Merge Sort**

## Algoritmos

### 1. Bubble Sort

El algoritmo de **Bubble Sort** compara pares de elementos adyacentes y los intercambia si están en el orden incorrecto. Este proceso se repite hasta que la lista está ordenada.

### 2. Selection Sort

El algoritmo de **Selection Sort** selecciona repetidamente el elemento más pequeño de la lista no ordenada y lo mueve al principio. Se repite este proceso hasta que toda la lista está ordenada.

### 3. Insertion Sort

El algoritmo de **Insertion Sort** construye la lista ordenada un elemento a la vez. Toma cada elemento de la lista y lo inserta en la posición correcta dentro de la lista ordenada.

### 4. Quick Sort

El algoritmo de **Quick Sort** utiliza la técnica de divide y vencerás. Selecciona un pivote y particiona la lista en dos sublistas: una con elementos menores que el pivote y otra con elementos mayores. Luego aplica recursivamente el mismo proceso a las sublistas.

### 5. Merge Sort

El algoritmo de **Merge Sort** también utiliza divide y vencerás. Divide la lista en dos mitades, ordena cada mitad y luego combina (o fusiona) las dos mitades ordenadas en una sola lista ordenada.

## Uso

Puedes probar los algoritmos con una lista de números como en el siguiente ejemplo:

```python
lista = [64, 34, 25, 12, 22, 11, 90]
print(ordenamiento_rapido(lista))  # Puedes reemplazar con cualquier función de ordenamiento


##Conclusion

###Bubble sort
Empezando por el bubble sort se nota una clara diferencia de tiempos, este es por lejos el mas pesado en terminos de rendimiento y se hace cada vez peor en una mayor cantidad de datos. Es el algoritmo mas simple pero no el mas eficiente. Diria bonito para enseñar.

###Selection sort
El Selection Sort tiene unas estadisticas intermedias algo mejores que el Insertion Sort y al parecer muy parecidas a los mejores algoritmos en terminos de listas pequeñas. Diria que es otro algoritmo facil de entender y que tiene resultados, pero en terminos generales no lo recomendaria. Pero es cierto que tiene buen manejo de memoria ya que solo hace a lo sumo una modificacion por elemento, sin tantos intercambios.

###Insertion Sort
Este algoritmo parecido a lo que haria cualquiera al ordenar elementos, tiene una eficiencia computacional no tan buena, peor que el selection sort. Necesita bastante manejo de memoria, o almenos una lista enlazada para poder funcionar bien, ya que de otra manera mueve los elementos por la memoria todo el rato.

###Quick Sort
Este algoritmo me sorprendio, no esperaba que un algoritmo podria ordenar 500.000 elementos en tan solo 2.31 seg. Tiene un rendimiendo exepcional, normal que sea unos de los algoritmos preferido por las librerias.
Ademas parece ser sensillo en terminos de codigo. El unico problema que veo podria ser un stackoverflow ya que maneja recursividad, y podria requerrir bastante memoria ram. Por otro lado el unico problema que tiene es que en cantidades de datos grandes, en ciertos casos puede tardar mas de lo esperado si se toma como punto de pivote el centro.

###Merge Sort
Al igual que Quick Sort tiene una eficiencia muy conveniente, este resolvio los 500.000 elementos en 2.38 seg. Podria decirse que es algo mas lento que Quick Sort aunque eso lo cubre con su estabilidad.