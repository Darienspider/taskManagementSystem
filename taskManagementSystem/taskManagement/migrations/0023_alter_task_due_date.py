# Generated by Django 5.1 on 2024-09-05 23:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskManagement', '0022_alter_task_due_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 5, 23, 57, 37, 17545, tzinfo=datetime.timezone.utc)),
        ),
    ]
