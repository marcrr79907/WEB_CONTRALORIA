from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):

    user_rol = models.CharField(max_length=20)
