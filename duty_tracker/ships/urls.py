from django.urls import path
from . import views

app_name= 'ships'
urlpatterns = [
    path('captain/', views.get_ship_crew),
    path('test/', views.user_test),
    path('my_crew/', views.get_own_crew)
]
