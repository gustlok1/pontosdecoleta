from django.db import models

# Create your models here.
class Pontos(models.Model):
    id = models.AutoField(primary_key=True)
    cidade = models.TextField(max_length=255)
    titulo_local = models.TextField(max_length=255)
    endereco = models.TextField(max_length=255)
    informacoes = models.TextField(max_length=255)