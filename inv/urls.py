from django.urls import path

from .views import CategoriaView
app_name = 'inv'
urlpatterns = [
    path('categorias/', CategoriaView.as_view(), name='categoria_list'),
]
