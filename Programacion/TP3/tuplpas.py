#facil
# frutas = ("anana", "granada", "sandia", "kiwi", "guayaba", "papaya")

# for a in frutas:
#     print(a)

#intermedio
    
# coordenadas = (33, 57)
# print(f"x = {coordenadas[0]} \ny = {coordenadas[1]}")

#dificil

import math
cartesianas = (33, 57)

def pasarApolar(tupla):
    x, y = tupla
    hipotenusa = math.sqrt(x**2 + y**2)
    alfa = math.atan(y/x)
    return (hipotenusa, alfa)

print(pasarApolar(cartesianas))