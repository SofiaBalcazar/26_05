from django.urls import path
from .views import *
urlpatterns = [
    #----> 
    path('',Home,name="Inicio"),
    path('registro/',Registro,name="Registro"),
]