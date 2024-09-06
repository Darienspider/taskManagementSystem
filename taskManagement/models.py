from django.db import models
import datetime
import django.utils.timezone as tz
from django.contrib.auth.models import AbstractUser, Group, Permission
from taskManagementSystem import settings

# Create your models here.
class Task(models.Model):
    task_ID = models.AutoField(primary_key=True)
    title = models.TextField(max_length=250)
    description = models.TextField(max_length=250)
    due_date = models.DateTimeField(default=tz.now())
    
    priority_choices = [
        ('High','High'),
        ('Medium','Medium'),
        ('Low','Low')
    ]
    priority = models.CharField(max_length= 10,choices=priority_choices,default='Low')
    category_choices = [
        ('School','School'),
        ('Personal','Personal'),
        ('Work','Work'),
        ('None','None')
    ]
    category = models.CharField(max_length= 24,choices=category_choices,default='None')
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='task_creator', on_delete=models.CASCADE, default = 1)
    
    status_choices = [
        ('completed','completed'),
        ('In Progress','In Progress'),
        ('Incomplete','Incomplete'),
    ]
    
    
    status = models.CharField(max_length= 24,choices=status_choices,default='Incomplete')


    def __str__(self):
        return self.title
    
class User(AbstractUser):
    roleChoices = [
        ('admin','admin'),
        ('manager','Manager'),
        ('user','User'),
    ]
    role = models.CharField(max_length=20, choices=roleChoices, default='user')
    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_set',  # Add a unique related_name here
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups'
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_permission_set',  # Add a unique related_name here
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions'
    )

    firstName = models.CharField(max_length=100, choices=roleChoices, default='user')
    lastName = models.CharField(max_length=100, choices=roleChoices, default='user')

    profile_image = models.ImageField(upload_to='profile_images/', null=True, blank=True)
    timezone = models.CharField(max_length=50, default='UTC')
    notifications_enabled = models.BooleanField(default=True)
    bio = models.TextField(null=True, blank=True)
    contactNumber = models.CharField(max_length=15, null=True, blank=True)
    
    assigned_tasks = models.ManyToManyField(Task, related_name='assigned_users', blank=True)
    created_tasks = models.ForeignKey(Task, related_name='task_created_by', blank=True, on_delete=models.CASCADE, null=True)
    email = models.EmailField(null=True)

    def __str__(self):
        return self.username
    
class Assignment(models.Model):
    task_id = models.ForeignKey(Task, on_delete=models.CASCADE)