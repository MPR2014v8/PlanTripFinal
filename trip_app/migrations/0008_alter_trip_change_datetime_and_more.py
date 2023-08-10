# Generated by Django 4.2.1 on 2023-08-10 06:56

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('businessplace_app', '0048_alter_businessplace_change_datetime_and_more'),
        ('trip_app', '0007_alter_trip_change_datetime_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='change_datetime',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 10, 13, 56, 58, 569257)),
        ),
        migrations.AlterField(
            model_name='tripdetail',
            name='change_datetime',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 10, 13, 56, 58, 569764)),
        ),
        migrations.AlterField(
            model_name='tripdetail',
            name='place',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='placeAllDetail', to='businessplace_app.businessplace'),
        ),
        migrations.AlterField(
            model_name='tripdetail',
            name='trip',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tripAllDetail', to='trip_app.trip'),
        ),
    ]
