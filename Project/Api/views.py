from django.shortcuts import render, get_object_or_404
from .forms import *
# Create your views here.
# ---- request retorna la pagina web
def Home(request):
    return render(request, 'Base.html')

def Registro(request):
    data={ 
        'Formulario':FormularioRegistro()
    }
    if request.method=="POST":
        query=FormularioRegistro(data=request.POST,files=request.FILES)
        if query.is_valid():
            query.save()
            data["Mensaje"]="Datos Registrados"
        else:
            data['Mensaje']="No se pudo Registrar"
    return render(request, 'Pages/Registro.html', data)

def VerProductos(request):
    query= Alumnos.objects.all()
    data={
        'AlumnosTabla':query
    }
    return render(request, 'Pages/Productos.html', data)

def Modificacion(request,ID_Alumno):
    query=get_object_or_404(Alumnos, ID_Alumno=ID_Alumno)
    data={ 
        'Formulario':FormularioRegistro(instance=query)
    }
    if request.method=="POST":
        query=FormularioRegistro(data=request.POST,files=request.FILES)
        if query.is_valid():
            query.save()
            data["Mensaje"]="Datos Modificados"
        else:
            data['Mensaje']="No se pudo Modificar"
    return render(request, 'Pages/Registro.html', data)


 