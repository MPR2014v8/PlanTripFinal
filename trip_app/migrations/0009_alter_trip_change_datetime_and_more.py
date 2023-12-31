# Generated by Django 4.2.1 on 2023-08-10 07:05

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('businessplace_app', '0049_alter_businessplace_change_datetime_and_more'),
        ('trip_app', '0008_alter_trip_change_datetime_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='change_datetime',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 10, 14, 5, 10, 941922)),
        ),
        migrations.AlterField(
            model_name='tripdetail',
            name='change_datetime',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 10, 14, 5, 10, 941922)),
        ),
        migrations.AlterField(
            model_name='tripdetail',
            name='place',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='businessplace_app.businessplace'),
        ),
        migrations.AlterField(
            model_name='tripdetail',
            name='trip',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trip_app.trip'),
        ),
    ]
