from django.shortcuts import render
from django.conf import settings  # Para acceder a API_URL
import requests                   # Para hacer la petición

def index(request):
    # 1. Realizar la solicitud GET a la API externa
    response = requests.get(settings.API_URL)
    
    # 2. Convertir la respuesta (texto) a una lista de diccionarios (JSON)
    posts = response.json()

    # 3. Calcular el dato que queremos mostrar (cantidad de posts)
    total_responses = len(posts)

    # 4. Preparar el contexto
    data = {
        'title': "Landing Page Dashboard",
        'total_responses': total_responses, # Agregamos el nuevo dato
    }

    return render(request, 'dashboard/index.html', data)