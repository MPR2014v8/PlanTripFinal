# Generated by Django 4.2.1 on 2023-09-03 08:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('businessplace_app', '0096_alter_businessplacepicture_change_datetime_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='businessplacepicture',
            name='change_datetime',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 3, 15, 11, 49, 936277)),
        ),
        migrations.AlterField(
            model_name='ratingandcomment',
            name='change_datetime',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 3, 15, 11, 49, 937276)),
        ),
        migrations.AlterField(
            model_name='virtualtour',
            name='change_datetime',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 3, 15, 11, 49, 937276)),
        ),
    ]