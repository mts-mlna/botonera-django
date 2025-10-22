from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name='inicio'),
    path('login/',login,name='login'),
    path('new_sound/',nuevosonido,name='nuevosonido')
]
