def busqueda_lineal(lista, objetivo):
    #Encontrar una coincidencia buscando valor por valor
    for i,e in enumerate(lista):
        if objetivo == e:
            return i
        
def busqueda_binaria(lista, elemento, start, end):
    #Recursivamente segmentar una lista ordenada en mitades hasta llegar a un solo valor
    
    if end >= start:
        mid = (end+start)//2

        if lista[mid] == elemento:
            return mid
        elif lista[mid] > elemento:
            return busqueda_binaria(lista, elemento,start, mid - 1)
        else:
            return busqueda_binaria(lista, elemento, mid + 1, end)
    else:
        return -1
    
lista = [1,4,5,7,9,10,13,14,17,24,28,43,204,443,459]

elem = 7
res1 = busqueda_lineal(lista, elem)
res2 = busqueda_binaria(lista, elem, 0, len(lista)-1)

print(f"El elemento {elem} esta en la posicion: \n\tBusqueda lineal: {res1} \n\tBusqueda binaria: {res2} ")