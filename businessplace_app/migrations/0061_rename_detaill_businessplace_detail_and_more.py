# Generated by Django 4.2.1 on 2023-08-23 09:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('businessplace_app', '0060_alter_businessplace_change_datetime_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='businessplace',
            old_name='detaill',
            new_name='detail',
        ),
        migrations.AlterField(
            model_name='businessplace',
            name='change_datetime',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 23, 16, 49, 51, 76991)),
        ),
        migrations.AlterField(
            model_name='businessplacepicture',
            name='change_datetime',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 23, 16, 49, 51, 78988)),
        ),
        migrations.AlterField(
            model_name='ratingandcomment',
            name='change_datetime',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 23, 16, 49, 51, 79988)),
        ),
        migrations.AlterField(
            model_name='virtualtour',
            name='change_datetime',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 23, 16, 49, 51, 79988)),
        ),
    ]
