# Generated by Django 4.2.1 on 2023-08-30 17:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trip_app', '0036_alter_trip_change_datetime_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='change_datetime',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 31, 0, 57, 48, 969099)),
        ),
        migrations.AlterField(
            model_name='tripdetail',
            name='change_datetime',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 31, 0, 57, 48, 969099)),
        ),
    ]
