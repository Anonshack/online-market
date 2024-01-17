
from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    gender_choices = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    
    gender = models.CharField(max_length=1, choices=gender_choices)
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
