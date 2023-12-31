# Generated by Django 4.2.1 on 2023-08-23 18:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('businessplace_app', '0064_alter_businessplace_change_datetime_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='businessplace',
            name='change_datetime',
        ),
        migrations.RemoveField(
            model_name='businessplace',
            name='created_datetime',
        ),
        migrations.AlterField(
            model_name='businessplacepicture',
            name='change_datetime',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 24, 1, 49, 18, 752295)),
        ),
        migrations.AlterField(
            model_name='ratingandcomment',
            name='change_datetime',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 24, 1, 49, 18, 755295)),
        ),
        migrations.AlterField(
            model_name='virtualtour',
            name='change_datetime',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 24, 1, 49, 18, 754291)),
        ),
    ]
