from django.db import models


class Times(models.Model):
    nome = models.CharField(max_length=255)
    cidade = models.CharField(max_length=255)
    titulos = models.CharField(max_length=255)
    craque = models.CharField(max_length=255)

    def __str__(self):
        return self.nome
