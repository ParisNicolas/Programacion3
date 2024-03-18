#facil
# doblones = [5,10,5,25,25,50]
# suma = 0
# max = doblones[0]

# for i in doblones:
#     suma += i
#     if i > max:
#         max = i

# print(f"hay en total: ${suma}")
# print(f"El promedio es {suma / len(doblones)}")
# print(f"La moneda mas valiosa es:{max}")


#intermedio

# cristales = [5,10,5,25,25,50]
# cristalesUnicos = list(set(cristales))
# print(cristalesUnicos)

#Dificil

def countOro(cofre1, cofre2):
    sum = 0
    for i in cofre1:
        sum += i
    for x in cofre2:
        sum += x
    return sum
print(countOro([5,10,5,25,25,50], [5,10,5,25,25,50]))