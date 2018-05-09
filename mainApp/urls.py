from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('kek/', views.kek, name='kek'),
]
