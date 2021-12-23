from django.urls import path
from . import views

app_name= 'ships'
urlpatterns = [
    path('captain/<int:ship_id>', views.get_ship_crew),
]
