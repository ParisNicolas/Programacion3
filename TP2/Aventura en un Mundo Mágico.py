#Facil
# nombre = input("Nombre del jugador: ")
# posiones = int(input("Cant. de posiones: "))

# print(f"\nBuenos dias {nombre}, bienvenido a pepitolandia.")
# print(f"Actualmente posee {posiones} posiones")

#Intermedio
# potHech = int(input("Potencia del hechizo: "))
# potEnem = int(input("Potencia del enemigo: "))

# if potHech > potEnem:
#     print("puedes derrotar al enemigo!")
# else: 
#     print("no puedes derrotar al enemigo:(")

#Dificil
n = int(input("cantidad de personajes: "))
k = int(input("tamaño de los grupos: "))

def calc_fact(n):
    if n==0 or n==1:
        return 1
    else: return n * calc_fact(n-1)

def calc_comb(n, k):
    if k > n:
        return 0
    else:
        return calc_fact(n) // (calc_fact(k) * calc_fact(n-k))

print(f"puedes hacer {calc_comb(n, k)} combinaciones")
