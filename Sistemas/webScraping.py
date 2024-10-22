import requests
from bs4 import BeautifulSoup


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}


#Consulta HTTP GET a la URL
response = requests.get('https://www.faunia.es/planea-tu-visita/animales/ajolote', headers=headers)

if response.status_code == 200:
    # Paso 3: Analizar el contenido HTML
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Paso 4: Extraer los datos específicos, como los títulos
    titulos = soup.find_all('h2', class_='cmp-title__text')
    for titulo in titulos:
        print(titulo.text)
else:
    print(f"Error al hacer la solicitud: {response.status_code}")