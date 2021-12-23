from django.contrib import admin
from .models import Ship, ShipClass, Feature, TransferRequest

# Register your models here.

admin.site.register(Ship)
admin.site.register(ShipClass)
admin.site.register(Feature)
admin.site.register(TransferRequest)
