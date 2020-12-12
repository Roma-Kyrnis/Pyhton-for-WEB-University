from django.db import models

class Person(models.Model):
    email = models.EmailField(max_length=25)
    password = models.TextField(max_length=24)

# Create your models here.
