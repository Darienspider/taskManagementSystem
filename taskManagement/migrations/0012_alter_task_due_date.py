# Generated by Django 5.1 on 2024-08-27 17:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskManagement', '0011_alter_task_due_date_alter_user_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 8, 27, 17, 46, 51, 336269, tzinfo=datetime.timezone.utc)),
        ),
    ]
