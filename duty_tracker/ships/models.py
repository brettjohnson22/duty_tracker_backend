from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.

class ShipClass(models.Model):
    name = models.CharField(max_length=50)
    complement = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Feature(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Ship(models.Model):
    name = models.CharField(max_length=50)
    ship_class = models.ForeignKey(ShipClass, on_delete=models.CASCADE)
    features = models.ManyToManyField(Feature)

    def __str__(self):
        return self.name

class TransferRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ship = models.ForeignKey(Ship, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name} - {self.ship.name}'