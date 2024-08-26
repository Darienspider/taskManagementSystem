from django.db import models
import datetime
import django.utils.timezone as tz
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
    category = models.CharField(max_length= 10,choices=category_choices,default='None')



    def __str__(self):
        return self.title