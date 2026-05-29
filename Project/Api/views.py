from django.shortcuts import render

# Create your views here.
# ---- resquest retorna la pagina web
def Home(request):
    return rendeer(request, 'Base.html')