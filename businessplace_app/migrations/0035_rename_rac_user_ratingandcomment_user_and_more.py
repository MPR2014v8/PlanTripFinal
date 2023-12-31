# Generated by Django 4.2.1 on 2023-07-20 01:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('businessplace_app', '0034_alter_businessplace_change_datetime_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ratingandcomment',
            old_name='rac_user',
            new_name='user',
        ),
        migrations.AlterField(
            model_name='businessplace',
            name='change_datetime',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 20, 8, 29, 48, 311074)),
        ),
        migrations.AlterField(
            model_name='businessplacepicture',
            name='change_datetime',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 20, 8, 29, 48, 312083)),
        ),
        migrations.AlterField(
            model_name='ratingandcomment',
            name='change_datetime',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 20, 8, 29, 48, 313689)),
        ),
        migrations.AlterField(
            model_name='virtualtour',
            name='change_datetime',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 20, 8, 29, 48, 312083)),
        ),
    ]
