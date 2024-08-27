from django import forms
from .models import Task, User

class TaskEntryForm(forms.Form):
    title = forms.CharField(label="Task Title", max_length=100)
    description = forms.CharField(label="Task Description", max_length=100)
    due_date = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
    category = forms.ChoiceField(label="Category", choices=[i for i in Task.category_choices], required=False)

# TODO: Figure out how to create a new user from the front end
class UserRegistrationForm(forms.Form):
    firstName = forms.CharField( label='firstName',max_length=100, required=False)
    lastName  = forms.CharField( label='lastName', max_length=100, required=False)
    contactNumber = forms.CharField( label='contactNumber', max_length=12, required=False)
    email = forms.EmailField(label='email')
    profile_image = forms.ImageField(label='profile_image', allow_empty_file=True, required=False)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)