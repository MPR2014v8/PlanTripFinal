# Generated by Django 4.2.1 on 2023-09-01 14:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trip_app', '0043_alter_trip_change_datetime_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='change_datetime',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 1, 21, 6, 50, 437753)),
        ),
        migrations.AlterField(
            model_name='tripdetail',
            name='change_datetime',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 1, 21, 6, 50, 437753)),
        ),
    ]
