from django.db import models
from django.contrib.auth.models import AbstractUser, User


class User(AbstractUser):
    nickname = models.CharField(max_length=50, blank=True)
    email = models.EmailField(unique=True)

    class Meta(AbstractUser.Meta):
        pass

# Create your models here.
