# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.conf import settings




category_choices = (
    ('CONSTRUCTION', 'CONSTRUCTION'),
    ('SPECIAL_EVENT', 'SPECIAL_EVENT'),
    ('INCIDENT', 'INCIDENT'),
    ('WEATHER_CONDITION', 'WEATHER_CONDITION'),
    ('ROAD_CONDITION', 'ROAD_CONDITION'),
)
state_choices = (
    ('validar', 'validar'),
    ('validado', 'validado'),
    ('resolvido', 'resolvido'),
)
# Create your models here.

class Localizacao(models.Model):
    nome = models.TextField()
    descricao = models.TextField()
    longitude = models.DecimalField(max_digits=5, decimal_places=3)
    latitude = models.DecimalField(max_digits=5, decimal_places=3)
    def __str__(self):
        return self.nome

class Incidente(models.Model):
    descricao = models.CharField(max_length=100, null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True, null=True)
    estado = models.CharField(max_length=10, null=True, choices=state_choices, default='validar')
    categoria = models.CharField(max_length=20, null=True, choices=category_choices)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.CASCADE)
    localizacao = models.ForeignKey(Localizacao, on_delete=models.CASCADE)
    #longitude = models.DecimalField(max_digits=30, decimal_places=15)
    #latitude = models.DecimalField(max_digits=30, decimal_places=15)
    def __str__(self):
        return self.estado



