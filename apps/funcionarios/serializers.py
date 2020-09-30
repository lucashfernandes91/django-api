from rest_framework import serializers
from .models import Funcionario

class FuncionarioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Funcionario
        fields = ('pk', 'primeiro_nome', 'ultimo_nome','telefone', 'email', 'empresas', 'criado_em',)

