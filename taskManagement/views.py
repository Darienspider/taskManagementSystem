from django.shortcuts import render, redirect, get_object_or_404

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
                creator = request.user,
                priority = form.cleaned_data["priority"],
            )
            new_task.save()
            

            context = {
                "title": "New Task Confirmed",
            }

            return render(request, "taskManagement/newTaskConfirmation.html", context)
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
    assigned_tasks = Task.objects.filter(assigned_users = request.user, status__in=['Incomplete','In Progress'])
    incompleted_tasks_by_user = Task.objects.filter(status ='Incomplete',assigned_users=request.user)
    completed_tasks = Task.objects.filter(status ='completed', assigned_users= request.user )
    inprogress_tasks = Task.objects.filter(assigned_users = request.user, status__in=['In Progress'])

    user_tasks = created_tasks | assigned_tasks
    context = {
        "title":" Task Management",
        "assigned_tasks": assigned_tasks,
        "Incomplete_tasks":incompleted_tasks_by_user,
        "completed_tasks" :completed_tasks,
        "in_progress":inprogress_tasks,
        "created_tasks":created_tasks
    }
    return render(request,"taskManagement/home.html",context=context)


@login_required
def update_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    
    if request.method == 'POST':
        form = TaskEntryForm(request.POST, instance=task)
        if form.is_valid():
            updated_task = form.save(commit=False)  # Save form data without committing to the database
            # Add the current user to the assigned_users if not already present
            if request.user not in updated_task.assigned_users.all():
                updated_task.assigned_users.add(request.user)
            updated_task.save()  # Save the task with the current user assigned
            return redirect('Home')  # Redirect to the homepage or another page
    else:
        form = TaskEntryForm(instance=task)
    
    context = {
        'form': form,
        'task': task,
        'title': 'Update Task'
    }
    return render(request, 'taskManagement/update_task.html', context)


@login_required
def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('Home')  # Redirect to the homepage or another page
    context = {
        'task': task,
        'title': 'Delete Task'
    }
    return render(request, 'taskManagement/delete_task.html', context)