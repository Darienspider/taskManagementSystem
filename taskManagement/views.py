from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import *

# Create your views here.
def index(request):
    all_tasks = Task.objects.order_by('due_date')
    context = {
        "tasks": all_tasks,
        "title":" Task Management"
    }
    return render(request,"taskManagement/taskmanagementHome.html",context=context)

def home (request):
    context = {
        "title":" Task Management"
    }
    return render(request,"taskManagement/home.html",context=context)