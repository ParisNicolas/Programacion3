from PIL import Image, ImageDraw
import time

def busqueda_en_imagen(ruta_imagen, tonoMinimo, tonoMaximo):
    """
    Busca todos los píxeles de un tono específico en una imagen en escala de grises.

    :param imagen: Lista de listas que representa una imagen en escala de grises.
                   Cada valor es un entero entre 0 y 255.
    :param tono: El tono de gris a buscar (un entero entre 0 y 255).
    :return: Un diccionario con las coordenadas (x, y) como claves y el tono de gris como valor.
    """

    if not (0 < tonoMinimo or tonoMaximo > 255):
        raise ValueError("El tono debe estar entre 0 y 255.")

    tonos = range(tonoMinimo, tonoMaximo+1)

    # Abre la imagen y convierte a escala de grises
    imagen = Image.open(ruta_imagen).convert('L')
    ancho, alto = imagen.size
    pixeles = imagen.load()

    imagen_color = Image.new('RGB', (ancho, alto), color='white')
    draw = ImageDraw.Draw(imagen_color)

    resultado = []

    for y in range(alto):
        for x in range(ancho):
            # Obtiene el valor de gris del píxel en (x, y)
            valor = imagen.getpixel((x, y))
            if valor in tonos:
                draw.point((x, y), fill=(255, 0, 0))
                resultado.append((x, y))

    imagen_color.save('imagen_resaltada.png')
    return resultado

ruta_imagen = 'imagen.jpg'
tonoMinimo = 20
tonoMaximo = 150

tInicial = time.time()
resultados = busqueda_en_imagen(ruta_imagen, tonoMinimo, tonoMaximo)
tFinal = time.time()

tiempo_transcurrido = tFinal-tInicial
print(f"Pasaron {tiempo_transcurrido:.5f} segundos")