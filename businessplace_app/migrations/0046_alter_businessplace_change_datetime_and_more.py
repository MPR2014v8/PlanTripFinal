# Generated by Django 4.2.1 on 2023-08-10 06:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('businessplace_app', '0045_alter_businessplace_change_datetime_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='businessplace',
            name='change_datetime',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 10, 13, 36, 48, 255679)),
        ),
        migrations.AlterField(
            model_name='businessplacepicture',
            name='change_datetime',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 10, 13, 36, 48, 256679)),
        ),
        migrations.AlterField(
            model_name='ratingandcomment',
            name='change_datetime',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 10, 13, 36, 48, 257676)),
        ),
        migrations.AlterField(
            model_name='virtualtour',
            name='change_datetime',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 10, 13, 36, 48, 256679)),
        ),
    ]
