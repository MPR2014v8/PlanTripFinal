# Generated by Django 4.2.1 on 2023-09-01 13:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('businessplace_app', '0081_alter_businessplacepicture_change_datetime_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='businessplacepicture',
            name='change_datetime',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 1, 20, 23, 32, 289509)),
        ),
        migrations.AlterField(
            model_name='ratingandcomment',
            name='change_datetime',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 1, 20, 23, 32, 290537)),
        ),
        migrations.AlterField(
            model_name='virtualtour',
            name='change_datetime',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 1, 20, 23, 32, 290537)),
        ),
    ]
