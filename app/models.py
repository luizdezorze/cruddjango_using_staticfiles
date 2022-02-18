from django.db import models


OPCOES = [
    ('', 'Selecione o am...'),
    ('', 'CEFTRIAXONA 1G'),
    ('', 'CLINDAMICINA 600MG/4ML'),
    ('', 'MEROPENEM 500MG'),
]


class Tratamentos(models.Model):
    paciente = models.CharField(max_length=150)
    setor = models.CharField(max_length=150)
    am = models.CharField(max_length=150, choices=OPCOES)
    duracao = models.IntegerField()
