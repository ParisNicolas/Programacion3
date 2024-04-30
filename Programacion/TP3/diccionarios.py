#facil

# edades = {
#     "Juan":20,
#     "Pepe":23,
#     "Juana":30
# }

# edades['Patok'] = 29
# del edades['Pepe']
# print(edades)

# for i in edades:
#     if edades[i] == "Facu":
#         print(f"Se encontro a: {i}")

#Intermedio

# frecuencias = {chr(i): 0 for i in range(97, 123)}

# palabra = "pepito"

# for l in palabra:
#     frecuencias[l] += 1

# print(frecuencias)

#Dificil

manuscrito = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed a placerat orci. Nulla varius vel eros id ultricies. Mauris in elit et lacus euismod porta. Nullam accumsan risus felis, a dictum lectus malesuada at. Vestibulum purus purus, lobortis ac faucibus et, mattis a quam. Nam rutrum quis nisi quis scelerisque. Quisque dignissim orci sed dolor venenatis sagittis. Suspendisse quis leo eget leo pellentesque sagittis sit amet id arcu. Fusce odio felis, interdum in neque ut, ultrices hendrerit odio. Pellentesque sit amet enim elit. Pellentesque ornare sed mauris vitae hendrerit. Nulla convallis rutrum leo et convallis."
frecuencia = {}

for i in manuscrito.split(" "):
    if i in frecuencia:
        frecuencia[i] += 1
    else:
        frecuencia[i] = 0 
print(f"palabra mas encontrada: {max(frecuencia.items(), key=lambda x:x[1])[0]}")