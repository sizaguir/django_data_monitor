from django.shortcuts import render

def home(request):
    # Renderizamos la plantilla que ubicaste en la carpeta dashboard
    return render(request, 'dashboard/base.html')