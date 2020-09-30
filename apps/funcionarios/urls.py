from django.urls import path
from apps.funcionarios.views import funcionario_lista, funcionario_detalhes

urlpatterns = [
    path('funcionarios/', funcionario_lista),
    path('funcionario/<int:pk>', funcionario_detalhes),
]