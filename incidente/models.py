# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
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
class Incidente(models.Model):
    descricao = models.CharField(max_length=100, null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add =True)
    update_date = models.DateTimeField()
    estado = models.CharField(max_length=10, null=True, choices=state_choices, default='validar')
    categoria = models.CharField(max_length=20, null=True, choices=category_choices)
    author = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete= models.CASCADE)


    def __str__(self):
        return self.estado



