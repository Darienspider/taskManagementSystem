from django import forms
from .models import Task

class TaskEntryForm(forms.Form):
    title = forms.CharField(label="Task Title", max_length=100)
    description = forms.CharField(label="Task Description", max_length=100)
    due_date = forms.DateTimeInput()
    
    category = forms.ChoiceField(label="Category", choices=[i for i in Task.category_choices], required=False)


    