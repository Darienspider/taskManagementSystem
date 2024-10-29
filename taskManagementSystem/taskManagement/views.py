from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import *
from .forms import TaskEntryForm
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm  
from .services import *




# Create your views here.
def index(request):
    all_tasks = Task.objects.order_by('due_date')
    context = {
        "tasks": all_tasks,
        "title":" Task Management"
    }
    return render(request,"taskManagement/taskmanagementHome.html",context=context)


@login_required(login_url='../login/')
def managerView(request):
    # get tasks and all of the users assigned to it
    managers = User.objects.filter(groups__name__in =['Manager'])
    all_users = User.objects.all()
    created_tasks = Assignment.objects.select_related('task')
    assigned_tasks = Assignment.objects.select_related('task', 'assigned_user').all()
    completed_tasks = Assignment.objects.select_related('task')
    unassigned_tasks = Assignment.objects.filter(assigned_user__isnull=True).select_related('task')  # Optimize queries
    context = {
        "title":"Manager Dashboard",
        'assigned_tasks': assigned_tasks,
        'unassigned_tasks': unassigned_tasks,
        'created_tasks':created_tasks,
        'completed_tasks': completed_tasks,

        
    }
    return render(request,"taskManagement/managerView.html",context=context)


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
            assigned_user = form.cleaned_data['assigned_to']
            Assignment.objects.create(task=new_task, assigned_user=assigned_user)
            context = {
                "title": "New Task Confirmed",
            }
            message = f'New task has been created:  {new_task.task_ID} - {new_task.title}'
            create_notification(assigned_user, message, notification_type='info')
            send_email_notification(assigned_user, 'New Task Assigned', message)

            return render(request, "taskManagement/newTaskConfirmation.html", context)
    else:
        form = TaskEntryForm()

    context = {
        "title": "New Task Entry",
        "form": form
    }
    return render(request, "taskManagement/entryForm.html", context)

def newUser1(request):
    if request.method == 'POST':        
        form = UserCreationForm(request.POST)
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
  
            return HttpResponse(f'<h1>Successfully created {form[data[0]].value()}{form[data[1]].value()} </h1></br> <a href="/home"> Return Home </a>')
    else:
        form = UserCreationForm()

    context = {
        "title": "New User Creation",
        "form": form
    }
    return render(request, "taskManagement/newUserForm.html", context)

def newUser(request):  
    if request.method == 'POST':  
        form = UserCreationForm(request.POST)  
        if form.is_valid():  
            new_user = form.save()  

            message = f'New user has been created: {new_user.id}'
            # send email to both request user and newly created user
            send_email_notification(request.user, 'New User Created', message)
            send_email_notification(new_user, 'User Account Created ', f'Account ID: {new_user.id}')
            send_email_notification('shadarien@shadwilliams.dev', 'User Account Created ', f'Account ID: {new_user.id}')

            return HttpResponse(f'<h1>Successfully created  </h1></br> <a href="/home"> Return Home </a>')
  
    else:  
        form = UserCreationForm()  
    context = {  
        'form':form  
    }  
    return render(request, "taskManagement/newUserForm.html", context) 

@login_required(login_url='../login/')
def home (request):
    created_tasks = Assignment.objects.select_related('task')
    assigned_tasks = Assignment.objects.select_related('task', 'assigned_user').all()
    # completed_tasks = Task.objects.filter(status ='completed', assigned_users= request.user )
    completed_tasks = Assignment.objects.select_related('task', 'assigned_user').all()
    inprogress_tasks = Task.objects.filter(assigned_users = request.user, status__in=['In Progress'])
    # user_tasks = created_tasks | assigned_tasks
    context = {
        "title":" Task Management",
        "assigned_tasks": assigned_tasks,
        "completed_tasks" :completed_tasks,
        "in_progress":inprogress_tasks,
        "created_tasks":created_tasks
    }
    return render(request,"taskManagement/home.html",context=context)

@login_required(login_url='../login/')
def update_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    assignment = Assignment.objects.filter(task=task).first() 
    
    if request.method == 'POST':
        form = TaskEntryForm(request.POST, instance=task)
        if form.is_valid():
            updated_task = form.save(commit=False)  # Save form data without committing to the database
            # Add the current user to the assigned_users if not already present
            if request.user not in updated_task.assigned_users.all():
                updated_task.assigned_users.add(request.user)
            
            if assignment:
                assignment.assigned_user = form.cleaned_data['assigned_to']
                assignment.save()
            updated_task.save()  # Save the task with the current user assigned
            return redirect('Home')  # Redirect to the homepage or another page
    else:
        # TODO: remove managers from list of users to select for assignments
        form = TaskEntryForm(instance=task)
    
    context = {
        'form': form,
        'task': task,
        'title': 'Update Task'
    }
    return render(request, 'taskManagement/update_task.html', context)

@login_required(login_url='../login/')
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