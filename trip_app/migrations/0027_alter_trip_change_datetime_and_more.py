# Generated by Django 4.2.1 on 2023-08-24 06:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trip_app', '0026_alter_trip_change_datetime_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='change_datetime',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 24, 13, 7, 1, 805796)),
        ),
        migrations.AlterField(
            model_name='tripdetail',
            name='change_datetime',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 24, 13, 7, 1, 806793)),
        ),
    ]
