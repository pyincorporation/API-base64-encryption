from django.db import models

from django.contrib.auth.models import AbstractUser
# Create your models here.

class UserAccount(AbstractUser):
    sex = models.CharField(max_length=120)
    majina = models.CharField(max_length=120)