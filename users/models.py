# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    pass
    # add additional fields in here
    class Meta:
        db_table = 'auth_user'
    def __str__(self):
        return self.username



