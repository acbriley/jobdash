from django.db import models

# Create your models here.


class Job(models.Model):
    title = models.CharField(max_length=350)
    company = models.CharField(max_length=350)
    location = models.CharField(max_length=350)
    workplace = models.CharField(max_length=350)
    link = models.TextField()
    details = models.TextField()
