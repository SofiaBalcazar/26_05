from django.shortcuts import render

# Create your views here.
# ---- resquest retorna la pagina web
def Home(request):
    return render(request, 'Base.html')

def Registro(request):
    return render(request, 'Pages/Registro.html')