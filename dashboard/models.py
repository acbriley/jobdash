from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager
# Create your models here.

# job model


class Job(models.Model):
    title = models.CharField(max_length=350)
    company = models.CharField(max_length=350)
    location = models.CharField(max_length=350)
    workplace = models.CharField(max_length=350)
    link = models.TextField()
    details = models.TextField()


class User(AbstractUser):
    username = None
    email = models.EmailField(
        verbose_name='email address',
        max_length=100,
        unique=True,
    )
    jobs = models.ManyToManyField(Job)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
