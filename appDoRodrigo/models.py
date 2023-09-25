from django.db import models

class Menções_honrosas(models.Model):
  nome = models.CharField(max_length=70)
  gols = models.CharField(max_length=50)
  partidas = models.CharField(max_length=70)
  titulos = models.CharField(max_length=20)

class Top_5(models.Model):
  nome = models.CharField(max_length=70)
  gols = models.CharField(max_length=50)
  partidas = models.CharField(max_length=70)
  titulos = models.CharField(max_length=20)

