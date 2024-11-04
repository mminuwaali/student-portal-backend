from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=12,blank=True,null=True)
    profile = models.ImageField(upload_to="profiles", blank=True, null=True)
