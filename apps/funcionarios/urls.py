from django.urls import path
from apps.funcionarios.views import funcionario_lista, funcionario_detalhes


urlpatterns = [
    path('', funcionario_lista),
    path('<str:username>', funcionario_detalhes),
]