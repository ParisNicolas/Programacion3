#Facil
print("Determinar objeto valioso")
brillo = input("El objeto brilla (si/no): ")

if brillo == "si":
    print("Pues entonces es valioso pibe")
else:
    print("Perdona pero no creo que eso sea valioso")


###########################################################
#Intermedio
mensaje = input("El mensaje tiene el simbolo \"♣\"? (si/no): ")

if mensaje == "si":
    print("date por muerto, es muy peligroso")
else:
    print("tranqui, todo bien")

###########################################################
#Dificil
import random

preguntas = [
    {"pregunta": "¿El hombre llego a la luna?", "res":"si"},
    {"pregunta": "¿Existen los pejelagartos?", "res":"no"},
    {"pregunta": "¿las pulgas muerden?", "res":"si"} 
]


random.shuffle(preguntas)

for p in preguntas:
    if input(p["pregunta"]) == p["res"]:
        print("Bien")
    else:
        print("mal")
        break


