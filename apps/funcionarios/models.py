from django.db import models
from apps.empresas.models import Empresa


class Funcionario(models.Model):
    primeiro_nome = models.CharField(max_length=20)
    ultimo_nome = models.CharField(max_length=20)
    email = models.EmailField(null=True, blank=True)
    telefone = models.CharField(null=True, max_length=12)
    empresas = models.ManyToManyField(Empresa)
    criado_em = models.DateTimeField(auto_now_add=True, auto_now=False)

    class Meta:
        ordering = ['primeiro_nome']
        verbose_name = u'funcionario'
        verbose_name_plural = u'funcionarios'

    def __str__(self):
        return self.primeiro_nome + " " + self.ultimo_nome

    full_name = property(__str__)