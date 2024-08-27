from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import *
from .forms import TaskEntryForm

# Create your views here.
def index(request):
    all_tasks = Task.objects.order_by('due_date')
    context = {
        "tasks": all_tasks,
        "title":" Task Management"
    }
    return render(request,"taskManagement/taskmanagementHome.html",context=context)

def new(request):
    if request.method == 'POST':
        form = TaskEntryForm(request.POST)
        if form.is_valid():
            new_task = Task(
                title=form.cleaned_data['title'],
                description=form.cleaned_data['description'],
                due_date=form.cleaned_data['due_date'],
                category=form.cleaned_data['category']
            )
            new_task.save()
            return HttpResponse(f"<h1>Successfully Saved {new_task.title}</h1>")
    else:
        form = TaskEntryForm()

    context = {
        "title": "New Task Entry",
        "form": form
    }
    return render(request, "taskManagement/entryForm.html", context)



def home (request):
    context = {
        "title":" Task Management"
    }
    return render(request,"taskManagement/home.html",context=context)