from django.urls import path
from apps.empresas.views import empresa_lista


urlpatterns = [
    path('', empresa_lista),
]
