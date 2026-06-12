from django.urls import path
from .views import *
urlpatterns = [
    #----> Pagina de funcion de
    path('',Home,name="Inicio"),
    path('registro/',Registro,name="Registro"),
    path('productos/',VerProductos,name="Productos")
]