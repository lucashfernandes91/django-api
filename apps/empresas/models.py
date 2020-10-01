from django.db import models


class Empresa(models.Model):
    nome = models.CharField(max_length=30)
    criado_em = models.DateTimeField(auto_now_add=True, auto_now=False)

    class Meta:
        ordering = ['nome']
        verbose_name = u'empresa'
        verbose_name_plural = u'empresas'

    def __str__(self):
        return self.nome

