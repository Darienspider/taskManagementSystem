# Generated by Django 5.1 on 2024-09-06 00:10

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskManagement', '0023_alter_task_due_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='creator',
            field=models.ForeignKey(default='2', on_delete=django.db.models.deletion.CASCADE, related_name='task_creator', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 6, 0, 10, 5, 895672, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='user',
            name='created_tasks',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='task_created_by', to='taskManagement.task'),
        ),
    ]
