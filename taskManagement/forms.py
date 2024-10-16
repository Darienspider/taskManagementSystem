from django import forms
from .models import Task, User
from django.contrib.auth.models import Group

class TaskEntryForm(forms.ModelForm):
    manager_group = Group.objects.get(name="Manager")
    title = forms.CharField(label="Task Title", max_length=100)
    description = forms.CharField(label="Task Description", max_length=100)
    due_date = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
    category = forms.ChoiceField(label="Category", choices=[i for i in Task.category_choices], required=False)
    status = forms.ChoiceField(label='Status',choices =[i for i in Task.status_choices], required=False)
    assigned_to = forms.ModelChoiceField (label= "Assignee", queryset=User.objects.exclude(groups=manager_group), required=False,initial=None)
    priority = forms.ChoiceField (label= "Assigned", choices= [i for i in Task.priority_choices], required=True)

    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'category','status','assigned_to', 'priority']  # Ensure these fields match the Task model
        widgets = {
            'due_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
        labels = {
            'title': 'Task Title',
            'description': 'Task Description',
            'due_date': 'Due Date',
            'category': 'Category',
            'status':'Status',
            'assigned_to':'Assignee',
            'priority':'Priority'
        }


# TODO: Figure out how to create a new user from the front end
class UserRegistrationForm(forms.Form):
    firstName = forms.CharField( label='firstName',max_length=100, required=False)
    lastName  = forms.CharField( label='lastName', max_length=100, required=False)
    contactNumber = forms.CharField( label='contactNumber', max_length=12, required=False)
    email = forms.EmailField(label='email')
    profile_image = forms.ImageField(label='profile_image', allow_empty_file=True, required=False)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)