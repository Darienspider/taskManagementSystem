# Generated by Django 5.1 on 2024-08-27 18:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskManagement', '0017_rename_contact_number_user_contactnumber_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 8, 27, 18, 26, 52, 606979, tzinfo=datetime.timezone.utc)),
        ),
    ]
