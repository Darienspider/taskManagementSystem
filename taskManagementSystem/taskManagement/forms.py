from django import forms
from .models import Task
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

class TaskEntryForm(forms.ModelForm):
    title = forms.CharField(label="Task Title", max_length=100)
    description = forms.CharField(label="Task Description", max_length=100)
    due_date = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
    category = forms.ChoiceField(label="Category", choices=[i for i in Task.category_choices], required=False)
    status = forms.ChoiceField(label='Status',choices =[i for i in Task.status_choices], required=False)
    assigned_to = forms.ModelChoiceField (label= "Assignee", queryset=User.objects.all(), required=False,initial=None)
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
