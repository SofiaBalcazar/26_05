from django.shortcuts import render
from .forms import *
# Create your views here.
# ---- resquest retorna la pagina web
def Home(request):
    return render(request, 'Base.html')

def Registro(request):
    data={ 
        'Formulario':FormularioRegistro()
    }
    return render(request, 'Pages/Registro.html', data)