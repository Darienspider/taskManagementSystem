from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import *
from .forms import TaskEntryForm, UserRegistrationForm
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    all_tasks = Task.objects.order_by('due_date')
    context = {
        "tasks": all_tasks,
        "title":" Task Management"
    }
    return render(request,"taskManagement/taskmanagementHome.html",context=context)

@login_required(login_url='../login/')
def newTask(request):
    if request.method == 'POST':
        form = TaskEntryForm(request.POST)
        if form.is_valid():
            new_task = Task(
                title=form.cleaned_data['title'],
                description=form.cleaned_data['description'],
                due_date=form.cleaned_data['due_date'],
                category=form.cleaned_data['category'],
                creator = request.user
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




def newUser(request):
    if request.method == 'POST':        
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            # ['firstName', 'lastName', 'contactNumber', 'email', 'password']
            data = form.changed_data
            User.objects.create(
                firstName=form[data[0]].value(),
                lastName=form[data[1]].value(),
                email=form[data[3]].value(),
                contactNumber = data[2],
                username = f'{form[data[0]].value()}{form[data[1]].value()}',
                password = make_password(form[data[4]].value())
            )
  
            return HttpResponse(f"<h1>Successfully created </h1>")
    else:
        form = UserRegistrationForm()

    context = {
        "title": "New User Creation",
        "form": form
    }
    return render(request, "taskManagement/newUserForm.html", context)




@login_required(login_url='../login/')
def home (request):
    created_tasks = Task.objects.filter(creator=request.user)
    assigned_tasks = Task.objects.filter(assigned_users  = request.user)
    task_status = Task.objects.filter(assigned_users = request.user, status ='Incomplete')
    user_tasks = created_tasks | assigned_tasks
    context = {
        "title":" Task Management",
        "assigned_tasks": user_tasks.distinct(),
        "Incomplete_tasks":task_status
        
    }
    return render(request,"taskManagement/home.html",context=context)