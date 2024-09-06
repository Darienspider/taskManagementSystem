from django.contrib import admin
from django.urls import path
from .views import *
from taskManagementSystem.urls import home as tmHome
urlpatterns = [
    path('',view=home, name='Home'),
    path('new/',view=newTask, name ='entry'),
    path('home/',view=tmHome, name= "TaskManagementHome"),
]
