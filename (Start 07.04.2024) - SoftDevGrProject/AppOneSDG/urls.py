from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('blist/', views.blist),
    path('navbar/', views.navbar),
]
