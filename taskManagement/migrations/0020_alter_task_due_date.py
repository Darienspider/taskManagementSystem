# Generated by Django 5.1 on 2024-08-27 18:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskManagement', '0019_alter_task_due_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 8, 27, 18, 32, 6, 468315, tzinfo=datetime.timezone.utc)),
        ),
    ]
