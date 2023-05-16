from django.db import models

class Esporte(models.Model):
    nome_esporte = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nome_esporte

class Time(models.Model):
    nome_time = models.CharField(max_length=100)
    data_criacao = models.DateField(auto_now_add=True)
    nome_esporte = models.ForeignKey(Esporte, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome_time
