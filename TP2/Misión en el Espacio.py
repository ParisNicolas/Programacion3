#Facil
# distancia = int(input("distancia a la luna (km): "))
# velocidad = int(input("velocidad del cohete (km/h): "))

# print(f"el cohete va a tardar: {distancia/velocidad} horas")


#Intermedio
# base = int(input("Digite la base de la superficie (m): "))
# altura = int(input("Digite la altura de la superficie (m): "))

# print(f"El area para la base de operaciones es de: {base*altura}m²")

#Dificil
import math

total_personas = int(input("Digite la cantidad de personas: "))
tamano_equipo = int(input("Digite el tamaño de los grupos: "))

def calcular_combinaciones(total_personas, tamano_equipo):

    if total_personas < tamano_equipo:
        return 0
    
    combinaciones = math.comb(total_personas, tamano_equipo)
    return combinaciones

resultado = calcular_combinaciones(total_personas, tamano_equipo)
print("Número total de combinaciones posibles:", resultado)