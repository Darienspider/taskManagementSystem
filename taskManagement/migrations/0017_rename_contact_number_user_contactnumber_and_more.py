# Generated by Django 5.1 on 2024-08-27 18:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskManagement', '0016_alter_task_due_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='contact_number',
            new_name='contactNumber',
        ),
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 8, 27, 18, 24, 47, 297970, tzinfo=datetime.timezone.utc)),
        ),
    ]
