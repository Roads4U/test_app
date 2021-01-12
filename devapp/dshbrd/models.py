from django.db import models

# Create your models here.
from django.db import models
from datetime import datetime
from django.utils import timezone
from django.contrib.auth.signals import user_logged_in
from django.contrib.auth.models import update_last_login
# from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.core.mail import EmailMessage
from django.dispatch import receiver
from django.template.loader import render_to_string
import string, random

class data_population(models.Model):
    id = models.AutoField(primary_key=True)
    country = models.TextField(blank=None, default='')
    province = models.TextField( blank=None, default='')
    population = models.IntegerField( blank=None, default='')
    year = models.TextField( blank=None, default='')