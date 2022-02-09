#from statistics import mode
import django

from venv import create
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

""" post_save
django.db.models.signals.post_save

Arguments sent with this signal:

sender - The model class.
instance - The actual instance being saved.
created - A boolean; True if a new record was created.
 """
class Profile(models.Model):

    user = models.models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    first_name = models.CharField(max_length=200, null=True, blank=True)
    last_name = models.CharField(max_length=200, null=True, blank=True)
    phone = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return str(self.name)

