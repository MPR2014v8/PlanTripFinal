# Generated by Django 4.2.1 on 2023-09-10 15:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('businessplace_app', '0107_alter_businessplacepicture_change_datetime_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='businessplacepicture',
            name='change_datetime',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 10, 22, 41, 51, 469108)),
        ),
        migrations.AlterField(
            model_name='ratingandcomment',
            name='change_datetime',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 9, 10, 22, 41, 51, 470107), null=True),
        ),
        migrations.AlterField(
            model_name='ratingandcomment',
            name='created_datetime',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 9, 10, 22, 41, 51, 470107), null=True),
        ),
        migrations.AlterField(
            model_name='virtualtour',
            name='change_datetime',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 10, 22, 41, 51, 469108)),
        ),
    ]
