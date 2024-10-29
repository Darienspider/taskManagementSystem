from django.db import models
import django.utils.timezone as tz
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User


class Task(models.Model):
    task_ID = models.AutoField(primary_key=True)
    title = models.CharField(max_length=250)
    description = models.TextField(max_length=250)
    due_date = models.DateTimeField(default=tz.now)
    
    priority_choices = [
        ('High', 'High'),
        ('Medium', 'Medium'),
        ('Low', 'Low')
    ]
    priority = models.CharField(max_length=10, choices=priority_choices, default='Low')
    
    category_choices = [
        ('School', 'School'),
        ('Personal', 'Personal'),
        ('Work', 'Work'),
        ('None', 'None')
    ]
    category = models.CharField(max_length=24, choices=category_choices, default='None')
    
    creator = models.ForeignKey(get_user_model(), related_name='task_creator', on_delete=models.CASCADE, default=1)
    
    status_choices = [
        ('completed', 'completed'),
        ('In Progress', 'In Progress'),
        ('Incomplete', 'Incomplete'),
    ]
    status = models.CharField(max_length=24, choices=status_choices, default='Incomplete')
    
    assigned_users = models.ManyToManyField(User, related_name='assigned_tasks', blank=True)

    def __str__(self):
        return self.title


class Assignment(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    assigned_user = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)

    def __str__(self):
        return f"{self.assigned_user} - {self.task.title}"

class Notification(models.Model):
    NOTIFICATION_TYPES = [
        ('info','Info'),
        ('warning','Warning'),
        ('alert','Alert'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name= 'notifications')
    notification_type = models.CharField(max_length=10, choices=NOTIFICATION_TYPES, default='info')
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.notification_type}: {self.message}"