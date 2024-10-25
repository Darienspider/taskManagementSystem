from django.contrib import admin
from django.urls import path
from .views import *
from taskManagementSystem.urls import home as tmHome


urlpatterns = [
    path('',view=home, name='Home'),
    path('new/',view=newTask, name ='entry'),
    path('home/',view=tmHome, name= "TaskManagementHome"),
    path('new-task/', view = newTask, name='new_task'),
    path('task/update/<int:pk>/', view = update_task, name='update_task'),
    path('task/delete/<int:pk>/', view = delete_task, name='delete_task'),
]
