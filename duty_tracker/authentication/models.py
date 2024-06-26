from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

# To add new columns to the authentication_user table include the properties
# in the model below
# In order for the new columns to appear in the database run:
# 1. python manage.py makemigrations
# 2. python manage.py migrate


class User(AbstractUser):

    RANK_CHOICES = [
        ('ADM', 'Admiral'),
        ('CPT', 'Captain'),
        ('CMNDR', 'Commander'),
        ('LTC', 'Lt. Commander'),
        ('LT', 'Lieutenant'),
        ('ESN', 'Ensign'),
    ]

    POSITION_CHOICES = [
        ('CPT', 'Captain'),
        ('XO', 'First Officer'),
        ('ENG', 'Chief Engineer'),
        ('SCI', 'Science Officer'),
        ('PIL', 'Pilot'),
        ('DOC', 'Doctor'),
    ]

    rank = models.CharField(max_length=15, choices=RANK_CHOICES, default='ESN')
    position = models.CharField(max_length=15, choices=POSITION_CHOICES, null=True, blank=True)
    ship = models.ForeignKey('ships.ship', null=True, blank=True, on_delete=models.CASCADE)

